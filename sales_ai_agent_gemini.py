"""
sales_ai_agent_gemini.py
=========================
Gemini-powered AI agent for your sales analysis project.

Loads cleaned_sales_data.csv with pandas and lets Gemini answer natural-language
questions about it by calling small, precise lookup functions (group-by, top rows,
filtered totals) instead of guessing numbers. Uses Gemini's automatic function
calling, so it decides on its own which lookup(s) it needs.

Setup
-----
    pip install -r requirements.txt

    # Get a free key at https://aistudio.google.com/apikey
    # Windows (PowerShell): setx GEMINI_API_KEY "AIza..."
    # macOS / Linux:        export GEMINI_API_KEY=AIza...

Usage
-----
    from sales_ai_agent_gemini import SalesAgent

    agent = SalesAgent("cleaned_sales_data.csv")
    print(agent.ask("Which region is most profitable?"))

Or run this file directly for an interactive chat in the terminal:
    python sales_ai_agent_gemini.py cleaned_sales_data.csv
"""

import json
import os
import sys

import pandas as pd
import google.generativeai as genai

MODEL = "gemini-2.0-flash"

SYSTEM_INSTRUCTION = (
    "You are a sales data analyst assistant. Always call one of the available "
    "functions to look up real numbers before answering -- never guess or make up "
    "figures. Keep answers concise (2-5 sentences), lead with the direct answer, "
    "format currency amounts clearly, and round percentages to 1 decimal."
)


class SalesAgent:
    def __init__(self, csv_path: str, api_key: str | None = None):
        self.df = pd.read_csv(csv_path)
        genai.configure(api_key=api_key or os.environ.get("GEMINI_API_KEY"))
        self.model = genai.GenerativeModel(
            model_name=MODEL,
            system_instruction=SYSTEM_INSTRUCTION,
            tools=[self.overall_summary, self.group_by, self.top_rows, self.filtered_summary],
        )
        self.chat = self.model.start_chat(enable_automatic_function_calling=True)

    # ------------------------------------------------------------------
    # Data lookup functions. Gemini reads these docstrings + type hints
    # to decide when and how to call them -- keep both accurate.
    # ------------------------------------------------------------------
    def overall_summary(self) -> dict:
        """Get overall dataset stats: total sales, total profit, average margin,
        total quantity sold, date range, and the valid values for Region,
        Product_Category, Sales_Rep, Sales_Channel, Payment_Method and
        Customer_Type. Call this first if you don't know what values exist.
        """
        df = self.df
        total_sales = float(df["Sales_Amount"].sum())
        total_profit = float(df["Profit"].sum())
        return {
            "rows": len(df),
            "total_sales": round(total_sales, 2),
            "total_profit": round(total_profit, 2),
            "avg_margin_pct": round(100 * total_profit / total_sales, 2) if total_sales else 0,
            "total_quantity_sold": int(df["Quantity_Sold"].sum()),
            "date_range": [str(df["Sale_Date"].min()), str(df["Sale_Date"].max())],
            "regions": sorted(df["Region"].unique().tolist()),
            "categories": sorted(df["Product_Category"].unique().tolist()),
            "reps": sorted(df["Sales_Rep"].unique().tolist()),
            "channels": sorted(df["Sales_Channel"].unique().tolist()),
            "payment_methods": sorted(df["Payment_Method"].unique().tolist()),
            "customer_types": sorted(df["Customer_Type"].unique().tolist()),
        }

    def group_by(self, field: str, metric: str = "Sales_Amount", agg: str = "sum",
                 filters_json: str = "{}", order: str = "desc", limit: int = 20) -> list:
        """Aggregate the sales data grouped by a categorical column.

        Args:
            field: Column to group by, e.g. Region, Sales_Rep, Product_Category,
                Customer_Type, Payment_Method, Sales_Channel, Month_Name, Quarter, Year.
            metric: Numeric column to aggregate: Sales_Amount, Profit,
                Quantity_Sold, or Profit_Margin.
            agg: One of "sum", "avg", "count".
            filters_json: JSON object string to restrict rows first, e.g.
                '{"Region": "North"}'. Use "{}" for no filter.
            order: "asc" or "desc".
            limit: Max number of groups to return.
        """
        df = self._apply_filters(json.loads(filters_json or "{}"))
        if field not in df.columns:
            return [{"error": f"Unknown field '{field}'. Valid fields: {list(df.columns)}"}]
        grouped = df.groupby(field)[metric]
        series = {"sum": grouped.sum, "avg": grouped.mean, "count": grouped.count}.get(agg, grouped.sum)()
        series = series.sort_values(ascending=(order == "asc")).head(limit)
        counts = df.groupby(field).size()
        return [
            {"key": str(k), "value": round(float(v), 2), "count": int(counts.get(k, 0))}
            for k, v in series.items()
        ]

    def top_rows(self, metric: str = "Sales_Amount", n: int = 10, order: str = "desc",
                 filters_json: str = "{}") -> list:
        """Get the top or bottom N individual orders sorted by a numeric metric.

        Args:
            metric: Sales_Amount, Profit, Quantity_Sold, or Profit_Margin.
            n: How many rows to return.
            order: "asc" for lowest first, "desc" for highest first.
            filters_json: JSON object string to restrict rows first, e.g.
                '{"Region": "North"}'. Use "{}" for no filter.
        """
        df = self._apply_filters(json.loads(filters_json or "{}"))
        df = df.sort_values(metric, ascending=(order == "asc")).head(n)
        cols = ["Sale_Date", "Sales_Rep", "Region", "Product_Category",
                "Sales_Amount", "Quantity_Sold", "Profit", "Profit_Margin"]
        return df[cols].round(2).to_dict(orient="records")

    def filtered_summary(self, filters_json: str) -> dict:
        """Get totals (sales, profit, quantity, avg margin, row count) for orders
        matching a filter.

        Args:
            filters_json: JSON object string, e.g.
                '{"Region": "North", "Product_Category": "Furniture"}'.
        """
        df = self._apply_filters(json.loads(filters_json or "{}"))
        total_sales = float(df["Sales_Amount"].sum())
        total_profit = float(df["Profit"].sum())
        return {
            "matching_rows": len(df),
            "total_sales": round(total_sales, 2),
            "total_profit": round(total_profit, 2),
            "total_quantity": int(df["Quantity_Sold"].sum()) if len(df) else 0,
            "avg_margin_pct": round(100 * total_profit / total_sales, 2) if total_sales else 0,
        }

    def _apply_filters(self, filters: dict) -> pd.DataFrame:
        df = self.df
        for field, value in (filters or {}).items():
            if field in df.columns:
                df = df[df[field].astype(str).str.lower() == str(value).lower()]
        return df

    # ------------------------------------------------------------------
    def ask(self, question: str) -> str:
        """Ask a natural-language question about the sales data. Returns Gemini's answer."""
        response = self.chat.send_message(question)
        return response.text.strip()


def main():
    if len(sys.argv) < 2:
        print("Usage: python sales_ai_agent_gemini.py <path_to_csv>")
        sys.exit(1)

    if not os.environ.get("GEMINI_API_KEY"):
        print("Set your GEMINI_API_KEY environment variable first.")
        sys.exit(1)

    agent = SalesAgent(sys.argv[1])
    print(f"Loaded {len(agent.df)} rows. Ask questions about your sales data (type 'exit' to quit).\n")
    while True:
        question = input("You: ").strip()
        if question.lower() in {"exit", "quit"}:
            break
        if not question:
            continue
        print("Agent:", agent.ask(question), "\n")


if __name__ == "__main__":
    main()

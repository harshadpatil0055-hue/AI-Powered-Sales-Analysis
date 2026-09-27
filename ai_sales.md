# 🤖 AI-Powered Sales Data Analyst

An end-to-end **Sales Data Analytics and AI project** that combines **Python, SQL, Power BI, and Generative AI** to analyze sales performance and provide intelligent answers to business questions.

The project transforms raw sales data into meaningful insights through data cleaning, exploratory data analysis, interactive dashboards, and an AI-powered Sales Assistant.

---

## 📌 Project Overview

The **AI-Powered Sales Data Analyst** helps businesses understand:

* 📈 Overall sales and profit performance
* 🌎 Sales by region
* 🛍️ Product and category performance
* 👥 Customer purchasing behavior
* 📦 Order and quantity trends
* 💰 Profit margins
* 🤖 AI-generated answers to sales-related questions

The project follows a complete data analytics workflow:

**Raw Data → Data Cleaning → SQL Analysis → EDA → Power BI Dashboard → AI Sales Assistant**

---

## 🎯 Objectives

* Clean and preprocess raw sales data.
* Perform exploratory data analysis using Python.
* Analyze sales data using SQL.
* Build interactive Power BI dashboards.
* Identify important sales and customer trends.
* Calculate important business KPIs.
* Integrate an AI assistant for natural-language sales analysis.
* Provide data-driven insights for business decision-making.

---

## 🛠️ Technologies Used

| Technology          | Purpose                    |
| ------------------- | -------------------------- |
| 🐍 Python           | Data cleaning and analysis |
| 🐼 Pandas           | Data manipulation          |
| 🔢 NumPy            | Numerical operations       |
| 📊 Matplotlib       | Data visualization         |
| 🎨 Seaborn          | Statistical visualization  |
| 🗄️ SQL / MySQL     | Data querying and analysis |
| 📈 Power BI         | Interactive dashboards     |
| 🤖 Generative AI    | AI Sales Assistant         |
| 📓 Jupyter Notebook | Development and analysis   |
| 💻 VS Code          | Development                |

---

## 📂 Project Structure

```text
AI-Powered-Sales-Data-Analyst/
│
├── Dataset/
│   └── sales_data.csv
│
├── Python/
│   ├── Data_Cleaning.ipynb
│   └── EDA.ipynb
│
├── SQL/
│   ├── create_table.sql
│   └── sales_queries.sql
│
├── PowerBI/
│   └── Sales_Dashboard.pbix
│
├── AI/
│   └── Sales_AI_Assistant.ipynb
│
├── Images/
│   ├── sales_overview.png
│   ├── product_analysis.png
│   └── customer_analysis.png
│
└── README.md
```

---

# 🔄 Project Workflow

### 1️⃣ Data Collection

The project starts with a raw sales dataset containing information such as:

* Order ID
* Order Date
* Customer
* Product
* Category
* Region
* Sales
* Quantity
* Profit

---

### 2️⃣ Data Cleaning

Python and Pandas were used to:

* Handle missing values
* Remove duplicate records
* Convert data types
* Format date columns
* Check inconsistent values
* Create calculated columns
* Validate the dataset

Example:

```python
import pandas as pd

df = pd.read_csv("sales_data.csv")

print(df.head())
print(df.info())
print(df.isnull().sum())
print(df.describe())
```

---

### 3️⃣ Exploratory Data Analysis

EDA was performed to identify:

* Sales trends
* Profit trends
* Regional performance
* Category performance
* Top-performing products
* Customer revenue
* Monthly sales patterns

Visualizations were created using:

```text
Matplotlib
Seaborn
```

---

# 🗄️ SQL Analysis

SQL was used to perform business-oriented analysis.

Examples of questions analyzed:

```sql
-- Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM sales;
```

```sql
-- Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM sales;
```

```sql
-- Sales by Region
SELECT Region, SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Region
ORDER BY Total_Sales DESC;
```

```sql
-- Top 5 Products
SELECT Product, SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Product
ORDER BY Total_Sales DESC
LIMIT 5;
```

---

# 📊 Power BI Dashboard

The Power BI dashboard contains **three main pages**.

## 📌 Page 1 — Sales Overview

### KPIs

* 💰 Total Sales
* 📈 Total Profit
* 📦 Total Orders

### Visualizations

* Sales Trend
* Sales by Region
* Sales by Category
* Monthly Sales Performance

---

## 📌 Page 2 — Product Analysis

### Analysis includes:

* 🏆 Top 10 Products
* Product Sales
* Product Profit
* Quantity Sold
* Category Performance

This page helps identify the products and categories contributing most to sales and profit.

---

## 📌 Page 3 — Customer Analysis

### Analysis includes:

* 👥 Top Customers
* Customer Revenue
* Orders per Customer
* Customer Segmentation
* Customer Purchasing Trends

---

# 🤖 AI Sales Assistant

The key feature of this project is the **Sales AI Assistant**.

Instead of manually searching through dashboards or writing SQL queries, users can ask questions in natural language.

### Example Questions

```text
What were our total sales?
```

```text
Which region generated the highest revenue?
```

```text
What are our top 5 products?
```

```text
Why did sales decrease in March?
```

```text
Which category has the highest profit margin?
```

The AI processes the sales data and generates a business-oriented response.

---

## 🔄 AI Assistant Workflow

```text
User Question
      ↓
Sales Dataset
      ↓
Data Processing
      ↓
AI / LLM
      ↓
Business Analysis
      ↓
Natural Language Answer
```

### Example

**User:**

> Which region generated the highest revenue?

**AI Sales Assistant:**

> The West region generated the highest revenue based on the available sales data.

---

# 📈 Key Business KPIs

The project focuses on important sales metrics such as:

### Total Sales

```text
Total Sales = SUM(Sales)
```

### Total Profit

```text
Total Profit = SUM(Profit)
```

### Total Orders

```text
Total Orders = COUNT(Order ID)
```

### Profit Margin

```text
Profit Margin = (Profit / Sales) × 100
```

### Average Order Value

```text
AOV = Total Sales / Total Orders
```

---

# 💡 Business Insights

The project can help businesses identify:

* Which regions generate the most revenue
* Which products perform best
* Which categories generate higher profits
* Changes in monthly sales
* High-value customers
* Low-performing products
* Profitability trends
* Potential reasons for changes in sales performance

---

# 🚀 Future Enhancements

Planned improvements include:

* 🔮 Sales forecasting
* 📊 Predictive analytics
* 🤖 Advanced AI Agent
* 💬 Conversational dashboard
* 🔍 Automatic anomaly detection
* 📧 Automated business reports
* ☁️ Cloud deployment
* 🔗 Power BI + AI integration
* 📱 Web-based Sales Analytics application

---

# 🧠 Skills Demonstrated

This project demonstrates practical knowledge of:

* Python
* Pandas
* NumPy
* Data Cleaning
* Exploratory Data Analysis
* Data Visualization
* SQL
* MySQL
* Power BI
* Dashboard Development
* KPI Analysis
* Business Intelligence
* Generative AI
* Prompt Engineering
* Data-driven Decision Making

---

# 📸 Dashboard Preview

### Sales Overview

![Sales Overview](Images/sales_overview.png)

### Product Analysis

![Product Analysis](Images/product_analysis.png)

### Customer Analysis

![Customer Analysis](Images/customer_analysis.png)

---

# 👨‍💻 Author

**Harshad Patil**

B.E. Computer Engineering
Pune, Maharashtra, India

### Skills

`Python` `SQL` `Power BI` `Pandas` `NumPy` `MySQL` `Data Analysis` `Generative AI`

---

⭐ If you find this project useful, consider giving the repository a star!

-- basic sql analysis

-- total sales
SELECT 
    SUM(Sales_Amount) AS Total_Sales
FROM sales;

-- total profit
SELECT 
    SUM(Profit) AS Total_Profit
FROM sales;

-- total quantity sold
SELECT 
    SUM(Quantity_Sold) AS Total_Quantity
FROM sales;

-- region analysis

-- sales by region
SELECT
    Region,
    SUM(Sales_Amount) AS Total_Sales
FROM sales
GROUP BY Region
ORDER BY Total_Sales DESC;

-- region by profit
SELECT
    Region,
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Region
ORDER BY Total_Profit DESC;

-- Region with highest sales
SELECT
    Region,
    SUM(Sales_Amount) AS Total_Sales
FROM sales
GROUP BY Region
ORDER BY Total_Sales DESC
LIMIT 1;

-- product category analysis

-- sales by category
SELECT
    Product_Category,
    SUM(Sales_Amount) AS Total_Sales
FROM sales
GROUP BY Product_Category
ORDER BY Total_Sales DESC;

-- profit by category
SELECT
    Product_Category,
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Product_Category
ORDER BY Total_Profit DESC;

-- average profit margin by category
SELECT
    Product_Category,
    ROUND(AVG(Profit_Margin), 2) AS Average_Profit_Margin
FROM sales
GROUP BY Product_Category
ORDER BY Average_Profit_Margin DESC;

-- sales representative analysis

-- sales by sales representative
SELECT
    Sales_Rep,
    SUM(Sales_Amount) AS Total_Sales
FROM sales
GROUP BY Sales_Rep
ORDER BY Total_Sales DESC;

-- top 5 sales representative
SELECT
    Sales_Rep,
    SUM(Sales_Amount) AS Total_Sales
FROM sales
GROUP BY Sales_Rep
ORDER BY Total_Sales DESC
LIMIT 5;

-- sales rep profit
SELECT
    Sales_Rep,
    SUM(Sales_Amount) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Sales_Rep
ORDER BY Total_Profit DESC;

-- monthly sales analysis

-- monthly sales
SELECT
    Year,
    Month,
    Month_Name,
    SUM(Sales_Amount) AS Total_Sales
FROM sales
GROUP BY Year, Month, Month_Name
ORDER BY Year, Month;

-- monthly profit
SELECT
    Year,
    Month,
    Month_Name,
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Year, Month, Month_Name
ORDER BY Year, Month;

-- customer analysis

-- sales by customer type
SELECT
    Customer_Type,
    SUM(Sales_Amount) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Customer_Type
ORDER BY Total_Sales DESC;

-- sales channel analysis

SELECT
    Sales_Channel,
    SUM(Sales_Amount) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Sales_Channel
ORDER BY Total_Sales DESC;

-- payment method analysis

SELECT
    Payment_Method,
    COUNT(*) AS Number_of_Orders,
    SUM(Sales_Amount) AS Total_Sales
FROM sales
GROUP BY Payment_Method
ORDER BY Total_Sales DESC;

-- discount analysis

-- average discount by analysis
SELECT
    Product_Category,
    ROUND(AVG(Discount), 2) AS Average_Discount
FROM sales
GROUP BY Product_Category
ORDER BY Average_Discount DESC;

-- discount vs profit
SELECT
    Discount,
    SUM(Sales_Amount) AS Total_Sales,
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Discount
ORDER BY Discount;

-- Classitying sales
SELECT
    Product_ID,
    Sales_Amount,
    CASE
        WHEN Sales_Amount >= 10000 THEN 'High Sales'
        WHEN Sales_Amount >= 5000 THEN 'Medium Sales'
        ELSE 'Low Sales'
    END AS Sales_Category
FROM sales;

-- finding high profit product
SELECT
    Product_ID,
    SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Product_ID
ORDER BY Total_Profit DESC
LIMIT 10;

-- finding product with low profit margin
SELECT
    Product_ID,
    AVG(Profit_Margin) AS Average_Profit_Margin
FROM sales
GROUP BY Product_ID
ORDER BY Average_Profit_Margin ASC
LIMIT 10;

-- ranking sales representative
SELECT
    Sales_Rep,
    SUM(Sales_Amount) AS Total_Sales,
    RANK() OVER (
        ORDER BY SUM(Sales_Amount) DESC
    ) AS Sales_Rank
FROM sales
GROUP BY Sales_Rep;

-- ranking sales representative region-wise
SELECT
    Region,
    Sales_Rep,
    SUM(Sales_Amount) AS Total_Sales,
    RANK() OVER (
        PARTITION BY Region
        ORDER BY SUM(Sales_Amount) DESC
    ) AS Region_Rank
FROM sales
GROUP BY Region, Sales_Rep;

-- sql view for power bi
CREATE VIEW sales_summary AS
SELECT
    Year,
    Month,
    Month_Name,
    Region,
    Product_Category,
    Sales_Channel,
    Customer_Type,
    SUM(Sales_Amount) AS Total_Sales,
    SUM(Total_Cost) AS Total_Cost,
    SUM(Profit) AS Total_Profit,
    SUM(Quantity_Sold) AS Total_Quantity,
    AVG(Profit_Margin) AS Avg_Profit_Margin
FROM sales
GROUP BY
    Year,
    Month,
    Month_Name,
    Region,
    Product_Category,
    Sales_Channel,
    Customer_Type;
    
-- checking sql view for power bi
SELECT *
FROM sales_summary
LIMIT 20;
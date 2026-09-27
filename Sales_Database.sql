CREATE DATABASE sales_db;

USE sales_db;

CREATE TABLE sales (
    Product_ID VARCHAR(50),
    Sale_Date DATE,
    Sales_Rep VARCHAR(100),
    Region VARCHAR(50),
    Sales_Amount DECIMAL(12,2),
    Quantity_Sold INT,
    Product_Category VARCHAR(100),
    Unit_Cost DECIMAL(12,2),
    Unit_Price DECIMAL(12,2),
    Customer_Type VARCHAR(50),
    Discount DECIMAL(10,2),
    Payment_Method VARCHAR(50),
    Sales_Channel VARCHAR(50),
    Region_and_Sales_Rep VARCHAR(150),
    Total_Cost DECIMAL(12,2),
    Profit DECIMAL(12,2),
    Profit_Margin DECIMAL(10,2),
    Year INT,
    Month INT,
    Month_Name VARCHAR(20),
    Quarter INT
);

show tables;

SELECT * 
FROM sales
LIMIT 10;

SELECT COUNT(*) AS total_records
FROM sales;

select * from sales;

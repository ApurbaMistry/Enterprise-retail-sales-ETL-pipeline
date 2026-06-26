-- Total Sales
SELECT SUM(Sales) AS Total_Sales
FROM sales;

-- Total Profit
SELECT SUM(Profit) AS Total_Profit
FROM sales;

-- Average Sales
SELECT AVG(Sales) AS Average_Sales
FROM sales;

-- Top 10 Highest Sales
SELECT *
FROM sales
ORDER BY Sales DESC
LIMIT 10;

-- Sales by Category
SELECT Category,
SUM(Sales) AS Total_Sales
FROM sales
GROUP BY Category;

-- Profit by Region
SELECT Region,
SUM(Profit) AS Total_Profit
FROM sales
GROUP BY Region;
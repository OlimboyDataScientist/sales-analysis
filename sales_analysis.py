# sales_analysis.py

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sqlite3

# Load dataset
df = pd.read_csv("data/superstore_sales.csv")

# Convert 'Order Date' to datetime
df['Order Date'] = pd.to_datetime(df['Order Date'])

# Basic overview
print("\nDataset Info:")
print(df.info())
print("\nMissing Values:")
print(df.isnull().sum())
print("\nSummary Statistics:")
print(df.describe())

# Create new columns
df['Year'] = df['Order Date'].dt.year
df['Month'] = df['Order Date'].dt.to_period('M').astype(str)

# Top 10 products by sales
print("\nTop 10 Sub-categories by Total Sales:")
print(df.groupby('Sub-category')['Sales'].sum().sort_values(ascending=False).head(10))

# Monthly sales trend
monthly_sales = df.groupby('Month')['Sales'].sum()
plt.figure(figsize=(12, 6))
monthly_sales.plot()
plt.title("Monthly Sales Trend")
plt.xlabel("Month")
plt.ylabel("Sales")
plt.xticks(rotation=45)
plt.tight_layout()
plt.savefig("visuals/Monthly Sales Trend.png")
plt.show()

# Sales by Region
region_sales = df.groupby('Region')['Sales'].sum()
sns.barplot(x=region_sales.index, y=region_sales.values)
plt.title("Sales by Region")
plt.ylabel("Sales")
plt.xlabel("Region")
plt.tight_layout()
plt.savefig("visuals/Sales by Region.png")
plt.show()

# Discount vs Profit
plt.figure(figsize=(8, 6))
sns.scatterplot(data=df, x='Discount', y='Profit')
plt.title("Discount vs Profit")
plt.tight_layout()
plt.savefig("visuals/discount_vs_profit.png")
plt.show()

# Save cleaned data for future use

#df.to_csv("superstore_sales_cleaned.csv", index=False)

# -----------------------------
# SQL ANALYSIS SECTION
# -----------------------------

# Create SQLite in-memory DB
# Create SQLite database file

#conn = sqlite3.connect("superstore_sales.db")  # Create a database file
#df.to_sql("sales", conn, index=False, if_exists='replace')  # Save the DataFrame to the database

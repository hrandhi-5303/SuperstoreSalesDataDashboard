import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load the dataset
file_path = 'superstore.csv'  # Adjust the filename if needed
sales_data = pd.read_csv(file_path)

# Quick look at the data
print(sales_data.head())
print(sales_data.info())

# Basic Sales Analysis: Total Sales by Region
region_sales = sales_data.groupby('Region')['Sales'].sum().reset_index()

# Visualization
plt.figure(figsize=(10, 6))
sns.barplot(x='Region', y='Sales', data=region_sales, hue='Region', palette='viridis', legend=False)
plt.title('Total Sales by Region')
plt.xlabel('Region')
plt.ylabel('Total Sales')
plt.show()


sales_data['Order.Date'] = pd.to_datetime(sales_data['Order.Date'])
monthly_sales = sales_data.groupby(sales_data['Order.Date'].dt.to_period('M')).sum().reset_index()

plt.figure(figsize=(12, 6))
sns.lineplot(x='Order.Date', y='Sales', data=monthly_sales)
plt.title('Monthly Sales Over Time')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()


top_products = sales_data.groupby('Product.Name')['Sales'].sum().sort_values(ascending=False).head(10)

plt.figure(figsize=(12, 6))
sns.barplot(x=top_products.values, y=top_products.index, palette='coolwarm')
plt.title('Top 10 Products by Sales')
plt.xlabel('Sales')
plt.ylabel('Product')
plt.tight_layout()
plt.show()


category_profit = sales_data.groupby('Category')['Profit'].sum().reset_index()

plt.figure(figsize=(8, 5))
sns.barplot(x='Category', y='Profit', data=category_profit, palette='muted')
plt.title('Profit by Product Category')
plt.xlabel('Category')
plt.ylabel('Profit')
plt.show()

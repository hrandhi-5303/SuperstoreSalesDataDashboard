import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Load Data
file_path = 'superstore.csv'
sales_data = pd.read_csv(file_path)

# Convert dates
sales_data['Order.Date'] = pd.to_datetime(sales_data['Order.Date'])

# Title and Sidebar Filters
st.title("📊 Superstore Sales Dashboard")
st.sidebar.header("Filter Options")

# Sidebar filters
region = st.sidebar.multiselect('Select Region:', options=sales_data['Region'].unique(), default=sales_data['Region'].unique())
category = st.sidebar.multiselect('Select Category:', options=sales_data['Category'].unique(), default=sales_data['Category'].unique())

# Filter data based on selection
filtered_data = sales_data[(sales_data['Region'].isin(region)) & (sales_data['Category'].isin(category))]

# Key Metrics
total_sales = int(filtered_data['Sales'].sum())
total_profit = int(filtered_data['Profit'].sum())
total_orders = filtered_data['Order.ID'].nunique()

st.metric("Total Sales", f"${total_sales:,}")
st.metric("Total Profit", f"${total_profit:,}")
st.metric("Total Orders", total_orders)

# Sales Over Time
st.subheader("Sales Over Time")
monthly_sales = filtered_data.groupby(filtered_data['Order.Date'].dt.to_period('M'))[['Sales', 'Profit', 'Quantity']].sum().reset_index()
monthly_sales['Order.Date'] = monthly_sales['Order.Date'].dt.to_timestamp()

fig, ax = plt.subplots(figsize=(10, 5))
sns.lineplot(x='Order.Date', y='Sales', data=monthly_sales, marker='o', ax=ax)
plt.title('Monthly Sales')
plt.xlabel('Month')
plt.ylabel('Sales')
plt.xticks(rotation=45)
st.pyplot(fig)

# Sales by Region
st.subheader("Sales by Region")
region_sales = filtered_data.groupby('Region')['Sales'].sum().sort_values(ascending=False).reset_index()

fig2, ax2 = plt.subplots(figsize=(8, 5))
sns.barplot(x='Sales', y='Region', data=region_sales, hue='Region', palette='viridis', ax=ax2, legend=False)
st.pyplot(fig2)

# Top Products
st.subheader("Top 5 Products by Sales")
top_products = filtered_data.groupby('Product.Name')['Sales'].sum().sort_values(ascending=False).head(5)

fig3, ax3 = plt.subplots(figsize=(10, 5))
sns.barplot(x=top_products.values, y=top_products.index, hue=top_products.index, palette='coolwarm', ax=ax3, legend=False)
st.pyplot(fig3)

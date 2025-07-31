import streamlit as st
import pandas as pd

df = pd.read_csv("data/superstore_sales.csv")

st.title('This is for analysis of sales data')
st.sidebar.header("Filter Options")

# Sidebar filters
categories = st.sidebar.multiselect(
    "Select Categories:",
    options=df["Product Category"].unique(),
    default=df["Product Category"].unique()
)

regions = st.sidebar.multiselect(
    "Select Regions:",
    options=df["Region"].unique(),
    default=df["Region"].unique()
)

# Filter dataframe
filtered_df = df[(df["Product Category"].isin(categories)) & (df["Region"].isin(regions))]

st.subheader("Filtered Data")
st.dataframe(filtered_df)

# Summary statistics
st.subheader("Summary Statistics")
st.write(filtered_df.describe())

# Visualizations
st.subheader("Sales by Product Category")
sales_by_category = filtered_df.groupby("Product Category")["Sales"].sum()
st.bar_chart(sales_by_category)

st.subheader("Sales by Region")
sales_by_region = filtered_df.groupby("Region")["Sales"].sum()
st.bar_chart(sales_by_region)

st.subheader("Profit vs Sales Scatter Plot")
st.scatter_chart(filtered_df, x="Sales", y="Profit", color="Product Category")

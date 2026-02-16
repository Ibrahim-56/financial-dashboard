
import streamlit as st
import pandas as pd
import plotly.express as px

st.set_page_config(page_title="Financial Dashboard", layout="wide")

# Load data
df = pd.read_csv("financial_dashboard_data.csv")

st.title("📊 Financial Performance Dashboard")

# KPI Cards
col1, col2, col3 = st.columns(3)
col1.metric("Total Revenue", f"{df['Revenue'].sum():,} SAR")
col2.metric("Total Expenses", f"{df['Expenses'].sum():,} SAR")
col3.metric("Total Profit", f"{df['Profit'].sum():,} SAR")

# Revenue Trend
fig1 = px.line(df, x="Month", y="Revenue", title="Revenue Trend")
st.plotly_chart(fig1, use_container_width=True)

# Expenses Trend
fig2 = px.line(df, x="Month", y="Expenses", title="Expenses Trend", color_discrete_sequence=["red"])
st.plotly_chart(fig2, use_container_width=True)

# Profit Bar Chart
fig3 = px.bar(df, x="Month", y="Profit", title="Monthly Profit", color="Profit", color_continuous_scale="greens")
st.plotly_chart(fig3, use_container_width=True)

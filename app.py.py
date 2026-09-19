import streamlit as st
import pandas as pd

# Page Configuration
st.set_page_config(page_title="Lead Analytics & Automation Dashboard", layout="wide")

st.title("📊 Verified Lead Intelligence & Analytics Dashboard")
st.write("Filter, search, and analyze target business leads in real-time.")

# Load Data
@st.cache_data
def load_data():
    return pd.read_csv("sample_leads.csv")

df = load_data()

# Sidebar Filters
st.sidebar.header("Filter Leads")
city_filter = st.sidebar.multiselect("Select City", options=df["City"].unique(), default=df["City"].unique())
category_filter = st.sidebar.multiselect("Select Category", options=df["Category"].unique(), default=df["Category"].unique())

filtered_df = df[(df["City"].isin(city_filter)) & (df["Category"].isin(category_filter))]

# Top Metrics
col1, col2, col3 = st.columns(3)
col1.metric("Total Leads", len(filtered_df))
col2.metric("Avg Rating", round(filtered_df["Google Rating"].mean(), 2) if not filtered_df.empty else 0)
col3.metric("Verified Businesses", len(filtered_df[filtered_df["Verified Status"] == "Verified"]))

# Data Table Display
st.subheader("📋 Lead Database")
st.dataframe(filtered_df, use_container_width=True)

# Download CSV
csv = filtered_df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Download Filtered Leads CSV",
    data=csv,
    file_name='extracted_leads.csv',
    mime='text/csv',
)
import streamlit as st
import pandas as pd
import os

# Page Config
st.set_page_config(
    page_title="B2B Lead Intelligence Dashboard",
    page_icon="🎯",
    layout="wide"
)

# Custom Styling
st.markdown("""
    <style>
    .main { background-color: #f8f9fa; }
    .stMetric { background-color: #ffffff; padding: 15px; border-radius: 10px; box-shadow: 0 2px 4px rgba(0,0,0,0.05); }
    </style>
""", unsafe_allow_html=True)

st.title("🎯 B2B Lead Intelligence & Prospecting Dashboard")
st.caption("Live Local Business Data, Google Ratings & Contact Extraction")

@st.cache_data
def load_data():
    file_path = "sample_leads.csv"
    if os.path.exists(file_path):
        df = pd.read_csv(file_path)
        df.columns = df.columns.str.strip()
        return df
    else:
        data = {
            "Business Name": ["Apex Digital Marketing", "Urban Living Real Estate", "FitLife Gym & Spa", "Verma & Sons Consultants", "Bright Sparks PR Agency"],
            "Category": ["Marketing Agency", "Real Estate", "Fitness", "Business Consultant", "PR Agency"],
            "City": ["Delhi", "Gurgaon", "Noida", "Delhi", "Gurgaon"],
            "Phone Number": ["+91 9876543210", "+91 9812345678", "+91 9998887776", "+91 9711223344", "+91 9555443322"],
            "Google Rating": [4.8, 4.5, 4.9, 4.2, 4.6],
            "Reviews Count": [120, 85, 210, 45, 95]
        }
        return pd.DataFrame(data)

df = load_data()

# --- SIDEBAR FILTERS ---
st.sidebar.header("🔍 Filter Prospects")

# Search Keyword
search_query = st.sidebar.text_input("Search Business Name", "")

# City Filter
if "City" in df.columns:
    cities = df["City"].unique().tolist()
    city_filter = st.sidebar.multiselect("Select Location", options=cities, default=cities)
    df = df[df["City"].isin(city_filter)]

# Category Filter
if "Category" in df.columns:
    categories = df["Category"].unique().tolist()
    category_filter = st.sidebar.multiselect("Select Niche / Industry", options=categories, default=categories)
    df = df[df["Category"].isin(category_filter)]

# Search Filter
if search_query and "Business Name" in df.columns:
    df = df[df["Business Name"].str.contains(search_query, case=False, na=False)]

# --- TOP METRICS ---
col1, col2, col3 = st.columns(3)
col1.metric("Verified Leads", len(df))
if "Google Rating" in df.columns and not df.empty:
    col2.metric("Avg Google Rating", f"⭐ {round(df['Google Rating'].mean(), 2)}")
if "Reviews Count" in df.columns and not df.empty:
    col3.metric("Total Reviews Scanned", f"💬 {df['Reviews Count'].sum()}")

st.divider()

# --- ANALYTICS CHARTS ---
if not df.empty and "Category" in df.columns and "City" in df.columns:
    c1, c2 = st.columns(2)
    with c1:
        st.subheader("📊 Leads Distribution by City")
        st.bar_chart(df["City"].value_counts())
    with c2:
        st.subheader("📈 Top Categories")
        st.bar_chart(df["Category"].value_counts())

st.divider()

# --- DATA TABLE ---
st.subheader("📋 Verified Business Directory")
st.dataframe(df, use_container_width=True)

# --- DOWNLOAD BUTTON ---
csv = df.to_csv(index=False).encode('utf-8')
st.download_button(
    label="📥 Export Verified Prospect List (CSV)",
    data=csv,
    file_name='targeted_b2b_leads.csv',
    mime='text/csv',
)

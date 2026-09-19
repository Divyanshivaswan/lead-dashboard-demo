import streamlit as st
import pandas as pd
import os

# Page Config
st.set_page_config(
    page_title="Leadno | B2B Prospect Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Complete Modern UI CSS with Compact Action Buttons matching Category Style
st.markdown("""
<style>
    /* Global Reset & Dark Background */
    .stApp {
        background-color: #0b0f17 !important;
        color: #e6edf3 !important;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, sans-serif;
    }
    
    /* Hide Streamlit Header & Footer */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
    header {visibility: hidden;}

    /* Navigation Header */
    .nav-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 0.8rem 0;
        border-bottom: 1px solid #21262d;
        margin-bottom: 1.5rem;
    }
    .brand-title {
        font-size: 1.3rem;
        font-weight: 800;
        color: #f0f6fc;
        letter-spacing: -0.03em;
    }
    .brand-tag {
        background: #1f6feb1a;
        color: #388bfd;
        border: 1px solid #1f6feb4d;
        font-size: 0.7rem;
        padding: 2px 8px;
        border-radius: 12px;
        font-weight: 600;
        margin-left: 8px;
    }

    /* Metric Cards */
    .metric-card {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 1rem;
        margin-bottom: 0.5rem;
        height: 100%;
    }
    .metric-label {
        font-size: 0.72rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #8b949e;
        font-weight: 600;
    }
    .metric-value {
        font-size: 1.4rem;
        font-weight: 700;
        color: #f0f6fc;
        margin-top: 0.2rem;
    }

    /* Search Input Box Styling (White Box) */
    .stTextInput div[data-baseweb="input"] {
        background-color: #ffffff !important;
        border: 1px solid #d0d7de !important;
        border-radius: 6px !important;
    }
    .stTextInput input {
        color: #24292f !important;
        -webkit-text-fill-color: #24292f !important;
    }
    .stTextInput input::placeholder {
        color: #57606a !important;
        -webkit-text-fill-color: #57606a !important;
    }
    
    /* Selectbox Styling */
    div[data-baseweb="select"] > div {
        background-color: #161b22 !important;
        color: #f0f6fc !important;
        border: 1px solid #30363d !important;
        border-radius: 6px !important;
    }

    /* Badges */
    .badge-cat {
        background: #21262d; 
        color: #8b949e; 
        border: 1px solid #30363d;
        padding: 3px 8px; 
        border-radius: 6px; 
        font-size: 0.75rem;
    }

    /* Compact Sleek Action Button matching Category style */
    .stButton button {
        background-color: #21262d !important;
        color: #58a6ff !important;
        border: 1px solid #30363d !important;
        border-radius: 6px !important;
        font-size: 0.75rem !important;
        font-weight: 500 !important;
        padding: 2px 10px !important;
        min-height: unset !important;
        width: 100%;
        transition: all 0.2s ease;
    }
    .stButton button:hover {
        background-color: #30363d !important;
        border-color: #58a6ff !important;
        color: #ffffff !important;
    }
</style>
""", unsafe_allow_html=True)

# Load CSV and safely map columns
@st.cache_data
def load_data():
    if os.path.exists("sample_leads.csv"):
        try:
            df = pd.read_csv("sample_leads.csv")
            records = []
            for idx, row in df.iterrows():
                records.append({
                    "id": idx,
                    "Business Name": str(row.get("Business Name", "Unknown Business")),
                    "Category": str(row.get("Category", "General")),
                    "Rating": str(row.get("Rating", "★ 4.5 (100)")),
                    "Location": str(row.get("Location", "Gurgaon")),
                    "Contact": str(row.get("Contact", "+91 98000 00000")),
                    "Decision Maker": str(row.get("Decision Maker", "Owner / Manager")),
                    "Pitch Angle": str(row.get("Pitch Angle", "Direct outreach for business expansion.")),
                    "Status": str(row.get("Status", "Verified"))
                })
            return records
        except Exception as e:
            st.error(f"Error reading CSV: {e}")
            
    # Fallback Default Data
    return [
        {
            "id": 0,
            "Business Name": "Clove Dental Gurgaon",
            "Category": "Dental Clinic",
            "Rating": "★ 4.8 (320)",
            "Location": "DLF Phase 4",
            "Contact": "+91 98101 23456",
            "Decision Maker": "Lead Dentist",
            "Pitch Angle": "Google Review automation & local SEO boost",
            "Status": "Verified"
        }
    ]

data = load_data()

# Header Section
st.markdown("""
    <div class="nav-header">
        <div>
            <span class="brand-title">LEADNO</span>
            <span class="brand-tag">B2B Intelligence Engine</span>
        </div>
        <div style="font-size: 0.8rem; color: #8b949e;">
            Pipeline Status: <b>Live Multi-Niche Scraper Active</b>
        </div>
    </div>
""", unsafe_allow_html=True)

# Metrics Grid
m1, m2, m3, m4 = st.columns(4)
total_records = len(data)

with m1:
    st.markdown(f'<div class="metric-card"><div class="metric-label">Total Leads</div><div class="metric-value">{total_records}</div></div>', unsafe_allow_html=True)
with m2:
    st.markdown(f'<div class="metric-card"><div class="metric-label">Niche Verticals</div><div class="metric-value">4 Active</div></div>', unsafe_allow_html=True)
with m3:
    st.markdown(f'<div class="metric-card"><div class="metric-label">Verification Rate</div><div class="metric-value">100%</div></div>', unsafe_allow_html=True)
with m4:
    st.markdown(f'<div class="metric-card"><div class="metric-label">Engine Status</div><div class="metric-value" style="color:#3fb950; font-size:1.1rem; margin-top:2px;">● Connected</div></div>', unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

# Instant Multi-Filters & Search Bar
c1, c2, c3 = st.columns([2.5, 1.3, 1.3])

with c1:
    search_query = st.text_input("Instant Search", placeholder="🔍 Search business name, location...", label_visibility="collapsed")

categories_list = ["All Categories"] + sorted(list(set(d.get("Category") for d in data)))
locations_list = ["All Locations"] + sorted(list(set(d.get("Location") for d in data)))

with c2:
    category_filter = st.selectbox("Category Filter", categories_list, label_visibility="collapsed")

with c3:
    location_filter = st.selectbox("Location Filter", locations_list, label_visibility="collapsed")

# Filtering Logic
filtered_leads = []
for lead in data:
    match_search = (
        search_query.lower() in lead["Business Name"].lower() or 
        search_query.lower() in lead["Location"].lower() or
        search_query.lower() in lead["Category"].lower() or
        search_query.lower() in lead["Pitch Angle"].lower()
    )
    match_cat = (category_filter == "All Categories") or (lead["Category"] == category_filter)
    match_loc = (location_filter == "All Locations") or (location_filter in lead["Location"])

    if match_search and match_cat and match_loc:
        filtered_leads.append(lead)

st.markdown("<br>", unsafe_allow_html=True)

# Table Header
st.markdown("""
<div style="display: grid; grid-template-columns: 2.2fr 1.3fr 1.2fr 1.5fr 1.5fr 1fr; padding: 10px 12px; font-size: 0.72rem; font-weight: 700; color: #8b949e; letter-spacing: 0.05em; border-bottom: 1px solid #30363d; margin-bottom: 8px;">
    <div>BUSINESS NAME</div>
    <div>CATEGORY</div>
    <div>RATING</div>
    <div>LOCATION</div>
    <div>CONTACT</div>
    <div style="text-align: right;">ACTION</div>
</div>
""", unsafe_allow_html=True)

# Render Rows
for idx, lead in enumerate(filtered_leads):
    cols = st.columns([2.2, 1.3, 1.2, 1.5, 1.5, 1])
    
    with cols[0]:
        st.markdown(f"<div style='padding-top: 6px; font-weight: 600; color: #f0f6fc;'>{lead.get('Business Name')}</div>", unsafe_allow_html=True)
    with cols[1]:
        st.markdown(f"<div style='padding-top: 6px;'><span class='badge-cat'>{lead.get('Category')}</span></div>", unsafe_allow_html=True)
    with cols[2]:
        st.markdown(f"<div style='padding-top: 6px; color:#d29922; font-weight:500;'>{lead.get('Rating')}</div>", unsafe_allow_html=True)
    with cols[3]:
        st.markdown(f"<div style='padding-top: 6px; color:#c9d1d9; font-size:0.85rem;'>{lead.get('Location')}</div>", unsafe_allow_html=True)
    with cols[4]:
        st.markdown(f"<div style='padding-top: 6px;'><code style='color:#58a6ff; background:#161b22; padding: 2px 6px; border-radius: 4px;'>{lead.get('Contact')}</code></div>", unsafe_allow_html=True)
    with cols[5]:
        if st.button("Inspect", key=f"btn_{idx}"):
            st.toast(f"Inspecting: {lead.get('Business Name')}", icon="⚡")

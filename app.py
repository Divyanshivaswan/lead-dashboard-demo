import streamlit as st
import pandas as pd
import json
st.set_page_config(
    page_title="Leadno | B2B Prospect Intelligence",
    page_icon="⚡",
    layout="wide",
    initial_sidebar_state="expanded"
)

st.markdown("""
<style>
    /* Main Background & Typography */
    .stApp {
        background-color: #0d1117;
        color: #c9d1d9;
        font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, Helvetica, Arial, sans-serif;
    }
    
    /* Clean Navbar Header */
    .nav-header {
        display: flex;
        align-items: center;
        justify-content: space-between;
        padding: 1rem 0rem 1.5rem 0rem;
        border-bottom: 1px solid #21262d;
        margin-bottom: 1.5rem;
    }
    .brand-title {
        font-size: 1.25rem;
        font-weight: 700;
        color: #f0f6fc;
        letter-spacing: -0.02em;
    }
    .brand-tag {
        background: #1f6feb22;
        color: #58a6ff;
        border: 1px solid #1f6feb44;
        font-size: 0.72rem;
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
        padding: 1.1rem;
        margin-bottom: 1rem;
    }
    .metric-label {
        font-size: 0.75rem;
        text-transform: uppercase;
        letter-spacing: 0.05em;
        color: #8b949e;
        font-weight: 600;
    }
    .metric-value {
        font-size: 1.6rem;
        font-weight: 700;
        color: #f0f6fc;
        margin-top: 0.3rem;
    }
    .metric-sub {
        font-size: 0.75rem;
        color: #3fb950;
        margin-top: 0.2rem;
        font-weight: 500;
    }

    /* Badge Pills */
    .badge-verified {
        background: #23863622;
        color: #3fb950;
        border: 1px solid #23863655;
        padding: 2px 8px;
        border-radius: 6px;
        font-size: 0.72rem;
        font-weight: 600;
    }
    .badge-category {
        background: #21262d;
        color: #8b949e;
        border: 1px solid #30363d;
        padding: 2px 8px;
        border-radius: 6px;
        font-size: 0.72rem;
    }

    /* Target Drawer Card inside Dialog */
    .drawer-box {
        background: #161b22;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 1.25rem;
        margin-top: 1rem;
    }
    .pitch-box {
        background: #0d1117;
        border-left: 3px solid #58a6ff;
        padding: 0.85rem;
        border-radius: 4px;
        font-size: 0.85rem;
        color: #d2a8ff;
        margin-top: 0.75rem;
    }

    /* Hide default Streamlit elements */
    #MainMenu {visibility: hidden;}
    footer {visibility: hidden;}
</style>
""", unsafe_allow_html=True)

@st.cache_data
def load_data():
    return pd.read_csv("sample_leads.csv").to_dict(orient="records")

data = load_data()

st.markdown("""
    <div class="nav-header">
        <div>
            <span class="brand-title">LEADNO</span>
            <span class="brand-tag">B2B Intelligence</span>
        </div>
        <div style="font-size: 0.8rem; color: #8b949e;">
            Regional Dataset: <b>Delhi NCR</b> | Active Pipeline
        </div>
    </div>
""", unsafe_allow_html=True)

m1, m2, m3, m4 = st.columns(4)

with m1:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Extracted Records</div>
            <div class="metric-value">1,482</div>
            <div class="metric-sub">↑ 18% this week</div>
        </div>
    """, unsafe_allow_html=True)

with m2:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Verified Contact Match</div>
            <div class="metric-value">98.4%</div>
            <div class="metric-sub">Direct phone numbers</div>
        </div>
    """, unsafe_allow_html=True)

with m3:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-label">High Trust Ratings</div>
            <div class="metric-value">895</div>
            <div class="metric-sub">4.0+ Star Businesses</div>
        </div>
    """, unsafe_allow_html=True)

with m4:
    st.markdown("""
        <div class="metric-card">
            <div class="metric-label">Est. Outreach Value</div>
            <div class="metric-value">₹4.2 Lakhs</div>
            <div class="metric-sub">B2B Deal Potential</div>
        </div>
    """, unsafe_allow_html=True)

st.markdown("<br>", unsafe_allow_html=True)

c1, c2, c3, c4 = st.columns([2, 1, 1, 1])

with c1:
    search_query = st.text_input("Search Business", placeholder="Search by name, location, keyword...", label_visibility="collapsed")

with c2:
    category_filter = st.selectbox("Category", ["All Categories", "Real Estate", "Gym & Fitness", "Healthcare", "Interior Design", "Education"], label_visibility="collapsed")

with c3:
    location_filter = st.selectbox("Location", ["All Locations", "Gurugram", "South Delhi", "Noida", "Faridabad"], label_visibility="collapsed")

with c4:
    rating_filter = st.selectbox("Rating", ["All Ratings", "4.5+ Stars", "4.0+ Stars"], label_visibility="collapsed")

filtered_leads = []
for lead in data:
    match_search = search_query.lower() in lead["name"].lower() or search_query.lower() in lead["location"].lower()
    match_cat = (category_filter == "All Categories") or (lead["category"] == category_filter)
    match_loc = (location_filter == "All Locations") or (location_filter in lead["location"])
    
    match_rat = True
    if rating_filter == "4.5+ Stars" and lead["rating"] < 4.5:
        match_rat = False
    elif rating_filter == "4.0+ Stars" and lead["rating"] < 4.0:
        match_rat = False

    if match_search and match_cat and match_loc and match_rat:
        filtered_leads.append(lead)

@st.dialog("Sales Intelligence Detail")
def show_lead_details(lead):
    st.markdown(f"### {lead['name']}")
    st.caption(f"{lead['category']} • {lead['location']}")
    
    st.markdown(f"""
        <div class="drawer-box">
            <div style="display: flex; justify-space-between; font-size: 0.85rem; margin-bottom: 8px;">
                <span style="color: #8b949e;">Phone Contact:</span>
                <b style="color: #58a6ff;">{lead['phone']}</b>
            </div>
            <div style="display: flex; justify-space-between; font-size: 0.85rem; margin-bottom: 8px;">
                <span style="color: #8b949e;">Target Decision Maker:</span>
                <b style="color: #f0f6fc;">{lead['decision_maker']}</b>
            </div>
            <div style="display: flex; justify-space-between; font-size: 0.85rem;">
                <span style="color: #8b949e;">Rating & Score:</span>
                <b style="color: #d29922;">★ {lead['rating']} ({lead['reviews']} reviews)</b>
            </div>
            <div class="pitch-box">
                <b>Recommended Pitch Angle:</b><br>
                "{lead['pitch_angle']}"
            </div>
        </div>
    """, unsafe_allow_html=True)
    
    st.markdown("<br>", unsafe_allow_html=True)
    if st.button("Copy Direct Outreach Script", use_container_width=True):
        st.toast("Pitch angle copied to clipboard!", icon="✅")

st.markdown(f"##### Showing {len(filtered_leads)} Verified Prospects")

# Custom Table Header
st.markdown("""
<div style="display: grid; grid-template-columns: 2.5fr 1.5fr 1.5fr 1.5fr 1.5fr 1fr; padding: 10px 12px; background: #161b22; border-radius: 6px; font-size: 0.75rem; font-weight: 600; color: #8b949e; margin-bottom: 8px;">
    <div>BUSINESS NAME</div>
    <div>CATEGORY</div>
    <div>RATING</div>
    <div>LOCATION</div>
    <div>CONTACT</div>
    <div style="text-align: right;">ACTION</div>
</div>
""", unsafe_allow_html=True)

# Table Rows
for lead in filtered_leads:
    col_a, col_b, col_c, col_d, col_e, col_f = st.columns([2.5, 1.5, 1.5, 1.5, 1.5, 1])
    
    with col_a:
        ver_tag = '<span class="badge-verified">Verified</span>' if lead["verified"] else ''
        st.markdown(f"<b>{lead['name']}</b> {ver_tag}", unsafe_allow_html=True)
        st.caption(lead["website"])
        
    with col_b:
        st.markdown(f"<span class='badge-category'>{lead['category']}</span>", unsafe_allow_html=True)
        
    with col_c:
        st.markdown(f"<span style='color:#d29922;'>★ {lead['rating']}</span> <span style='color:#8b949e; font-size:0.75rem;'>({lead['reviews']})</span>", unsafe_allow_html=True)
        
    with col_d:
        st.markdown(f"<span style='font-size:0.85rem;'>{lead['location']}</span>", unsafe_allow_html=True)
        
    with col_e:
        st.markdown(f"<code style='color:#58a6ff;'>{lead['phone']}</code>", unsafe_allow_html=True)
        
    with col_f:
        if st.button("Inspect", key=f"btn_{lead['id']}", use_container_width=True):
            show_lead_details(lead)
            
    st.markdown("<hr style='margin: 4px 0px; border-color: #21262d;'>", unsafe_allow_html=True)

with st.sidebar:
    st.markdown("### Request Custom List")

import streamlit as st
from core.scoring import get_recommendations
from ui.results import display_results
st.markdown("""
<style>
    .stApp {
        background: linear-gradient(180deg, #FFFFFF 0%, #F0F5FF 100%);
    }
    .stButton>button {
        background-color: #2563EB;
        color: white;
        border-radius: 8px;
        padding: 0.6em 1.5em;
        border: none;
        font-weight: 600;
    }
    .stButton>button:hover {
        background-color: #1D4ED8;
        color: white;
    }
    div[data-testid="stExpander"] {
        border: 1px solid #E2E8F0;
        border-radius: 12px;
        margin-bottom: 12px;
        background-color: #FAFBFF;
    }
    h1, h2, h3 {
        color: #1E293B;
    }
</style>
""", unsafe_allow_html=True)
st.set_page_config(page_title="Meritly", page_icon="🎓", layout="centered")st.markdown('<meta name="google-site-verification" content="<meta name="google-site-verification" content="uNK9gFMssRhyKHO07pbFelFQTcux-NmFx4sjOh6ks1s" />" />', unsafe_allow_html=True)

st.title("🎓 Meritly")
st.subheader("Find the right engineering college for you — not just a predicted one.")

st.divider()

st.write("Tell us about your exam result, and we'll help you build a confident shortlist.")

exam = st.selectbox("Which exam did you give?", ["MHT-CET", "JEE Main"])
percentile = st.number_input("Your percentile", min_value=0.0, max_value=100.0, step=0.01)
category = st.selectbox("Category", ["Open", "OBC", "SC", "ST", "EWS", "VJ/NT", "Other"])
branch = st.selectbox("Preferred branch", ["Computer Science", "AI & ML", "Mechanical", "Civil", "Electronics", "Other"])
cities = st.multiselect("Preferred cities", ["Pune", "Mumbai", "Nagpur", "Nashik", "Aurangabad", "Any"])

submitted = st.button("Find My Colleges")

if submitted:
    results = get_recommendations(percentile, branch, cities)
    st.success(f"Found {len(results['Dream'])} Dream, {len(results['Likely'])} Likely, and {len(results['Safe'])} Safe colleges for you.")
    display_results(results)
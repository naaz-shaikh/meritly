import streamlit as st
from core.scoring import get_recommendations
from ui.results import display_results
st.set_page_config(page_title="Meritly", page_icon="🎓", layout="centered")

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
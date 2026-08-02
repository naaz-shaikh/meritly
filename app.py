import streamlit as st

st.title("Meritly")
st.write("Find engineering colleges based on your percentile")

percentile = st.number_input(
    "Enter your percentile",
    min_value=0.0,
    max_value=100.0
)

branch = st.selectbox(
    "Choose preferred branch",
    ["Computer Engineering", "IT", "AI/DS", "Mechanical", "Electronics"]
)

city = st.selectbox(
    "Preferred city",
    ["Mumbai", "Pune", "Nashik", "Nagpur", "Any"]
)

if percentile:
    st.write(f"Your percentile is: {percentile}")
    st.write(f"Preferred branch: {branch}")
    st.write(f"Preferred city: {city}")
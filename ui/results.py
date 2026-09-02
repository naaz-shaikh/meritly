import streamlit as st


def render_college_card(college):
    """
    Displays one college's full details in a clean expandable card.
    Takes a single college dictionary (one entry from our results list).
    """
    # The header line shown even when the card is collapsed
    score = college['score']
    if score >= 80:
        badge = "🟢"
    elif score >= 60:
        badge = "🟡"
    else:
        badge = "🔴"

    header = f"{badge} {college['college_name']} — {college['branch']} · Score: {score}/100"

    with st.expander(header):
                col1, col2 = st.columns(2)

    with col1:
                st.write(f"**City:** {college['city']}")
                st.write(f"**Cutoff Percentile:** {college['cutoff_percentile']}")
                st.write(f"**Annual Fees:** ₹{college['fees_annual']:,}")
                st.write(f"**NAAC Grade:** {college['naac_grade']}")
                st.write(f"**NBA Accredited:** {college['nba_accredited']}")

    with col2:
            st.write(f"**Average Package:** {college['avg_package_lpa']} LPA")
            st.write(f"**Highest Package:** {college['highest_package_lpa']} LPA")
            st.write(f"**Placement Rate:** {college['placement_percentage']}%")
            st.write(f"**Hostel Available:** {college['hostel_available']}")
            st.write(f"[Visit Website]({college['website']})")

            st.write(f"✅ **Pros:** {college['pros']}")
            st.write(f"⚠️ **Cons:** {college['cons']}")


def display_results(results):
    """
    Takes the full results dictionary (Dream/Likely/Safe lists)
    and renders each category as a labeled section of cards.
    If a category has zero colleges, we skip showing an empty section.
    """
    section_info = {
        "Dream": "🌟 Dream Colleges — a stretch, but worth aiming for",
        "Likely": "🎯 Likely Colleges — your realistic sweet spot",
        "Safe": "🛡️ Safe Colleges — you should comfortably get in"
    }

    for category, label in section_info.items():
        colleges = results[category]

        if len(colleges) == 0:
            continue  # don't show an empty, confusing section

        st.subheader(label)
        for college in colleges:
            render_college_card(college)
        st.divider()
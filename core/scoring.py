import pandas as pd


def classify_college(user_percentile, cutoff_percentile):
    """
    Decides if a college is a Dream, Likely, or Safe option
    based on the gap between the student's percentile and the college's cutoff.
    Returns None if the college is unrealistic to include at all.
    """
    gap = user_percentile - cutoff_percentile

    if gap < -2:
        return None  # too far out of reach, don't show it at all
    elif gap < 0:
        return "Dream"
    elif gap < 3:
        return "Likely"
    else:
        return "Safe"


def naac_to_score(grade):
    """
    Converts a NAAC letter grade into a 0-10 numeric score,
    so it can be combined mathematically with other factors.
    """
    grade_map = {
        "A++": 10,
        "A+": 8.5,
        "A": 7,
        "B++": 5,
        "B+": 4,
        "B": 3
    }
    return grade_map.get(grade, 3)  # default to 3 if grade is unrecognized


def calculate_score(row, preferred_branch, preferred_cities):
    """
    Calculates a 0-100 recommendation score for a single college row,
    based on placement, package, branch match, city match, and NAAC grade.
    """
    # Placement percentage is already 0-100, so we use it directly, weighted at 35%
    placement_score = row["placement_percentage"] * 0.35

    # Average package: we cap comparison at 15 LPA so no single college dominates the score
    package_score = min(row["avg_package_lpa"] / 15, 1) * 100 * 0.25

    # Branch match: full points if exact match, else zero
    branch_score = 100 * 0.20 if row["branch"] == preferred_branch else 0

    # City match: full points if student picked "Any" or the college's city is in their list
    if "Any" in preferred_cities or row["city"] in preferred_cities:
        city_score = 100 * 0.10
    else:
        city_score = 0

    # NAAC grade converted to a 0-10 scale, then stretched to match the 0-100 scoring system
    naac_score = (naac_to_score(row["naac_grade"]) / 10) * 100 * 0.10

    total_score = placement_score + package_score + branch_score + city_score + naac_score
    return round(total_score, 1)


def get_recommendations(user_percentile, preferred_branch, preferred_cities):
    """
    Main function the app calls. Takes the student's inputs,
    loads the dataset, classifies each college, scores it,
    and returns three separate lists: dream, likely, safe.
    """
    from core.data_loader import load_colleges
    df = load_colleges()

    results = {"Dream": [], "Likely": [], "Safe": []}

    for _, row in df.iterrows():
        category = classify_college(user_percentile, row["cutoff_percentile"])
        if category is None:
            continue  # skip unrealistic colleges entirely

        score = calculate_score(row, preferred_branch, preferred_cities)

        college_data = row.to_dict()
        college_data["score"] = score

        results[category].append(college_data)

    # Sort each category by score, highest first
    for category in results:
        results[category] = sorted(results[category], key=lambda x: x["score"], reverse=True)

    return results
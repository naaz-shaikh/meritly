# 🎓 Meritly

**An Engineering College Decision Platform for MHT-CET students.**

Meritly isn't a college predictor — it's a decision-support tool. Instead of just telling students their odds, it helps them build a confident, personalized shortlist of Dream, Likely, and Safe colleges based on their percentile, category, preferred branch, and city.

🔗 **Live app:** [meritly.streamlit.app](https://meritly.streamlit.app)
![Meritly Screenshot](screenshot.png)

## Why I built this

Every year, thousands of MHT-CET students in Maharashtra make one of the biggest decisions of their lives — which engineering college to attend — based on scattered PDFs, rumors, and guesswork. Meritly brings that decision-making into one clean, data-driven place.

## How it works

Students enter their MHT-CET percentile, category, preferred branch, and cities. Meritly classifies colleges into three categories based on cutoff gap, then ranks each one using a weighted recommendation score built from:

- Placement percentage (35%)
- Average package (25%)
- Branch match (20%)
- City match (10%)
- NAAC accreditation grade (10%)

## Tech stack

- **Frontend/Backend:** Python, Streamlit
- **Data:** Pandas, CSV (SQLite planned)
- **Deployment:** Streamlit Community Cloud

## Roadmap

- [x] Core recommendation engine
- [x] Live deployment
- [ ] Category-wise cutoffs (OBC/SC/ST/EWS)
- [ ] College comparison tool
- [ ] Student reviews
- [ ] CAP priority list generator

## About me

Built by Naaz Shaikh, a Class 12 student from Maharashtra preparing for MHT-CET 2027, while learning software development from scratch.

import streamlit as st
import pandas as pd

from src.recommendation_engine import get_eligible_schemes
from src.ai_explainer import explain_scheme

# ==========================================
# PAGE CONFIG
# ==========================================

st.set_page_config(
    page_title="Government Scheme Eligibility Assistant",
    page_icon="🏛️",
    layout="wide"
)

# ==========================================
# LOAD DATA
# ==========================================

try:
    df = pd.read_csv("data/schemes.csv")
except Exception as e:
    st.error(f"Error loading dataset: {e}")
    st.stop()

# ==========================================
# TITLE
# ==========================================

st.title("AI-Powered Government Scheme Eligibility Assistant")

st.markdown("""
Enter your details to discover government schemes
for which you may be eligible.
""")

st.divider()

# ==========================================
# DROPDOWN DATA
# ==========================================

states = sorted(
    [s for s in df["state"].unique() if s != "All"]
)

occupations = sorted(
    df["occupation"].unique()
)

educations = sorted(
    df["education"].unique()
)

categories = sorted(
    set(
        item.strip()
        for cat in df["category"].unique()
        for item in str(cat).split("/")
    )
)

# ==========================================
# USER INPUT
# ==========================================

col1, col2 = st.columns(2)

with col1:

    age = st.number_input(
        "Age",
        min_value=0,
        max_value=100,
        value=20
    )

    income = st.number_input(
        "Annual Income (Rs.)",
        min_value=0,
        value=200000
    )

    state = st.selectbox(
        "State",
        states
    )

with col2:

    occupation = st.selectbox(
        "Occupation",
        occupations
    )

    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )

    category = st.selectbox(
        "Category",
        categories
    )

    education = st.selectbox(
        "Education",
        educations
    )

# ==========================================
# SEARCH BUTTON
# ==========================================

if st.button("Find Eligible Schemes"):

    try:

        schemes = get_eligible_schemes(
            age=age,
            income=income,
            state=state,
            occupation=occupation,
            gender=gender,
            category=category,
            education=education
        )

        if len(schemes) == 0:

            st.warning(
                "No eligible schemes found."
            )

        else:

            st.success(
                f"{len(schemes)} eligible scheme(s) found."
            )

            for scheme in schemes:

                scheme_name = scheme["Scheme Name"]

                st.subheader(
                    scheme_name
                )

                st.write(
                    f"Benefit: {scheme['Benefit']}"
                )

                try:

                    explanation = explain_scheme(
                        scheme_name=scheme_name,
                        age=age,
                        income=income,
                        state=state,
                        occupation=occupation,
                        gender=gender,
                        category=category,
                        education=education
                    )

                    st.text(explanation)

                except Exception as exp_error:

                    st.error(
                        f"Explanation Error: {exp_error}"
                    )

                st.divider()

    except Exception as e:

        st.error(
            f"Application Error: {e}"
        )

# ==========================================
# SIDEBAR
# ==========================================

st.sidebar.title("About")

st.sidebar.info("""
AI-Powered Government Scheme
Eligibility Assistant

Technology Used:

- Python
- Pandas
- Streamlit
- Scikit-Learn
- Machine Learning
""")
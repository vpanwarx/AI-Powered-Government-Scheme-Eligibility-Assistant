# ==========================================
# AI Government Scheme Eligibility Assistant
# AI Explainer Module
# ==========================================

import pandas as pd

# ==========================================
# LOAD DATASET
# ==========================================

try:

    df = pd.read_csv(
        "data/schemes.csv"
    )

except Exception as e:

    print(
        f"Dataset Loading Error: {e}"
    )

    df = pd.DataFrame()

# ==========================================
# EXPLAIN SCHEME
# ==========================================

def explain_scheme(
    scheme_name,
    age,
    income,
    state,
    occupation,
    gender,
    category,
    education
):

    try:

        scheme = df[
            df["scheme_name"] == scheme_name
        ]

        if scheme.empty:

            return (
                "No explanation available."
            )

        scheme = scheme.iloc[0]

        explanation = f"""
Scheme Name:
{scheme['scheme_name']}

Why You Are Eligible:

- Age: {age}
- Income: Rs. {income}
- State: {state}
- Occupation: {occupation}
- Gender: {gender}
- Category: {category}
- Education: {education}

Benefit:

{scheme['benefit']}

Eligibility Criteria:

- Age Range:
  {scheme['min_age']} to {scheme['max_age']}

- Maximum Income:
  Rs. {scheme['income_limit']}
"""

        return explanation

    except Exception as e:

        return (
            f"Explanation Error: {e}"
        )

# ==========================================
# MATCH SCORE
# ==========================================

def calculate_match_score(
    age,
    income,
    scheme_name
):

    try:

        scheme = df[
            df["scheme_name"] == scheme_name
        ]

        if scheme.empty:

            return 50

        scheme = scheme.iloc[0]

        score = 100

        if income > scheme["income_limit"]:

            score -= 30

        if age < scheme["min_age"]:

            score -= 20

        if age > scheme["max_age"]:

            score -= 20

        return max(score, 50)

    except:

        return 50

# ==========================================
# SHORT EXPLANATION
# ==========================================

def get_short_explanation(
    scheme_name
):

    try:

        scheme = df[
            df["scheme_name"] == scheme_name
        ]

        if scheme.empty:

            return (
                "Information unavailable."
            )

        scheme = scheme.iloc[0]

        return (
            f"{scheme['scheme_name']} provides "
            f"{scheme['benefit']}."
        )

    except:

        return (
            "Information unavailable."
        )

# ==========================================
# TESTING
# ==========================================

if __name__ == "__main__":

    print(

        explain_scheme(

            scheme_name="PM Scholarship",

            age=20,

            income=200000,

            state="Uttar Pradesh",

            occupation="Student",

            gender="Male",

            category="General",

            education="12th Pass"

        )

    )
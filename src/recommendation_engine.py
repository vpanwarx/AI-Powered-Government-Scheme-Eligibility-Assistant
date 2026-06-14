import pandas as pd

# Load dataset
df = pd.read_csv("data/schemes.csv")

education_levels = {
    "Any": 0,
    "8th Pass": 1,
    "10th Pass": 2,
    "12th Pass": 3,
    "Graduate": 4
}

def get_eligible_schemes(
    age,
    income,
    state,
    occupation,
    gender,
    category,
    education
):

    eligible_schemes = []

    user_education_level = education_levels.get(
        education,
        0
    )

    for _, scheme in df.iterrows():

        if age < scheme["min_age"]:
            continue

        if age > scheme["max_age"]:
            continue

        if income > scheme["income_limit"]:
            continue

        if scheme["state"] != "All":
            if scheme["state"].lower() != state.lower():
                continue

        if scheme["occupation"].lower() != occupation.lower():
            continue

        if scheme["gender"] != "All":
            if scheme["gender"].lower() != gender.lower():
                continue

        if scheme["category"] != "General":

            scheme_categories = [
                x.strip().upper()
                for x in str(
                    scheme["category"]
                ).split("/")
            ]

            if category.upper() not in scheme_categories:
                continue

        required_level = education_levels.get(
            scheme["education"],
            0
        )

        if user_education_level < required_level:
            continue

        eligible_schemes.append({

            "Scheme Name":
                scheme["scheme_name"],

            "Benefit":
                scheme["benefit"]

        })

    return eligible_schemes


if __name__ == "__main__":

    results = get_eligible_schemes(

        age=20,

        income=200000,

        state="Uttar Pradesh",

        occupation="Student",

        gender="Male",

        category="General",

        education="12th Pass"

    )

    print(results)
# ==========================================
# AI Government Scheme Eligibility Assistant
# Model Predictor
# ==========================================

import joblib
import pandas as pd
import os

# ==========================================
# LOAD MODEL FILES
# ==========================================

required_files = [

    "models/scheme_recommendation_model.pkl",

    "models/state_encoder.pkl",

    "models/occupation_encoder.pkl",

    "models/gender_encoder.pkl",

    "models/category_encoder.pkl",

    "models/education_encoder.pkl"

]

for file in required_files:

    if not os.path.exists(file):

        raise FileNotFoundError(
            f"Missing file: {file}"
        )

model = joblib.load(
    "models/scheme_recommendation_model.pkl"
)

state_encoder = joblib.load(
    "models/state_encoder.pkl"
)

occupation_encoder = joblib.load(
    "models/occupation_encoder.pkl"
)

gender_encoder = joblib.load(
    "models/gender_encoder.pkl"
)

category_encoder = joblib.load(
    "models/category_encoder.pkl"
)

education_encoder = joblib.load(
    "models/education_encoder.pkl"
)

# ==========================================
# SAFE ENCODER
# ==========================================

def safe_transform(
    encoder,
    value
):

    classes = list(
        encoder.classes_
    )

    if value in classes:

        return encoder.transform(
            [value]
        )[0]

    # fallback

    if "All" in classes:

        return encoder.transform(
            ["All"]
        )[0]

    return 0

# ==========================================
# PREDICT FUNCTION
# ==========================================

def predict_scheme(

    state,
    occupation,
    gender,
    category,
    education,
    age,
    income

):

    try:

        state_encoded = safe_transform(
            state_encoder,
            state
        )

        occupation_encoded = safe_transform(
            occupation_encoder,
            occupation
        )

        gender_encoded = safe_transform(
            gender_encoder,
            gender
        )

        category_encoded = safe_transform(
            category_encoder,
            category
        )

        education_encoded = safe_transform(
            education_encoder,
            education
        )

        user_data = pd.DataFrame({

            "state_encoded":
                [state_encoded],

            "occupation_encoded":
                [occupation_encoded],

            "gender_encoded":
                [gender_encoded],

            "category_encoded":
                [category_encoded],

            "education_encoded":
                [education_encoded],

            "min_age":
                [age],

            "max_age":
                [age],

            "income_limit":
                [income]

        })

        prediction = model.predict(
            user_data
        )

        return prediction[0]

    except Exception as e:

        return f"Prediction Error: {e}"

# ==========================================
# TEST
# ==========================================

if __name__ == "__main__":

    result = predict_scheme(

        state="Uttar Pradesh",

        occupation="Student",

        gender="Male",

        category="General",

        education="12th Pass",

        age=20,

        income=200000

    )

    print("\nRecommended Scheme:")

    print(result)
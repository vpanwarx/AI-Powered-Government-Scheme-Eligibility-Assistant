# ==========================================
# AI Government Scheme Eligibility Assistant
# Phase 3 - Machine Learning Model Training
# ==========================================

import pandas as pd
import joblib
import os

from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score

# ==========================================
# CREATE MODELS FOLDER
# ==========================================

os.makedirs("models", exist_ok=True)

print("=" * 60)
print("PHASE 3 : MACHINE LEARNING MODEL TRAINING")
print("=" * 60)

# ==========================================
# LOAD PROCESSED DATASET
# ==========================================

try:

    df = pd.read_csv(
        "processed_data/clean_schemes.csv"
    )

    print("\nDataset Loaded Successfully")

except Exception as e:

    print("\nError Loading Dataset")
    print(e)

    exit()

# ==========================================
# DATASET INFO
# ==========================================

print("\nDataset Shape:")
print(df.shape)

print("\nFirst 5 Rows:")
print(df.head())

# ==========================================
# CHECK REQUIRED COLUMNS
# ==========================================

required_columns = [

    "state_encoded",
    "occupation_encoded",
    "gender_encoded",
    "category_encoded",
    "education_encoded",
    "min_age",
    "max_age",
    "income_limit",
    "scheme_name"

]

missing_columns = [
    col for col in required_columns
    if col not in df.columns
]

if missing_columns:

    print("\nMissing Columns:")
    print(missing_columns)

    exit()

# ==========================================
# FEATURES
# ==========================================

X = df[

    [
        "state_encoded",
        "occupation_encoded",
        "gender_encoded",
        "category_encoded",
        "education_encoded",
        "min_age",
        "max_age",
        "income_limit"
    ]

]

# ==========================================
# TARGET
# ==========================================

y = df["scheme_name"]

# ==========================================
# TRAIN TEST SPLIT
# ==========================================

X_train, X_test, y_train, y_test = train_test_split(

    X,
    y,

    test_size=0.20,

    random_state=42

)

print(
    f"\nTraining Samples: {len(X_train)}"
)

print(
    f"Testing Samples: {len(X_test)}"
)

# ==========================================
# MODEL
# ==========================================

model = RandomForestClassifier(

    n_estimators=300,

    max_depth=15,

    random_state=42

)

# ==========================================
# TRAIN MODEL
# ==========================================

model.fit(

    X_train,

    y_train

)

print("\nModel Training Completed")

# ==========================================
# PREDICTIONS
# ==========================================

y_pred = model.predict(

    X_test

)

# ==========================================
# ACCURACY
# ==========================================

accuracy = accuracy_score(

    y_test,

    y_pred

)

print(
    f"\nModel Accuracy: {accuracy * 100:.2f}%"
)

# ==========================================
# FEATURE IMPORTANCE
# ==========================================

importance_df = pd.DataFrame({

    "Feature": X.columns,

    "Importance":
        model.feature_importances_

})

importance_df = importance_df.sort_values(

    by="Importance",

    ascending=False

)

print("\nFeature Importance")

print(importance_df)

# ==========================================
# SAVE MODEL
# ==========================================

joblib.dump(
    model,
    "models/scheme_recommendation_model.pkl"
)

print("Model Saved Successfully")

# ==========================================
# SAMPLE PREDICTION
# ==========================================

sample = X.iloc[[0]]

prediction = model.predict(

    sample

)

print("\nSample Prediction")

print(
    "Predicted Scheme:",
    prediction[0]
)

# ==========================================
# FILES GENERATED
# ==========================================

print("\nGenerated Files")

print(
    "models/scheme_recommendation_model.pkl"
)

print("\nPHASE 3 COMPLETED SUCCESSFULLY")

print("=" * 60)
print("Training Finished Successfully")
print("Saving Model...")
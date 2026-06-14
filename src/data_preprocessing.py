# ==========================================
# AI Government Scheme Eligibility Assistant
# Phase 2 - Data Preprocessing
# ==========================================

import pandas as pd
import joblib
import os
import sys

from sklearn.preprocessing import LabelEncoder

# ==========================================
# UTF-8 SUPPORT
# ==========================================

try:
    sys.stdout.reconfigure(encoding="utf-8")
except:
    pass

# ==========================================
# CREATE REQUIRED FOLDERS
# ==========================================

os.makedirs("models", exist_ok=True)
os.makedirs("processed_data", exist_ok=True)

print("=" * 60)
print("PHASE 2 : DATA PREPROCESSING")
print("=" * 60)

# ==========================================
# LOAD DATASET
# ==========================================

try:

    df = pd.read_csv("data/schemes.csv")

    print("\nDataset Loaded Successfully")

except Exception as e:

    print("\nError Loading Dataset")
    print(e)

    exit()

# ==========================================
# DATASET OVERVIEW
# ==========================================

print("\nDataset Shape:")
print(df.shape)

print("\nColumn Names:")
print(df.columns.tolist())

# ==========================================
# REQUIRED COLUMNS
# ==========================================

required_columns = [

    "scheme_id",
    "scheme_name",
    "state",
    "occupation",
    "gender",
    "category",
    "education",
    "min_age",
    "max_age",
    "income_limit",
    "benefit"

]

missing_columns = [

    col for col in required_columns

    if col not in df.columns

]

if missing_columns:

    print("\nMissing Columns Found:")
    print(missing_columns)

    exit()

print("\nAll Required Columns Found")

# ==========================================
# REMOVE DUPLICATES
# ==========================================

duplicates = df.duplicated().sum()

print(f"\nDuplicate Records Found: {duplicates}")

df.drop_duplicates(inplace=True)

print(
    f"Records After Cleaning: {len(df)}"
)

# ==========================================
# HANDLE MISSING VALUES
# ==========================================

print("\nChecking Missing Values...")

for column in df.columns:

    if df[column].dtype == "object":

        df[column] = df[column].fillna(
            "Unknown"
        )

    else:

        df[column] = df[column].fillna(
            df[column].median()
        )

print("Missing Values Handled Successfully")

# ==========================================
# LABEL ENCODING
# ==========================================

state_encoder = LabelEncoder()

occupation_encoder = LabelEncoder()

gender_encoder = LabelEncoder()

category_encoder = LabelEncoder()

education_encoder = LabelEncoder()

# ==========================================
# ENCODE COLUMNS
# ==========================================

df["state_encoded"] = state_encoder.fit_transform(
    df["state"]
)

df["occupation_encoded"] = occupation_encoder.fit_transform(
    df["occupation"]
)

df["gender_encoded"] = gender_encoder.fit_transform(
    df["gender"]
)

df["category_encoded"] = category_encoder.fit_transform(
    df["category"]
)

df["education_encoded"] = education_encoder.fit_transform(
    df["education"]
)

print("\nEncoding Completed Successfully")

# ==========================================
# SAVE ENCODERS
# ==========================================

joblib.dump(
    state_encoder,
    "models/state_encoder.pkl"
)

joblib.dump(
    occupation_encoder,
    "models/occupation_encoder.pkl"
)

joblib.dump(
    gender_encoder,
    "models/gender_encoder.pkl"
)

joblib.dump(
    category_encoder,
    "models/category_encoder.pkl"
)

joblib.dump(
    education_encoder,
    "models/education_encoder.pkl"
)

print("\nEncoders Saved Successfully")

# ==========================================
# SAVE CLEAN DATASET
# ==========================================

df.to_csv(
    "processed_data/clean_schemes.csv",
    index=False
)

print(
    "\nProcessed Dataset Saved Successfully"
)

# ==========================================
# BASIC DATASET STATS
# ==========================================

print("\nDataset Statistics")

print(
    f"Total Schemes: {len(df)}"
)

print(
    f"Unique States: {df['state'].nunique()}"
)

print(
    f"Unique Occupations: {df['occupation'].nunique()}"
)

print(
    f"Unique Categories: {df['category'].nunique()}"
)

print(
    f"Unique Education Levels: {df['education'].nunique()}"
)

print(
    f"Minimum Age: {df['min_age'].min()}"
)

print(
    f"Maximum Age: {df['max_age'].max()}"
)

print(
    f"Maximum Income Limit: Rs. {df['income_limit'].max():,}"
)

print(
    f"Average Income Limit: Rs. {df['income_limit'].mean():,.2f}"
)

# ==========================================
# FILES GENERATED
# ==========================================

print("\nGenerated Files")

print(
    "processed_data/clean_schemes.csv"
)

print(
    "models/state_encoder.pkl"
)

print(
    "models/occupation_encoder.pkl"
)

print(
    "models/gender_encoder.pkl"
)

print(
    "models/category_encoder.pkl"
)

print(
    "models/education_encoder.pkl"
)

print("\nPHASE 2 COMPLETED SUCCESSFULLY")
print("=" * 60)
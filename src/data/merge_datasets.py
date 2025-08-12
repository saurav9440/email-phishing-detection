import os
import pandas as pd

# Paths
RAW_DATA_DIR = "data/raw"
PROCESSED_DATA_DIR = "data/processed"
OUTPUT_FILE = os.path.join(PROCESSED_DATA_DIR, "merged_dataset.csv")

# Known possible text columns (case-insensitive matching)
TEXT_COLUMNS = [
    "EmailText", 
    "message", 
    "body", 
    "text", 
    "content", 
    "Message", 
    "email", 
    "Email", 
    "raw_text",
    "text_combined"  # Added for phishing_email.csv
]


# List of datasets to merge
DATASETS = [
    "CEAS_08.csv",
    "Enron.csv",
    "Ling.csv",
    "Nazario.csv",
    "Nigerian_Fraud.csv",
    "phishing_email.csv",
    "SpamAssassin.csv"
]

all_dfs = []

# Ensure processed directory exists
os.makedirs(PROCESSED_DATA_DIR, exist_ok=True)

for file in DATASETS:
    path = os.path.join(RAW_DATA_DIR, file)
    if not os.path.exists(path):
        print(f"⚠️ File not found: {file}")
        continue

    print(f"📂 Reading {file} ...")
    try:
        df = pd.read_csv(path, encoding="latin1")  # 'latin1' to avoid encoding errors
    except Exception as e:
        print(f"⚠️ Could not read {file}: {e}")
        continue

    # Find matching text column
    found_col = None
    for col in df.columns:
        if col.strip().lower() in [c.lower() for c in TEXT_COLUMNS]:
            found_col = col
            break

    if not found_col:
        print(f"⚠️ Could not process {file}: No email text column found")
        continue

    # Keep only the email text column
    df = df[[found_col]].rename(columns={found_col: "email_text"})

    # Add a source label
    df["source"] = file

    # Drop NaNs & empty
    df.dropna(subset=["email_text"], inplace=True)
    df = df[df["email_text"].str.strip() != ""]

    all_dfs.append(df)

# Merge all datasets
if all_dfs:
    final_df = pd.concat(all_dfs, ignore_index=True)
    final_df.to_csv(OUTPUT_FILE, index=False, encoding="utf-8")
    print(f"✅ Merged dataset saved to {OUTPUT_FILE}")
    print(f"📊 Total records: {len(final_df)}")
else:
    print("❌ No datasets merged. Please check your CSV files and column names.")

import pandas as pd



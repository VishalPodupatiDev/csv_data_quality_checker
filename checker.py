import sys
import pandas as pd
import re

# 📂 Step 1: Get CSV filename from the terminal
if len(sys.argv) < 2:
    print("❗Usage: python checker.py <your_csv_file.csv>")
    exit()

file_path = sys.argv[1]

# 📥 Step 2: Load CSV
df = pd.read_csv(file_path)

# ✅ Basic Info
print("🔍 Data Overview")
print("-" * 40)
print(df.info())
print("\n")

# ❌ Missing Values
print("❌ Missing Values")
print("-" * 40)
print(df.isnull().sum())
print("\n")

# 🔁 Duplicate Rows
print("🔁 Duplicate Rows")
print("-" * 40)
print(f"Total duplicate rows: {df.duplicated().sum()}")
print("\n")

# 📧 Invalid Email Check
if 'email' in df.columns:
    def validate_email(email):
        pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
        return bool(re.match(pattern, str(email)))

    invalid_emails = df[~df['email'].apply(validate_email)]
    print("📧 Invalid Emails Found:")
    print(invalid_emails[['email']])
    print("\n")
else:
    print("ℹ️ No 'email' column found — skipping email check.\n")

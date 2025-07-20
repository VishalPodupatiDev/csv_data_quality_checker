# 🧹 CSV Data Quality Checker

A Python tool to analyze and report data quality issues in CSV files.

## ✅ Features

- Detects missing values
- Identifies duplicate rows
- Validates email formatting with regex
- Prints a summary report to the terminal
- Reusable for any CSV by passing filename via terminal

📁 Project Structure

csv_data_quality_checker/
├── checker.py          # Main script to analyze data
├── requirements.txt    # Dependencies (pandas)
├── test_data.csv       # Sample file for testing
└── README.md           # You're reading it now

## 🚀 How to Run

```bash
pip install pandas
python checker.py your_file.csv

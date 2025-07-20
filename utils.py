import re
import pandas as pd

def validate_emails(email):
    if pd.isnull(email):
        return False
    pattern = r"^[\w\.-]+@[\w\.-]+\.\w+$"
    return re.match(pattern, email) is not None

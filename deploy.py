# deploy.py
from datetime import datetime

# Get the current timestamp in a clean format
# Example: 20251026143005
timestamp = datetime.now().strftime("%Y%m%d%H%M%S")

# Define the content of the requirements.txt file
# The comment includes the timestamp, which makes the file unique on every run.
requirements_content = f"""
# Deployment Timestamp: {timestamp}
# This file forces a clean rebuild on Streamlit Cloud.

streamlit>=1.30.0
pandas>=2.0.0
"""

# Overwrite the requirements.txt file with the new content
with open("requirements.txt", "w") as f:
    f.write(requirements_content.strip())

print("✅ requirements.txt has been updated with a new timestamp.")
print("You are now ready to commit and push your changes to GitHub.")
print("Streamlit Cloud will now perform a full, clean rebuild.")

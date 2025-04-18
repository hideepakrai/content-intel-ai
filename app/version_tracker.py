# app/version_tracker.py

import csv
import os
from datetime import datetime
import pandas as pd

VERSION_FILE = "versions/version_log.csv"

def log_version_change(component, summary, developer="Van"):
    """Logs a version change entry into version_log.csv"""
    os.makedirs("versions", exist_ok=True)

    # Initialize file if it doesn't exist
    if not os.path.exists(VERSION_FILE):
        with open(VERSION_FILE, mode="w", newline="") as file:
            writer = csv.writer(file)
            writer.writerow(["Date", "Component", "Change Summary", "Developer", "Notes"])

    # Append new log entry
    with open(VERSION_FILE, mode="a", newline="") as file:
        writer = csv.writer(file)
        writer.writerow([
            datetime.now().strftime("%Y-%m-%d %H:%M:%S"),
            component,
            summary,
            developer,
            ""
        ])

def get_current_log():
    """Returns current version log as DataFrame"""
    if not os.path.exists(VERSION_FILE):
        return pd.DataFrame(columns=["Date", "Component", "Change Summary", "Developer", "Notes"])
    return pd.read_csv(VERSION_FILE)

# app/task_flow.py

import json
import pandas as pd

FLOW_FILE = "versions/task_flow.json"

def get_flow_status():
    """Returns the task flow tracker as DataFrame"""
    try:
        with open(FLOW_FILE, "r") as file:
            flow = json.load(file)

        rows = []
        for module, details in flow.items():
            rows.append({
                "Module": module,
                "Status": details.get("status", "unknown"),
                "Features": ", ".join(details.get("features", []))
            })
        return pd.DataFrame(rows)

    except FileNotFoundError:
        return pd.DataFrame(columns=["Module", "Status", "Features"])

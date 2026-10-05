import json
import os

FILE_PATH = "transactions.json"

def load_data():
    if not os.path.exists(FILE_PATH):
        return {"balance": 0, "transactions": []}
    try:
        with open(FILE_PATH, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        return {"balance": 0, "transactions": []}

def save_data(data):
    with open(FILE_PATH, "w") as f:
        json.dump(data, f, indent=4)
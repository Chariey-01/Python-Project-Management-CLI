import json
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
DATA_PATH = os.path.join(BASE_DIR, "data", "database.json")


def load_data():
    """
    Load data from database.json
    """

    if not os.path.exists(DATA_PATH):
        return {"users": [], "projects": []}

    try:
        with open(DATA_PATH, "r") as file:
            return json.load(file)

    except json.JSONDecodeError:
        return {"users": [], "projects": []}


def save_data(data):
    """
    Save data to database.json
    """

    os.makedirs(os.path.dirname(DATA_PATH), exist_ok=True)
    with open(DATA_PATH, "w") as file:
        json.dump(data, file, indent=4)

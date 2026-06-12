import json
import os

DATA_PATH = "data/database.json"


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

    with open(DATA_PATH, "w") as file:
        json.dump(data, file, indent=4)
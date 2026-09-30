import json
file="data/expenses.json"

def load_data():

    try:
        with open(file, "r") as f:
            return json.load(f)
    except FileNotFoundError:
        return {"budget": 0.0, "expenses": []}

def save_data(data):
    with open(file, "w") as f:
        json.dump(data, f, indent=4)

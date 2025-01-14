import json

class DataHandler:
    def save_user_data(self, data, file="data/user_data.json"):
        with open(file, "w") as f:
            json.dump(data, f)

    def load_user_data(self, file="data/user_data.json"):
        try:
            with open(file, "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return {}

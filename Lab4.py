import json

# Load data from JSON file
def loa_dataset(file_path):
    try:
        with open(file_path, 'r') as file:
            data = json.load(file)
        return data
    except FileNotFoundError:
        return "The file could not be found"
    except json.JSONDecodeError:
        return "The file could not be decoded"
    
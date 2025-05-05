def preprocess_input(user_input):
    # Function to preprocess user input for normalization
    user_input = user_input.lower().strip()
    return user_input

def load_json_file(file_path):
    # Function to load a JSON file and return its contents
    import json
    with open(file_path, 'r') as file:
        data = json.load(file)
    return data

def extract_intents(data):
    # Function to extract intents from the loaded data
    intents = {}
    for intent in data['intents']:
        intents[intent['tag']] = intent['patterns']
    return intents

def normalize_response(response):
    # Function to normalize the response for consistent formatting
    return response.strip()
import random

class ResponseGenerator:
    def __init__(self, intents):
        self.intents = intents

    def get_response(self, intent_name):
        for intent in self.intents['intents']:
            if intent['intent'] == intent_name:
                return random.choice(intent['responses'])  # Randomly select a response
        return "I'm sorry, I don't understand that."
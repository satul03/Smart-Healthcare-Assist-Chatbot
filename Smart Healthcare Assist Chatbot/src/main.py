# healthcare-chatbot/src/main.py

from chatbot.intents import IntentHandler
from chatbot.responses import ResponseGenerator
from models.model import ChatbotModel
import json

def load_data(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def main():
    # Load intents and responses
    intents = load_data('data/dataset.json')
    
    # Initialize components
    intent_handler = IntentHandler(intents)  # Pass the dictionary directly
    response_generator = ResponseGenerator(intents)  # Pass intents here
    chatbot_model = ChatbotModel()

    # Train the model (if applicable)
    chatbot_model.train(intents)

    print("Healthcare Chatbot is ready to assist you!")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Chatbot: Goodbye!")
            break
        
        # Process user input
        intent = intent_handler.match_intent(user_input)
        response = response_generator.get_response(intent)
        
        print(f"Chatbot: {response}")

if __name__ == "__main__":
    main()
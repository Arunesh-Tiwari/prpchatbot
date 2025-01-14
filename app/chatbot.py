import json
from app.nlp_processor import NLPProcessor
from app.model import SelfLearningModel
from app.data_handler import DataHandler

class Chatbot:
    def __init__(self):
        self.nlp = NLPProcessor()
        self.model = SelfLearningModel()
        self.data_handler = DataHandler()

    def process_message(self, message):
        intent = self.nlp.identify_intent(message)
        response = self.model.generate_response(intent)
        self.model.learn_from_interaction(message, intent)
        return response

if __name__ == "__main__":
    bot = Chatbot()
    print("PRP Finance Chatbot is running!")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            break
        print("Bot:", bot.process_message(user_input))

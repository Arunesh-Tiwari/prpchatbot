class SelfLearningModel:
    def __init__(self):
        self.user_responses = {}

    def generate_response(self, intent):
        responses = {
            "add_transaction": "Please provide the details of the transaction.",
            "unknown": "I'm not sure I understand. Could you rephrase?",
        }
        return responses.get(intent, "Sorry, I didn't catch that.")

    def learn_from_interaction(self, message, intent):
        # Store the user's interaction for later reinforcement
        if intent not in self.user_responses:
            self.user_responses[intent] = []
        self.user_responses[intent].append(message)

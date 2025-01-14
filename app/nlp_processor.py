import random

class NLPProcessor:
    def identify_intent(self, message):
        # Simplified intent identification for MVP
        if "transaction" in message.lower():
            return "add_transaction"
        return "unknown"

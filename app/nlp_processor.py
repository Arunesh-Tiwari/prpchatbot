import re

class NLPProcessor:
    def identify_intent(self, message):
        # Improved keyword-based intent identification
        transaction_keywords = ["transaction", "payment", "expense", "spend"]
        
        # Check if any transaction-related keyword is in the message
        if any(keyword in message.lower() for keyword in transaction_keywords):
            return "add_transaction"

        return "unknown"

from app.chatbot import Chatbot

def main():
    bot = Chatbot()
    print("PRP Finance Chatbot is running! Type 'exit' to quit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["exit", "quit"]:
            print("Goodbye!")
            break
        print("Bot:", bot.process_message(user_input))

if __name__ == "__main__":
    main()

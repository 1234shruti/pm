import re

def chatbot():

    print("Chatbot: Hello! I am a simple chatbot.")
    print("Chatbot: Type 'bye' to exit.")

    while True:

        user_input = input("You: ").lower().strip()

        # Predefined rules and pattern matching

        if re.search(r"\b(hi|hello|hey)\b", user_input):
            print("Chatbot: Hello! How can I help you?")

        elif re.search(r"\b(name|who are you)\b", user_input):
            print("Chatbot: I am a rule-based chatbot.")

        elif re.search(r"\b(how are you)\b", user_input):
            print("Chatbot: I am fine! Thank you.")

        elif re.search(r"\b(help)\b", user_input):
            print("Chatbot: I can respond to greetings and simple questions.")

        elif re.search(r"\b(time|date)\b", user_input):
            from datetime import datetime
            print("Chatbot:", datetime.now().strftime("%H:%M:%S, %d-%m-%Y"))

        elif re.search(r"\b(bye|exit|quit)\b", user_input):
            print("Chatbot: Goodbye! Have a nice day.")
            break

        else:
            print("Chatbot: Sorry, I don't understand that.")


# Start the chatbot
chatbot()
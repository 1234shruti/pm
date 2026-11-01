def chatbot():
    print("Chatbot: Hello! How can I help you?")

    while True:
        user = input("You: ").lower()

        if "hello" in user or "hi" in user:
            print("Chatbot: Hello! Nice to meet you.")

        elif "name" in user:
            print("Chatbot: I am a Python chatbot.")

        elif "how are you" in user:
            print("Chatbot: I am fine. Thank you!")

        elif "bye" in user:
            print("Chatbot: Goodbye!")
            break

        else:
            print("Chatbot: Sorry, I don't understand.")


chatbot()
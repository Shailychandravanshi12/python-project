def chatbot():
    print("Chatbot: Hello! I am a simple chatbot. How can I help you?")
    while True:
        user_input = input("You: ").strip().lower()

        if user_input in ["hi", "hello", "hey"]:
            print("Chatbot: Hello! How can I assist you today?")
        elif user_input in ["how are you?", "how are you doing?"]:
            print("Chatbot: I'm just a bunch of code, but I'm functioning as expected!")
        elif user_input in ["what is your name?", "who are you?"]:
            print("Chatbot: I'm a simple chatbot created in Python.")
        elif user_input in ["bye", "goodbye", "exit"]:
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: I'm sorry, I don't understand that.")

if __name__ == "__main__":
    chatbot()
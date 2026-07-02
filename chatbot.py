# Rule-Based AI Chatbot

print("Hello! I am your AI ChatBot.")
print("Type 'exit' to end the chat.\n")

while True:
    user_input = input("You: ").lower()

    if user_input in ["hi", "hello", "hey"]:
        print("ChatBot: Hello! How are you?")

    elif user_input in ["how are you", "how are you?"]:
        print("ChatBot: I am fine. Thank you for asking!")

    elif user_input in ["what is your name", "your name"]:
        print("ChatBot: I am a Rule-Based AI ChatBot.")

    elif user_input in ["bye", "exit", "quit"]:
        print("ChatBot: Goodbye! Have a nice day.")
        break

    else:
        print("ChatBot: Sorry, I don't understand that.")
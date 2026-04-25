print("🤖 AI Chatbot (type 'exit' to stop)")

while True:
    user_input = input("You: ").lower()

    if user_input == "exit":
        print("Bot: Goodbye! 👋")
        break

    elif "hello" in user_input or "hi" in user_input:
        print("Bot: Hello! How can I help you?")

    elif "your name" in user_input:
        print("Bot: I am a simple AI chatbot created using Python.")

    elif "how are you" in user_input:
        print("Bot: I'm just code, but I'm doing great! 😄")

    elif "ai" in user_input:
        print("Bot: AI stands for Artificial Intelligence. It helps machines think and learn.")

    elif "bye" in user_input:
        print("Bot: Bye! Have a nice day 👋")
        break

    else:
        print("Bot: Sorry, I didn't understand that.")
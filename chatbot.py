# Simple Rule-Based Chatbot using if-else
# Objective: Simulates a chatbot using basic Python logic

def chatbot():
    print("🤖 Chatbot: Hello! I’m your friendly chatbot. Type 'bye' to exit.")

    while True:
        user_input = input("You: ").lower()

        if user_input == "hi" or user_input == "hello":
            print("🤖 Chatbot: Hello there! How can I help you today?")
        
        elif "how are you" in user_input:
            print("🤖 Chatbot: I’m doing great, thank you! How about you?")
        
        elif "your name" in user_input:
            print("🤖 Chatbot: I’m a simple rule-based chatbot created in Python.")
        
        elif "weather" in user_input:
            print("🤖 Chatbot: I can’t check live weather yet, but it’s always sunny in my world! 🌞")
        
        elif "bye" in user_input:
            print("🤖 Chatbot: Goodbye! Have a great day 👋")
            break
        
        else:
            print("🤖 Chatbot: I don’t understand that yet. Please try asking something else.")

if __name__ == "__main__":
    chatbot()

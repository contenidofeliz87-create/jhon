import random

class Chatbot:
    def __init__(self):
        self.responses = {
            "hello": ["Hello! How can I help you today?", "Hi there! What's on your mind?"],
            "how are you?": ["I'm just a computer program, but thanks for asking! How can I assist you?"],
            "bye": ["Goodbye! Have a great day!"],
            "help": ["I'm here to help! What do you need assistance with?"]
        }

    def get_response(self, user_input):
        user_input = user_input.lower()
        if user_input in self.responses:
            return random.choice(self.responses[user_input])
        else:
            return "I'm sorry, I don't understand that. Can you ask something else?"


def main():
    chatbot = Chatbot()
    print("Welcome to the interactive chatbot! Type 'bye' to exit.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "bye":
            print(chatbot.get_response(user_input))
            break
        response = chatbot.get_response(user_input)
        print(f"Chatbot: {response}")

if __name__ == '__main__':
    main()
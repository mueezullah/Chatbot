import datetime
import random

print("\n---Custom ChatBot---")
def chatbot():

    print("HELLO!")
    print("Type 'bye' to end chat.\n")

    #predifined jokes#
    jokes = [
        "I told my computer I needed a break, Now it’s frozen.",
        "Why did the math book look sad? Because it had too many problems.",
        "Why was the computer cold? It left its Windows open!",
        "Why don’t some couples go to the gym? Because some relationships don’t work out!"
    ]

    funfacts = [
        "Honey never spoils. Archaeologists have found pots of honey in ancient Egyptian tombs that are over 3,000 years old!",
        "Octopuses have three hearts and blue blood.",
        "Bananas are berries, but strawberries aren't!",
        "Sharks have been around for over 400 million years, while trees appeared around 350 million years ago."
    ]

    prompts = 0
    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "bye":
            print(f"Chatbot: Goodbye! You asked {prompts} questions. It was a nice chatting with you")
            break

        prompts += 1

        if user_input.lower() in ["hi", "hello"]:
            print("Chatbot: Hello! How can I help you?")

        elif user_input.lower() == "how are you":
            print("Chatbot: I am feeling great!")

        elif user_input.lower() == "tell me a joke":
            print(f"Chatbot: {random.choice(jokes)}")

        elif user_input.lower() == "what is python":
            print("Chatbot: Python is a high-level language know for its simplicity.")

        elif user_input.lower() == "what can you do":
            print("Chatbot: I can tell jokes, show the time, perform calculations, reverse words, and many more")

        elif user_input.lower() == "what time is it":
            current_time = datetime.datetime.now().strftime("%H:%M:%S")
            print(f"Chatbot: The current time is {current_time} ")

        elif user_input.lower() == "calculate something for me":
            math_operation = input("Chatbot: Enter the operations e.g, 9+2: ")
            try:
                result = eval(math_operation)
                print(f"Chatbot: The result is: {result}")
            except:
                print("Chatbot: Sorry, I couldn't calculate that.")

        elif user_input.lower() == "reverse the word":
            word = input("Chatbot: Please enter the word:")
            print(f"Chatbot: The reversed word is: {word[::-1]}")

        elif user_input.lower() == "who created you":
            print("Chatbot: I was created by Mueez Ullah to help people learn and have fun at the same time")

        elif user_input.lower() == "tell me the fun fact":
            print(f"Chatbot: {random.choice(funfacts)}")

        else:
            print("Chatbot: I am Sorry, I don't understand that. Could you please try asking something else")

chatbot()
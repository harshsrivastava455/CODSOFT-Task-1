#ADVANCED MULTI-LANGUAGE RULE-BASED CHATBOT
#Supports:
#English
#Hindi
#Mixed Hindi + English

from datetime import datetime
import random

print("Smart AI ChatBot")
print("Type 'bye' or 'exit' to stop.\n")

# Main chatbot loop
while True:

    user = input("You: ").lower().strip()

    # EXIT
    if user in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day")
        break
    
    # GREETINGS
    elif any(word in user for word in
             ["hello", "hi", "hey", "namaste", "hii", "good morning",
              "good evening", "good night"]):

        responses = [
            "Hello How can I help you?",
            "Hi Nice to meet you!",
            "Namaste Aap kaise ho?",
            "Hey! What can I do for you?"
        ]

        print("Bot:", random.choice(responses))

    # NAME
    elif ("your name" in user or
          "tumhara naam" in user or
          "aapka naam" in user):

        print("Bot: Mera naam Smart ChatBot hai")

    # HOW ARE YOU
    elif ("how are you" in user or
          "kaise ho" in user or
          "kese ho" in user):

        print("Bot: Main bilkul theek hoon")

    # TIME
    elif ("time" in user or
          "samay" in user):

        current_time = datetime.now().strftime("%H:%M:%S")
        print("Bot: Current time is", current_time)

    # DATE
    elif ("date" in user or
          "today" in user or
          "aaj ki date" in user):

        current_date = datetime.now().strftime("%d-%m-%Y")
        print("Bot: Today's date is", current_date)

    # DAY
    elif ("day" in user or
          "aaj ka din" in user):

        current_day = datetime.now().strftime("%A")
        print("Bot: Today is", current_day)

    # THANK YOU
    elif ("thank you" in user or
          "thanks" in user or
          "dhanyawad" in user):

        print("Bot: You're welcome")

    # STUDY QUESTIONS
    elif ("python" in user):
        print("Bot: Python is a popular programming language.")

    elif ("java" in user):
        print("Bot: Java is an object-oriented programming language.")

    elif ("html" in user):
        print("Bot: HTML is used to create web pages.")

    elif ("css" in user):
        print("Bot: CSS is used for website styling.")

    elif ("javascript" in user):
        print("Bot: JavaScript adds interactivity to websites.")

    elif ("ai" in user or "artificial intelligence" in user):
        print("Bot: AI means machines that can think and learn like humans.")

    elif ("machine learning" in user):
        print("Bot: Machine Learning is a branch of AI.")

    elif ("database" in user):
        print("Bot: Database stores organized information.")

    elif ("computer network" in user):
        print("Bot: Computer Network connects multiple computers together.")

    
    # MATHEMATICS
    elif ("2+2" in user):
        print("Bot: 2 + 2 = 4")

    elif ("square root of 16" in user):
        print("Bot: Square root of 16 is 4")

    elif ("formula of area of circle" in user):
        print("Bot: Area of circle = π × r × r")
        
    # WEATHER
    elif ("weather" in user):
        print("Bot: Please connect me with internet for live weather updates")
    # JOKES
    elif ("joke" in user):
        jokes = [
            "Why do programmers hate nature? Because it has too many bugs",
            "Why was the computer cold? Because it left its Windows open",
            "Why did Python go to school? To improve its class"
        ]

        print("Bot:", random.choice(jokes))
        
    # MOTIVATION
    elif ("motivate me" in user or
          "motivation" in user):

        print("Bot: Success comes from consistency, not luck")
    # HELP
    
    elif ("help" in user):
        print("""
Bot: I can answer questions about:
- Greetings
- Time & Date
- Programming
- AI
- Math
- Motivation
- Jokes
- General Questions
        """)
        
    # DEFAULT RESPONSE
    else:
        print("Bot: Sorry mujhe iska answer nahi pata.")

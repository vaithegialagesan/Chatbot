import random
import string
from datetime import datetime

# Memory for session
session_memory = {}  # {meaning_key: answer}

# Words to ignore (stop words)
STOP_WORDS = {"what", "is", "a", "an", "the", "of", "about", "tell", "me"}

def normalize(text):
    text = text.lower()
    text = text.translate(str.maketrans("", "", string.punctuation))
    words = text.split()
    words = [w for w in words if w not in STOP_WORDS]
    return " ".join(words)

def greet():
    return random.choice([
        "Hello! How can I help you?",
        "Hi there! What can I do for you?",
        "Hey! Nice to meet you 😊",
        "Greetings! Ask me anything."
    ])

def joke():
    return random.choice([
        "Why do programmers hate nature? Too many bugs",
        "Why did Python break up with Java? Too many classes",
        "I would tell you a joke about Python, but it's too easy to interpret."
    ])

def get_time():
    return datetime.now().strftime("Current time is %H:%M:%S")

def get_date():
    return datetime.now().strftime("Today's date is %d-%m-%Y")

def chatbot_response(user_input):
    meaning_key = normalize(user_input)

    # Check session memory first
    if meaning_key in session_memory:
        return session_memory[meaning_key]

    # Predefined responses
    responses = {
        "hi": greet(),
        "hello": greet(),
        "hey": greet(),
        "how are you": "I'm doing great! Thanks for asking",
        "whats up": "Just chatting with you!",
        "what are you doing": "I'm waiting to help you",
        "your name": "I'm a Python-based chatbot",
        "who are you": "I'm a chatbot created using Python.",
        "who made you": "I was created by a Python developer.",
        "time": get_time(),
        "date": get_date(),
        "day": datetime.now().strftime("Today is %A"),
        "help": "You can ask me about time, date, jokes, math, or general questions.",
        "features": "I can chat, tell jokes, give date/time, and do basic math.",
        "python": "Python is a popular, easy-to-learn programming language.",
        "java": "Java is an object-oriented programming language.",
        "programming": "Programming is the process of writing instructions for computers.",
        "joke": joke(),
        "funny": joke(),
        "bye": "Goodbye! Have a nice day",
        "exit": "Exiting chat... See you soon!"
    }

    # Math logic
    if "add" in meaning_key:
        nums = [int(i) for i in meaning_key.split() if i.isdigit()]
        if len(nums) >= 2:
            return f"Result: {nums[0] + nums[1]}"

    if "subtract" in meaning_key:
        nums = [int(i) for i in meaning_key.split() if i.isdigit()]
        if len(nums) >= 2:
            return f"Result: {nums[1] - nums[0]}"

    if "multiply" in meaning_key:
        nums = [int(i) for i in meaning_key.split() if i.isdigit()]
        if len(nums) >= 2:
            return f"Result: {nums[0] * nums[1]}"

    if "divide" in meaning_key:
        nums = [int(i) for i in meaning_key.split() if i.isdigit()]
        if len(nums) >= 2 and nums[1] != 0:
            return f"Result: {nums[0] / nums[1]}"

    # Keyword matching
    for key in responses:
        if key in meaning_key:
            return responses[key]

    # Unknown question → learn
    print("Bot: I don't know the answer to that. Do you want me to remember it? (yes/no)")
    store = input("You: ").lower()

    if store == "yes":
        answer = input("Bot: What should I answer if asked this question again?\nYou: ")
        session_memory[meaning_key] = answer
        return "Got it! I will remember this for now."
    else:
        return "Okay, I won't remember this."

def main():
    print("Advanced Chatbot Started (type 'exit' to quit)")
    while True:
        user_input = input("You: ").strip()
        if normalize(user_input) == "exit":
            print("Bot: Exiting chat... See you soon!")
            break
        response = chatbot_response(user_input)
        print("Bot:", response)

if __name__ == "__main__":
    main()
import random

def get_random_joke():
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "I told my computer I needed a break, and it said: 'No problem — I’ll go to sleep.'",
        "Why was the math book sad? It had too many problems.",
        "Parallel lines have so much in common. It’s a shame they’ll never meet.",
        "What did one wall say to the other? I’ll meet you at the corner!",
        "Why can’t your nose be 12 inches long? Because then it would be a foot.",
        "Why do we tell actors to 'break a leg?' Because every play has a cast.",
    ]
    return random.choice(jokes)

while True:
    print("\nRandom Joke Generator")
    print("1. Tell me a joke")
    print("2. Exit")

    choice = input("Choose an option (1/2): ")

    if choice == '1':
        print("\n😂 Joke:", get_random_joke())
    elif choice == '2':
        print("Goodbye! Keep laughing 😄")
        break
    else:
        print("Invalid choice! Please enter 1 or 2.")

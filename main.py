import json
import random
from datetime import datetime

# Load tips and quotes from JSON file
with open("tips.json", "r") as file:
    data = json.load(file)

study_tips = data["study_tips"]
quotes = data["quotes"]

# Ask user name
name = input("Enter your name: ")

print(f"\nHello, {name}! Welcome to Smart Student Assistant.")

while True:
    print("\n===== SMART STUDENT ASSISTANT =====")
    print("1. Generate Study Tip")
    print("2. Generate Motivation Quote")
    print("3. Display Current Date & Time")
    print("4. Exit")

    choice = input("Enter your choice: ")

    if choice == "1":
        tip = random.choice(study_tips)
        print("\n📚 Study Tip:")
        print(tip)

        with open("output.txt", "a") as file:
            file.write(f"Study Tip: {tip}\n")

    elif choice == "2":
        quote = random.choice(quotes)
        print("\n💡 Motivation Quote:")
        print(quote)

        with open("output.txt", "a") as file:
            file.write(f"Motivation Quote: {quote}\n")

    elif choice == "3":
        now = datetime.now()
        current_time = now.strftime("%d-%m-%Y %H:%M:%S")

        print("\n🕒 Current Date & Time:")
        print(current_time)

        with open("output.txt", "a") as file:
            file.write(f"Date & Time: {current_time}\n")

    elif choice == "4":
        print("\nThank you for using Smart Student Assistant!")
        break

    else:
        print("Invalid choice. Please try again.")
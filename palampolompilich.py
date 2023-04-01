import random

user_score = 0
computer1_score = 0
computer2_score = 0

for i in range(5):
    user_choice = input("Enter your choice ✋ or 🤚 : ")

    computer1_choice = random.choice(["🤚", "✋"])
    computer2_choice = random.choice(["🤚", "✋"])

    print("You chose:", user_choice)
    print("Computer 1 chose:", computer1_choice)
    print("Computer 2 chose:", computer2_choice)
    
    if (user_choice == "🤚" and computer1_choice == "✋" and computer2_choice == "✋") or \
       (user_choice == "✋" and computer1_choice == "🤚" and computer2_choice == "🤚"):
        user_score += 2
        print("You win!")
    elif (computer1_choice == "🤚" and user_choice == "✋" and computer2_choice == "✋") or \
         (computer1_choice == "✋" and user_choice == "🤚" and computer2_choice == "🤚"):
        computer1_score += 2
        print("Computer 1 wins!")
    elif (computer2_choice == "🤚" and computer1_choice == "✋" and user_choice == "✋") or \
         (computer2_choice == "✋" and computer1_choice == "🤚" and user_choice == "🤚"):
        computer2_score += 2
        print("Computer 2 wins!")
    else:
        user_score += 1
        computer1_score += 1
        computer2_score += 1
        print("Draw")

if user_score > computer1_score and user_score > computer2_score:
    print("You win the game!")
elif computer1_score > user_score and computer1_score > computer2_score:
    print("Computer 1 wins the game!")
elif computer2_score > user_score and computer2_score > computer1_score:
    print("Computer 2 wins the game!")
else:
    print("Draw")

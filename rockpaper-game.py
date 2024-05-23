import random

rock = '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

paper = '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

scissors = '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''

options = [rock, paper, scissors]

# Randomly choose for the computer
computer_choice = random.choice(options)

# Map user input to options
user_options = int(input("Enter 0 for rock, 1 for paper, 2 for scissors: "))

# Ensure user_options is valid
if user_options < 0 or user_options > 2:
    print("Invalid choice!")
    exit()

print("You chose:")
if user_options == 0:
    user_choice = rock
    print(rock)
elif user_options == 1:
    user_choice = paper
    print(paper)
else:
    user_choice = scissors
    print(scissors)

print("Computer chose:")
print(computer_choice)

# Determine the winner
if user_choice == rock and computer_choice == scissors:
    print("You win!")
elif user_choice == paper and computer_choice == rock:
    print("You win!")
elif user_choice == scissors and computer_choice == paper:
    print("You win!")
elif user_choice == computer_choice:
    print("It's a draw!")
else:
    print("You lose!")


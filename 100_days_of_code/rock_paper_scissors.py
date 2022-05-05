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
images = [rock, paper, scissors]
#Write your code below this line 👇
import random
user_choice = int(input("What do you choose? Type 0 for Rock, 1 for Paper and 2 for Scissors: "))
print(f"The user chose {user_choice}")
print(images[user_choice])
print("\n")
computer = (random.randint(0, 2))
print(f"The computer chose: {computer}")
print(images[computer])
if user_choice >=3 or user_choice <0:
  print("You entered an invalid number. Please try again.")
elif computer == user_choice:
  print("It\'s a tie")
elif user_choice == 0 and computer == 2:
  print(f"Rock beats scissors. The user wins")
elif user_choice == 1 and computer == 0:
  print(f"Paper beats Rock. The user wins")  
elif user_choice == 2 and computer == 1:
  print(f"Scissors beats Paper. The user wins")
elif computer == 0 and user_choice == 2:
  print(f"Rock beats scissors. The computer wins")
elif computer == 1 and user_choice == 0:
  print(f"Paper beats Rock. The computer wins")  
else:
  print(f"Scissors beats Paper. The computer wins")
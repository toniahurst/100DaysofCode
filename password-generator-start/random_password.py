#Password Generator Project
import random
from random import shuffle
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password?\n")) 
nr_symbols = int(input(f"How many symbols would you like?\n"))
nr_numbers = int(input(f"How many numbers would you like?\n"))
difficulty = input(f"Would you like an easy or a hard level password? Enter E or H\n")
#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
password = ""
for number in range(0, nr_letters):
  password += letters[(random.randint(0, nr_letters))]
for number in range(0, nr_symbols):
  password += symbols[(random.randint(0, nr_symbols))]
for number in range(0, nr_numbers):
  password += numbers[(random.randint(0, nr_numbers))]
  
#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P 
if difficulty == "H":    
  print(f"Original password is: {password}")
  new_password = list(password)
  new_password = random.sample(new_password, len(password))
  new_password = ''.join(new_password)               
  print(f"Your new password is: {new_password}")

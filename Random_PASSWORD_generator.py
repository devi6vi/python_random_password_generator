import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the password generator ")
letters_user = int(input("How many letters in your password?\n"))
numbers_user = int(input("How many numbers in your password?\n"))
symbols_user = int(input("How many symbols in your password?\n"))

password_list = []

for i in range(letters_user):
    password_list.append(random.choice(letters))
for i in range(numbers_user):
    password_list.append(random.choice(numbers))
for i in range(symbols_user):
    password_list.append(random.choice(symbols))


random.shuffle(password_list)
# print(password_list)  (Optional)

password = ""
for char in password_list:
    password += char

print(f"Your new password could be {password}")
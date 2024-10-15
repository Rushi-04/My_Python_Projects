import random
print("Welcome to python's Password Generator")

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o',
           'p', 'q', 'r', 's', 't','u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 
           'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 
           'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

no_of_letters = int(input("How many Letters would you like to have in your password? :"))
no_of_symbols = int(input("How many Symbols would you like to have in your password? :"))
no_of_numbers = int(input("How many Numbers would you like to have in your password? :"))

passwordlst = []
for num1 in range(1,no_of_letters+1):
    passwordlst += random.choice(letters)
     

for num2 in range(1,no_of_symbols+1):
    passwordlst += random.choice(symbols)
 

for num3 in range(1,no_of_numbers+1):
    passwordlst += random.choice(numbers)
    
random.shuffle(passwordlst)

password = ""                      #printing list
for char in passwordlst:
    password += char

print("Here's your password:- ",password)
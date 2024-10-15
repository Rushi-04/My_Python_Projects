#Program to reverse a string 

a = "rushi"

name = ""
t = [-1,-2,-3,-4,-5]
for char in t:
    name += a[char]
    
print(name)


name = "madam"

r = name[::-1]
print(r)

if r==name:
    print("it's a palindrome")

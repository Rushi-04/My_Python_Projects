print("Welcome to the Love Calculator")

name1 = input("Enter your first name: ")
name2 = input("Enter your second name: ")

lower_case1 = name1.lower()
lower_case2 = name2.lower()

t1 = lower_case1.count("t")
r1 = lower_case1.count("r")
u1 = lower_case1.count("u")
e1 = lower_case1.count("e")

t2 = lower_case2.count("t")
r2 = lower_case2.count("r")
u2 = lower_case2.count("u")
e2 = lower_case2.count("e")

l1 = lower_case1.count("l")
o1 = lower_case1.count("o")
v1 = lower_case1.count("v")
e1 = lower_case1.count("e")

l2 = lower_case2.count("l")
o2 = lower_case2.count("o")
v2 = lower_case2.count("v")
e2 = lower_case2.count("e")

first_digit = int(t1+r1+u1+e1+t2+r2+u2+e2)
second_digit = int(l1+o1+v1+e1+l2+o2+v2+e2)

print(f"Your Love percentage is {first_digit}{second_digit}%")
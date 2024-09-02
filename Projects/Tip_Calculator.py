print("Welcome to the Tip Calculator")

amount = float(input("What was the total bill? Rs "))

per = int(input("What percentage of tip would you like to give? 10, 12 or 15: "))

people = int(input("In how many people do you want to split the bill?: "))

tip = (per/100)*amount

final_amount = tip + amount 

print(f"Each person should pay:{round(final_amount,2)} Rs")

print(round(2354.523,2))

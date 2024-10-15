print("BMI Calculator 2.0")

weight = float(input("Enter your weight in kg: "))                
height = float(input("Enter your height in m: "))
bmi1 = (weight/(height**2))
bmi = round(bmi1,2)

if bmi < 18.5:
    print(f"bmi is {bmi}, you are slightly underweight")
elif 18.5 <bmi<25:
    print(f"bmi is {bmi}, You have normal body weight")
elif 25 <bmi<30:
    print(f"bmi is {bmi}, you are slightly overweight")
elif 30 <bmi<35:
    
    print(f"bmi is {bmi}, you are obese")
else :  
    
    print(f"bmi is {bmi}, you are clinically obese")
    
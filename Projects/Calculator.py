import pyttsx3
engine = pyttsx3.init()

def Add(x,y):
    return x+y

def Sub(x,y):
    return x-y

def Mul(x,y):
    return x*y

def Div(x,y):
    return x/y

def Mod(x,y):
    return x%y

def operand():

    engine.say("Choose the Operation you want to perform")
    engine.runAndWait()
    operand1 = int(input("""
  Choose the Operation you want to perform (Please Choose corresponding number)                    
  1.Addition (+)
  2.Subtraction (-)                    
  3.Multiplication (*)
  4.Division (/)
  5.Modulus (%)
  ---> """))
    return operand1
    
def operation(z):
  if z == 1:
   result = Add(x=num1,y=num2)
  elif z == 2:
   result = Sub(x=num1,y=num2)
  elif z == 3:
   result = Mul(x=num1,y=num2)
  elif z == 4:
   result = Div(x=num1,y=num2)
  elif z == 5:
   result = Mod(x=num1,y=num2)
  else:
    engine.say("Please Choose correct number from 1 to 5")
    engine.runAndWait()
    print("\nPlease Choose correct number from 1 to 5")
    operand()
  return result




want = True
while want == True:
  
  engine.say("Hello Vaishnav Sir, I am Jarvis, Welcome to the PyCalculator")
  print("'Welcome to the PYCalculator'")
  
  engine.say("Enter First Number")
 
  num1 = float(input("Enter First Number: "))
  
  engine.say("Enter Second Number")
 
  num2 = float(input("Enter Second Number: "))
  
  d = operand()
  
  r = operation(d)
  engine.say(f"Your answer is {r}")

  print(f"Your answer is {r}")
  
  engine.say("Do you want to continue")

  marzi = input("Do you want to continue (y) or (n)\n--->")

  if marzi == "y":
      want = True
  else :
      want = False
      engine.say("Thank's for using PyCalculator, Good Bye!")
   
      print("\nThank's for using PyCalculator, Good Bye!")
      
import random
import pyttsx3
engine = pyttsx3.init()
print('''
      
     __                    _                     ___                         _                   ___                        
  /\ \ \ _   _  _ __ ___  | |__    ___  _ __    / _ \ _   _   ___  ___  ___ (_) _ __    __ _    / _ \ __ _  _ __ ___    ___ 
 /  \/ /| | | || '_ ` _ \ | '_ \  / _ \| '__|  / /_\/| | | | / _ \/ __|/ __|| || '_ \  / _` |  / /_\// _` || '_ ` _ \  / _ \
/ /\  / | |_| || | | | | || |_) ||  __/| |    / /_\\ | |_| ||  __/\__ \\__ \| || | | || (_| | / /_\\| (_| || | | | | ||  __/
\_\ \/   \__,_||_| |_| |_||_.__/  \___||_|    \____/  \__,_| \___||___/|___/|_||_| |_| \__, | \____/ \__,_||_| |_| |_| \___|
                                                                                       |___/                                ''')
print("Welcome to Number Guessing Game")
engine.say("Welcome to the Number Guessing Game")
engine.runAndWait()


engine.say("Choose difficulty 'easy'or 'hard'")
engine.runAndWait()
difficulty = int(input("Choose dificulty\n1)'easy'\n2)'hard'\n--> "))
print("I'm Thinking of a number from 0 to 100")
engine.say("I;m thinking of a number from 1 to 100")
engine.runAndWait()


if difficulty == 1:
    attempts = 10
elif difficulty == 2:
    attempts = 5

print(f"You have {attempts} attempts remaining to guess the number")
engine.say(f"You have {attempts} attempts remaining to guess the number")
engine.runAndWait()

# Create a list of numbers from 1 to 100
number_list = list(range(1, 101))

number = random.choice(number_list)

guessed = False

while guessed == False:
    guess = int(input("Make a guess:"))
    if guess == number:
        print("You got it\nyou won!")
        print(f"The answer was {number}")
        engine.say("You got the number, you won!")
        engine.runAndWait()
        break
    if guess < number:
        print("to low\nguess again")
        engine.say("too low")
        engine.runAndWait()
        attempts -=1
    elif guess > number:
        print("to high\nguess again")
        engine.say("too high")
        engine.runAndWait()
        attempts -=1
    print(f"You have {attempts} attempts remaining to guess the number")
    engine.say(f"{attempts} attempts remaining")
    engine.runAndWait()
    
    if attempts == 0:
        print(f"The answer was {number}")
        print("You have exhausted all your attempts\nyou loose")
        engine.say("You are out of the attempts, you loose")
        engine.runAndWait()
        break
    
    
                

alphabet = ['a','b','c','d','e','f','g','h','i','j','k','l','m',
'n','o','p','q','r','s','t','u','v','w','x','y','z','a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']


def ceapher(start_text,shift_number,direction_of_program):
    end_text = ""        
    if direction_of_program == 'decode':
        shift_number *= -1    
    for char in start_text:
       if char in alphabet: 
         position = alphabet.index(char)
         new_position = position + shift_number    
         new_word = alphabet[new_position]
         end_text += new_word
       else:
        end_text+=char      
    print(f"The {direction_of_program}d message is {end_text}")

should_continue = True
while should_continue:    
  print("Welcome to Ceapher Cipher !")
  text = input("Type your message:\n").lower()
  shift = int(input("Type the shift number:\n"))
  direction = input("Type 'encode' to encrypt, Type 'decode' to decrypt:\n")

  shift = shift % 25
  ceapher(start_text=text,shift_number=shift,direction_of_program=direction)
  decision = input("Do you want to try again 'yes' or 'no':\n")

  if decision == 'no':
      should_continue = False
      print("Thanks Visit Again!")
      
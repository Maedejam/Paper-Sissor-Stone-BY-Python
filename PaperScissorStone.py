import random

options =["paper", "scissor", "stone"]

choose = input("Choose paper or scissor or stone: ")
system = random.choice(options)
print(f"The system choice is {system}")
count = 0

while True:
    if choose ==system:
        print("Both you, are the same!")
               
    elif (choose== "stone" and system== "scissor") or (choose== "scissor" and system == "paper") or (choose == "paper" and system == "stone"):       
        print("You win!")
        count +=1        
        
    elif (choose == "stone" and system == "paper") or (choose == "paper" and system == "scissor") or (choose== "scissor" and system== "stone"):        
        print("You loose")
                
    again = input("paly again? ")
    if again == 'yes':
        choose = input("Choose paper or scissor or stone: ")
    else:
        break
print(f"Total number of winnig is {count}")

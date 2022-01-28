from os import sep
import random

words=["mouse","air","solid","shake","ceiling","true","easy",
"deep","chocolate","pie","tree"]

choosenWord=random.choice(words)
print(choosenWord)
n=len(choosenWord)
print(n)
print("""
 _                                             
| |                                            
| |__   __ _ _ __   __ _ _ __ ___   __ _ _ __  
| '_ \ / _` | '_ \ / _` | '_ ` _ \ / _` | '_ \ 
| | | | (_| | | | | (_| | | | | | | (_| | | | |
|_| |_|\__,_|_| |_|\__, |_| |_| |_|\__,_|_| |_|
                    __/ |                      
                   |___/                       """)



print(("""  
  +---+
      |
      |
      |
      |
     ==="""))

answer=[]
chances=7
for i in range(n):
    answer+="_"
print(*answer,sep=" ")
incorrect=0
guesses=[]
while(chances>1):
    
    occurence=0
    guess=input("Guess A Word ")
    if (not guess.isalpha()):
        print("error pls enter only alphabets!\n")
    elif(guess in guesses):
        print("\nAlready guessed this word..try again\n")
    else:
        guesses.append(guess)
        
    
        for position in range(n):
            if(choosenWord[position]==guess):
                answer[position]=guess
                occurence=occurence+1
          
        if(occurence==0):
            incorrect=incorrect+1
            chances=chances-1  
        string=""
        for items in answer:
            string+=items
        print(*answer,sep=" ")

        if(string==choosenWord):
            print("\nPLAYER WON wohooo!!")
            break    

        if(occurence==0):
            if(incorrect==1):
                print("""
                +---+
                 O   |
                     |
                     |
                    ===""")
            elif(incorrect==2):
                print(""" 
                +---+
                 O   |
                 |   |
                     |
                    ===""")
            elif(incorrect==3):
                print("""
                +---+
                  O   |
                 /|   |
                      |
                      ===""")

            elif(incorrect==4):
                print("""
                +---+
                 O   |
                /|\  |
                     |
                     ===""")

            elif(incorrect==5):
                print(""" 
                +---
                 O   |
                /|\  |
                /    |
                    ===""")

            elif(incorrect==6):
                print("""
                +---
                 O   |
                /|\  |
                / \  |
                    ===""")
                print("GAME OVER U ARE OUT OF CHANCES")
                print(f"THE CORRECT ANSWER was {choosenWord}")

           

  


import random

type=['rock','paper','scissors']
myTurn=input("Enter ROCK,PAPER,SCISSORS\n")
print('Computer turn....choose')
choice=type[random.randint(0,2)]
print(choice)
if (choice==myTurn) :
    print('***tie***')
elif(myTurn=='rock' and choice=='scissors'):
    print("Player wins...")
elif(choice=='rock' and  myTurn=='scissors'):
    print("Comp wins...")
elif(myTurn=='scissors' and choice=='paper'):
    print('Player winns')
elif(myTurn=='scissors' and choice=='paper'):
    print('Comp winns')
elif(myTurn=="paper" and choice=='rock'):
    print("player wins")
else: print("comp wins")

# RANDOM PASSWORD GENERATOR (8 digits)

import random
import string
from venv import create



letters=list(string.ascii_letters)
number=['1','2','3','4','5','6','7','8','9','0']
symbols=["!","@","#","$","%","^","&","*","(",")"]

# for more than 8 character password take input from the user and apply for loop 
selLetters=random.choices(letters,k=3)
selNum=random.choices(number,k=2)
selSym=random.choices(symbols,k=1)
sel=selLetters+selNum+selSym

random.shuffle(sel)
print(*sel,sep="")

# or
# password=""

# for char in sel:
#     password += char

# print(password)
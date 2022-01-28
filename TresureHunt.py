row1=['😂','😂','😂']
row2=['😂','😂','😂']
row3=['😂','😂','😂']

map=[row1,row2,row3]
print(f'{row1}\n{row2}\n{row3}')
str=input("Enter the place u want to place the treasure 🪙")
i=int(str[0])
j=int(str[1])

map[i-1][j-1]='🪙'

print(f'{row1}\n{row2}\n{row3}')

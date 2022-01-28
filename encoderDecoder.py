
def encoder(msgg,shiftno):
    string=''
    for letter in msgg:
        position= alphabets.index(letter)
        position=(position+shiftno)%26
        newchar=alphabets[position]
        string+=newchar
    print(f"the encoded string is {string} ")





def decoder(msgg,shiftno):
    string=''
    for letter in msgg:
        position= alphabets.index(letter)
        position=(position-shiftno)%26
        newchar=alphabets[position]
        string+=newchar
    print(f"the encoded string is {string} ")


alphabets=['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
char="yes"
while(char=="yes"):
    todo=input("type 'encode' for encoding or 'decode' for decoding ")
    msgg=input("input your message ").lower()
    shiftno=int(input("enter ur shift no "))

    if (todo.lower()=="encode"):
        encoder(msgg,shiftno)
    elif(todo.lower()=='decode'):
        decoder(msgg,shiftno)


    char=input("do u want to continue encoding/ decoding messages??? yes or no?").lower()
    

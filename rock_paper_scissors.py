import random 
from getpass import getpass
choices = { 1:"🪨",2:"🧻",3:"✂️"}
outcomes = {1:3,2:1,3:2}
cc,uc = 0,0
while True :
    print("Press Enter to start the game: (Press n to stop)")
    a = getpass(prompt = "")
    if a == 'n' or a == 'N' :
        break
    print("Pick an option:")
    print("1. 🪨\n2. 🧻\n3. ✂️")
    try :
        c = int(input())
        if c not in [1,2,3] :
            raise
    except :
        print("Invalid option.")
        continue
    b = random.randint(1,3)
    print(choices[c]," vs",choices[b])
    if outcomes[c] == b :
        print("You won!!!")
        uc += 1
    elif outcomes[b] == c :
        print("Computer won")
        cc += 1
    else :
        print("Tie")
    print("Scores :\nUser:",uc,"\tComputer:",cc)
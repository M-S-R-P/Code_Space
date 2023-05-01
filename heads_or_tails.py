import random
from getpass import getpass
while True :
    print("Press Enter to flip a coin or press n to quit",end=" ")
    a = input().strip()
    if a == 'n' or a == 'N' :
        break
    b = random.randint(0,1)
    if b == 0 :
        print("Heads!")
    else :
        print("Tails!")
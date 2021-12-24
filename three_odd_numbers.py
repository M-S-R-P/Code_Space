num1=int(input("Enter first value:"))
num2=int(input("Enter second value:"))
num3=int(input("Enter third value:"))
chck = 0
odd1,odd2,odd3=0,0,0,
if num1%2==1 :
    odd1 = num1
if num2%2==1 :
    odd2 = num2
if num3%2==1 :
    odd3 = num3
if odd1<odd2 :
    chck = odd2
else :
    chck = odd1
if odd1<odd3 :
    chck = odd3
if chck!=0 :
    print('The greatest odd number is: '+str(chck)+'.')
elif chck == 0 :
    print("None of the entered value is odd.")

a = int(input())
b = a*3
count = 0 
for i in range(a) :
    if i+1 == (a+1)/2 :
        print('WELCOME'.center(b, '-'))
        count = 1
    elif count == 0 :
        print( ('.|.'*(2*i+1) ).center(b, '-') )
    elif count == 1 :
        print(('.|.'*((a-i)*2-1)).center(b, '-'))
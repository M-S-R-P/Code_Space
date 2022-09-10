def alphrang(a) :
    def sub_alph(b) :
        lst = []
        d = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
        for i in range(1,b+2) :
            lst.append(d[a-i+1])
        lst += lst[-2::-1]
        print('-'.join(lst).center(4*a-3,'-'))
    for i in range(a) :
        sub_alph(i)
    for i in range(a-2,-1,-1) :
        sub_alph(i)


a = int(input())
alphrang(a)
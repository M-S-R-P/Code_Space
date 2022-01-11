def print_rangoli(size):
    dct = {1:'a',2:'b',3:'c',4:'d',5:'e',6:'f',7:'g',8:'h',9:'i',10:'j',11:'k',12:'l',13:'m',14:'n',15:'o',16:'p',17:'q',18:'r',19:'s',20:'t',21:'u',22:'v',23:'w',24:'x',25:'y',26:'z'}
    for i in range(size) :
        lst=[]
        ss=''
        for j in range(i+1) :
            lst.append(dct[size-j])
       #print(lst)
        flst = lst[:]
        lst.reverse()
        flst+=lst
       #print(flst)
        flst.pop(int(len(flst)/2)-1)
       #print(flst)
        ss='-'.join(flst)
        print(ss.center(size*4-3, '-'))
    for i in range(size-1) :
        l = int((len(flst)-1)/2)
        flst.pop(l)
        flst.pop(l)
        ss='-'.join(flst)
        print(ss.center(size*4-3, '-'))

a = int(input())
print_rangoli(a)
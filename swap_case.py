def swap_case(s):
    lst = list(s)
    for i in range(len(lst)) :
        if lst[i].isupper() :
            q = lst[i]
            lst[i]=q.lower()
        elif lst[i].islower :
            w = lst[i]
            lst[i]=w.upper()
    
    ss = ''.join(lst)
    return ss


s = 'Hello World!!!'
print(swap_case(s))
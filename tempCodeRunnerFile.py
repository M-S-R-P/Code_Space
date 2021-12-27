nstlst = []
for i in range(len(name)) :
    nstlst.insert(i , [name[i], score[i]]) 
nstlst.sort(key = lambda x:x[1], reverse = True)

least = nstlst[-1][1]

while (nstlst[-1][1]) == least :
    nstlst.pop()

last = 1
fnl = []
fnl.append(nstlst[-1][0])
if len(nstlst) != 1 :
    while nstlst[-last][1] == nstlst[-last-1][1] :
        fnl.append(nstlst[-last-1][0])
        last += 1
        if last >= len(nstlst) :
            break
fnl.sort()
for i in fnl :
    print (fnl[i])
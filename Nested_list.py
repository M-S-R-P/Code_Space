name=[]
score=[]
for _ in range(int(input())):
    name.append(input())
    score.append(float(input()))

nstlst = []
for i in range(len(name)) :
    nstlst.insert(i , [name[i], score[i]]) 
nstlst.sort(key = lambda x:x[1], reverse = True)

least = nstlst[-1][1]

while (nstlst[-1][1]) == least :
    nstlst.pop()

last = 1
print(nstlst[-1][0])
while nstlst[-last][1] == nstlst[-last-1][1] :
    print(nstlst[-last-1][0])
    last += 1
'''-----------------Implementation of Stack ADT in Python------------------'''
class Empty(Exception) :
    # Exception used when Stack is empty
    pass

class Stack() :
    # initialising list :
    def __init__(self) :
        self._data = []
    
    def push(self,e) :
        self._data.append(e)

    def is_empty(self) :
        return len(self._data) == 0 

    def pop(self) :
        if self.is_empty() :
            raise Empty("Stack is empty")
        return self._data.pop()
    
    def top(self) :
        return self._data[-1]

    def __len__(self) :
        return len(self._data)
    

# --------------------Stack Class Completed--------------------------
# ----------Driver Code : ( Matching delimiters )--------------------
s = Stack()
lefty = "([{"
righty = ")]}"
f = open("test.txt","r") 
ln = 1
for i in f :
    for j in i :
        if j in lefty :
            s.push(j)
            continue
        if j in righty :
            if s.is_empty() :
                print("Line no:",ln,"is incorrect") 
                break
            if s.is_empty() :
                print("Line no:",ln,"is incorrect")
                break
            if s.pop() != lefty[righty.index(j)] :
                print("Line no:",ln,"is incorrect")
                break
    else :
        print("Line no:",ln,"is correct")
    ln += 1
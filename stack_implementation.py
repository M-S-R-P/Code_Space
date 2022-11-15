'''-----------------Implementation of Stack ADT in Python------------------'''
class Empty(Exception) :
    # Exception used when Stack is empty
    pass

class Stack() :
    # initialising list :
    def __init__(self) :
        self._data = []
        self._size = 0 
    
    def push(self,e) :
        self._data.append(e)
        self._size += 1
    
    def pop(self) :
        if self._size == 0 :
            raise Empty("Stack is empty")
        self._size -= 1
        return self._data.pop()
    
    def top(self) :
        return self._data[-1]

# ----------Stack Class Completed-------------
# ----------Driver Code : --------------------
s = Stack()
s.push(123)
s.push("String")
for i in range(100,111) :
    s.push(i)
print(s.pop())
print(s._size)
print(s.top()) 
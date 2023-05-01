class Node() :
        __slots__ = 'data' , 'next'
        #def init(self,data=-1,next=None) :
        #    self.data = data
        #    self.next = next

class LinkedList() :
    
    def __init__(self) :
        self.head = None
        self.tail = None
        self.len = 0

    def append(self,data) :
        if self.head == None :      
            temp_node = Node()
            temp_node.data = data
            self.head = temp_node
            self.tail = temp_node
        else :
            temp_node = Node()
            temp_node.next = None
            temp_node.data = data
            self.tail.next = temp_node
            self.tail = temp_node
            self.len += 1

    def pop(self) :
        if self.head == None :
            print("List is empty") 
            return -1
        temp_data = self.head.data
        self.head = self.head.next
        return temp_data

    def display(self) :
        temp = self.head
        while(temp != None) :
            print(temp.data,end='-->')
            temp = temp.next
        print()
    
s = LinkedList()
s.append(1234)
for i in range(1,11) :
    s.append(i)
s.display()
for i in range(5) :
    print(s.pop())
s.display()
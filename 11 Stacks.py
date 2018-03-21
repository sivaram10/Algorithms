#Implementing Stacks

class Stack:
    
    def __init__(self):
        self.elements = []
        
    def push(self, element):
        self.elements.append(element)
        
    def pop(self):
        if self.isEmpty():
            print("This is an empty stack. There are no elements to remove")
        else:
            return self.elements.pop()
    def top(self):
        if self.isEmpty():
            print("This is an empty stack. There are no elements to remove")
        else:
            return self.elements[len(self.elements)-1]
    
    def isEmpty(self):
        return self.elements == []
    
    def size(self):
        return len(self.elements)
    
s= Stack()

s.isEmpty()
s.pop()
s.push(10)
s.top()
s.push(3)
s.top()
s.pop()
s.size()
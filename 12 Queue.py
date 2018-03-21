#Implementing Queues

class Queue:
    
    def __init__(self):
        self.elements = []
        
    def isEmpty(self):
        return self.elements == []
        
    def size(self):
        return len(self.elements)
    
    def enqueue(self, element):
        self.elements.insert(0, element)
        
    def dequeue(self):
        if self.isEmpty():
            print("Queue is empty. There are no elements to remove.")
        else:
            self.elements.pop()
            
    def tail(self):
        if self.isEmpty():
            print("Queue is empty.")
        else:
            return len(self.elements)-1
        
    def head(self):
        if self.isEmpty():
            print("Queue is empty.")
        else:
            return 0          
    
q = Queue()
q.size()
q.isEmpty()
q.dequeue()
q.enqueue(2)
q.dequeue()
q.tail()
q.head()
q.enqueue(2)
q.tail()
q.head()
q.enqueue(5)
q.tail()
q.head()
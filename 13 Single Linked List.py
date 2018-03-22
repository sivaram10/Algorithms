#Single Linked list implementation

class Node:
    
    def __init__(self, element):
        self.data = element
        self.next = None
        
    def getData(self):
        return self.data
    
    def getNext(self):
        return self.next
    
    def setData(self, newelement):
        self.data = newelement
        
    def setNext(self, newnext):
        self.next = newnext


class SingleLinkedList:
    
    def __init__(self):
        self.head = None
        
    def isEmpty(self):
        return self.head == None
    
    def add(self, element):
        temp = Node(element)
        temp.setNext(self.head)
        self.head = temp
        
    def size(self):
        current = self.head
        count = 0
        while current != None:
            count = count+1
            current = current.getNext()
        return count
    
    def search(self, element):
        current = self.head
        found = False
        while current != None and not found:
            if current.getData() == element:
                found = True
            else:
                current = current.setNext()
        return found
    
    def remove(self, element):
        current = self.head
        previous = None
        found = False
        while not found:
            if current.getData() == element:
                found = True
            else:
                previous = current
                current = current.getNext()
                
        if previous == None:
            self.head = current.getNext()
        else:
            previous.setNext(current.getNext())
            
    def show(self):
        current = self.head
        while current is not None:
            print(current.getData(),"->", end="", sep="")
            current = current.getNext()
        print(None)
        
    def reverseLinkedList(self):
        current = self.head
        reverseList = SingleLinkedList()
        while current is not None:
            reverseList.add(current.getData())
            current = current.getNext()
        reverseList.show()
        
mylist=SingleLinkedList()
mylist.add(1)
mylist.add(2)
mylist.add(3)
mylist.add(4)
mylist.add(5)
mylist.size()
mylist.search(5)
mylist.show()
mylist.remove(4)
mylist.show()
mylist.size()
mylist.reverseLinkedList()

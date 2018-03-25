# Binary Tree implementaion

class BinaryTree:
    
    def __init__(self, root):
        self.key = root
        self.leftChild = None
        self.rightChild = None
        
    def insertRight(self, newNode):
        if self.rightChild == None:
            self.rightChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.rightChild = self.rightChild
            self.rightChild = temp
            
    def insertLeft(self, newNode):
        if self.leftChild == None:
            self.leftChild = BinaryTree(newNode)
        else:
            temp = BinaryTree(newNode)
            temp.leftChild = self.leftChild
            self.leftChild = temp
            
    def getRightChild(self):
        return self.rightChild
    
    def getLeftChild(self):
        return self.leftChild
    
    def setRoot(self, obj):
        self.key = obj
        
    def getRoot(self):
        return self.key
    
    def preOrder(self):
        print(self.key)
        if self.leftChild:
            self.leftChild.preOrder()
        if self.rightChild:
            self.rightChild.preOrder()
            
    def postOrder(self):
        if self.leftChild:
            self.leftChild.postOrder()
        if self.rightChild:
            self.rightChild.postOrder()
        print(self.key)
        
    def inOrder(self):
        if self.leftChild:
            self.leftChild.inOrder()
        print(self.key)
        if self.rightChild:
            self.rightChild.inOrder()
        

tree = BinaryTree('a')
print(tree.getRoot())
print(tree.getLeftChild())
tree.insertLeft('b')
print(tree.getLeftChild())
print(tree.getLeftChild().getRoot())
tree.insertRight('c')
print(tree.getRightChild())
print(tree.getRightChild().getRoot())
tree.insertLeft('d')
tree.getRightChild().setRoot('change root')
print(tree.getRightChild().getRoot())
tree.insertLeft('d')
tree.insertLeft('e')
tree.postOrder()
tree.preOrder()
tree.inOrder()
    
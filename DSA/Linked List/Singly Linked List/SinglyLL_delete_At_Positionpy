class Node:
    def __init__(self):
        self.data=int(input("Enter data :"))
        self.next=None
class SinglyLL:
    def __init__(self):
        self.head=None    
    def insertNode(self):
        newnode=Node()
        
        if self.head is None:
            self.head=newnode
            return
        
        current=self.head
        while current.next:
            current=current.next
        current.next=newnode
    
    def LLsize(self):
        current =self.head
        size=0
        while current.next:
            current=current.next 
            size=size+1
        return size
    
    def deletePos(self, size, pos):
        if pos>size:
            return
        current=self.head
        for i in range(pos-1):
            dummy=current
            current=current.next
        dummy.next=current.next
        current.next=None

    def display(self):
        current= self.head
        while current:
            print(current.data,"->",end="")
            current=current.next
        print("None")

LL= SinglyLL()
choice=1
while(choice):
    LL.insertNode()
    choice=int(input("Enter choice -"))
sz=LL.LLsize()
ps=int(input("Enter position :"))
LL.deletePos(sz,ps)
LL.display()


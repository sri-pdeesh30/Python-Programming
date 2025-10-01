class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLinkedList():
    def __init__(self):
        self.head=None

    def insert(self):
        data=int(input("Enter Data :"))
        newnode=Node(data)
        
        if self.head==None:
            self.head=newnode
        else:
            current=self.head
            while current.next:
                current=current.next
            current.next=newnode
    
    def findLength(self):
        length=0
        temp=self.head
        while temp:
            temp=temp.next 
            length=length+1
        return length

    def insert_at_Position(self,size,pos):
       if pos>size:
           print("Invalid position")
           return
       data=int(input("Enter data to be inserted :"))
       newnode=Node(data)
       if pos==1:
           newnode.next=self.head
           self.head=newnode
           return
       temp=self.head
       for i in range(pos-2):
           temp=temp.next
       newnode.next=temp.next
       temp.next=newnode
           
    def display(self):
        current=self.head
        while current:
            print(current.data,"->",end=" ")
            current=current.next 
        print("None")

LL=SinglyLinkedList()
choice=1
while choice:
    LL.insert()
    choice=int(input("Enter choice :"))
LL.display()
sz=LL.findLength()
LL.insert_at_Position(sz,3)
LL.display()




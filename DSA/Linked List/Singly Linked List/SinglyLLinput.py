class Node:
    def __init__(self):
        self.data=int(input("Enter Data part :"))
        self.next=None
class SinglyLL:
    def __init__(self):
        self.head=None
    def insertNode(self):
        newnode=Node()
        if self.head==None:
            self.head=newnode
            return
        current=self.head
        while current.next:
            current=current.next
        current.next=newnode
    def display(self):
        current=self.head
        while current:
            print(current.data,"->",end=" ")
            current=current.next
        print("None")
LL=SinglyLL()
choice=1
while choice:
    LL.insertNode()
    choice=int(input("Enter choice :"))
LL.display()
    



            




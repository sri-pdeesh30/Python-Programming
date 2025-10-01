class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class SinglyLinkedList:
    def __init__(self):
        self.head=None

    def insert(self):
        data=int(input("Enter Data :"))
        newnode=Node(data)

        if self.head is None:
            self.head=newnode
        else:
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=newnode
    
    def display(self):
        temp=self.head
        while temp:
            print(temp.data,"->",end="")
            temp=temp.next
        print("None")
    
    def delete_at_beg(self):
        temp=self.head
        self.head=temp.next 
        temp.next=None
        del temp
LL1=SinglyLinkedList()
choice=1
while choice:
    LL1.insert()
    choice=int(input("Enter choice :"))
LL1.display()
LL1.delete_at_beg()
LL1.display()

class Node:
    def __init__(list):
        list.data=int(input("Enter data :"))
        list.next=None

class Singly:
    def __init__(list):
        list.head=None
    def insert(list):
        newnode=Node()

        if list.head is None:
            list.head=newnode
            return
        
        list.current=list.head
        while list.current.next:
            list.current=list.current.next
        list.current.next=newnode
        return list.head
    def delete_end(list):
        if list.head is None:
            return
        if list.head.next is None:
            list.head=None
            return
        list.current=list.head
        prev=None
        while list.current.next:
            prev=list.current
            list.current=list.current.next
        prev.next=None
        return list.head
    
    def display(list):
        list.current=list.head
        while list.current:
            print(list.current.data,"=>",end=" ")
            list.current=list.current.next
        print("None")

obj1=Singly()
obj2=Singly()

choice=1
while(choice):
    obj1.insert()
    obj2.insert()
    choice=int(input("\nEnter choice :"))

obj1.delete_end()
obj2.delete_end()

obj1.display()
obj2.display()
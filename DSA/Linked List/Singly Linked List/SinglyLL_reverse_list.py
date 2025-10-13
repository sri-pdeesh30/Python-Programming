class Node:
    def __init__(list):
        list.data = int(input("Enter data :"))
        list.next = None
class Singly:
    def __init__(list):
        list.head = None
        list.current = None
    
    def insert(list):
        newnode=Node()

        if list.head is None:
            list.head = newnode
            return
        
        list.current = list.head
        while list.current.next:
            list.current = list.current.next
        list.current.next = newnode

    def reverse(list):
        list.prev=None
        list.current=list.head
        
        while list.current:
            list.third=list.current.next
            list.current.next=list.prev 
            list.prev=list.current
            list.current=list.third
        list.head=list.prev

    def display(list):
        list.current=list.head
        while list.current:
            print(list.current.data,"=>",end=" ")
            list.current=list.current.next
        print("None")
        
LL=Singly()
choice=1
while choice:
    LL.insert()
    choice=int(input("Enter choice :"))
LL.reverse()
LL.display()
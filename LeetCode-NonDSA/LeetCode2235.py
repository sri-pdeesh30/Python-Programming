'''class Solution(object):
    def sum(self, num1, num2):
       return num1+num2'''
class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Singly:
    def __init__(self):
        self.head=None
    def insert(self,data):
        newnode=Node(data)
        
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
n1=Singly()
n1.insert(12)
n1.insert(13)
n1.insert(14)
n1.insert(15)
n1.insert(16)
n1.insert(17)
n1.insert(18)
n1.insert(19)
n1.insert(20)
n1.display()

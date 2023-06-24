class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class Sll:
    def __init__(self):
        self.head=None
    def insert_beginning(self,data):
        nb=Node(data)
        nb.next=self.head
        self.head=nb
    def display(self):
        if self.head is None:
            print("list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"->",end=" ")
                temp=temp.next
node_1=Node("anu")
SL=Sll()
SL.head=node_1
node_2=Node("vysh")
SL.head.next=node_2
print(node_1.next)
node_3=Node("anvitha")
node_2.next=node_3
print(node_2.next)

SL.display()
SL.insert_beginning("VYSHNAVI")
print()
SL.display()
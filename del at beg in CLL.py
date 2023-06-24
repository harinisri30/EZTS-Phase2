class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def _init_(self):
        self.head=None
        self.tail=None
    def del_begin(self):
        if self.head is None:
            print("CLL not exist")
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
            self.tail.next=self.head
    def display(self):
        if self.head is None:
            print("empty CLL")
        else:
            temp=self.head
            print(temp.data,"->",end=" ")
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,"->",end=" ")
            print(temp.next.data)    
cl=CLL()
node_1=Node(10)
node_2=Node(20)
node_3=Node(30)
print(node_1)
print(node_2)
cl.head=node_1
cl.tail=node_2
cl.tail.next=cl.head
node_1.next=node_2
cl.tail=node_2
cl.tail.next=cl.head
node_2.next=node_3
cl.tail=node_3
cl.tail.next=cl.head
cl.display()
cl.del_begin()
cl.display()
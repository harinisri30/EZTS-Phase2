class Node:
    def __init__(self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def del_last(self):
        temp1=self.head.next
        prev=self.head
        while temp1!=self.head:
            temp1=self.head.next
            prev=self.head
        temp1.next=None
        self.tail=prev
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
cl.del_last()
cl.display()
class Node:
    def __init__ (self,data):
        self.data=data
        self.next=None
class CLL:
    def __init__(self):
        self.head=None
        self.tail=None
    def display(self):
        if self.head is None:
            print("empty cLL")
        else:
            temp=self.head
            print(temp.data,"->",end=" ")
            while temp.next!=self.head:
                temp=temp.next
                print(temp.data,"->",end=" ")
            print(temp.next.data)
    def del_begin(self):
        if self.head is None:
            print("CLL is empty")
        else:
            temp=self.head
            self.head=temp.next
            temp.next=None
            self.tail.next=self.head
    def del_pos(self,pos):
       if self.head is None:
           print("circular linked list is empty")
       else:
           if(pos==1):
               del_begin()
           else:
               temp=self.head.next
               prev=self.head
               for i in range(1,pos-1):
                   temp=temp.next
                   prev=prev.next
               prev.next=temp.next
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
cl.del_pos(3)
cl.display()
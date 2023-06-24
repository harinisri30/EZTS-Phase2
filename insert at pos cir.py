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
    def insert_begin(self,data):
        new_node=Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.tail.next=self.head
        else:
            new_node.next=self.head
            self.head=new_node
            self.tail.next=self.head
    def insert_pos(self,pos,data):
       new_node=Node(data)
       if self.head is None:
           self.head=new_node
           slef.tail=new_node
           self.tail.next=self.head
       else:
           if(pos==1):
               insert_begin(data)
           else:
               temp=self.head
               for i in range(1,pos-1):
                   temp=temp.next
               new_node.next=temp.next
               temp.next=new_node
              
       
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
cl.insert_pos(2,100)
cl.display()
class Node:
    def __init__(self,data):
        self.prev=None
        self.data=data
        self.next=None
class DLL:
    def _init_(self):
        self.head=None
    def del_pos(self,pos):
       prev=self.head
       temp=self.head.next
       for i in range(1,pos-1):
           temp=temp.next
           prev=prev.next
       prev.next=temp.next
       temp.next=None
       temp.prev=prev
    def display(self):
        if self.head is None:
            print("DLL")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<->",end=" ")
                temp=temp.next
        
node_1=Node("harini sri")
print(node_1.data)
print(node_1.prev)
print(node_1.next)
dl=DLL()
print(dl.head)
dl.head=node_1
node_2=Node("anvitha")
node_1.next=node_2
node_2.prev=node_1
print(node_1.next)
node_3=Node("vyshnavi")
node_2.next=node_3
node_3.prev=node_2
node_4=Node("roshvitha")
node_3.next=node_4
node_4.prev=node_3
dl.display()
dl.del_pos(2)
print()
dl.display()
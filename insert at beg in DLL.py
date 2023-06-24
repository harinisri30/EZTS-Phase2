class Node:
    def __init__ (self,data):
        self.prev=None
        self.data=data
        self.next=None
class DLL:
    def __init__ (self):
        self.head=None
    def display(self):
        if self.head is None:
            print("doubly linked list is empty")
        else:
            temp=self.head
            while temp:
                print(temp.data,"<-->",end=" ")
                temp=temp.next
    def insert_begin(self,data):
        new_node=Node(data)
        temp=self.head
        new_node.next=temp
        temp.prev=new_node
        self.head=new_node
node_1=Node("harini sri")
print(node_1)
print(node_1.data)
print(node_1.prev)
print(node_1.next)
dl=DLL()
print(dl.head)
dl.head=node_1
print(dl.head)
print(dl.head.data)
node_2=Node("anvitha")
print(node_2)
print(node_2.data)
node_1.next=node_2
node_2.prev=node_1
print(node_1.next)
print(node_2.prev)
print(node_1.next.data)
print(node_2.prev.data)
node_3=Node("vyshu")
node_2.next=node_3
node_3.prev=node_2
print(node_2)
print(node_3)
print(node_2.next)
print(node_3.prev)
node_4=Node("rosh")
node_5=Node("snehitha")
node_3.next=node_4
node_4.prev=node_3
node_4.next=node_5
node_5.prev=node_4
dl.insert_begin("hari")
print()
dl.display()


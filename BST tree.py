class BST:
    def __init__ (self,key):
        self.key=key
        self.l_child=None
        self.r_child=None
    def insert_node(self,data):
        if self.key is None:
            print("BST doesn't exists")
            return
        if self.key==data:
            print("data is already present")
            return
        if self.key>data:
            if self.l_child:
                self.l_child.insert_node(data)
            else:
                self.l_child=BST(data)
        else:
            if self.r_child:
                self.r_child.insert_node(data)
            else:
                self.r_child=BST(data)    
root=BST(5)
root.insert_node(30)
root.insert_node(50)
root.insert_node(10)
root.insert_node(35)
root.insert_node(12)
root.insert_node(60)
root.insert_node(47)
root.insert_node(43)
root.insert_node(27)
root.insert_node(17)
root.insert_node(2)
print(root)


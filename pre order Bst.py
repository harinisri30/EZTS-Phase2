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
    def pre_order(self):
        print(self.key,end=" ")
        if self.l_child:
            self.l_child.pre_order()
        if self.r_child:
            self.r_child.pre_order()
root=BST(5)
lst=[1,2,4,5,7,4,8,3,4,5]
print(root)
for i in lst:
    root.insert_node(i)
root.pre_order()
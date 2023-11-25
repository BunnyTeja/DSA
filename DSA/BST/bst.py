class BinarySearchTreeNode:
    def __init__(self,data):
        self.data = data
        self.left = None
        self.right = None

    def addchild(self,data):
        if self.data == data:
            return
        #Add left subtre
        if data < self.data :
            if self.left: 
                self.left.addchild(data)
            else:
                self.left =  BinarySearchTreeNode(data)
        else:
        #Add right sub tree
             if self.right: 
                self.right.addchild(data)
             else:
                self.right =  BinarySearchTreeNode(data)
    
    def inordertraversal(self):
        elements = []
        # visit left node
        if self.left:
            elements += self.left.inordertraversal()
        # visit left node
        elements.append(self.data)
        # visit right node
        if self.right:
            elements += self.right.inordertraversal()
        return elements

    def postordertraversal(self):
        elements = []
        
        if self.left:
            elements += self.left.postordertraversal()  # this will take entirely to the left and
            # return the list with single element 
        if self.right:
            elements += self.right.postordertraversal()
        elements.append(self.data)  # here we will append the elements to the list
        return elements
    
    def preordertraversal(self):
        elements = []
        if self.data:
            elements.append(self.data)  # here we will append the elements to the list
        if self.left:
            elements += self.left.preordertraversal()  # this will take entirely to the left and
            # return the list with single element 
        if self.right:
            elements += self.right.preordertraversal()
        return elements
        

    def search(self,value):
        if self.data == value:
            return True
        elif value < self.data:
            if self.left:
               return self.left.search(value)
            else:
                return False
        else:
            if self.right:
               return self.right.search(value)
            else:
                return False
            
    def find_min(self):
        min_ele = self.data
        if self.left:
            return self.left.find_min()
        else:
            return min_ele

    def find_max(self):
        max_ele = self.data
        if self.right:
            return self.right.find_max()
        else:
            return max_ele

    def cal_sum(self):
        sum_all = 0
        if self.data:
            sum_all += self.data
        if self.left:
            sum_all += self.left.cal_sum()
        if self.right:
            sum_all += self.right.cal_sum()
        return sum_all
    
    def del_node(self,val):
        if val < self.data:
            if self.left:
                self.left = self.left.del_node(val)
        elif val > self.data:
            if self.right:
                self.right = self.right.del_node(val)
        else:
            if self.left is None and self.right is None:
                return None # this none will be returned and assigned 
                #to the curent node which is equal to the val 
            elif self.left is None:
                return self.right # this node will be assigned to the current node whose value is equal to val
            elif self.right is None:
                return self.left
            else:
                # minele = self.right.find_min() # find the min ele in right sub tree
                # self.data = minele # replace the current node value with least node value in right subtree
                # self.right = self.right.delete(minele) # then replace the right subtree by deleteing the min ele node in the right sub tree

                # 2nd way# Another way is to find the max ele in left subtree and assign the value
                # to current node data and delete the maxele from left subtree and return the 
                maxele = self.left.find_max()
                self.data = maxele
                self.left = self.left.delete(maxele)

        return self # finally we are returning the tree object after deleting the val


def buildtree(elements):
    root = BinarySearchTreeNode(elements[0])

    for i in range(1,len(elements)):
        root.addchild(elements[i])
    return root

if __name__ == '__main__':
    numbers = [15, 12, 7, 14, 27, 20, 23, 88]
    numbers_tree = buildtree(numbers)
    print("inorder", numbers_tree.inordertraversal())
    print("postorder", numbers_tree.postordertraversal())
    print("preorder", numbers_tree.preordertraversal())
    print(numbers_tree.search(25))
    print(numbers_tree.find_min())
    print(numbers_tree.find_max())
    print(numbers_tree.cal_sum())
    numbers_tree.del_node(20)
    print("inorder after deleting 20", numbers_tree.inordertraversal())


       


# Definition for a  binary tree node
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    # @param root, a tree node
    # @return nothing, do it in place
    def flatten(self, root):
        if root == None:
            return
        self.flatten(root.left)
        self.flatten(root.right)
        #now that we have two flattened children, attach left LL to deepest node in right LL
        #if left is none then the tree is flat
        if root.left == None:
            return
        iterator = root.left
        #until deepest node in left LL
        while iterator.right:
            iterator = iterator.right
        #assign right LL to be child of left LL
        iterator.right = root.right
        #assign right child to be left LL (with right LL attached to bottom of left LL)
        root.right = root.left
        #remove left child to complete flattening
        root.left = None

#
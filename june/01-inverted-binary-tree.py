#!/usr/bin/env python
# coding: utf-8

# In[3]:


# Invert a binary tree.

# Example:

# Input:

#      4
#    /   \
#   2     7
#  / \   / \
# 1   3 6   9
# Output:

#      4
#    /   \
#   7     2
#  / \   / \
# 9   6 3   1
# Trivia:
# This problem was inspired by this original tweet by Max Howell:

# Google: 90% of our engineers use the software you wrote (Homebrew), but you can’t invert a binary tree on a whiteboard so f*** off.


# In[4]:


# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = None
#         self.right = None
class Solution:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right
        
    def invertTree(self, root: TreeNode) -> TreeNode:
        if TreeNode is None:
            return 
        else:                       
            temp = TreeNode
            invertTree(TreeNode.left)
            invertTree(TreeNode.right)
            TreeNode.left = TreeNode.right
            TreeNode.right = temp
           
    def printTree(TreeNode):
        if TreeNode is None:
            return 
        printTree(TreeNode.left)
        print (TreeNode.val)
        printTree(TreeNode.right)
             
        example_tree = TreeNode(4)
        example_tree.left = TreeNode(2)
        example_tree.right = TreeNode(7)
        example_tree.left.left = TreeNode(1)
        example_tree.left.right = TreeNode(3)
        example_tree.right.left = TreeNode(6)
        example_tree.right.right = TreeNode(9)

        print("Orginial Tree")
        printTree(example_tree)

        invertTree(example_tree)

        print("Reversed Tree")
        printTree(example_tree)



        
        


# In[ ]:





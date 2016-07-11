# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None



class Solution(object):
    def height(self,x):
        if x.left != None:
            heightleft = self.height(x.left)+1
        else: 
            heightleft = 1
        if x.right != None:
            heightright = self.height(x.right)+1
        else:
            heightright = 1
        if heightleft > heightright:
            height = heightleft
        else:
            height = heightright
        return height
            
    
    
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if root == None:
            height = 0
        else:
            height = self.height(root)
        return  height

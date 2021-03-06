# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val   = x
#         self.left = None
#         self.right = None

class Solution:
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        return self.isValidBSTHelper(root, -sys.maxsize - 1, sys.maxsize)
    
    def isValidBSTHelper(self, root, minV, maxV):
        if root == None:
            return True
        if root.val <= minV or root.val >= maxV:
            return False
        return self.isValidBSTHelper(root.left, minV, root.val) and self.isValidBSTHelper(root.right, root.val, maxV)

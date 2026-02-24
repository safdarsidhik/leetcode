# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumRootToLeaf(self, root: Optional[TreeNode]) -> int:
        return self.dfs(root, 0)
    
    def dfs(self, node, currentNumber):
        if not node:
            return 0
        
        currentNumber = currentNumber * 2 + node.val
        
        if not node.left and not node.right:
            return currentNumber
        
        return self.dfs(node.left, currentNumber) + \
               self.dfs(node.right, currentNumber) 
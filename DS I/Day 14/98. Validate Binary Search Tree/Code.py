# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: Optional[TreeNode]) -> bool:
        values = []
        self.in_order_traversal(root, values)
        for i in range(1, len(values)):
            if values[i-1] >= values[i]:
                return False
        return True
    
    def in_order_traversal(self, root, values):
        if root is None:
                return
        self.in_order_traversal(root.left, values)
        values.append(root.val)
        self.in_order_traversal(root.right, values)
        
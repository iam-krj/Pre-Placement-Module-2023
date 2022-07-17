# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
def f(p,q):
    return (p is q) if not (p and q) else (p.val==q.val) and (f(p.left, q.right) and f(p.right, q.left))


class Solution:
    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
        return f(root, root)
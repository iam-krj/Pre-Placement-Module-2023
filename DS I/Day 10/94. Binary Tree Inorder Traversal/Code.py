import numpy as np
class Solution:
    def matrixReshape(self, mat: List[List[int]], r: int, c: int) -> List[List[int]]:
        return mat if len(mat) * len (mat[0]) != r*c or len(mat) * len(mat[0])==1 else list(np.reshape(mat,(r,c)))
            
       
        # Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        # # self.inorderTraversal(root.left)
        # print(root.val, end=" ")
        # self.inorderTraversal(root.right)
        # # inorderTraversal(root)
        
        if root is None:
            return []
        to_left = self.inorderTraversal(root.left)
        to_right = self.inorderTraversal(root.right)
        return [*to_left, root.val, *to_right]
        
        
#         *is used to unpack the elements in the list
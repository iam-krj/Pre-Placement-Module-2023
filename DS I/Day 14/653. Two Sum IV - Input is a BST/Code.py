# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTarget(self, root: Optional[TreeNode], k: int) -> bool:
        
        self.l  = []
        self.inorder(root)
        l,r =0, len(self.l)-1
        
        while(l<r):
            if self.l[l]+self.l[r]==k:
                return True
            elif self.l[l]+self.l[r]>k:
                r-=1
            else:
                l+=1
        return False
    
    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.l.append(root.val)
            self.inorder(root.right)

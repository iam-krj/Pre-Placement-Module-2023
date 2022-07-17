class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        to_left =  self.preorderTraversal(root.left)
        to_right = self.preorderTraversal(root.right)
        return [root.val,*to_left, *to_right]
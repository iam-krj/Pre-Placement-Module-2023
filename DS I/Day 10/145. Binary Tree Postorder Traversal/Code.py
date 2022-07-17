class Solution:
    def postorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root is None:
            return []
        to_left =  self.postorderTraversal(root.left)
        to_right = self.postorderTraversal(root.right)
        return [*to_left, *to_right, root.val]
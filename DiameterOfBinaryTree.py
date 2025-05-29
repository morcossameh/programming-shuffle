# Problem: https://leetcode.com/problems/diameter-of-binary-tree/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.max_diameter = 0

        def dfs(node):
            if not node:
                return 0  # height of empty node is 0
                
            left = dfs(node.left)
            right = dfs(node.right)

            # Update the global diameter
            self.max_diameter = max(self.max_diameter, left + right)

            # Return height of subtree rooted at this node
            return max(left, right) + 1

        dfs(root)
        return self.max_diameter

'''
111. Minimum Depth of Binary Tree
Easy

1442

692

Add to List

Share
Given a binary tree, find its minimum depth.

The minimum depth is the number of nodes along the shortest path from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:

Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its minimum depth = 2.

Accepted
420,024
Submissions
1,124,911
'''
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def minDepth(self, root: TreeNode) -> int:
        
        if not root:
            return 0
        
        if not root.left and not root.right:
            return 1 
        
        if root.left and root.right:
            return min(self.minDepth(root.left), self.minDepth(root.right)) + 1 
        
        if root.left:
            return self.minDepth(root.left) + 1
        
        if root.right:
            return self.minDepth(root.right) + 1 
        
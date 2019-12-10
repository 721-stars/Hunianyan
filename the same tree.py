# -*- coding: utf-8 -*-
"""
Created on Tue Dec  3 19:23:45 2019

@author: Administrator
"""
class Solution(object):
    def isSameTree(self, p, q):
        if p and q:
            return p.val==q.val and self.isSameTree(p.left,q.left) and self.isSameTree(p.right,q.right)
        if p==None and q==None:
            return True
        else:
            return False

class TreeNode:

     def __init__(self, x):

         self.val = x

         self.left = None

         self.right = None

if __name__ == "__main__":
    p = TreeNode(1)
    p.left, p.right = TreeNode(2),TreeNode(3)
    q=TreeNode(1)
    q.left,q.right= TreeNode(2), TreeNode(2)
    print(Solution().isSameTree(p,q))

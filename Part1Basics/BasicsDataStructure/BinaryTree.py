#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 15:52
# @Author  : qkwu
# @File    : BinaryTree.py

"""
二叉树，每个节点最多有两颗子树，子树有左右之分
常被用于实现二叉查找树与二叉堆
n0 = n2 + 1 （度节点个数关系）
满二叉树 完全二叉树
"""

class TreeNode:
    def __init__(self, val):
        self.val = val
        self.left, self.right = None, None

class Traversal(object):
    """树的遍历，递归实现"""
    def __init__(self):
        self.traverse_path = list()

    def preorder(self, root):
        if root:
            self.traverse_path.append(root.val)
            self.preorder(root.left)
            self.preorder(root.right)

    def inorder(self,root):
        if root:
            self.inorder(root.left)
            self.traverse_path.append(root.val)
            self.inorder(root.right)

    def postorder(self,root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            self.traverse_path.append(root.val)


"""
树类题目的复杂度分析
可统计对每个节点被访问的次数，进而求得总的时间复杂度。
"""

"""
Binary Search Tree - 二叉查找树
一颗二叉查找树(BST)是一颗二叉树，其中每个节点都含有一个可进行比较的键及相应的值，
且每个节点的键都大于等于左子树中的任意节点的键，而小于右子树中的任意节点的键。
使用中序遍历可得到有序数组，这是二叉查找树的又一个重要特征。
二叉查找树使用的每个节点含有两个链接，它是将链表插入的灵活性和有序数组查找的高效性结合起来的高效符号表实现。
"""
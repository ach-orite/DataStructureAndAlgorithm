#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 15:27
# @Author  : qkwu
# @File    : LinkedList.py

class ListNode:
    def __init__(self, val):
        self.val = val
        self.next = None

    def reverse(self, head):
        """反转链表  O(n)"""
        prev = None
        while head:
            temp = head.next
            head.next = prev
            prev = head
            head = temp
        return prev

class DListNode:
    def __init__(self, val):
        self.val = val
        self.prev = self.next = None

    def reverse(self, head):
        """反转双向链表，核心在于next与prev域的交换"""

"""
删除链表中的节点需要知道这个点的前驱节点，还有一种是伪删除
复制一个和要删除的节点值一样的节点然后删除，这样就不用知道其前驱
prev -> next = prev -> next -> next
"""

"""
链表指针的鲁棒性：
当访问链表中某个节点的cur.next时 一定要先判断cur是否为None
全部操作结束后，判断是否有环；有环的话，则置其中一端为None
"""

"""
Dummy Node
虚拟节点， 一般是dummy -> head
DummyNode的使用多针对单链表没有前指针的问题，保证链表的head不会丢失。
除此之外，还可以用dummynode来进行head的删除操作

当链表的head可能变化时，使用dummynode可以很好的简化代码，最终返回dummy.next即新的链表
"""

"""
快慢指针
一般是在单链表中让快慢两个指针都从表头开始遍历，当快指针到达末尾的时候，获取慢指针所在位置的值（如一半）
应用：1 取中间某个节点的值   2 判断是否有环（快追上慢）
"""


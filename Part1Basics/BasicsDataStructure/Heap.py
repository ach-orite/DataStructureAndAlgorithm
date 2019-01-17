#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 13:53
# @Author  : qkwu
# @File    : Heap.py

"""
堆通常指的是二叉堆，是一个近似完全二叉树的数据结构
使用数组来实现，子节点索引大于（或小于）父节点，每个节点的左右子树又是一个二叉堆
常用于实现优先队列
"""

"""
特点：
1 数组表示，以完全二叉树理解
2 同时最优地利用空间和时间
3 在索引从0开始数组里：父节点i 左孩子（2i+1）右孩子(2i+2) 子节点i 父节点(floor((i-1)/2))
"""

"""
基本操作（最大堆为例）
1. 最大堆调整，将堆的末端子节点作调整，使得子节点永远小于父节点
2. 创建 将堆所有数据重新排序
3. 堆排序 移除堆顶，并做最大堆调整的递归运算
"""

class MaxHeap:
    """最大堆实现"""
    def __init__(self, array=None):
        if array:
            self.heap = self._max_heapify(array)
        else:
            self.heap = []

    def _sink(self, array, i):
        # move node down the tree
        left, right = 2 * i + 1, 2 * i + 2
        max_index = i
        # should compare two children then determine which one to swap with
        flag = array[left] > array[right]
        if left < len(array) and array[left] > array[max_index] and flag:
            max_index = left
        if right < len(array) and array[right] > array[max_index] and not flag:
            max_index = right
        if max_index != i:
            array[i], array[max_index] = array[max_index], array[i]
            self._sink(array, max_index)

    def _swim(self, array, i):
        # move node up the tree
        if i == 0:
            return
        father = (i - 1) / 2
        if array[father] < array[i]:
            array[father], array[i] = array[i], array[father]
            self._swim(array, father)

    def _max_heapify(self, array):
        for i in range(len(array) // 2, -1, -1):
            self._sink(array, i)
        return array

    def push(self, item):
        self.heap.append(item)
        self._swim(self.heap, len(self.heap) - 1)

    def pop(self):
        self.heap[0], self.heap[-1] = self.heap[-1], self.heap[0]
        item = self.heap.pop()
        self._sink(self.heap, 0)
        return item
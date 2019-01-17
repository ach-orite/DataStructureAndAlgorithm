#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/16 16:58
# @Author  : qkwu
# @File    : Queue.py

# 在python中 队列(先进先出)是使用list实现的

queue = []
queue.append(1)  # Insert
queue.pop(0)  # Remove 必须是0

# Priority Queue 优先队列
# 使用heapq来实现

import heapq
e = 'element'
# enqueue  O(logn)
heapq.heappush(queue, e)
# dequeue  O(logn)
heapq.pop(queue)
# init  O(nlogn)
heapq.heapify(queue)
# peek  O(1)
queue[0]


# Deque 双端队列 同时具有栈和队列性质
import collections
dq = collections.deque()

# enqueue left  O(1)
dq.appendleft(e)
# enqueue right O(1)
dq.append(e)
# dequeue left  O(1)
dq.popleft()
# dequeue right O(1)
dq.pop()
# peek
left = dq[0]
right = dq[-1]


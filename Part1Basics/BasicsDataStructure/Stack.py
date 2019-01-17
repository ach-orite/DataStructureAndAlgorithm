#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 14:19
# @Author  : qkwu
# @File    : Stack.py

"""
栈是一种先进后出的数据结构
"""

stack = []

# efficient stack
import collections
stack = collections.deque()

e = 'element'
stack.pop()
stack.append(e)
peek = stack[-1]

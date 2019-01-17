#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Time    : 2019/1/17 14:24
# @Author  : qkwu
# @File    : Map.py


# Map是一种关联数组的数据结构，常被称为字典或键值对

hash_map = {}
hash_map['shuan'] = 98
point = hash_map['shuan'] # get value by key
point = hash_map.pop('shuan') # remove by key, return value

keys = hash_map.keys()
for key, value in hash_map.items():
    pass
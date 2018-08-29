#!/usr/bin/python
# -*- coding: UTF-8 -*-

counter = 100  # 赋值整型变量
miles = 1000.0  # 浮点型
name = "John"  # 字符串
a, b, c = 1, 2, "john"  # 多对象赋值
print(counter, "---", miles, "===", name)
print(a, "---", b, "===", c)
a = 1
b = 10
print(a, "---", b)
# 删除单个或多个对象的引用
print(id(a))
del a, b
# print(id(a))
# NameError: name 'a' is not defined


# 字符串
s = 'ilovepython'
print(s[1:5])
print(s * 2)

# 列表 数组
list = [ 'runoob', 786 , 2.23, 'john', 70.2 ]
tinylist = [123, 'john']
print(list)  # 输出完整列表
print(list[0])  # 输出列表的第一个元素
print(list[1:3])  # 输出第二个至第三个的元素
print(list[2:])  # 输出从第三个开始至列表末尾的所有元素
print(tinylist * 2)  # 输出列表两次
print(list + tinylist)  # 打印组合的列表

# 元组用"()"标识。内部元素用逗号隔开。但是元组不能二次赋值，相当于只读列表。
tinyuple = (123, 234)
# tinyuple[0] = 222 非法操作

# Python 字典
'''
列表是有序的对象集合，字典是无序的对象集合。 
两者之间的区别在于：字典当中的元素是通过键来存取的，而不是通过偏移存取。 
字典用"{ }"标识。字典由索引(key)和它对应的值value组成。
'''
dict = {}
dict['one'] = "This is one"
dict[2] = "This is two"
print('one' not in dict);

tinydict = {'name': 'john', 'code': 6734, 'dept': 'sales'}
print(dict['one'])  # 输出键为'one' 的值
print(dict[2])  # 输出键为 2 的值
print(tinydict)  # 输出完整的字典
print(tinydict.keys())  # 输出所有键
print(tinydict.values())  # 输出所有值

# 输出对象的类型
print(type(tinydict))
print(type(tinyuple))
print(type(tinylist))
# 判断对象的类型，是否与给出的相同
print(isinstance(counter, int));

a = int("333");
print(a);

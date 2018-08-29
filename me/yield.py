#!usr/bin/python3
import sys

'''
迭代器(Iterator)是允许程序员遍历集合的所有元素的对象，而不管其具体实现。在Python中，迭代器对象实现了iter()和next()两种方法。
String，List或Tuple对象可用于创建Iterator。
'''
list = [1,2,3,4]
it = iter(list) # this builds an iterator object
print (next(it), end=" ") #prints next available element in iterator
# Iterator object can be traversed using regular for statement

# for x in it:
#    print (x, end=" ")
# or using next() function
while True:
   try:
      print (next(it), end=" ")
   except StopIteration:
      break;

print("==============================")
#发生器(generator)是使用yield方法产生或产生一系列值的函数。
'''
当一个生成器函数被调用时，它返回一个生成器对象，而不用执行该函数。 当第一次调用next()方法时，函数开始执行，
直到它达到yield语句，返回yielded值。 yield保持跟踪，即记住最后一次执行，而第二个next()调用从前一个值继续。
'''
def fibonacci(n): #generator function
   a, b, counter = 0, 1, 0
   while True:
      if (counter > n):
         return
      yield a
      a, b = b, a + b
      counter += 1
f = fibonacci(5) #f is iterator object

while True:
   try:
      print (next(f), end=" ")
   except StopIteration:
      sys.exit()  # you have to import sys module for this
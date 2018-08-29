# -*- coding: utf-8 -*-
#字符串按单词反转 'i love you!' --> "you! love i"
s = 'i love you!'
list = s.split(" ")
s_11 = ""
for i in list:
    if i == list[0]:
        s_11 = i + s_11
    else:
        s_11 = i + " " + s_11
print(s_11)

#打印10000以内的所有素数
for i in range(2, 20):
    if i <= 2:
        print(2)
    else:
        a = True
        for j in range(2, i):
            if i % j / 2 == 0:
                a = False
                break
        if a:
            print(i)

#自己实现一个函数支持可变参数
def my_get(*abc, **kvs):
    print(abc)
    # print(type(abc))
    print(kvs)
    # print(type(kvs))

my_get(1, 2, 3, 'abc', adc = '111', ccc = '123')
my_get(*(1, 2, 3, 'abc'), **{'adc':'111', 'ccc':'123'})

#自己实现函数解决hanoi塔问题
def hannuota(n, source, targe, help):
    if n < 1:
        print('valueError')
    elif n == 1:
        print(source + '-->' + targe, n)
    else:
        hannuota(n - 1, source, help, targe);
        print(source + '-->' + help, n)
        hannuota(n - 1, help, targe, source)
        print(help + '-->' + targe, n)

hannuota(2, 'A', 'B', 'C')
#实现一个sort函数，通过参数指定拍讯函数用来实现按不同顺序进行排序
def sort(a, b, cmp = None):
    if cmp is None:
        if a < b:
            print(b, a, '====')
        else:
            print(a, b, '====')
    else:
        cmp(a, b)

def cmp(a, b):
    if a < b:
        print(a, b, '----')
    else:
        print(b, a, '----')
sort(1, 2, cmp)
sort(2, 1)

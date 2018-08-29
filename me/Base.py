from Tools.scripts.treesync import raw_input

'''
基本语法
'''
# 单行注释
print("Hello, World!");
print("你好，豆豆!");
paragraph = """这是一个段落。;
你好
"""
print(paragraph);
if True:
    print("Answer")
    print("True")
elif 1:
    print('123')
else:
    print("Answer")
    # 没有严格缩进，在执行时会不按照逻辑进行
    print("False")

# 等待用户输入，并回车结束
paragraph = raw_input("Press the enter key to exit.");

print(paragraph);
print((1024).to_bytes(2, byteorder = 'big'))
#本地字节规则的指示器，big-endian平台的值是'big',little-endian平台的值是'little'
print((1024).to_bytes(2, byteorder = 'little'))
print((65536).to_bytes(8, byteorder = 'little'))
print((-1024).to_bytes(4, byteorder = 'big', signed = True))#有符号
print((-1024).to_bytes(4, byteorder = 'little', signed = True))
print((500).to_bytes(2, byteorder = 'big'))
print((3345).to_bytes(2, byteorder = 'big'))    # why \r\x11
print((3124).to_bytes(2, byteorder = 'big'))    # why \x0c4 => \x0c + 4(0x34)
print((3140).to_bytes(2, byteorder ='little'))  # why D\x0c => D(0x44) + 0x0c
'''
%x --- hex 十六进制
%d --- dec 十进制
%o --- oct 八进制
'''
print('%x' % 3345)
print('%x' % 3124)
print(0xd11)
print(0xc34)

b = b'china\r\nus'
print(type(b))
s = b.decode()
print(s)
print(s.encode())

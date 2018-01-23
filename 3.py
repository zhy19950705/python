print(ord('A'))
print(ord('中'))
print(chr(66))
print(chr(23666))
print('\u4e2d\u6587')
x=b'ABC'
print(x)
a='ABC'.encode('ascii')
print(a)
b='中午'.encode('utf-8')
print(b)
# c='中文'.encode('ascii')
# print(c)

d=b'ABC'.decode('ascii')
print(d)

e=b'\xe4\xb8\xad\xff'.decode('utf-8',errors='ignore')#忽略小部分无效的字节
print("e:"+e)

print(len('ABC')+len('中午'))#求string的长度

print(len(b'Abc'))#求bytes的长度;
print(len(b'\xe4\xb8\xad\xe6\x96\x87'))
print(len('中文'.encode('utf-8')))

print('Hell,%s' % 'world')# %格式化字符串
print('Hi,%s,you have $%d.'% ('zjc',1000))

print('%2d-%02d' % (3,1))
print('%.2f' % 3.1415)

print('age:%s. gender: %s ' % (25,True))
print('growth rate: %d %%' % 7)   #用%%表示%

s1=72
s2=85
r=(s2-s1)/s2
print('%.2f' % r)
names=['aa','bb','cc']
for name in names:
    print(name)

sum =0
for x in [1,2,3,4,5]:
    sum=sum+x
print(sum)

print(list(range(5)))

sum=0
for x in range(101):
    sum=sum+x
print(sum)

L=['zjc','xww']
for x in L:
    print('Hello,%s' % (x))

n=1
while n<100:
    if(n>10):
        break
    print(n)
    n=n+1
print('end')

n=0
while n<10:
      n=n+1
      if n%2==0:
          continue
      print(n)
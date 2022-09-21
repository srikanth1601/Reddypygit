from collections import namedtuple

N = int(input())
names = [str(x) for x in input().split()]
sum =0
for i in range(N):
    lis = [x for x in input().split()]
    sum += int(lis[names.index('MARKS')])  
print(sum/N)

from math import gcd
from random import Random
from itertools import product

def counts(n, A):
 b=[1]+[0]*(n-1)
 for a in A: b=[b[j]+b[(j-a)%n] for j in range(n)]
 return b

def check(n,m):
 units=[a for a in range(1,n) if gcd(a,n)==1];N=sum(m)
 A=[a for a,c in zip(units,m) for _ in range(c)]
 cc={a: m[i]+m[units.index((-a)%n)] for i,a in enumerate(units)}
 inv=all(cc[a]==cc[(2*a)%n] for a in units)
 b=counts(n,A)
 cor=[sum(b[j]*b[(j+s)%n] for j in range(n)) for s in range(n)]
 flat=(all(x==(4**N-1)//n for x in cor[1:]) if (4**N-1)%n==0 else False)
 # Also zero must match
 flat &= cor[0]*n==4**N+n-1
 assert flat==inv, (n,m,inv,flat,cor)
 return inv
stats={}
for n in range(3,22,2):
 units=[a for a in range(1,n) if gcd(a,n)==1]
 if len(units)>12: continue
 found=sum(check(n,m) for m in product(range(2),repeat=len(units)))
 stats[n]=(2**len(units),found)
print('EXHAUSTIVE_BINARY',stats)
rr=Random(31415)
for n in (25,27,33,35,45,65,91,105):
 units=[a for a in range(1,n) if gcd(a,n)==1]
 for _ in range(100):
  # random sparse with small total n
  m=[0]*len(units)
  for z in range(5):m[rr.randrange(len(units))]+=rr.randrange(2)
  check(n,m)
 print('RANDOM_OK',n,100)
for n,A in [(9,[1,1,2,2,4,4]),(15,[1,2,4,8]),(21,[1,2,4,8,16,11])]:
 b=counts(n,A);N=len(A);cs=[sum(b[j]*b[(j+s)%n] for j in range(n)) for s in range(n)]
 print('EXAMPLE',n,'A',A,'b',b,'cor',cs,'flat',len(set(cs[1:]))==1,'uniform_nonempty',b[0]-1==b[1])

# Independent exact reference profiles for the two illustrative boundary cases.
b=counts(65,[1,2,4,8,16,32])
assert b == [1]*64+[0]
assert [sum(b[j]*b[(j+k)%65] for j in range(65)) for k in range(65)] == [64]+[63]*64
print('COMPOSITE_EXAMPLE_OK n=65 b_0..63=1 b_64=0 autocorrelation=64,63')

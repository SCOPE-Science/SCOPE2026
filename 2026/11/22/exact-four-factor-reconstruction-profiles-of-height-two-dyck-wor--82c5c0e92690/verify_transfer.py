#!/usr/bin/env python3
"""Independent generating-function coefficient checks and local occurrence identities."""
from fractions import Fraction
from itertools import product
from random import Random

def expected_count(n):
  total=1
  for b in range(n//2+1):
    for c in range(n//3+1):
      L=b+c
      if L==0:continue
      for k in range(1,L+1):
        for f,g in product((0,1),repeat=2):
          amin=k-1+f+g
          if c:
            valid=n>=2*b+3*c+amin
          elif k==1 and f==g==0:
            valid=n==2*b
          else:
            valid=n>=2*b+amin
          total+=int(valid)
  return total

def polynomial_times(a,b,N):
  r=[0]*(N+1)
  for i,x in enumerate(a):
    for j,y in enumerate(b):
      if i+j<=N:r[i+j]+=x*y
  return r

N=55
# F = z*(1+z^2+z^3-z^4+3z^5-z^6+2z^7-2z^8) / ((1-z)^2 (1-z^3)(1-z^4))
# Invert the factors by formal recurrence, independently of feasibility tuple count.
num=[0]*(N+1)
for j,v in enumerate([1,0,1,1,-1,3,-1,2,-2], start=1):num[j]=v
f1=[i+1 for i in range(N+1)] # 1/(1-z)^2
f3=[int(i%3==0) for i in range(N+1)]
f4=[int(i%4==0) for i in range(N+1)]
series=polynomial_times(polynomial_times(polynomial_times(num,f1,N),f3,N),f4,N)
for n in range(1,N+1):assert series[n]==expected_count(n),(n,series[n],expected_count(n))
assert series[:16]==[0,1,2,4,8,12,20,30,43,58,78,101,129,160,197,239]

rng=Random(0x5A2D)
for trial in range(500):
    n=rng.randint(2,250)
    parts=[]
    while n:
        p=rng.randint(1,n)
        parts.append(p); n-=p
    L=sum(p>=2 for p in parts)
    if not L: continue
    b=parts.count(2);c=sum(p>=3 for p in parts)
    d=sum(parts[i]>=2 and parts[i+1]>=2 for i in range(len(parts)-1))
    f=int(parts[0]==1);g=int(parts[-1]==1);m=sum(parts)
    w=''.join('1'+'10'*(p-1)+'0' for p in parts)
    h={format(v,'04b'):sum(w[i:i+4]==format(v,'04b') for i in range(len(w)-3)) for v in range(16)}
    expect={'1100':b,'1101':c,'0100':c,'1010':m-3*L+1-f-g+d,
        '0101':m-2*b-3*c-f-g,'1011':L-1+f-d,'0010':L-1+g-d,
        '0011':d,'1001':L-1+g,'0110':L-1+f}
    assert h=={s:expect.get(s,0) for s in h},(parts,h,expect)
print('TRANSFER_AND_OCCURRENCE_OK',N,series[N])

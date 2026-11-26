"""Exact integer arithmetic for ternary alphabet Abelian-square modulus-nine law."""
from collections import defaultdict
from math import comb
P={(0,0):3,(1,0):1,(-1,0):1,(0,1):1,(0,-1):1,(1,-1):1,(-1,1):1}
S=P.copy(); del S[(0,0)]

def mult(A,B):
    C=defaultdict(int)
    for (i,j),v in A.items():
      for (k,l),w in B.items(): C[(i+k,j+l)] += v*w
    return dict(C)

def power(A,n):
    C={(0,0):1}
    for _ in range(n): C=mult(C,A)
    return C

P3=power(P,3); Psub={(3*i,3*j):v for (i,j),v in P.items()}
assert all((P3.get(k,0)-Psub.get(k,0))%3==0 for k in set(P3)|set(Psub))
R={k:(P3.get(k,0)-Psub.get(k,0))//3 for k in set(P3)|set(Psub)}
for d in range(3):
    RP=mult(R,power(P,d))
    projection={(i//3,j//3):v%3 for (i,j),v in RP.items() if i%3==0 and j%3==0 and v%3}
    expected={k:(d*v)%3 for k,v in S.items() if (d*v)%3}
    assert projection==expected,(d,projection,expected)
for n in range(0,220):
    ct=power(P,n)[(0,0)] if n<8 else None
    if ct is not None:
        direct=sum(comb(n,j)**2*comb(2*j,j) for j in range(n+1))
        assert ct==direct
A=[1,3]
for n in range(1,1600):
    v=((10*n*n+10*n+3)*A[n]-9*n*n*A[n-1])
    assert v%(n+1)**2==0
    A.append(v//(n+1)**2)
for n in range(1601):
    x=n; r=1
    while x:
        d=x%3; r=r*[1,3,6][d]%9; x//=3
    assert A[n]%9==r,(n,A[n]%9,r)
    if n<120:
        direct=sum(comb(n,j)**2*comb(2*j,j) for j in range(n+1))
        assert direct==A[n]

for r in range(1,7):
    count1=sum(1 for n in range(3**r) if n<1601 and A[n]%9 in (3,6)) if 3**r<=1601 else None
    if count1 is not None: assert count1==2*r
print('PASS: all three Laurent support projections; CT/binomial checks; recurrence and mod-nine digit law for n=0..1600')

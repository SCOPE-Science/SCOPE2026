"""Exact arithmetic checks for the Rademacher projection stopping theorem."""
from fractions import Fraction as F
from itertools import product

def mm(A,B):
    return [[sum(a*b for a,b in zip(row,col)) for col in zip(*B)] for row in A]
def proj(u):
    d=len(u);return [[F(i==j)-F(u[i]*u[j],d) for j in range(d)] for i in range(d)]
def identity(d):return [[F(i==j) for j in range(d)] for i in range(d)]
def hadamard(n):
    H=[[1]]
    while len(H)<n:
        H=[r+r for r in H]+[r+[-v for v in r] for r in H]
    return H
checks=0
for d in [2,4,8]:
    H=hadamard(d);P=identity(d)
    for u in H:P=mm(proj(u),P)
    assert all(not a for row in P for a in row)
    checks+=d*d
for d in [3,5,7]:
    S=list(product([-1,1],repeat=d));Q=[[int((i!=j)) for j in range(d)] for i in range(d)]
    for u in S:
        B=[[d*int(i==j)-u[i]*u[j] for j in range(d)] for i in range(d)]
        assert [[v%2 for v in row] for row in B]==Q
        checks+=1
    for u in S[:min(len(S),12)]:
        for v in S[:min(len(S),12)]:
            x=[sum((d*int(i==j)-v[i]*v[j])*(d*int(j==0)-u[j]*u[0]) for j in range(d)) for i in range(d)]
            assert [z%2 for z in x]==[int(i!=0) for i in range(d)]
            checks+=1
for d in [2,3,4,5,8]:
    for num in range(-5,6):
        eta=F(num,2*d);c=1-2*eta+d*eta*eta
        assert c-F(1,1)+F(1,d)==d*(eta-F(1,d))**2
        checks+=1
print('PASS',checks,'exact rational/integer checks')

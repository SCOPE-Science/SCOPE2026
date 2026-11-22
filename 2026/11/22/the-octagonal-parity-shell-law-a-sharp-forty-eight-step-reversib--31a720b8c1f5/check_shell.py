#!/usr/bin/env python3
"""Exact modular check of the nine radial-shell relations and wave dynamics.
This does not enumerate any physical octagon's full vertex set.
"""
from math import gcd
D = 9
# Columns of A on radial shell basis, root at shell zero.
cols = [1 << 1, (1 << 0) | (1 << 2)] + [1 << (j+1) for j in range(2,8)] + [0]
assert len(cols) == D

def apply(C,v):
    out=0
    for i,c in enumerate(C):
        if (v>>i)&1:out ^=c
    return out

def compose(C,E):
    return [apply(C,x) for x in E]

def rank(C,dim):
    basis={}
    for x in C:
        v=x
        while v:
            k=v.bit_length()-1
            if k in basis:v^=basis[k]
            else:
                basis[k]=v;break
    return len(basis)

def identity(n):return [1<<i for i in range(n)]
def plus(C,E):return [a^b for a,b in zip(C,E)]
def power(C,k):
    z=identity(len(C))
    while k:
        if k&1:z=compose(C,z)
        C=compose(C,C);k>>=1
    return z

I=identity(D)
M2=power(cols,2)
M7=power(cols,7)
assert compose(M7,plus(M2,I)) == [0]*D
# Degree eight polynomial cannot annihilate the radial cyclic vector.
powers=[apply(power(cols,j),1) for j in range(D)]
assert rank(powers,D) == 9
assert rank(power(cols,7),D) < rank(power(cols,6),D)
assert rank(power(plus(cols,I),2),D) < rank(plus(cols,I),D)
# T(u,w)=(Au+w,u) in dimension 18.
T=[]
for j in range(D):T.append(apply(cols,1<<j) | (1<<(D+j)))
for j in range(D):T.append(1<<j)
N=2*D
assert power(T,48)==identity(N)
assert power(T,24)!=identity(N)
assert power(T,16)!=identity(N)

def ker(C):return len(C)-rank(C,len(C))
def exponent(t):
    k=0
    while t%2==0:t//=2;k+=1
    zero=ker(cols) if k==0 else 2*ker(power(cols,2**(k-1)))
    one=2*ker(power(plus(cols,I),2**k)) if t%3==0 else 0
    return zero+one

def mobius(n):
    out=1;p=2
    while p*p<=n:
        if n%p==0:
            n//=p
            if n%p==0:return 0
            out=-out
            while n%p==0:n//=p
        p+=1
    if n>1:out=-out
    return out

periods=[]
for t in [1,2,3,4,6,8,12,16,24,48]:
    actual=ker(plus(power(T,t),identity(N)))
    predicted=exponent(t)
    assert actual==predicted,(t,actual,predicted)
    count=sum(mobius(t//d)*(2**exponent(d)) for d in range(1,t+1) if t%d==0)
    assert count>0 and count%t==0,(t,count)
    periods.append((t,actual,count//t))
print('Radial A minimal polynomial: X^7 (X+1)^2')
print('Wave order 48, primitive orbit periods and Q=2 shell-module counts:')
for row in periods:print(*row)
print('PASS')

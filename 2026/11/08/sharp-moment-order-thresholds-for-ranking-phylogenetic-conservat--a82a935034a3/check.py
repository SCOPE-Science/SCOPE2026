#!/usr/bin/env python3
"""Exact rational checks for moment-order sensitivity in rooted PD protection."""
from fractions import Fraction as F
from itertools import combinations
from math import comb, factorial

def laws(n):
    eps=F(1,2**(n+1))
    b=[F(comb(n,j),2**n) for j in range(n+1)]
    v=[(-1)**(n-1-j)*comb(n-1,j) for j in range(n)]+[0]
    return b,[[b[j]+sgn*eps*v[j] for j in range(n+1)] for sgn in [-1,1]],eps

def falling(x,r):
    out=1
    for t in range(r):out*=x-t
    return out

def q(law,r):
    n=len(law)-1
    return sum(law[j]*F(falling(j,r),falling(n,r)) for j in range(r,n+1))

def assignments(law):
    n=len(law)-1
    return {mask:law[mask.bit_count()]/comb(n,mask.bit_count()) for mask in range(1<<n)}

def pd(edges, survivors):
    return sum(length for clade,length in edges if clade&survivors)

def intervention_gain(law,edges,target):
    n=len(law)-1; dist=assignments(law)
    val=F(0)
    for extinct,prob in dist.items():
        survivors=((1<<n)-1)^extinct
        val+=prob*(pd(edges,survivors|(1<<target))-pd(edges,survivors))
    return val

def direct_gain(law,edges,target):
    return sum(length*q(law,clade.bit_count()) for clade,length in edges if clade&(1<<target))

for n in range(3,11):
    base,(minus,plus),eps=laws(n)
    assert all(t>0 for L in (minus,plus) for t in L)
    assert sum(minus)==sum(plus)==1
    assert all(q(minus,r)==q(plus,r) for r in range(n-1))
    assert q(minus,n)==q(plus,n)
    assert q(plus,n-1)-q(minus,n-1)==2*eps/n
    print('n=',n,' lower-order moments 0..',n-2,' equal; distinguishing moment',n-1,' gap',2*eps/n)

# Root has children A={a,b,c} and {d}; A branches to {a,b} and c.
# tips ordered (a,b,c,d), all positive edge lengths.
edges=[(0b0001,F(3)),(0b0010,F(1,8)),(0b0100,F(1,8)),(0b1000,F(11,2)),(0b0011,F(1)),(0b0111,F(8))]
base,(minus,plus),eps=laws(4)
for name,law in [('minus',minus),('base',base),('plus',plus)]:
    gains=[intervention_gain(law,edges,i) for i in range(4)]
    independent=[direct_gain(law,edges,i) for i in range(4)]
    assert gains==independent,(name,gains,independent)
    if name=='minus': assert gains[3]>max(gains[:3]) and gains[0]-gains[3]==-F(1,16)
    elif name=='plus': assert gains[0]>max(gains[1:]) and gains[0]-gains[3]==F(1,16)
    else: assert gains[0]==gains[3]>gains[1] and gains[3]>gains[2]
    print(name,'K law',list(map(str,law)), 'q1..4',[str(q(law,i)) for i in range(1,5)], 'gains', list(map(str,gains)))
print('PASS exact enumeration of all 16 extinction subsets and all tree edges.')

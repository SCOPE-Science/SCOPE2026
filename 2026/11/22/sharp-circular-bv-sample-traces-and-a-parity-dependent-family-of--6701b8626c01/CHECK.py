"""Exact arithmetic checks for sharp periodic BV/W^{1,1} sampling trace design."""
from fractions import Fraction as F
from itertools import product
from math import gcd, floor

def trace_constant_squared(gaps):
    n=len(gaps)
    assert all(x>0 for x in gaps) and sum(gaps)==1
    largest=F(0)
    witness=None
    for k in range(n):
        for start in range(n):
            L=sum((gaps[(start+j)%n] for j in range(k+1)),F(0))
            value=(k*(1-L)**2+(n-k)*L**2)/4
            if value>largest:
                largest,witness=value,(k,start,L)
    return largest,witness

def optimum(n):
    return F(floor(n*n/4)+1,4*n)

def alternating(n,e):
    return [(F(1,1)+(e if j%2==0 else -e))/n for j in range(n)]

checks=0
for n in range(2,39):
    uniform=[F(1,n)]*n
    val,_=trace_constant_squared(uniform)
    assert val==optimum(n),(n,val,optimum(n))
    checks+=1
for n in range(2,25):
    for raw in product([1,2,3],repeat=min(n,7)):
        if n>7:break
        g=[F(x,sum(raw)) for x in raw]
        val,_=trace_constant_squared(g)
        assert val>=optimum(n)
        checks+=1
for n in (2,6,10,14,18,22,26,30):
    for e in (F(0),F(1,4),F(2,5),F(5,12),F(1,2),F(3,4)):
        val,_=trace_constant_squared(alternating(n,e))
        should=optimum(n) if e*e+2*e<=1 else (F((n//2)**2+1,4*n)+(e*e+2*e-1)/(4*n))
        assert val==should,(n,e,val,should)
        checks+=1
for n in (4,8,12,16):
    assert gcd(n,n//2+1)==1
    checks+=1
for n in (6,10,14,18):
    assert gcd(n,n//2+1)==2
    checks+=1
print('PASS',checks,'exact rational cases')
print('n=6 optimal C^2',optimum(6),'alternating tolerance |epsilon| <= sqrt(2)-1')

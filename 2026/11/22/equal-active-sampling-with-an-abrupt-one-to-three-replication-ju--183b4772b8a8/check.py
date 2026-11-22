"""Exact arithmetic verification of a two-target sample-viability allocation theorem.
Run: python3 check.py (standard library only)."""
from fractions import Fraction as Q
from itertools import product
from math import exp, log

# Rational polynomial dictionary operations.
def clean(a):
    return {k:v for k,v in a.items() if v}
def add(a,b):
    d=dict(a)
    for k,v in b.items(): d[k]=d.get(k,Q(0))+v
    return clean(d)
def scale(a,c): return clean({k:c*v for k,v in a.items()})
def mul(a,b):
    d={}
    for k,v in a.items():
        for j,w in b.items(): d[k+j]=d.get(k+j,Q(0))+v*w
    return clean(d)
def power(a,n):
    out={0:Q(1)}
    for _ in range(n): out=mul(out,a)
    return out
def minus(a,b): return add(a,scale(b,-1))
def poly_for(k,p=Q(4,5)):
    # variable z = exp(-lambda B/6), k divides 6.
    a={0:1-p,6//k:p}
    b={0:1-p,12//k:p}
    return add(minus({0:Q(1)},scale(power(a,k),2)),power(b,k))
P1,P2,P3=(poly_for(k) for k in (1,2,3))
z1={1:Q(1)}
poly_minus_one=minus(z1,{0:Q(1)})
poly_plus_one=add(z1,{0:Q(1)})
three_z4_minus_one={4:Q(3),0:Q(-1)}
last={4:Q(1),2:Q(2),0:Q(2)}
rhs=scale(mul(mul(power(poly_minus_one,2),power(poly_plus_one,2)),mul(three_z4_minus_one,last)),Q(-12,125))
assert minus(P3,P1)==rhs, 'Factorization of P3-P1 failed'
# Reduce at z^4=1/3 via exact arithmetic.
def reduce_mod(a):
    d={}
    for n,c in a.items():
        k,r=divmod(n,4); d[r]=d.get(r,Q(0))+c/Q(3)**k
    return clean(d)
expected={3:Q(8,675)*54,2:Q(8,675)*(-18),0:Q(8,675)*(-13)}
assert reduce_mod(minus(P3,P2))==clean(expected),'Crossover gap reduction failed'
q=Q(759,1000)
assert 3*q**4 < 1
assert 54*q**3-18*q**2-13>0
assert 54*q**3-18*q**2-13==Q(241797866,1000000000) or 54*q**3-18*q**2-13>0
# Cross-check P_k against an exact enumeration of all viable bottle patterns.
def exact_by_enumeration(k,B,p):
    # B here is chosen so e^{-lambda B/k} is rational, and all viable sets simple.
    total=Q(0)
    for bits in product((0,1), repeat=k):
        m=sum(bits)
        prob=p**m*(1-p)**(k-m)
        total+=prob*(1-B**m)**2
    return total
for p in (Q(1,5),Q(1,2),Q(4,5)):
    for t in (Q(1,4),Q(1,2),Q(3,4)):
        for k in (1,2,3):
            formula=1-2*(1-p+p*t)**k+(1-p+p*t**2)**k
            assert formula==exact_by_enumeration(k,t,p)
# Exploratory grid checks; not offered as infinite proof.
p=.8
Bstar=1.5*log(3)
def score(k,B):
    t=exp(-B/k)
    return 1-2*(1-p+p*t)**k+(1-p+p*t*t)**k
for B in (Bstar-.05,Bstar+.05):
    vals=[score(k,B) for k in (1,2,3)]
    assert vals.index(max(vals))==(0 if B<Bstar else 2)
print('PASS: exact polynomial identities, 27 enumerated model checks, rational separation, crossover spot checks')

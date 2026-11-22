#!/usr/bin/env python3
"""Exact checks for random chord local/global crossing fluctuation formulas."""
from fractions import Fraction as F
from functools import lru_cache
from math import factorial

@lru_cache(None)
def matchings(points):
    points=tuple(points)
    if not points:
        yield ()
        return
    first=points[0]
    for j in range(1,len(points)):
        second=points[j]
        rest=points[1:j]+points[j+1:]
        for other in matchings_tuple(rest):
            yield ((first,second),)+other

@lru_cache(None)
def matchings_tuple(points):
    points=tuple(points)
    if not points:
        return ((),)
    a=points[0]
    out=[]
    for j in range(1,len(points)):
        b=points[j]
        for o in matchings_tuple(points[1:j]+points[j+1:]):
            out.append(((a,b),)+o)
    return tuple(out)

def cross(x,y):
    a,b=x; c,d=y
    return (a<c<b)!=(a<d<b)

def fpoly(t):
    # 4 * [integral_0^t s h(s)ds + t*integral_t^(1/2) h(s)ds],
    # h(s)=2s(1-s)-1/3, and the integrals have exact primitives.
    t=F(t)
    A=lambda x: -x**4/F(2)+2*x**3/F(3)-x*x/F(6)
    B=lambda x: -2*x**3/F(3)+x*x-x/F(3)
    return 4*(A(t)+t*(B(F(1,2))-B(t)))

nassert=0
for t in [F(0),F(1,20),F(1,10),F(1,6),F(1,4),F(1,3),F(2,5),F(1,2)]:
    q=2*t*(1-t)
    assert fpoly(t)==q*q/6,(t, fpoly(t),q*q/6)
    assert q*(1-q)/45 - q**4/36 >= 0
    nassert+=2

# Exact moments of first projection Q=2U(1-U) for U uniform [0,1].
assert F(1,3)==F(2)*(F(1,2)-F(1,3))
assert F(2,15)==F(4)*(F(1,3)-F(1,2)+F(1,5))
assert F(2,15)-F(1,9)==F(1,45)
nassert+=3

for n in range(2,7):
    records=matchings_tuple(tuple(range(2*n)))
    count=len(records)
    assert count==factorial(2*n)//(2**n*factorial(n))
    sums=[0,0,0,0]
    for m in records:
        c=sum(cross(m[i],m[j]) for i in range(n) for j in range(i+1,n))
        # Distinguish the chord containing the leftmost circular endpoint.
        d=sum(cross(m[0],m[j]) for j in range(1,n))
        sums[0]+=c; sums[1]+=c*c; sums[2]+=d; sums[3]+=c*d
    ec,ec2,ed,ecd=[F(v,count) for v in sums]
    assert ec==F(n*(n-1),6),(n,ec)
    assert ec2-ec*ec==F(n*(n-1)*(n+3),45),(n,ec2-ec*ec)
    assert ed==F(n-1,3),(n,ed)
    assert ecd-ec*ed==F(2*(n-1)*(n+3),45),(n,ecd-ec*ed)
    nassert+=5

# Exact finite centered-deletion identity from the decomposed conditional integrals.
for n in range(2,100):
    lhs=(n-1)*F(1,5)+(n-1)*(n-2)*F(1,45)
    rhs=F((n-1)*(n+7),45)
    assert lhs==rhs
    nassert+=1

print(f"PASS: {nassert} exact assertions, including all {(2*6-1)}!!-type finite matchings through six chords")

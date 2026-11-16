#!/usr/bin/env python3
"""Supplementary exact-arithmetic checks for three equal-ball Fourier-intensity jet identities."""
from fractions import Fraction as F
from itertools import product

def moments(vals, k):
    return sum((a-b)**k for a in vals for b in vals)

def centered(vals):
    m = sum(vals)/3
    return [v-m for v in vals]

def fpoly(B, x, y):
    return [F(a)*x+F(b)*y for a,b in B]

def assert_eq(a,b):
    assert a == b,(a,b)

count=0
for v in product(range(-3,4),repeat=3):
    t = centered([F(q) for q in v]); p2=sum(a*a for a in t); p3=sum(a**3 for a in t)
    m2=moments(t,2);m4=moments(t,4);m6=moments(t,6)
    assert_eq(m2,6*p2); assert_eq(m4,9*p2*p2)
    assert_eq(m6,F(33,2)*p2**3-18*p3**2)
    count+=3
A=[(F(2),F(1)),(F(-1),F(2)),(F(-1),F(-3))]
B=[(F(2,7),F(3)),(F(-13,7),F(-2)),(F(11,7),F(-1))]
assert_eq([sum(t[0] for t in Q) for Q in (A,B)],[0,0]); count+=1
assert_eq([sum(t[1] for t in Q) for Q in (A,B)],[0,0]); count+=1
for x,y in product(range(-3,4),repeat=2):
    v=fpoly(A,F(x),F(y));w=fpoly(B,F(x),F(y))
    assert_eq(sum(t*t for t in v),sum(t*t for t in w))
    assert_eq(moments(v,4),moments(w,4));count+=2
assert sum(t[0]**3 for t in A)!=sum(t[0]**3 for t in B)
assert abs(sum(t[0]**3 for t in A))!=abs(sum(t[0]**3 for t in B))
count+=2
assert B != A and B != [(-a,-b) for a,b in A]
assert sorted(B)!=sorted(A) and sorted(B)!=sorted([(-a,-b) for a,b in A]);count+=2
print('THREE_BALL_EXACT_MOMENT_CHECK_OK assertions='+str(count))

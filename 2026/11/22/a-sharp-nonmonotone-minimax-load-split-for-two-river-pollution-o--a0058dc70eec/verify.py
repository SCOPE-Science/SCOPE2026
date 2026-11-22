#!/usr/bin/env python3
"""Exact-rational finite checks for the two-outfall minimax theorem.
Only standard-library fractions; finite corroboration, not a universal proof.
"""
from fractions import Fraction as F
from random import Random

def peak_fraction(w, q):
    assert F(0) <= w <= 1 and F(0) < q < 1
    # z=e^{-u}; upstream interval z in [q,1].
    upstream = w * (F(1,4) if q <= F(1,2) else q*(1-q))
    # Downstream quadratic A*z-B*z*z, z in [0,q].
    a = w + (1-w)/q
    b = w + (1-w)/(q*q)
    zv = a/(2*b)
    downstream = a*a/(4*b) if zv <= q else a*q - b*q*q
    return max(upstream,downstream)

def analytic(q):
    if q <= F(1,3):
        return 1/(2*(1-q)),1/(8*(1-q))
    return 1/(1+q),q/(1+q)**2

checks=0
for q in [F(1,100),F(1,8),F(1,4),F(1,3),F(2,5),F(1,2),F(3,4),F(99,100)]:
    w, f=analytic(q)
    assert F(0)<w<1; checks+=1
    assert peak_fraction(w,q)==f; checks+=1
    for j in range(0,401):
        v=F(j,400)
        assert peak_fraction(v,q)>=f;checks+=1
        if v!=w:
            assert peak_fraction(v,q)>f;checks+=1
# exact particularly informative: q=1/4 optimum 2/3 and 1/6
assert analytic(F(1,4))==(F(2,3),F(1,6));checks+=1
assert analytic(F(1,3))==(F(3,4),F(3,16));checks+=1
assert analytic(F(1,2))==(F(2,3),F(2,9));checks+=1
rng=Random(20261120)
for _ in range(3000):
    q=F(rng.randint(1,999),1000)
    w,v=analytic(q)
    assert peak_fraction(w,q)==v;checks+=1
    t=F(rng.randint(0,1000),1000)
    assert peak_fraction(t,q)>=v;checks+=1
    if w!=t:
        assert peak_fraction(t,q)>v;checks+=1
# Monotone rise and fall of upstream fraction as q decreases through 1/3.
for q1,q2 in zip([F(i,1000) for i in range(1,999)], [F(i,1000) for i in range(2,1000)]):
    w1,_=analytic(q1);w2,_=analytic(q2)
    if q2<=F(1,3): assert w1<w2
    elif q1>=F(1,3): assert w1>w2
    checks+=1
print('PASS:',checks,'exact-rational assertions')

#!/usr/bin/env python3
"""Exact checks for alternating-competence majority accuracy.

Uses only Python standard library; all test equalities use rational arithmetic.
The all-size statement is proved analytically in RESULT.md, not by these tests.
"""
from fractions import Fraction as F
from math import comb

assertions = 0

def check(statement):
    global assertions
    assert statement
    assertions += 1

def majority(m, p, q):
    result = F(0)
    for k in range(m + 2):
        pk = F(comb(m + 1, k)) * p**k * (1 - p)**(m + 1 - k)
        for j in range(m + 1):
            if k + j > m:
                result += pk * F(comb(m, j)) * q**j * (1 - q)**(m - j)
    return result

def pair_walk(m, p, q):
    a, b = p * q, (1 - p) * (1 - q)
    c = 1 - a - b
    d = {0: F(1)}
    for _ in range(m):
        nxt = {}
        for k, v in d.items():
            for j, w in ((1, a), (0, c), (-1, b)):
                nxt[k+j] = nxt.get(k+j,F(0)) + v*w
        d=nxt
    return d

# The witness is a strict committee-size reversal.
p, q = F(9,10), F(2,5)
check(majority(0,p,q) == F(9,10))
check(majority(1,p,q) == F(441,500))
check(majority(2,p,q) == F(22221,25000))
check(majority(0,p,q) > majority(1,p,q))
check(majority(2,p,q) > majority(1,p,q))
check(p+q>1)

# Independent binomial and trinomial representations of increments.
for pn in range(6,10):
    for qn in range(1,5):
        pp,qq=F(pn,10),F(qn,10)
        a,b=pp*qq,(1-pp)*(1-qq)
        c=1-a-b
        last_ratio=None
        for m in range(9):
            d=pair_walk(m,pp,qq)
            check(sum(d.values())==1)
            t,v=d[0],d.get(1,F(0))
            check(d.get(-1,F(0))*a == d.get(1,F(0))*b)
            difference=majority(m+1,pp,qq)-majority(m,pp,qq)
            check(difference==pp*(1-pp)*(2*qq-1)*t+b*(2*pp-1)*v)
            if last_ratio is not None:
                check(v/t>last_ratio)
            last_ratio=v/t
            if pp+qq<=1:
                check(difference<0)

# A second enumeration via independent Bernoulli convolution.
for pn,qn in ((9,4),(8,3),(7,4),(6,4),(9,1),(8,4)):
    pp,qq=F(pn,10),F(qn,10)
    for m in range(14):
        mass=[F(1)]
        for x in [pp]*(m+1)+[qq]*m:
            nxt=[F(0)]*(len(mass)+1)
            for j,v in enumerate(mass):
                nxt[j]+=v*(1-x)
                nxt[j+1]+=v*x
            mass=nxt
        check(sum(mass)==1)
        check(sum(mass[m+1:])==majority(m,pp,qq))

# No reversal at or below mean pair competence 1/2;
# at a supercritical pair competence, first step is strictly harmful.
for pn in range(6,10):
    for qn in range(1,5):
        pp,qq=F(pn,10),F(qn,10)
        check(majority(1,pp,qq)<majority(0,pp,qq))
# For barely supercritical pairs the eventual recovery may occur after
# more than twenty pairs. The all-size existence statement is analytic.

print('PASS: %d exact rational assertions' % assertions)

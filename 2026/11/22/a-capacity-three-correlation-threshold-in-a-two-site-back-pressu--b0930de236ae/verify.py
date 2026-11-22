#!/usr/bin/env python3
"""Exact certificate for a two-site capacitated back-pressure exclusion process.
Uses integer polynomial arithmetic; no numerical solvers or external packages.
"""
from collections import deque
from fractions import Fraction


def trim(p):
    p = list(p)
    while len(p) > 1 and p[-1] == 0:
        p.pop()
    return tuple(p)

def add(a, b):
    return trim([ (a[i] if i < len(a) else 0) +
                  (b[i] if i < len(b) else 0)
                  for i in range(max(len(a),len(b))) ])

def neg(a):
    return tuple(-x for x in a)

def sub(a,b):
    return add(a,neg(b))

def mul(a,b):
    p = [0]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):
            p[i+j] += x*y
    return trim(p)

def scale(a,k):
    return trim([k*x for x in a])

def val(a,t):
    return sum((x*t**i for i,x in enumerate(a)), Fraction(0))

ZERO=(0,); ONE=(1,); T=(0,1)
P = lambda *x: trim(x)

WEIGHTS={
 1:{(0,0):ONE,(0,1):ONE,(1,0):scale(T,2),(1,1):ONE},
 2:{(0,0):ONE,(0,1):ONE,(1,0):scale(T,2),
    (1,1):P(1,2),(1,2):ONE,(2,0):P(0,0,4),
    (2,1):scale(T,2),(2,2):ONE},
 3:{(0,0):P(1,3),(0,1):P(1,3),
    (1,0):mul(P(0,2),P(1,3)),
    (1,1):mul(P(1,2),P(1,3)),
    (1,2):P(1,3,4),
    (2,0):mul(P(0,0,4),P(1,2)),
    (2,1):mul(P(0,2),P(1,3,4)),
    (2,2):mul(P(1,2),P(1,3)),
    (2,3):P(1,3),
    (3,0):mul(P(0,0,0,8),P(1,2)),
    (3,1):mul(P(0,0,4),P(1,2)),
    (3,2):mul(P(0,2),P(1,3)),
    (3,3):P(1,3)}
}
Z_EXPECTED={1:P(3,2),2:P(5,6,4),3:P(7,31,42,32,16)}
CNUM_EXPECTED={1:P(1,-2),2:P(11,8,-16,-8),
               3:P(46,354,934,878,-228,-1104,-736,-128)}
# C numerator = Z*M12 - M1*M2, ordered low to high.
P2=P(-11,-8,16,8)
P3=P(-23,-177,-467,-439,114,552,368,64)


def transitions(state,c):
    x,y=state
    if x<c:
        yield (x+1,y), T
    if y>0:
        yield (x,y-1), T
    if x>y:
        yield (x-1,y+1), ONE


def reachable(c):
    todo=deque([(0,0)])
    seen={(0,0)}
    while todo:
        a=todo.popleft()
        for b,_ in transitions(a,c):
            if b not in seen:
                seen.add(b);todo.append(b)
    return seen


def moment(w,func):
    res=ZERO
    for (x,y),poly in w.items():
        res=add(res,scale(poly,func(x,y)))
    return res

for c,w in WEIGHTS.items():
    states=reachable(c)
    assert states==set(w), (c,states^set(w))
    # Every state in the support communicates with the empty state:
    for s in states:
        todo=deque([s]);seen={s}
        while todo:
            a=todo.popleft()
            for b,_ in transitions(a,c):
                if b not in seen:
                    seen.add(b);todo.append(b)
        assert (0,0) in seen
    balance={s:ZERO for s in states}
    for s,weight in w.items():
        for dest,rate in transitions(s,c):
            flow=mul(weight,rate)
            balance[s]=sub(balance[s],flow)
            balance[dest]=add(balance[dest],flow)
    assert all(p==ZERO for p in balance.values()),(c,balance)
    Z=moment(w,lambda x,y:1)
    assert Z==Z_EXPECTED[c],(c,Z)
    m1=moment(w,lambda x,y:x)
    m2=moment(w,lambda x,y:y)
    m12=moment(w,lambda x,y:x*y)
    numerator=sub(mul(Z,m12),mul(m1,m2))
    assert numerator==CNUM_EXPECTED[c],(c,numerator)
    cov=Fraction(val(numerator,Fraction(1)),val(Z,Fraction(1))**2)
    expected={1:Fraction(-1,25),2:Fraction(-1,45),3:Fraction(1,1024)}[c]
    assert cov==expected,(c,cov)
    print('capacity',c,'states',len(states),'Z',Z,'covariance_at_unit_rates',cov)

assert P2==neg(CNUM_EXPECTED[2])
assert scale(P3,-2)==CNUM_EXPECTED[3]

def positive_sign_changes(p):
    coeffs=[x for x in reversed(p) if x!=0]
    return sum((a>0)!=(b>0) for a,b in zip(coeffs,coeffs[1:]))

# Descartes' rule: each polynomial has exactly one positive root,
# since it has one sign variation and changes from negative to positive at infinity.
assert positive_sign_changes(P2)==positive_sign_changes(P3)==1
assert val(P2,Fraction(0))<0<val(P2,Fraction(1))
assert val(P3,Fraction(0))<val(P3,Fraction(1))<0
print('exact polynomial and unique-positive-root sign checks: PASS')

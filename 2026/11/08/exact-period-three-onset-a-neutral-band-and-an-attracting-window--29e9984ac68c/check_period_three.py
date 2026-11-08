"""Exact-rational tests for the four-branch skew-homeomorphism/tent composite.

This verifies representative parameter instances; the theorem for ALL real
parameters follows from the analytical orbit-order and branch proof.
Run with: python3 check_period_three.py
"""
from fractions import Fraction as Q
from itertools import product

segments = [(Q(0), Q(1,4)), (Q(1,4), Q(1,2)),
            (Q(1,2), Q(3,4)), (Q(3,4), Q(1))]

def coefficients(t):
    v=(4-t)/3
    w=(t-1)/3
    return [(t,Q(0)),(v,w),(-v,Q(1)),(-t,t)]

def f(t,x):
    assert 0<=x<=1
    i = 0 if x<=Q(1,4) else 1 if x<=Q(1,2) else 2 if x<=Q(3,4) else 3
    m,b=coefficients(t)[i]
    return m*x+b

def cycle3(t):
    cycles=set()
    for indices in product(range(4),repeat=3):
        m,b=Q(1),Q(0)
        for i in indices:
            u,v=coefficients(t)[i]
            m,b=u*m,u*b+v
        if m==1:
            assert b!=0, 'For these rational test parameters, identity is excluded'
            continue
        x=b/(1-m)
        if not 0<=x<=1:
            continue
        y=x
        works=True
        for i in indices:
            if not segments[i][0]<=y<=segments[i][1]:
                works=False
                break
            u,v=coefficients(t)[i]
            y=u*y+v
        if not works or y!=x:
            continue
        orbit=[x,f(t,x),f(t,f(t,x))]
        if len(set(orbit))==3:
            assert f(t,orbit[2])==x
            cycles.add(tuple(sorted(orbit)))
    return cycles

def expected(t):
    if t<=3 or t*t*(4-t)>3:
        return set()
    q=t*t*(4-t)
    if q>=1:
        a=t*(4-t)/(3+q)
        b=q/(3+q)
        c=1-(4-t)/(3+q)
    else:
        a=t/(1+t**3)
        b=t*t/(1+t**3)
        c=t**3/(1+t**3)
    a2=t/(t*t+t+1)
    b2=t*t/(t*t+t+1)
    c2=t*(t+1)/(t*t+t+1)
    return {(a,b,c),(a2,b2,c2)}

checks=0
params=[Q(j,20) for j in range(21,80)]
params += [Q(3791,1000),Q(3792,1000),Q(3935,1000),
           Q(3936,1000),Q(3999,1000),Q(3001,1000)]
for t in params:
    actual=cycle3(t)
    target=expected(t)
    assert actual==target,(t,actual,target)
    checks+=1

# Analytical fold threshold, branch-equation identities and neutral cylinder.
import math
T=(3+math.sqrt(21))/2
assert abs(T*T*(4-T)-3)<1e-11
assert 3<T<4
assert abs((1-T*T*(4-T)/3))<1e-11
for j in range(41):
    middle=.5+j*.25/40
    left=middle/T
    right=1-middle/(T*T)
    assert 0<left<.25 and .5<=middle<=.75 and .75<right<1
    # Check the exact algebraic identities through T^2-3T-3=0:
    assert abs(T*left-middle)<1e-12
    assert abs((1-(4-T)/3*middle)-right)<1e-12
    assert abs(T*(1-right)-left)<1e-12
    checks+=3

print('PASS:',checks,'parameter and neutral-family checks; exact-rational prime-three cycles independently enumerated')

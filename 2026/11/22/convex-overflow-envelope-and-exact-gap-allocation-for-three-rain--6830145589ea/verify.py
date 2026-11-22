#!/usr/bin/env python3
"""Exact rational stress checks for a three-pulse capped loss store.
The theorem is proved separately; these bounded checks are not an infinite proof.
"""
from fractions import Fraction as Q
from itertools import product
from math import sqrt

checks = 0

def check(b):
    global checks
    assert b
    checks += 1

def positive(v):
    return max(Q(0), v)

def store_recurrence(C, a, b, c, E, x):
    # x = exp(-k t), E/x = exp(-k(T-t)); no floating point.
    s1 = min(C, a)
    r1 = positive(a-C)
    r2 = positive(x*s1+b-C)
    s2 = min(C, x*s1+b)
    r3 = positive((E/x)*s2+c-C)
    return r1+r2+r3

def convex_envelope(C, a, b, c, E, x):
    u=min(C,a)
    return positive(a-C)+max(Q(0),u*x+b-C,E*u+E*b/x+c-C,u*x+b+E*C/x+c-2*C)

def expression(C, a, b, c, E, x):
    u=min(C,a)
    return positive(a-C)+positive(u*x+b-C)+positive((E/x)*min(C,u*x+b)+c-C)

def candidates(C,a,b,c,E):
    u=min(C,a)
    ans=[float(E),1.]
    thresholds=[(C-b)/u]
    if c<C: thresholds.append(E*C/(C-c))
    if C-c-E*u>0: thresholds.append(E*b/(C-c-E*u))
    for th in thresholds:
        if E<=th<=1: ans.append(float(th))
    ans.append(sqrt(float(E*C/u)))
    return [z for z in ans if float(E)<=z<=1.]

def float_eval(C,a,b,c,E,x):
    C,a,b,c,E=map(float,(C,a,b,c,E))
    u=min(C,a)
    return max(0,a-C)+max(0,u*x+b-C)+max(0,E/x*min(C,u*x+b)+c-C)

values=[Q(1,4),Q(1,2),Q(3,4),Q(1),Q(3,2),Q(2)]
retentions=[Q(1,4),Q(1,2),Q(3,4)]
for a,b,c in product(values,repeat=3):
 for E in retentions:
    C=Q(1)
    X=[E+(Q(1)-E)*Q(i,8) for i in range(9)]
    Y=[store_recurrence(C,a,b,c,E,x) for x in X]
    for x,y in zip(X,Y):
        check(y==expression(C,a,b,c,E,x))
        check(y==convex_envelope(C,a,b,c,E,x))
    for i in range(8):
        xm=(X[i]+X[i+1])/2
        check(2*expression(C,a,b,c,E,xm)<=Y[i]+Y[i+1])
    # All zero-runoff-after-first points satisfy exactly the analytical interval.
    u=min(C,a)
    for x,y in zip(X,Y):
        zero=(y==positive(a-C))
        interval=(b<C and C-c-E*u>0 and x<=(C-b)/u and x>=E*b/(C-c-E*u))
        check(zero==interval)
    cand=candidates(C,a,b,c,E)
    best=min(float_eval(C,a,b,c,E,z) for z in cand)
    # Golden-grid is independent test: no point beats theoretical candidate.
    for i in range(101):
        z=float(E)+(1.-float(E))*i/100
        check(float_eval(C,a,b,c,E,z)>=best-1e-11)

# A nondegenerate interval of zero future spill when a first pulse is retained.
# C=1, a=1/2, b=1/4, c=1/8, E=1/4:
# x between 1/12 and 3/2, intersect [1/4,1] -> entire feasible interval.
for x in (Q(1,4),Q(1,2),Q(3,4),Q(1)):
    check(store_recurrence(Q(1),Q(1,2),Q(1,4),Q(1,8),Q(1,4),x)==0)

# Exact both-saturation example: first pulse 1, second and third 9/10, E=1/4.
C=Q(1);a=Q(1);b=c=Q(9,10);E=Q(1,4)
check(store_recurrence(C,a,b,c,E,Q(1,2))==Q(4,5))
check(store_recurrence(C,a,b,c,E,Q(1))==Q(21,20))
check(store_recurrence(C,a,b,c,E,E)==Q(21,20))
# Equal-gap loss can be arbitrarily large relative to backloaded drying.
# u=1/2, b=1/4, c=1-E/2, E=1/(n*n); x_equal=1/n.
for n in (2,3,5,10,20,100,1000):
 E=Q(1,n*n); a=Q(1,2); b=Q(1,4);c=C-E/2
 f_opt=store_recurrence(C,a,b,c,E,Q(1))
 f_equal=store_recurrence(C,a,b,c,E,Q(1,n))
 check(f_opt==E*b)
 check(f_equal==Q(1,n)*b)
 check(f_equal/f_opt==n)
print('PASS',checks,'exact or controlled-tolerance assertions')

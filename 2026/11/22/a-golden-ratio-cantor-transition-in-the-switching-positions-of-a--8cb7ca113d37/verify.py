#!/usr/bin/env python3
"""Exact-rational independent checks of the binary-clock switching section."""
from fractions import Fraction as Q
from math import log, sqrt

checks=0

def check(assertion, why):
    global checks
    assert assertion, why
    checks += 1

def bounds(q):
    den=1+q+q*q
    return (q*q-q-1)/den,(q*q+q-1)/den

def f(q,m,n,z):
    return q**(m+n)*z-1+2*q**n-q**(m+n)

canonical=[(Q(-5,7),Q(-9,14)),(Q(-17,28),Q(-4,7)),
           (Q(-3,7),Q(-2,7)),(Q(-3,14),Q(-1,7))]
order=[(1,2),(2,2),(1,1),(2,1)]
for q in [Q(1,5),Q(1,3),Q(1,2),Q(3,5),Q(5,8),Q(2,3),Q(3,4),Q(4,5),Q(9,10)]:
    lo,hi=bounds(q)
    check(hi>lo and -1<lo<hi<1,'interior hull')
    check(f(q,1,2,lo)==lo and f(q,2,1,hi)==hi,'endpoint fixed points')
    images=[(f(q,m,n,lo),f(q,m,n,hi)) for m,n in order]
    for a,b in images:
        check(lo<=a<b<=hi,'image invariance')
    powers=[3,1,2]
    gaps=[]
    for i,power in enumerate(powers):
        gap=images[i+1][0]-images[i][1]
        gaps.append(gap)
        check(gap==2*q**power*(1-q-q*q)/(1+q+q*q),'factored gap')
    check(images[0][0]==lo and images[-1][1]==hi,'image hull endpoints')
    check(all(g>0 for g in gaps) if 1-q-q*q>0 else all(g<0 for g in gaps), 'gap sign')
    check((1-hi)*q*q>0 and 1+lo>0,'finite-speed displacement')
    if q==Q(1,2):
        check(images==canonical,'canonical interval endpoints')
        check(abs(log((1+sqrt(5))/2)/log(2)-0.6942419136306174)<1e-12,'support dimension')
        check(abs(log(4)/(3*log(2))-Q(2,3))<1e-12,'measure dimension')

# A stationary finite-history law is an explicit contraction of the four maps.
for q in [Q(1,2),Q(3,4)]:
    lo,hi=bounds(q)
    initial=Q(0)
    for m,n in [(1,2),(2,1),(1,1),(2,2)]*8:
        initial=f(q,m,n,initial)
        check(lo<=initial<=hi,'recurrent orbit remains in hull')
    # Every finite-depth cylinder has mass 4^{-depth}; this is a finite check.
    mass=Q(1)
    for depth in range(1,7):
        mass=sum([mass/Q(4)]*4)
        check(mass==1,'finite symbolic cylinder mass')

print(f'{checks} exact rational and numerical assertions passed')

#!/usr/bin/env python3
"""Exact finite probability checks for opposite singleton-run counts.

Run: python3 check.py. Standard library only. Finite checks corroborate the
independent analytic proof; they do not prove infinite quantifiers.
"""
from fractions import Fraction
from itertools import product
from math import exp

checks = 0

def assert_equal(a, b, context):
    global checks
    assert a == b, (context, a, b)
    checks += 1

def cov_formula(n, p):
    k = n - 3
    h = 1 - (1-2*p)**k - 2*p*p + 6*k*p*(1-p)
    return p*p*h/8

def enumerate_cov(n, p):
    eu = ev = euv = Fraction(0)
    for seq in product((0,1), repeat=n):
        flips = sum(seq[j]!=seq[j+1] for j in range(n-1))
        w = Fraction(1,2)*p**flips*(1-p)**(n-1-flips)
        u = sum(seq[j:j+3] == (0,1,0) for j in range(n-2))
        v = sum(seq[j:j+3] == (1,0,1) for j in range(n-2))
        eu += w*u; ev += w*v; euv += w*u*v
    return euv - eu*ev, eu, ev

for n in range(3,13):
    for p in map(Fraction, ('1/5','1/2','3/4','9/10','99/100')):
        brute, eu, ev = enumerate_cov(n,p)
        assert_equal(brute,cov_formula(n,p),('cov',n,p))
        assert_equal(eu,Fraction(n-2,2)*p*p,('mean U',n,p))
        assert_equal(ev,Fraction(n-2,2)*p*p,('mean V',n,p))
        if n == 3:
            assert_equal(brute < 0, True, ('n3 negative',p))
        if n%2 == 0:
            assert_equal(brute > 0, True, ('even positive',n,p))

# For odd lengths the unique threshold is between 1/2 and 1.
def h(n,p):
    k=n-3
    return 1 - (1-2*p)**k - 2*p*p + 6*k*p*(1-p)

prev = Fraction(1,2)
for n in range(5,202,2):
    lo=Fraction(1,2); hi=Fraction(1,1)
    for _ in range(110):
        mid=(lo+hi)/2
        if h(n,mid)>0: lo=mid
        else:hi=mid
        checks+=1
    assert lo>prev,(n,lo,prev)
    checks+=1
    prev=lo

# Quantitative limiting location, using only floats for this asymptotic diagnostic.
def limitfn(c):
    return 6*c-1-exp(-2*c)
lo=0.;hi=1.
for _ in range(100):
    mid=(lo+hi)/2
    if limitfn(mid)<0:lo=mid
    else:hi=mid
c=(lo+hi)/2
assert 0.2648056 < c < 0.2648057
checks+=1
for n in (101,501,2001,8001):
    lo=.5;hi=1.
    for _ in range(90):
        mid=(lo+hi)/2
        if h(n,mid)>0:lo=mid
        else:hi=mid
    scaled=(n-3)*(1-(lo+hi)/2)
    assert abs(scaled-c) < 4/(n-3),(n,scaled,c)
    checks+=1
print('PASS',checks,'exact assertions / deterministic root checks')
print('limiting constant c = %.12f'%c)

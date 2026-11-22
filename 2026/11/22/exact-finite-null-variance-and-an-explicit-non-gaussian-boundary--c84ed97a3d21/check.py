#!/usr/bin/env python3
"""Independent checks for a cyclic rank-sum null law.

Standard library only. Finite enumerations and numerical experiments support,
but do not replace, the analytic proof in RESULT.md.
"""
from bisect import bisect_left
from fractions import Fraction
from itertools import permutations, product
from math import tan, pi, sinh, cosh, isclose
from random import Random

CHECKS = 0

def check(condition, description):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(description)

def rank_sum(a, order):
    n = len(a)
    original = [(a[i], order[i]) for i in range(n)]
    permuted = [(a[j], order[(j+1)%n]) for j in range(n)]
    wins = sum(t < v for t in original for v in permuted)
    return Fraction(wins,n*n)

def fast_rank_sum(a, order):
    n = len(a)
    d = 0
    for bit in (0,1):
        ix = [i for i in range(n) if a[i]==bit]
        ranks = sorted(order[i] for i in ix)
        d += sum(bisect_left(ranks,order[(j+1)%n]) for j in ix)
        d -= len(ix)*(len(ix)-1)//2
    return Fraction(n-1,2*n)+Fraction(d,n*n)

def quadratic_identity(a, order):
    n = len(a)
    b = [1-2*t for t in a]
    t = sum(order[(i+1)%n]>order[i] for i in range(n))
    csum = sum(b[i]*b[k]*(
        int(order[i]<order[(k+1)%n])+
        int(order[k]<order[(i+1)%n])-1)
        for i in range(n) for k in range(i+1,n))
    d = Fraction(t+csum,2)
    return Fraction(n-1,2*n)+d/Fraction(n*n)

for n in range(3,7):
    total = 0
    s1 = Fraction(0)
    s2 = Fraction(0)
    for a in product((0,1),repeat=n):
        for order in permutations(range(n)):
            r = rank_sum(a,order)
            check(r==fast_rank_sum(a,order),f'fast rank formula n={n}')
            check(r==quadratic_identity(a,order),f'quadratic decomposition n={n}')
            z = n*(r-Fraction(1,2))
            s1 += z
            s2 += z*z
            total += 1
    mean = s1/total
    var = s2/total-mean*mean
    check(mean==Fraction(-1,4),f'exact mean n={n}')
    check(var==Fraction(3*n-2,48*n),f'exact variance n={n}')
    print('n=',n,'exhaustive cases=',total,'mean=',mean,'variance=',var)

# The positive frequency multiset is 2*pi*k, k>=1, and roots of tan(w/2)=w.
# Confirm the analytic product expansion with independently computed partial sums.
roots=[]
for k in range(25000):
    lo=2*k*pi+1e-8
    hi=(2*k+1)*pi-1e-8
    for _ in range(65):
        md=(lo+hi)/2
        if tan(md/2)>md:
            hi=md
        else:
            lo=md
    roots.append((lo+hi)/2)

s2=sum(1/w**2 for w in roots) + Fraction(1,24)
s4=sum(1/w**4 for w in roots) + Fraction(1,1440)
check(abs(s2-Fraction(1,4))<3e-5,'reciprocal-square spectral trace')
check(abs(s4-Fraction(5,144))<5e-8,'reciprocal-fourth spectral trace')
check(abs(roots[0]-2.331122370414423)<1e-12,'first transcendental spectral frequency')

def spectral_product(t):
    x=t/4
    h = sinh(x)/x if x else 1.
    return h*(2*cosh(x)-h)

for t in (0.25,.5,1,2,4,8):
    p=1.
    for w in roots:
        p *= (1+t*t/(4*w*w))
    p *= sinh(t/4)/(t/4)
    check(abs(p-spectral_product(t))<2.2e-4,'spectral product at t='+str(t))

# Independent simulation sanity check: not an infinite-distribution certificate.
rng=Random(719316)
for n in (200,500):
    v=[]
    for j in range(4000):
        a=[rng.randrange(2) for _ in range(n)]
        order=list(range(n)); rng.shuffle(order)
        v.append(float(n*(fast_rank_sum(a,order)-Fraction(1,2))))
    m=sum(v)/len(v); var=sum((t-m)**2 for t in v)/len(v)
    check(abs(m+0.25)<.025,'simulated mean')
    check(abs(var-1/16)<.012,'simulated variance')
    print('simulation',n,'mean',m,'variance',var)

print('PASS',CHECKS,'assertions')

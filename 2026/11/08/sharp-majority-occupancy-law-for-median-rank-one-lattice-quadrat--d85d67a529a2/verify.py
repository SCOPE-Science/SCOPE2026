#!/usr/bin/env python3
"""Independent finite checks of a majority-occupancy law for Fourier lattice quadrature.
No third-party packages required. Finite checks supplement an analytic theorem.
"""
from itertools import product, combinations
from collections import Counter
from fractions import Fraction
from math import comb, cos, pi, sqrt

checks = 0

def check(condition, context):
    global checks
    checks += 1
    if not condition:
        raise AssertionError(context)

def occupancy_q(slopes, s):
    counts = sorted((slopes.count(j) for j in range(s)), reverse=True)
    threshold = (len(slopes)+1)//2
    total = 0
    for q, v in enumerate(counts, 1):
        total += v
        if total >= threshold:
            return q
    raise AssertionError("missing majority")

def independent_q(slopes, s):
    threshold = (len(slopes)+1)//2
    for q in range(1, s+1):
        for chosen in combinations(range(s), q):
            if sum(a in chosen for a in slopes) >= threshold:
                return q
    raise AssertionError("missing covering set")

# Actual p-point lattice evaluations versus the predicted character alias.
for p in (3, 5, 7, 11):
    for z1 in range(1,p):
        for z2 in range(1,p):
            slope = (z2 * pow(z1, -1, p)) % p
            for j in range(1,p):
                value = sum(cos(2*pi*t*(z2-j*z1)/p) for t in range(p))/p
                check(abs(value-(1 if j == slope else 0)) < 1e-12,
                      ("character",p,z1,z2,j,value))

# Explicitly enumerate all short draw sequences and independently enumerate
# every support of Fourier coefficients to optimize their binary positive median.
for p,r in ((3,1),(3,3),(3,5),(5,1),(5,3),(5,5),(7,3),(7,5)):
    s=p-1
    histogram=Counter()
    for slopes in product(range(s), repeat=r):
        q=occupancy_q(slopes,s)
        q2=independent_q(slopes,s)
        check(q==q2,("majority support",p,r,slopes,q,q2))
        check(1<=q<=min((r+1)//2,s//2), ("deterministic floor",p,r,slopes,q))
        histogram[q]+=1
    check(sum(histogram.values())==s**r,("normalization",p,r))
    if p==5 and r==3:
        check(Fraction(histogram[1],s**r)==Fraction(5,8),("p5r3",histogram))
    if p==7 and r==5:
        check(Fraction(histogram[1],s**r)==Fraction(23,108),("p7r5",histogram))
        check(Fraction(histogram[3],s**r)==Fraction(5,54),("p7r5",histogram))
    # Unique majority category probability is a disjoint binomial tail.
    probability=Fraction(s*sum(comb(r,k)*(s-1)**(r-k) for k in range((r+1)//2,r+1)),s**r)
    check(Fraction(histogram[1],s**r)==probability,("one-bin tail",p,r,histogram))

# A fixed half-frequency integrand has exactly half its generators aliasing.
for s in (2,4,6,8,10):
    d=s//2
    for r in (1,3,5,9,11):
        good=sum(comb(r,k) for k in range((r+1)//2,r+1))
        check(Fraction(good,2**r)==Fraction(1,2),("fixed integrand",s,r))

print(f"PASS: {checks} independent finite assertions")

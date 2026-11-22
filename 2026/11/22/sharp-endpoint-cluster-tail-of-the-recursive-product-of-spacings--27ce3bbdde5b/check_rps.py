#!/usr/bin/env python3
"""Standalone exact checks for the far-left null tail of recursive spacing statistics.
Not a substitute for the analytic proof of the all-n tail limit.
"""
from fractions import Fraction
from math import comb, factorial, log, exp, gamma
from itertools import combinations
from random import Random

rng=Random(84219)
checks=0

def direct_rps_product(s):
    # Returns exp(-R), exactly, using the published normalization algorithm.
    arr=list(s); p=Fraction(1,1)
    while len(arr)>1:
        for z in arr: p*=z
        arr=[arr[i]+arr[i+1] for i in range(len(arr)-1)]
        tot=sum(arr)
        arr=[a/tot for a in arr]
    return p

def binomial_product(s):
    # Closed convolution representation derived in RESULT.md.
    m=len(s); p=Fraction(1,1)
    for j in range(m-1):
        a=[sum(comb(j,k)*s[i+k] for k in range(j+1)) for i in range(m-j)]
        z=sum(a)
        for x in a: p*=x/z
    return p

for m in range(2,9):
    for rep in range(43):
        vals=[rng.randint(1,100) for _ in range(m)]
        s=[Fraction(x,sum(vals)) for x in vals]
        assert direct_rps_product(s)==binomial_product(s)
        checks+=1

for m in range(2,13):
    positions=range(m)
    for j in range(1,m):
        for subset in combinations(positions,j):
            chosen=set(subset)
            count=sum(all(i+k in chosen for k in range(r))
                      for r in range(1,m) for i in range(m-r+1))
            assert count <= j*(j+1)//2
            if j==m-1 and count == j*(j+1)//2:
                assert subset in [tuple(range(m-1)),tuple(range(1,m))]
            checks+=1

# n=2: exact product formula and beta integral constant
for _ in range(100):
    a,b,c=[Fraction(x,1) for x in [rng.randrange(1,101) for _ in range(3)]]
    z=a+b+c; a/=z;b/=z;c/=z
    assert direct_rps_product([a,b,c]) == a*b*c*(a+b)*(b+c)/(1+b)**2
    checks+=1
const=2*gamma(Fraction(1,3))**2/gamma(Fraction(2,3))
assert abs(const-10.5998325017127)<1e-11
checks+=1
print('Exact checks passed:',checks)
print('C2 =',format(const,'.14f'))
print('n=2 rate = 2/3')

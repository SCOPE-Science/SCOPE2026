#!/usr/bin/env python3
"""Reproduce finite and algebraic checks for two binomial-parity transforms.
No third-party dependencies are used. The infinite statements require the proof.
"""
from fractions import Fraction as Q
from math import isqrt

def fibs(k):
    a, b = 0, 1
    out = [a]
    for i in range(k):
        out.append(b)
        a, b = b, a + b
    return out

F = fibs(55)

def transform(n, shift):
    answer, run = 1, 0
    while n:
        if n & 1:
            run += 1
        elif run:
            answer *= F[run + shift]
            run = 0
        n >>= 1
    if run:
        answer *= F[run + shift]
    return answer

def odd_binom(n, k):
    return 0 <= k <= n and (k & (n-k)) == 0

def original_binomial_pair(n):
    first = sum(odd_binom(n-k, 2*k) and odd_binom(n, k)
                for k in range(n+1))
    second = sum(odd_binom(3*k, k) and odd_binom(n, k)
                 for k in range(n+1))
    return first, second

for n in range(1200):
    assert original_binomial_pair(n) == (transform(n, 1), transform(n, 2))
print('1200 independent binomial-parity comparisons: PASS')

# A rational series with numerator P and denominator 1+d1*z+...
# satisfies a triangular recurrence for its exact coefficients.
def coefficients(numer, denom, length):
    ret = []
    for n in range(length):
        t = numer[n] if n < len(numer) else 0
        for j in range(1, min(n, len(denom)-1)+1):
            t -= denom[j] * ret[n-j]
        ret.append(t)
    return ret

forms = [
    ([1], [1,-2,-1]),
    ([1,1], [1,-2,-2]),
    ([1,-1], [1,-3,-1,1]),
    ([1,2,-1], [1,-3,-4,2]),
    ([1], [1,-3,-2,1]),
]
expected = [coefficients(p,d,17) for p,d in forms]
for L in range(15):
    values = [(transform(n,1),transform(n,2)) for n in range(1<<L)]
    actual = [sum(u for u,v in values),sum(v for u,v in values),
              sum(u*u for u,v in values),sum(v*v for u,v in values),
              sum(u*v for u,v in values)]
    assert actual == [x[L] for x in expected], (L,actual)
print('15 full dyadic-block moment comparisons: PASS')

# Exact rational roots isolations, using integer arithmetic only.
def cubefun(c2,c1,c0,x):
    return x**3 + c2*x*x + c1*x + c0
intervals = [
    (-3,-1,1,Q(32143,10000),Q(32144,10000)),
    (-3,-4,2,Q(38951,10000),Q(38952,10000)),
    (-3,-2,1,Q(34908,10000),Q(34909,10000)),
]
for c2,c1,c0,lo,hi in intervals:
    assert cubefun(c2,c1,c0,lo) < 0 < cubefun(c2,c1,c0,hi)
# Each cubic has three distinct real roots: two further sign-changing intervals
# exhaust its degree and certify dominance of the positive large root.
secondary = [
    ((-68,100),(-67,100),(46,100),(47,100)),
    ((-130,100),(-129,100),(39,100),(40,100)),
    ((-84,100),(-83,100),(34,100),(35,100)),
]
for (c2,c1,c0,lo,hi),(al,ad,bl,bd) in zip(intervals,secondary):
    x1,x2,y1,y2 = Q(al[0],al[1]),Q(ad[0],ad[1]),Q(bl[0],bl[1]),Q(bd[0],bd[1])
    assert cubefun(c2,c1,c0,x1)*cubefun(c2,c1,c0,x2) < 0
    assert cubefun(c2,c1,c0,y1)*cubefun(c2,c1,c0,y2) < 0
    assert max(abs(x1),abs(x2),abs(y1),abs(y2)) < lo
# Strictly less than one for the limiting correlation base.
assert Q(34909,10000)**2 < Q(32143,10000)*Q(38951,10000)
# The cross moment dominates the product of the means: rational-safe bounds.
assert Q(34908,10000) > Q(33,10) > (1+2**.5)*(1+3**.5)/2
print('Three exact algebraic intervals and strict spectral separation: PASS')
print('All checks passed. Finite enumeration is not an infinite proof.')

#!/usr/bin/env python3
"""Finite exact checks for synchronous mutual-proposal matching on complete graphs.

This verifies finite formulas only. It does not certify the asymptotic martingale CLT.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import factorial

CHECKS = 0

def check(condition, why):
    global CHECKS
    CHECKS += 1
    if not condition:
        raise AssertionError(why)

def falling(x, j):
    ans = 1
    for i in range(j):
        ans *= x-i
    return ans

def factorial_moment(m, r):
    if 2*r > m:
        return Fraction(0)
    return Fraction(falling(m, 2*r), 2**r * (m-1)**(2*r))

def theoretical_probabilities(m):
    max_pairs = m//2
    pmf = []
    for k in range(max_pairs+1):
        p = sum((Fraction((-1)**(r-k), factorial(k)*factorial(r-k)) * factorial_moment(m, r)
                 for r in range(k, max_pairs+1)), Fraction(0))
        pmf.append(p)
    return pmf

def direct_probabilities(m):
    counts = Counter()
    neighbours = [[j for j in range(m) if j != i] for i in range(m)]
    for choices in product(*neighbours):
        pairs = sum(choices[i] == j and choices[j] == i
                    for i in range(m) for j in range(i+1,m))
        counts[pairs] += 1
    denom = (m-1)**m
    return [Fraction(counts[k], denom) for k in range(m//2+1)]

# Completely independent enumeration of all possible no-self-loop proposals.
for m in range(2, 8):
    actual = direct_probabilities(m)
    predicted = theoretical_probabilities(m)
    check(len(actual) == len(predicted), f'PMF support {m}')
    for k, (a,b) in enumerate(zip(actual,predicted)):
        check(a == b, f'PMF formula m={m},k={k}')
        check(b >= 0, f'PMF nonnegativity m={m},k={k}')
    check(sum(predicted) == 1, f'PMF normalization {m}')
    for r in range(m//2+1):
        actual_r = sum((p*falling(k,r) for k,p in enumerate(actual)),Fraction(0))
        check(actual_r == factorial_moment(m,r),f'factorial moment m={m},r={r}')
    check(2*sum(k*actual[k] for k in range(len(actual))) == Fraction(m,m-1),
          f'mean removal {m}')
    ed = sum(2*k*actual[k] for k in range(len(actual)))
    vd = sum((2*k-ed)**2*actual[k] for k in range(len(actual)))
    check(vd == Fraction(2*m*(m-2)**2,(m-1)**3),f'variance removal {m}')
    check(1-actual[0] >= Fraction(1,8),f'uniform success bound {m}')

# Exact rational one-step laws and exact absorption-time moment recurrences.
E = {0:Fraction(0),1:Fraction(0)}
S = {0:Fraction(0),1:Fraction(0)}
for m in range(2, 49):
    pmf=theoretical_probabilities(m)
    check(sum(pmf)==1, f'normalization at {m}')
    for p in pmf: check(p >= 0, f'nonnegative probability at {m}')
    check(sum(k*p for k,p in enumerate(pmf))*2 == Fraction(m,m-1), f'mean {m}')
    q=1-pmf[0]
    check(q>=Fraction(1,8), f'success {m}')
    E[m]=(1+sum((pmf[k]*E[m-2*k] for k in range(1,len(pmf))),Fraction(0)))/q
    future_mean=pmf[0]*E[m]+sum((pmf[k]*E[m-2*k] for k in range(1,len(pmf))),Fraction(0))
    S[m]=(1+2*future_mean+sum((pmf[k]*S[m-2*k] for k in range(1,len(pmf))),Fraction(0)))/q
    check(S[m]-E[m]**2>=0,f'nonnegative absorption variance {m}')
    check(E[m] <= 2*(m//2), f'optional stopping mean bound {m}')

check(E[2] == 1 and S[2] == 1,'m=2 moments')
check(E[3] == Fraction(4,3) and S[3] == Fraction(20,9),'m=3 moments')
# Uniform-in-size elementary inequalities used in the analytic proof.
for m in range(2, 300):
    mu = Fraction(m,m-1)
    v = Fraction(2*m*(m-2)**2,(m-1)**3)
    check(0 <= v <= 2, f'variance upper bound {m}')
    check(abs(v-2) <= Fraction(4,m-1),f'variance deviation {m}')
    check(Fraction(1,2) <= mu/2 <= 1, f'mean pair count bounds {m}')

print('PASS:',CHECKS,'finite exact checks; m=2..7 exhaustive proposal mappings; m=2..48 exact PMFs and stopping moments; m=2..299 bounds.')
print('Selected exact E[T_m]:',', '.join(f'{m}:{E[m]}' for m in range(2,7)))

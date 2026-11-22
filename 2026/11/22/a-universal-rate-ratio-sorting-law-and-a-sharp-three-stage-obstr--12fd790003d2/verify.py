#!/usr/bin/env python3
"""Reproduce exact counterexamples and finite checks for stage-wise exposure ordering.

Uses only the Python standard library. These computations corroborate, but do
not substitute for, the analytical adjacent-interchange proof in RESULT.md.
"""
from fractions import Fraction
from itertools import permutations
import math
import random

checks = 0

def check(condition, message="failed check"):
    global checks
    if not condition:
        raise AssertionError(message)
    checks += 1

def mat_product(A, B):
    return [[sum(A[i][k]*B[k][j] for k in range(len(B)))
             for j in range(len(B[0]))] for i in range(len(A))]

def two_transient(p, q, t):
    a, b = math.exp(-p*t), math.exp(-q*t)
    J = t*a if abs(p-q)<1e-12 else (a-b)/(q-p)
    return [[a, 0.0], [p*J, b]]

def two_completion(blocks):
    T = [[1.0, 0.0], [0.0, 1.0]]
    for p,q,t in blocks:
        T = mat_product(two_transient(p,q,t),T)
    return 1-T[0][0]-T[1][0]

def exact_pure_birth(phase_rates):
    """Matrix at time log(2), for distinct nonnegative integer stage rates."""
    rates = list(phase_rates) + [0]
    n = len(rates)
    check(len(set(rates)) == n)
    M = [[Fraction(0) for _ in range(n)] for _ in range(n)]
    for i in range(n):
        for j in range(i,n):
            numerator = math.prod(rates[i:j])
            M[j][i] = Fraction(numerator)*sum(
                (Fraction(1,2**rates[k]) /
                 math.prod(rates[l]-rates[k] for l in range(i,j+1) if l!=k)
                for k in range(i,j+1)), Fraction(0))
    for i in range(n):
        check(sum(M[k][i] for k in range(n))==1)
        for k in range(n):check(M[k][i]>=0)
    return M

def exact_completion(blocks, initial_stage=0):
    n = len(blocks[0])+1
    T = [[Fraction(int(i==j)) for j in range(n)] for i in range(n)]
    for block in blocks:
        T=mat_product(exact_pure_birth(block),T)
    return T[n-1][initial_stage]

# Exact two-stage benchmark: equal integrated first- and second-stage hazards.
A2=(3,1); B2=(1,3)
f_ab=exact_completion([A2,B2]); f_ba=exact_completion([B2,A2])
check(f_ab==Fraction(27,32))
check(f_ba==Fraction(9,16))
check(f_ab-f_ba==Fraction(9,32))

# Three stages: the same adjacent pair changes preference after a prefix.
A3=(4,1,2); B3=(1,4,3); C3=(8,1,2)
check(exact_completion([A3,B3])-exact_completion([B3,A3]) == Fraction(245,768))
check(exact_completion([C3,A3,B3])-exact_completion([C3,B3,A3])
      == Fraction(-59245,1376256))

rng=random.Random(20261120)
for _ in range(250):
    n=rng.randint(2,6)
    blocks=[(rng.uniform(.1,5.0), rng.uniform(.1,5.0), rng.uniform(.05,2.0))
            for _ in range(n)]
    baseline=two_completion(sorted(blocks, key=lambda b:-b[0]/b[1]))
    for perm in permutations(blocks):
        check(baseline+2e-12>=two_completion(perm), "sorted blocks were not optimal")

# Exact swap identity with arbitrary prefixes/suffixes, and survival weighting.
for _ in range(1000):
    p,q,r,s=[rng.uniform(.15,4.0) for z in range(4)]
    t,u=rng.uniform(.1,2.0),rng.uniform(.1,2.0)
    prefix=[(rng.uniform(.2,3),rng.uniform(.2,3),rng.uniform(.1,1))]
    suffix=[(rng.uniform(.2,3),rng.uniform(.2,3),rng.uniform(.1,1))]
    d=two_completion(prefix+[(p,q,t),(r,s,u)]+suffix)-two_completion(prefix+[(r,s,u),(p,q,t)]+suffix)
    J=lambda x,y,z: z*math.exp(-x*z) if abs(x-y)<1e-12 else (math.exp(-x*z)-math.exp(-y*z))/(y-x)
    rhs=(p*s-r*q)*J(p,q,t)*J(r,s,u)*math.exp(-prefix[0][0]*prefix[0][2])*math.exp(-suffix[0][1]*suffix[0][2])
    check(abs(d-rhs)<1e-11,"swap identity failed")

print(f"PASS: {checks:,} deterministic assertions; exact examples and floating comparisons")
print("two-stage benchmark:",f_ab,f_ba,"difference",f_ab-f_ba)
print("three-stage swaps:",Fraction(245,768),Fraction(-59245,1376256))

"""Exact diagnostic checks for a repeatedly opening, resetting habitat corridor.
Uses only the Python standard library. Re-run: python corridor_checker.py
The symbolic proof and global inequalities are supplied separately in RESULT.md.
"""
from fractions import Fraction as F
from itertools import product
from math import prod


def solve(A, b):
    n = len(b)
    aug = [list(map(F, A[i])) + [F(b[i])] for i in range(n)]
    for k in range(n):
        pivot = next(i for i in range(k, n) if aug[i][k] != 0)
        aug[k], aug[pivot] = aug[pivot], aug[k]
        u = aug[k][k]
        aug[k] = [x / u for x in aug[k]]
        for i in range(n):
            if i != k:
                r = aug[i][k]
                aug[i] = [x - r*y for x, y in zip(aug[i], aug[k])]
    return [aug[i][-1] for i in range(n)]


def matrix_mean(a, b, rates, s):
    # 0: corridor closed; j+1: open with j completed migration stages.
    n = len(rates)
    M = [[F(0) for _ in range(n+1)] for _ in range(n+1)]
    M[0][0] = a*s
    M[0][1] = -a*s
    for j, m in enumerate(rates):
        i = j + 1
        M[i][i] = b*s + m
        M[i][0] = -b*s
        if j < n-1:
            M[i][i+1] = -m
    return solve(M, [F(1)]*(n+1))[0]


def renewal_mean(a, b, rates, s):
    q_inv = prod((1+b*s/m for m in rates), start=F(1))
    return 1/(a*s) + (a+b)*(q_inv-1)/(a*b*s)


def derivative_poly(a, b, rates, s):
    # P = product(1+(b/m)s)=sum_{k=0}^n c_k s^k.
    c = [F(1)]
    for m in rates:
        d = [F(0)]*(len(c)+1)
        for k,v in enumerate(c):
            d[k] += v
            d[k+1] += v*b/m
        c = d
    return -1/(a*s*s) + (a+b)/(a*b)*sum(((k-1)*c[k]*s**(k-2) for k in range(2, len(c))), F(0))


checks = 0
for n in range(1, 6):
    for a, b in product((F(1),F(3,2)), (F(2),F(5,3))):
        for rates in product((F(1),F(5,2)), repeat=n):
            for s in (F(1,4), F(2,3), F(1), F(3)):
                m1 = matrix_mean(a,b,rates,s)
                m2 = renewal_mean(a,b,rates,s)
                assert m1 == m2, (a,b,rates,s,m1,m2)
                checks += 1
                # Rational central difference converges to analytic derivative.
                h = F(1, 100000)
                d = (renewal_mean(a,b,rates,s+h) - renewal_mean(a,b,rates,s-h))/(2*h)
                assert abs(d-derivative_poly(a,b,rates,s)) < F(1,10000)
                checks += 1

# For all models in the grid with at least 2 stages, each additional
# stage raises the derivative strictly at every positive test rate.
for n in range(2, 6):
    for s in (F(1,5),F(1,2),F(1),F(5)):
        old = derivative_poly(F(2),F(3),(F(1),)*n,s)
        new = derivative_poly(F(2),F(3),(F(1),)*(n+1),s)
        assert new > old
        checks += 1

# Closed form for two and three stages with unit parameters.
for s in (F(1,2),F(3,4),F(2)):
    assert renewal_mean(F(1),F(1),(F(1),F(1)),s) == 1/s+4+2*s
    assert renewal_mean(F(1),F(1),(F(1),F(1),F(1)),s) == 1/s+6+6*s+2*s*s
    checks += 2

print(f"PASS: {checks} exact rational assertions")

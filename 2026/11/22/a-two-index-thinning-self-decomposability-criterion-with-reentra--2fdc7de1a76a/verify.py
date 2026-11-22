#!/usr/bin/env python3
"""Exact-arithmetic diagnostics for a negative-transmuted geometric count law.

This finite program checks the stated algebra and witnesses; universal
inequalities are proved separately by mathematical arguments.
"""
from fractions import Fraction as F
from math import factorial


def canonical(q, alpha, lam, k):
    rho = q * (q + alpha) / (1 + alpha * q)
    return (lam if k == 1 else F(0)) + q ** k + q ** (2 * k) - rho ** k


def differences(q, alpha):
    rho = q * (q + alpha) / (1 + alpha * q)
    return [q ** k * (1 - q) + q ** (2 * k) * (1 - q * q)
            - rho ** k * (1 - rho) for k in (1, 2)]


def scaled_pmf(q, alpha, lam, n):
    tg = lambda j: (1 - alpha) * (1 - q) * q ** j + alpha * (1 - q*q) * q ** (2*j)
    return sum((lam ** j / factorial(j) * tg(n-j) for j in range(n+1)), F(0))


checks = 0
qs = [F(1, 5), F(1, 2), F(9, 10), F(99, 100)]
alphas = [F(-1), F(-19,20), F(-9,10), F(-7,10), F(-1,10)]
lambdas = [F(0), F(1,10), F(1)]
for q in qs:
    for alpha in alphas:
        rho = q * (q + alpha) / (1 + alpha * q)
        assert -q <= rho < q*q
        checks += 1
        d1, d2 = differences(q, alpha)
        for lam in lambdas:
            vals = [scaled_pmf(q, alpha, lam, n) for n in range(24)]
            assert all(x > 0 for x in vals)
            for n in range(21):
                left = (n+1) * vals[n+1]
                right = sum((vals[j] * canonical(q, alpha, lam, n+1-j)
                             for j in range(n+1)), F(0))
                assert left == right, (q, alpha, lam, n)
                checks += 1
            assert canonical(q,alpha,lam,1)-canonical(q,alpha,lam,2) == lam+d1
            assert canonical(q,alpha,lam,2)-canonical(q,alpha,lam,3) == d2
            checks += 2
        if d2 >= 0:
            for k in range(2, 75):
                assert canonical(q,alpha,F(0),k) >= canonical(q,alpha,F(0),k+1)
                checks += 1
        else:
            assert canonical(q,alpha,F(0),2) < canonical(q,alpha,F(0),3)
            checks += 1

q, alpha = F(9,10), F(-7,10)
rho = q*(q+alpha)/(1+alpha*q)
d1, d2 = differences(q,alpha)
assert rho == F(18,37)
assert d1 == F(-81009,13690000)
assert d2 == F(4261245327,50653000000)
checks += 3

q, alpha = F(1,2), F(-9,10)
rho = q*(q+alpha)/(1+alpha*q)
assert rho == F(-4,11)
assert differences(q,alpha)[1] == F(-719,85184)
checks += 2

q=F(99,100)
for alpha, sign in [(F(-1),-1),(-q,1),(F(-19,20),-1),(F(-1,10),1)]:
    d1,d2=differences(q,alpha)
    assert (d2 > 0)-(d2 < 0) == sign
    assert 1+d1>0
    checks += 2

print('PASS exact rational diagnostics:',checks)

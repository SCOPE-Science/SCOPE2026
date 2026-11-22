"""Finite exact checks supporting the proportional-recent-memory Gaussian path limit.

Run: python3 check.py   (Python 3 standard library only)
These are finite consistency checks, not a substitute for the asymptotic proof.
"""
from fractions import Fraction as F
from math import floor

checks = 0

def check(cond, message):
    global checks
    checks += 1
    if not cond:
        raise AssertionError(message)


def weights(n, c, a):
    W = [[F(0)] * (n+1) for _ in range(n+1)]
    for j in range(1, n+1):
        W[j][j] = F(1)
        if j >= 2:
            m = max((c*j).numerator // (c*j).denominator, 1)
            for k in range(1, j):
                W[j][k] = W[j-1][k] + a/F(m) * (W[j-1][k] - W[j-m-1][k])
    return W


def enumerate_expectations(n, c, a):
    # Complete enumeration of all 2^n sign paths for small n.
    m = [0] + [max((c*j).numerator // (c*j).denominator, 1) for j in range(1,n+1)]
    moments = [[F(0)]*(n+1) for _ in range(n+1)]
    eps2 = [F(0)]*(n+1)
    paths = [((), F(1))]
    for j in range(1,n+1):
        next_paths = []
        for history, prob in paths:
            drift = a * sum(history[-m[j]:], 0)/m[j] if j >= 2 else F(0)
            for x in (-1,1):
                q = (F(1)+x*drift)/2
                check(q >= 0 and q <= 1, 'conditional probability')
                next_paths.append((history+(x,), prob*q))
                eps2[j] += prob*q*(x-drift)**2
        paths = next_paths
    check(sum(v for _,v in paths) == F(1), 'total probability')
    for path, prob in paths:
        sums = [F(0)]
        for x in path: sums.append(sums[-1]+x)
        for i in range(1,n+1):
            for j in range(1,n+1):
                moments[i][j] += prob*sums[i]*sums[j]
    return moments,eps2


for c,p in ((F(1,2),F(2,5)),(F(2,3),F(3,5)),(F(3,4),F(1,2))):
    a = 2*p-1
    for n in range(2,9):
        W = weights(n,c,a)
        actual,eps2 = enumerate_expectations(n,c,a)
        for i in range(1,n+1):
            for j in range(1,n+1):
                predicted=sum((W[i][k]*W[j][k]*eps2[k] for k in range(1,min(i,j)+1)),F(0))
                check(actual[i][j]==predicted, f'martingale Gram mismatch {(c,p,n,i,j)}')
        for i in range(1,n+1):
            for k in range(1,i+1):
                check(F(0) < W[i][k] <= F(1) if p<=F(1,2) else W[i][k]>=F(1), 'weight positivity monotonicity')
        if p==F(1,2):
            for i in range(1,n+1):
                for j in range(1,n+1):
                    check(actual[i][j] == min(i,j), 'Brownian neutral covariance')

print(f'PASS: {checks} exact-rational checks across 21 exhaustive finite models')

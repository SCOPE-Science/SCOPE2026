"""Exact full-configuration verification of two-particle jump-activity noise.

Requires Python 3 standard library only. Run: python verify_bipartite_activity.py
Particles exchange along each occupied-vacant edge at unit rate.
"""
from fractions import Fraction as F
from itertools import combinations


def solve(a, b):
    """Gauss-Jordan solve over rational numbers; a is square and invertible."""
    n = len(b)
    w = [[F(x) for x in a[i]] + [F(b[i])] for i in range(n)]
    for j in range(n):
        pivot = next(k for k in range(j, n) if w[k][j])
        w[j], w[pivot] = w[pivot], w[j]
        z = w[j][j]
        w[j] = [v/z for v in w[j]]
        for i in range(n):
            if i != j:
                z = w[i][j]
                if z:
                    w[i] = [x-z*y for x, y in zip(w[i], w[j])]
    return [row[-1] for row in w]


def full_configuration_fano(r, s):
    n = r+s
    states = list(combinations(range(n), 2))
    index = {state: i for i, state in enumerate(states)}
    m = len(states)
    Q = [[0]*m for _ in range(m)]
    for state in states:
        i = index[state]
        for occupied in state:
            targets = range(r, n) if occupied < r else range(r)
            for dest in targets:
                if dest in state:
                    continue
                new = tuple(sorted((dest, state[1] if occupied == state[0] else state[0])))
                Q[i][index[new]] += 1
                Q[i][i] -= 1
    assert all(Q[i][j] == Q[j][i] for i in range(m) for j in range(m))
    rates = [-Q[i][i] for i in range(m)]
    mu = F(sum(rates), m)
    A = [[-x for x in row] for row in Q]
    rhs = [F(x)-mu for x in rates]
    A[-1] = [1]*m
    rhs[-1] = F(0)
    h = solve(A, rhs)
    assert sum(h) == 0
    assert all(sum(F(-Q[i][j])*h[j] for j in range(m)) == F(rates[i])-mu
               for i in range(m))
    variance_rate = mu + F(2, m)*sum((F(rates[i])-mu)*h[i] for i in range(m))
    return mu, variance_rate / mu


def formula(r, s):
    n = r+s
    mu = F(4*r*s*(n-2), n*(n-1))
    delta = r-s
    excess = F(n*n+delta*delta*(n*n-6*n+4), n*n*(n-1)**2)
    return mu, 1+excess


def main():
    count=0
    for n in range(4, 10):
        for r in range(1, n//2+1):
            s = n-r
            got = full_configuration_fano(r, s)
            exp = formula(r, s)
            assert got == exp, (r, s, got, exp)
            count += 1
    print('PASS: exact full-configuration stationary Poisson equations,', count, 'unlabeled bipartitions')
    for n in range(4, 90):
        fs = [formula(r, n-r)[1] for r in range(1, n//2+1)]
        if n <= 5:
            assert fs == sorted(fs)
        else:
            assert fs == sorted(fs, reverse=True)
    print('PASS: finite-size extremizer ordering, all total sizes 4..89')
    for r,s in [(1,3),(2,2),(1,4),(2,3),(1,5),(2,4),(3,3),(2,8),(6,6)]:
        print(f'K_{{{r},{s}}}: mean rate={formula(r,s)[0]}, F={formula(r,s)[1]}')


if __name__ == '__main__':
    main()

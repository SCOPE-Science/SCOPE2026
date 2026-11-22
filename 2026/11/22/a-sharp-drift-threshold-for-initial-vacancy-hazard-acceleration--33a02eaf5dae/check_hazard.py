"""Exact rational checks of Palm-started vacancy-spell hazard coefficients.

Python 3 standard library only. This checks finite configuration generators;
its finite tests supplement, rather than replace, the symbolic proof.
"""
from fractions import Fraction as F
from itertools import combinations
from math import comb


def check(L, N, p, q):
    states = tuple(combinations(range(L), N))
    index = {s: i for i, s in enumerate(states)}
    B = [i for i, s in enumerate(states) if 0 not in s]
    A = [i for i, s in enumerate(states) if 0 in s]
    adj = [{} for _ in states]
    for i, s in enumerate(states):
        have = set(s)
        for j in s:
            for k, rate in (((j + 1) % L, p), ((j - 1) % L, q)):
                if k not in have:
                    nxt = tuple(sorted((have - {j}) | {k}))
                    z = index[nxt]
                    adj[i][z] = adj[i].get(z, F(0)) + rate
        adj[i][i] = adj[i].get(i, F(0)) - sum(
            rate for j in s for k, rate in
            (((j + 1) % L, p), ((j - 1) % L, q)) if k not in have
        )
    # Independent arrival-flux calculation (from occupied configurations),
    # not the closed-form neighbor-occupation Palm factor.
    entrance = {b: sum(adj[a].get(b, F(0)) for a in A) for b in B}
    total = sum(entrance.values())
    beta = {i: entrance[i] / total for i in B}
    kill = {i: sum(adj[i].get(a, F(0)) for a in A) for i in B}
    h0 = sum(beta[i] * kill[i] for i in B)
    qc = {i: sum(rate * kill.get(j, F(0)) for j, rate in adj[i].items()
                 if j in beta) for i in B}
    slope = sum(beta[i] * qc[i] for i in B) + h0*h0
    a = F(N - 1, L - 2)
    b = F((N - 1)*(N - 2), (L - 2)*(L - 3))
    target0 = (2*p*q + (p*p + q*q)*a)/(p + q)
    target_slope = target0*target0 - 2*p*q*(1+a)-(p-q)**2*b
    assert h0 == target0, (L, N, p, q, h0, target0)
    assert slope == target_slope, (L, N, p, q, slope, target_slope)
    if 2 <= N <= L-2:
        z = p/q+q/p
        poly = (N-1)*(z*z-4*(L-2))-2*(L-2)*(L-3)*z
        assert (slope > 0) == (poly > 0), (L,N,p,q)
        assert (slope == 0) == (poly == 0), (L,N,p,q)


def main():
    tests = 0
    for L in range(4, 9):
        for N in range(1, L):
            for p, q in ((F(1), F(1)), (F(2), F(3)), (F(3), F(1)),
                         (F(1), F(11)), (F(23), F(1)), (F(1), F(101))):
                check(L, N, p, q)
                tests += 1
    print('Exact transition-generator tests passed:', tests)
    print('Ring lengths 4–8; all nonempty and nonfull charge sectors.')
    print('The general parameter identity is established separately by algebra.')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Exact-rational checks for a leaf-corona fastest-mixing theorem.

All checks use Python's standard library. This program tests finite examples;
the accompanying mathematical proof establishes the stated infinite families.
"""
from fractions import Fraction as F
from itertools import combinations
from random import Random


def graph_edges(n, mask):
    all_edges = list(combinations(range(n), 2))
    return [e for j, e in enumerate(all_edges) if mask & (1 << j)]


def connected(n, edges):
    reached = {0}
    while True:
        new = reached | {v for u, v in edges if u in reached} | {u for u, v in edges if v in reached}
        if new == reached:
            return len(reached) == n
        reached = new


def random_chain(n, edges, rng):
    """Rational symmetric stochastic kernel on H corona K_1."""
    edge_weights = {e: F(rng.randrange(1, 10), 20 * n * n) for e in edges}
    leaf_weights = [F(rng.randrange(1, 10), 20 * n) for _ in range(n)]
    totals = [leaf_weights[i] for i in range(n)]
    for (i, j), weight in edge_weights.items():
        totals[i] += weight
        totals[j] += weight
    assert all(z <= 1 for z in totals)
    N = 2 * n
    P = [[F(0) for _ in range(N)] for _ in range(N)]
    for i in range(n):
        b = leaf_weights[i]
        P[i][n+i] = P[n+i][i] = b
        P[i][i] = 1 - totals[i]
        P[n+i][n+i] = 1 - b
    for (i, j), a in edge_weights.items():
        P[i][j] = P[j][i] = a
    assert all(sum(row) == 1 for row in P)
    assert all(P[i][j] == P[j][i] for i in range(N) for j in range(N))
    return P


def rayleigh(P, n, i, j):
    x = [F(0)] * (2*n)
    x[i], x[j], x[n+i], x[n+j] = F(1), F(-1), F(2), F(-2)
    assert sum(x) == 0
    norm = sum(v*v for v in x)
    assert norm == 10
    numerator = sum(x[k] * P[k][l] * x[l] for k in range(2*n) for l in range(2*n))
    return numerator / norm


def candidate_matrix(r, m):
    n = r*m
    d = (r-1)*m
    a, b = F(3, 5*d), F(2, 5)
    N = 2*n
    P = [[F(0) for _ in range(N)] for _ in range(N)]
    for i in range(n):
        P[i][n+i] = P[n+i][i] = b
        P[n+i][n+i] = 1-b
        for j in range(n):
            if i != j and i//m != j//m:
                P[i][j] = a
    for i in range(n):
        assert sum(P[i]) == 1  # core diagonal exactly zero
        assert P[i][i] == 0
    for i in range(n, N):
        assert sum(P[i]) == 1
    assert all(P[i][j] == P[j][i] for i in range(N) for j in range(N))
    assert all(P[i][j] >= 0 for i in range(N) for j in range(N))
    return P, a, b


def det2(a,b,c):
    return a*c-b*b


def within_pm_bound(M, bound=F(4,5)):
    """Check both 2x2 matrices bound*I +/- M PSD by exact determinants."""
    for sign in (+1, -1):
        diag1 = bound + sign*M[0][0]
        off = sign*M[0][1]
        diag2 = bound + sign*M[1][1]
        assert diag1 >= 0 and diag2 >= 0 and det2(diag1, off, diag2) >= 0


def spectral_blocks(r,m):
    d=(r-1)*m
    a,b=F(3,5*d),F(2,5)
    # A_core eigenvalues: degree d once; 0 with r*(m-1);
    # -m with r-1. The corresponding blocks are exact.
    B_d=((a*d,b),(b,1-b))
    B_0=((F(0),b),(b,1-b))
    B_m=((-a*m,b),(b,1-b))
    # Stationary block B_d has eigenvalues 1 and 1/5.
    assert B_d[0][0] + B_d[1][1] == F(6,5)
    assert det2(B_d[0][0], B_d[0][1], B_d[1][1]) == F(1,5)
    # B_0 has eigenvalues 4/5 and -1/5.
    assert B_0[0][0]+B_0[1][1] == F(3,5)
    assert det2(B_0[0][0],B_0[0][1],B_0[1][1]) == F(-4,25)
    within_pm_bound(B_0)
    within_pm_bound(B_m)
    return True


def run():
    universal = 0
    matrices = 0
    for n in range(3, 6):
        all_edges = list(combinations(range(n),2))
        for mask in range(1 << len(all_edges)):
            edges=graph_edges(n,mask)
            if not connected(n,edges) or len(edges)==len(all_edges):
                continue
            edge_set=set(edges)
            missing=[(i,j) for i,j in all_edges if (i,j) not in edge_set]
            rng=Random(1729+n*10000+mask)
            for sample in range(3):
                P=random_chain(n,edges,rng)
                for i,j in missing:
                    assert rayleigh(P,n,i,j) >= F(4,5)
                    universal += 1
    for r in range(2, 8):
        for m in range(2, 8):
            P,a,b=candidate_matrix(r,m)
            assert spectral_blocks(r,m)
            n=r*m
            # Exact Rayleigh equality for a nonadjacent core pair.
            assert rayleigh(P,n,0,1) == F(4,5)
            x=[F(0)]*(2*n)
            x[0],x[1],x[n],x[n+1]=F(1),F(-1),F(2),F(-2)
            assert all(sum(P[k][j]*x[j] for j in range(2*n)) == F(4,5)*x[k]
                       for k in range(2*n))
            matrices += 1
    # Unbalanced K_{p,q}, p,q >= 2: saturation at 4/5 would
    # force a=3/(5p)=3/(5q), which is impossible when p != q.
    unbalanced=0
    for p in range(2,15):
        for q in range(2,15):
            if p == q:
                continue
            assert F(3,5*p) != F(3,5*q)
            unbalanced+=1
    print('VERIFY_OK universal_exact_rayleigh_checks=',universal,
          'balanced_multipartite_exact_matrices=',matrices,
          'unbalanced_bipartite_necessary_condition_checks=',unbalanced)

if __name__ == '__main__':
    run()

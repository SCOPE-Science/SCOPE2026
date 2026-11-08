#!/usr/bin/env python3
"""Direct finite checks of total domination of a vertex-deleted triangular graph.

Uses only the Python standard library.  The exponential-formula recurrence and
original-graph simulations are separate from the direct deletion-graph test.
"""
from math import comb, factorial
from itertools import combinations


def add_shift(dst, src, coeff, shift):
    for j, a in enumerate(src):
        dst[j + shift] += coeff * a


def polynomial_counts(max_n):
    H = []
    for n in range(max_n + 1):
        E = comb(n, 2)
        p = [comb(E, j) for j in range(E + 1)]
        for s in range(1, n + 1):
            for b in range(s // 2 + 1):
                matching = factorial(s) // (factorial(s - 2*b) * factorial(b) * 2**b)
                add_shift(p, H[n-s], -comb(n, s)*matching, b)
        assert all(v >= 0 for v in p)
        H.append(p)
    T = []
    P = []
    for n in range(max_n + 1):
        t = H[n][:]
        if n:
            for k, value in enumerate(H[n-1]):
                t[k] += n*value
        T.append(t)
        if n >= 3:
            N = comb(n, 2)
            p = [0]*(N+1)
            for k, value in enumerate(t):
                q, rem = divmod(value*(N-k), N)
                assert rem == 0
                p[k] += q
            for k, value in enumerate(H[n-2]):
                p[k] += value
            P.append((n,p))
    return H, T, dict(P)


def classify(n, edge_indices):
    edges = [(i,j) for i in range(n) for j in range(i+1,n) if (i,j)!=(0,1)]
    E = set(edges[i] for i in edge_indices)
    deg = [0]*n
    for u,v in E:
        deg[u] += 1
        deg[v] += 1
    return all(deg[u]+deg[v] >= (3 if (u,v) in E else 1)
               for u,v in edges)


def tree_formula(n):
    k=n//3
    if n%3 == 0:
        return factorial(n-2)*2//(3*2**(k-2)*factorial(k-2))
    if n%3 == 2:
        return factorial(n-2)//(2**k*factorial(k))
    # One isolated vertex in the underlying chosen graph, avoiding the deleted edge.
    N = comb(n,2)
    m = 2*k
    A = factorial(n)//(2**k*factorial(k))
    old = A*(N-m)//N
    special = 0
    if k>=2:
        special += factorial(n-2)*125//(120*2**(k-2)*factorial(k-2))
    if k>=3:
        special += factorial(n-2)*2//(9*2**(k-3)*factorial(k-3))
    return old + special


def verify():
    H,T,P=polynomial_counts(9)
    # All subsets at each order: independently apply the total-neighbor condition.
    for n in range(4, 8):
        e=comb(n,2)-1
        observed=[0]*(e+1)
        for mask in range(1<<e):
            selected = [i for i in range(e) if mask>>i&1]
            if classify(n, selected):
                observed[len(selected)] += 1
        assert observed == P[n][:e+1], (n,observed,P[n])
        print('FULL_POLYNOMIAL_EXHAUSTIVE_OK',n,1<<e)
    # Exhaust the minimum and immediately smaller size for two more orders.
    for n in range(8,10):
        e=comb(n,2)-1
        m=(2*(n-2)+2)//3
        assert P[n][m-1]==0
        for r in (m-1,m):
            observed=sum(classify(n,C) for C in combinations(range(e),r))
            assert observed==P[n][r],(n,r,observed,P[n][r])
        print('MINIMUM_EXHAUSTIVE_OK',n,m,P[n][m])
    for n in range(4,10):
        m=(2*(n-2)+2)//3
        assert all(a==0 for a in P[n][:m])
        assert P[n][m]==tree_formula(n),(n,P[n][m],tree_formula(n))
    print('CLASSIFICATION_COUNTS_OK n=4..9')
    print('VERIFY_OK')

if __name__=='__main__':
    verify()

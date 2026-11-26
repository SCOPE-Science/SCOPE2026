#!/usr/bin/env python3
"""Reproducible finite-field checks for reversible waves on two-subset Kneser graphs.
Only Python's standard library is needed. Finite checks are not a substitute for the proof.
"""
from itertools import combinations


def matmul(a, b):
    n = len(a)
    out = [[0] * n for _ in range(n)]
    for i in range(n):
        for l, v in enumerate(a[i]):
            if v:
                bl = b[l]
                for j in range(n):
                    out[i][j] += v * bl[j]
        out[i] = [z % 3 for z in out[i]]
    return out


def rank(a):
    a = [list(map(lambda x: x % 3, row)) for row in a]
    m, n = len(a), len(a[0]); pivot = 0
    for j in range(n):
        r = next((t for t in range(pivot, m) if a[t][j]), None)
        if r is None:
            continue
        a[pivot], a[r] = a[r], a[pivot]
        if a[pivot][j] == 2:
            a[pivot] = [(2*x) % 3 for x in a[pivot]]
        for t in range(pivot + 1, m):
            c = a[t][j]
            if c:
                a[t] = [(v - c*u) % 3 for v, u in zip(a[t], a[pivot])]
        pivot += 1
        if pivot == m:
            break
    return pivot


def eye(n):
    return [[int(i == j) for j in range(n)] for i in range(n)]


def graph(n):
    edges = list(combinations(range(n), 2)); N = len(edges)
    a = [[int(i != j and not(set(edges[i]) & set(edges[j])))
          for j in range(N)] for i in range(N)]
    return edges, a


def wave(a):
    N = len(a)
    return [[(a[i][j] if j < N else (-int(j == N+i)) % 3)
             for j in range(2*N)] for i in range(N)] + [
            [int(j == i) if j < N else 0 for j in range(2*N)]
            for i in range(N)]


def expected(n, t):
    N = n*(n-1)//2
    c2 = int(t % 2 == 0); c3 = int(t % 3 == 0)
    c4 = int(t % 4 == 0); c6 = int(t % 6 == 0)
    if n % 3 == 0:
        return 2*n*c4 + (N-n)*(c2+c6)
    if n % 3 == 1:
        return (n-1)*(1+c3) + (N-n+1)*(c2+c6)
    z = t; h = 1
    while z % 3 == 0:
        z //= 3; h *= 3
    return 2*c4 + (n-1)*c2*min(4,h) + (N-2*n+1)*(c2+c6)


def run_matrices():
    for n in range(4, 11):
        _, a = graph(n); b = wave(a); d = len(b)
        I = eye(d); P = eye(d)
        for t in range(1, 37):
            P = matmul(P, b)
            if t in (1, 2, 3, 4, 6, 9, 12, 18, 36):
                nullity = d - rank([[(P[i][j] - I[i][j]) % 3
                                    for j in range(d)] for i in range(d)])
                assert nullity == expected(n, t), (n, t, nullity, expected(n,t))
            if t == {0:12, 1:6, 2:36}[n%3]:
                assert P == I, (n, 'claimed period does not return identity')
        print('n=%d N=%d checked 9 fixed-space nullities and period identity' % (n, len(a)))


def run_states():
    # A separate coordinate-level oracle checks all 3^12 wave states for KG(4,2).
    n = 4; edges, a = graph(n); N = len(edges)
    neighbors = [[j for j in range(N) if a[i][j]] for i in range(N)]
    divisor_counts = {1:0,2:0,3:0,6:0}
    for number in range(3**(2*N)):
        digits=[]; x=number
        for _ in range(2*N):digits.append(x%3); x//=3
        u,v=digits[:N],digits[N:]
        first=(u,v)
        for k in range(1,7):
            u,v=([(sum(u[j] for j in neighbors[i])-v[i])%3 for i in range(N)],u)
            if k in divisor_counts and (u,v)==first:
                divisor_counts[k]+=1
    for k,c in divisor_counts.items():
        assert c == 3**expected(n,k), (k,c,3**expected(n,k))
    print('n=4: all 531441 states checked; fixed populations', divisor_counts)

if __name__ == '__main__':
    run_matrices()
    run_states()
    print('ALL CHECKS PASSED')

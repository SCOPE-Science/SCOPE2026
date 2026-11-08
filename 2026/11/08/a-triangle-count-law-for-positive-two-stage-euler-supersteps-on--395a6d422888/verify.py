#!/usr/bin/env python3
"""Exact-arithmetic checks of two-substep Euler endpoint positivity on regular graphs.

No external dependencies; finite tests supplement, but do not replace, the algebraic proof.
"""
from fractions import Fraction as F
from itertools import combinations
from math import isqrt


def connected(adj):
    n = len(adj)
    seen = {0}
    stack = [0]
    while stack:
        i = stack.pop()
        for j in range(n):
            if adj[i][j] and j not in seen:
                seen.add(j)
                stack.append(j)
    return len(seen) == n


def graph_n(n, mask):
    adj = [[0] * n for _ in range(n)]
    for b,(i,j) in enumerate(combinations(range(n), 2)):
        if (mask >> b) & 1:
            adj[i][j] = adj[j][i] = 1
    return adj


def matrix_product(A, B):
    n = len(A)
    return [[sum(A[i][k]*B[k][j] for k in range(n)) for j in range(n)] for i in range(n)]


def matrix_update(A, s, p):
    n = len(A)
    d = sum(A[0])
    assert d and all(sum(row) == d for row in A)
    A2 = matrix_product(A, A)
    return [[(1-s+p+p/F(d) if i==j else
              (s-2*p)/d * A[i][j]+p/F(d*d)*A2[i][j]) for j in range(n)]
            for i in range(n)]


def edge_floor(A, A2):
    return min(A2[i][j] for i in range(len(A)) for j in range(i+1,len(A)) if A[i][j])


def predicted(A, s, p):
    d = sum(A[0]); A2 = matrix_product(A,A)
    t = edge_floor(A,A2)
    return 1-s+(1+F(1,d))*p >= 0 and s >= (2-F(t,d))*p


def cycle(n):
    a = [[0]*n for _ in range(n)]
    for i in range(n): a[i][(i+1)%n] = a[(i+1)%n][i] = 1
    return a


def parts_graph(r,k):
    n = r*k
    return [[int(i!=j and i//k!=j//k) for j in range(n)] for i in range(n)]


def complete(n):
    return [[int(i!=j) for j in range(n)] for i in range(n)]


def check(A):
    n = len(A)
    d = sum(A[0]); assert d>=1 and all(sum(row)==d for row in A) and connected(A)
    A2 = matrix_product(A,A)
    t = edge_floor(A,A2)
    if t == d-1:
        assert all(A[i][j] == (i!=j) for i in range(n) for j in range(n))
        q = F(d,d+1)
        for x in (F(1,2),F(3,1),F(20,1)):
            P = matrix_update(A, x+q, x*q)
            assert all(z == F(1,n) for row in P for z in row)
    else:
        s = F(2*d-t,d-1-t)
        p = F(d,d-1-t)
        P = matrix_update(A,s,p)
        exact = [[F(A2[i][j]-t*A[i][j]-d*(i==j),d*(d-1-t)) for j in range(n)] for i in range(n)]
        assert P == exact
        assert all(v >= 0 for row in P for v in row)
        assert all(sum(row) == 1 for row in P)
        assert not predicted(A,s+F(1,100),p)
        # Feasible slightly short of the sharp total: choose an exact product p=(s-1)/c.
        short = (s+2)/2
        ps = (short-1)/(1+F(1,d))
        assert ps>0 and ps<=short*short/4 and predicted(A,short,ps)
        assert all(v >= 0 for row in matrix_update(A,short,ps) for v in row)
    for x in [F(1,5),F(1,2),F(4,5),F(1),F(6,5),F(2),F(7,2),F(5)]:
        for y in [F(1,8),F(1,4),F(3,5),F(1),F(2),F(4)]:
            s,p = x+y,x*y
            P = matrix_update(A,s,p)
            actual = all(v>=0 for row in P for v in row)
            assert actual == predicted(A,s,p), (n,d,t,x,y)
            assert all(sum(row)==1 for row in P)
    return 48


def main():
    count=0; pairs=0
    for n in range(2,7):
        edges=n*(n-1)//2
        for mask in range(1<<edges):
            A=graph_n(n,mask)
            d=sum(A[0])
            if d and all(sum(row)==d for row in A) and connected(A):
                pairs+=check(A); count+=1
    extras=[cycle(7),cycle(8),cycle(9),parts_graph(3,2),parts_graph(3,3),parts_graph(4,2),parts_graph(3,4),complete(8)]
    for A in extras:
        pairs+=check(A); count+=1
    assert pairs==48*count
    print('VERIFICATION_OK: {} labeled connected regular graphs, {} rational endpoint pairs; sharp boundary identities checked'.format(count,pairs))

if __name__=='__main__': main()

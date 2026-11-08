#!/usr/bin/env python3
"""Reproduce the exact finite leaf-response theorem using integer and rational arithmetic.

No third-party dependencies. Finite checks are tests, not a substitute for the all-order proof.
"""
from fractions import Fraction as F
from itertools import combinations

CHECKS = 0

def check(actual, expected, tag):
    global CHECKS
    CHECKS += 1
    if actual != expected:
        raise AssertionError((tag, actual, expected))

def determinant(matrix):
    """Fraction-free elimination of a square integer matrix."""
    n = len(matrix)
    if n == 0:
        return 1
    a = [list(row) for row in matrix]
    prev = 1
    sign = 1
    for k in range(n - 1):
        if a[k][k] == 0:
            h = next((t for t in range(k + 1, n) if a[t][k]), None)
            if h is None:
                return 0
            a[k], a[h] = a[h], a[k]
            sign *= -1
        pivot = a[k][k]
        for i in range(k + 1, n):
            for j in range(k + 1, n):
                num = a[i][j] * pivot - a[i][k] * a[k][j]
                assert num % prev == 0
                a[i][j] = num // prev
            a[i][k] = 0
        prev = pivot
    return sign * a[-1][-1]

def edges(a, b, add):
    out = [(i, a + j) for i in range(a) for j in range(b)]
    if add:
        out.append((0, 1))
    return out

def weighted_tree_count(a, b, xs, ys, add):
    n = a + b
    weights = xs + ys
    L = [[0] * n for _ in range(n)]
    for i, j in edges(a, b, add):
        w = weights[i] * weights[j]
        L[i][i] += w
        L[j][j] += w
        L[i][j] -= w
        L[j][i] -= w
    return determinant([row[:-1] for row in L[:-1]])

def closed_Z(a, b, xs, ys, add):
    prod = 1
    for z in xs + ys:
        prod *= z
    X, Y = sum(xs), sum(ys)
    if not add:
        return prod * X**(b-1) * Y**(a-1)
    return prod * X**(b-1) * Y**(a-2) * (Y+xs[0]+xs[1])

def spanning_counts(a, b, add):
    n = a + b
    E = edges(a, b, add)
    count = total_leaves = 0
    for chosen in combinations(E, n - 1):
        parent = list(range(n))
        def root(i):
            while parent[i] != i:
                i = parent[i]
            return i
        degrees = [0]*n
        good = True
        for i,j in chosen:
            ii,jj = root(i),root(j)
            if ii == jj:
                good = False
                break
            parent[ii] = jj
            degrees[i] += 1
            degrees[j] += 1
        if good:
            count += 1
            total_leaves += degrees.count(1)
    return count, F(total_leaves, count)

def leaf_response(a,b):
    q = (F(b-1,b) ** (a-2))
    r = (F(a-1,a) ** (b-1))
    return F(2,b+2)*(q-r)

def known_E(a,b):
    return a*F(a-1,a)**(b-1)+b*F(b-1,b)**(a-1)

def expected_sign(a,b):
    return 0 if (a,b)==(2,1) else (1 if b>=a else -1)

def main():
    for a in range(2,6):
        for b in range(1,6):
            xs = [2+(i*3)%7 for i in range(a)]
            ys = [3+(j*2)%5 for j in range(b)]
            for add in [False,True]:
                check(weighted_tree_count(a,b,xs,ys,add),closed_Z(a,b,xs,ys,add),('weighted',a,b,add))
                check(weighted_tree_count(a,b,[1]*a,[1]*b,add),closed_Z(a,b,[1]*a,[1]*b,add),('plain',a,b,add))
            if a+b<=7:
                n0,L0 = spanning_counts(a,b,False)
                n1,L1 = spanning_counts(a,b,True)
                check(n0,closed_Z(a,b,[1]*a,[1]*b,False),('count0',a,b))
                check(n1,closed_Z(a,b,[1]*a,[1]*b,True),('count1',a,b))
                check(L0,known_E(a,b),('expect0',a,b))
                check(L1-L0,leaf_response(a,b),('delta',a,b))
    for a in range(2,121):
        for b in range(1,121):
            d=leaf_response(a,b)
            check((d>0)-(d<0),expected_sign(a,b),('sign',a,b))
    print('VERIFY_OK',CHECKS,'exact assertions')

if __name__=='__main__':
    main()

#!/usr/bin/env python3
"""Exact, standalone certificate for two-unit-chord path A/D design.
Run: python3 VERIFY.py. Only the Python 3 standard library is needed.
"""
from fractions import Fraction
from itertools import combinations


def candidate_edges(n):
    return [(i, j) for i in range(n) for j in range(i + 2, n)]


def vector(n, e):
    a, b = e
    clipped = [min(max(t - a, 0), b - a) for t in range(n)]
    total = sum(clipped)
    return [n * x - total for x in clipped]


def pair_score(n, e, f, re, rf, ree, rff):
    a, b = e
    c, d = f
    le, lf = b - a, d - c
    h = max(0, min(b, d) - max(a, c))
    det = (le + 1) * (lf + 1) - h * h
    ref = sum(x * y for x, y in zip(re, rf))
    numerator = (lf + 1) * ree + (le + 1) * rff - 2 * h * ref
    return det, Fraction(numerator, det)


def optima(n):
    es = candidate_edges(n)
    vecs = [vector(n, e) for e in es]
    norms = [sum(x * x for x in r) for r in vecs]
    best_d, best_a = -1, Fraction(-1)
    arg_d, arg_a = [], []
    checked = 0
    for i, j in combinations(range(len(es)), 2):
        checked += 1
        e, f = es[i], es[j]
        d, a = pair_score(n, e, f, vecs[i], vecs[j], norms[i], norms[j])
        if d > best_d:
            best_d, arg_d = d, [(e, f)]
        elif d == best_d:
            arg_d.append((e, f))
        if a > best_a:
            best_a, arg_a = a, [(e, f)]
        elif a == best_a:
            arg_a.append((e, f))
    assert checked == len(es) * (len(es)-1)//2
    return best_d, best_a, arg_d, arg_a, checked


def laplacian(n, pair):
    L = [[0] * n for _ in range(n)]
    edges = [(i, i+1) for i in range(n-1)] + list(pair)
    for i, j in edges:
        L[i][i] += 1
        L[j][j] += 1
        L[i][j] -= 1
        L[j][i] -= 1
    return L


def determinant_bareiss(A):
    A = [list(row) for row in A]
    N = len(A)
    if N == 1:
        return A[0][0]
    sign, previous = 1, 1
    for k in range(N-1):
        if A[k][k] == 0:
            swap = next((i for i in range(k+1, N) if A[i][k] != 0), None)
            assert swap is not None
            A[k], A[swap] = A[swap], A[k]
            sign *= -1
        pivot = A[k][k]
        for i in range(k+1, N):
            for j in range(k+1, N):
                z = A[i][j]*pivot-A[i][k]*A[k][j]
                assert z % previous == 0
                A[i][j] = z//previous
            A[i][k] = 0
        previous = pivot
    return sign*A[-1][-1]


def inverse_fraction(mat):
    n = len(mat)
    A = [[Fraction(x) for x in row] + [Fraction(int(i==j)) for j in range(n)]
         for i,row in enumerate(mat)]
    for k in range(n):
        pivot = next(i for i in range(k,n) if A[i][k] != 0)
        A[k], A[pivot] = A[pivot], A[k]
        fac = A[k][k]
        A[k] = [x/fac for x in A[k]]
        for i in range(n):
            if i==k: continue
            fac=A[i][k]
            if fac:
                A[i] = [x-fac*y for x,y in zip(A[i],A[k])]
    return [row[n:] for row in A]


def direct_kf_and_treecount(n, pair):
    L = laplacian(n,pair)
    grounded = [row[:-1] for row in L[:-1]]
    tree = determinant_bareiss(grounded)
    G = inverse_fraction(grounded)
    trace = sum(G[i][i] for i in range(n-1))
    summation = sum(sum(row) for row in G)
    return tree, n*trace-summation


def main():
    manifest = {
        4:(8,3,3), 5:(12,1,1), 6:(16,3,3), 7:(21,3,3),
        8:(27,1,1),9:(33,3,3),10:(40,3,3),11:(48,1,1),
        12:(56,3,3),13:(65,3,3),14:(75,1,1),15:(85,3,2),
    }
    total = 0
    results = {}
    for n in range(4,16):
        best_d,best_a,D,A,count=optima(n)
        results[n] = (best_d,best_a,D,A)
        total += count
        assert (best_d,len(D),len(A)) == manifest[n], (n,best_d,len(D),len(A))
        if n<=14:
            assert A == D, (n,A,D)
        else:
            assert set(A).isdisjoint(D)
        # Independent grounded Laplacian computations at each size on several pairs.
        choices= sorted(set(A + D))
        if n<=8:
            es=candidate_edges(n)
            choices += list(combinations(es, 2))[:min(6,len(es)*(len(es)-1)//2)]
        for pair in set(choices):
            value, actual_kf = direct_kf_and_treecount(n,pair)
            e, f = pair
            re,rf = vector(n,e),vector(n,f)
            det, gain_scaled = pair_score(n,e,f,re,rf,sum(x*x for x in re),sum(y*y for y in rf))
            predicted_kf = Fraction(n**3-n,6)-gain_scaled/n
            assert value==det and actual_kf==predicted_kf,(n,pair,actual_kf,predicted_kf)
        print('n=%d: %d configurations, D optimum %d (%d sets), A optimum (%d sets), matches=%s'
              %(n,count,best_d,len(D),len(A),A==D))
    assert total==13104,total
    d, a, D, A = results[15]
    assert D == [((0,9),(4,14)),((0,10),(4,14)),((0,10),(5,14))]
    assert A == [((0,9),(4,13)),((1,10),(5,14))]
    assert a == Fraction(5388)
    for pair in D:
        trees,kf=direct_kf_and_treecount(15,pair)
        assert (trees,kf)==(85,Fraction(3420,17))
    for pair in A:
        trees,kf=direct_kf_and_treecount(15,pair)
        assert (trees,kf)==(75,Fraction(1004,5))
    assert Fraction(3420,17)-Fraction(1004,5)==Fraction(32,85)
    print('PASS: 13,104 exhaustive candidate pairs, n=4..15; sharp first disagreement at n=15.')
    print('PASS: independent exact grounded-Laplacian determinant/inverse replay on extremizers.')

if __name__ == '__main__':
    main()

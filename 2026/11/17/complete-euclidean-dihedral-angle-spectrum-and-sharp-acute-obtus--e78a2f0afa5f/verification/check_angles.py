#!/usr/bin/env python3
"""Exact finite checks for cycle Laplacian-simplex ridge angles.

Requires SymPy. These computations corroborate the separate all-n proof.
"""
import math
import sympy as sp


def exact_check(n):
    L = sp.zeros(n)
    for i in range(n):
        L[i, i] = 2
        L[i, (i-1) % n] -= 1
        L[i, (i+1) % n] -= 1
    J = sp.ones(n, n)/n
    W = (L+J).inv()-J  # independently computed rational pseudoinverse
    assert L*W == sp.eye(n)-J
    assert W*sp.ones(n, 1) == sp.zeros(n, 1)
    G = W.T*W
    D = (n*n-1)*(n*n+11)
    diag = sp.Rational(D, 720*n)
    assert G[0, 0] == diag
    for i in range(n):
        for j in range(n):
            d = min((i-j) % n, (j-i) % n)
            u = d*(n-d)
            expected = diag*(1-sp.Rational(30*u*(u+2), D))
            assert G[i, j] == expected, (n, i, j, G[i,j], expected)
    # Completely independent direct facet-normal solve from vertex coordinates:
    # n_i . (L e_j) = -1/n for j != i, 1 . n_i = 0.
    for i in range(n):
        A = sp.Matrix.vstack(*[L[:, j].T for j in range(n) if j != i], sp.ones(1, n))
        b = sp.Matrix([sp.Rational(-1,n)]*(n-1)+[0])
        normal = A.inv()*b
        assert normal == W[:, i]
        assert sum(normal[k]*L[k, i] for k in range(n)) == sp.Rational(n-1,n)
    return n*(n-1)//2


def cutoff(n):
    D = (n*n-1)*(n*n+11)
    num_obtuse = num_right = num_acute = 0
    for i in range(n):
        for j in range(i+1,n):
            d = min(j-i,n-(j-i))
            u = d*(n-d)
            sign = D-30*u*(u+2)
            if sign > 0: num_obtuse += 1
            elif sign < 0: num_acute += 1
            else: num_right += 1
    return num_obtuse, num_right, num_acute


def main():
    count = 0
    for n in range(3, 12):
        count += exact_check(n)
        obt, right, acute = cutoff(n)
        assert obt+right+acute == n*(n-1)//2
        assert (obt > 0) == (n >= 5)
        assert acute > 0
        # n unordered facets yield n ridge pairs per distance,
        # except antipodal pairs when n is even.
        assert sum(n if 2*d<n else n//2 for d in range(1,n//2+1)) == n*(n-1)//2
    tstar = (1-math.sqrt(1-4/math.sqrt(30)))/2
    assert 0.240 < tstar < 0.241
    for n in (50, 101, 300, 1000):
        obt, right, acute = cutoff(n)
        assert abs(obt/(n*(n-1)/2) - 2*tstar) < 0.04
        assert obt+right+acute == n*(n-1)//2
    print(f'CYCLE_LAPLACIAN_DIHEDRAL_PASS exact_n=3..11 facet_pairs={count} direct_normals=yes large_n=50,101,300,1000')


if __name__ == '__main__': main()

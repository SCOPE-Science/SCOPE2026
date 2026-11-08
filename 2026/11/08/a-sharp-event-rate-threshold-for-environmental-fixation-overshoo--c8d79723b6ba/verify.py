#!/usr/bin/env python3
"""Exact-rational checks for a reciprocal two-environment fixation theorem.

Uses only Python's standard library. Finite tests supplement the analytic proof.
"""
from fractions import Fraction as F
from itertools import product


def solve(A, b):
    a = [[F(v) for v in row] + [F(bi)] for row, bi in zip(A, b)]
    n = len(a)
    for k in range(n):
        pivot = next(i for i in range(k, n) if a[i][k] != 0)
        a[k], a[pivot] = a[pivot], a[k]
        scale = a[k][k]
        for j in range(k, n + 1):
            a[k][j] /= scale
        for i in range(n):
            if i == k:
                continue
            m = a[i][k]
            for j in range(k, n + 1):
                a[i][j] -= m * a[k][j]
    return [row[-1] for row in a]


def direct(a, c, d, k):
    up1 = [c*a/(a+1), c/(a+1)]
    down1 = [c/(a+1), c*a/(a+1)]
    up2 = [d/(a*a+1), d*a*a/(a*a+1)]
    down2 = [d*a*a/(a*a+1), d/(a*a+1)]
    mat = [[F(0) for _ in range(4)] for _ in range(4)]
    rhs = [F(0)]*4
    for i in (1, 2):
        for e in (0, 1):
            z = (i-1)*2+e
            up = (up1 if i == 1 else up2)[e]
            down = (down1 if i == 1 else down2)[e]
            mat[z][z] = up+down+k
            mat[z][(i-1)*2+(1-e)] -= k
            if i == 1:
                mat[z][2+e] -= up
            else:
                mat[z][e] -= down
                rhs[z] = up
    h = solve(mat, rhs)
    return (h[0]+h[1])/2


def formula(a, c, d, k):
    A = a*a+a+1
    H = (a+1)*(a*a+1)
    G = (a+1)*H
    D = 3*H*H*k*k+(c+d)*(a+1)*A*H*k+a*A*A*c*d
    return a/A+(a-1)**2*G*k*(c*A+2*(a*a+1)*k)/(2*A*D)


def gap(a, c, d, k):
    A = a*a+a+1
    H = (a+1)*(a*a+1)
    G = (a+1)*H
    D = 3*H*H*k*k+(c+d)*(a+1)*A*H*k+a*A*A*c*d
    return (a-1)**2*(G*(c-2*d)*k-2*a*A*c*d)/(6*D)


def derivative_sign(a, c, d, k):
    A = a*a+a+1
    H = (a+1)*(a*a+1)
    return A*H*H*(2*d-c)*k*k+4*a*(a*a+1)*A*A*c*d*k+a*A**3*c*c*d


def main():
    values_a=[F(1,3),F(1,2),F(2,3),F(1),F(3,2),F(2),F(3)]
    values_c=[F(1,4),F(1),F(3),F(7)]
    values_d=[F(1,3),F(1),F(2),F(5)]
    values_k=[F(0),F(1,10),F(1,2),F(1),F(2),F(5),F(10)]
    assertions=0
    for a,c,d,k in product(values_a,values_c,values_d,values_k):
        f=direct(a,c,d,k)
        assert f == formula(a,c,d,k)
        assertions+=1
        assert f-F(1,3)==gap(a,c,d,k)
        assertions+=1
        assert (F(0)<=f<=F(1))
        assertions+=1
        if a!=1 and k>0:
            assert f>a/(a*a+a+1)
            assertions+=1
        if a!=1 and c<=2*d and k>0:
            assert f<F(1,3)
            assertions+=1
        if a!=1 and c>2*d and k>0:
            k0=2*a*(a*a+a+1)*c*d/((a+1)**2*(a*a+1)*(c-2*d))
            assert (f>F(1,3)) == (k>k0)
            assertions+=1
        if a!=1 and k>0 and c<=2*d:
            assert derivative_sign(a,c,d,k)>0
            assertions+=1
    # Independent exact example in the overshoot regime.
    a,c,d=F(2),F(3),F(1)
    assert direct(a,c,d,F(0))==F(2,7);assert direct(a,c,d,F(1))==F(491,1486)
    assertions+=2
    assert gap(a,c,d,F(28,15))==0
    assertions+=1
    assert derivative_sign(a,c,d,F(4))>0 and derivative_sign(a,c,d,F(5))<0
    assertions+=2
    # For one transient count, conditional chance of fixation is a convex average.
    for u0,d0,u1,d1 in product([F(1,3),F(1),F(3)],[F(1,2),F(2)],[F(1,4),F(2)],[F(1,2),F(4)]):
        for k in [F(0),F(1,3),F(3)]:
            X=solve([[u0+d0+k,-k],[-k,u1+d1+k]],[u0,u1])
            lo=min(u0/(u0+d0),u1/(u1+d1))
            hi=max(u0/(u0+d0),u1/(u1+d1))
            assert lo<=X[0]<=hi and lo<=X[1]<=hi
            assertions+=1
    print(f'PASS: {assertions} exact-rational assertions')

if __name__=='__main__':
    main()

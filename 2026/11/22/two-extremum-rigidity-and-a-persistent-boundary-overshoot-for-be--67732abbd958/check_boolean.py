#!/usr/bin/env python3
"""Reproducible checks of Bernstein Boolean-sum step-response identities.

Only Python's standard library is needed. Finite tests support, not replace,
the analytical proof for every degree.
"""
from fractions import Fraction as F
from math import comb, exp, log, e


def q(n, j, k):
    p = F(k, n)
    return sum(F(comb(n, ell)) * p**ell * (1-p)**(n-ell)
               for ell in range(j, n+1))


def coeff(n, j):
    return [F(2 if k >= j else 0) - q(n, j, k)
            for k in range(n+1)]


def deriv_coeff(n, j):
    a = coeff(n, j)
    return [a[k+1]-a[k] for k in range(n)]


def bernstein_eval(a, x):
    n = len(a)-1
    if x == 1:
        return float(a[-1])
    if x == 0:
        return float(a[0])
    weight = (1-x)**n
    out = float(a[0])*weight
    ratio = x/(1-x)
    for k in range(1, n+1):
        weight *= (n-k+1)/k * ratio
        out += float(a[k])*weight
    return out


def root_of_derivative(n, j, left, right, increasing):
    dc = deriv_coeff(n, j)
    # root where derivative changes from positive to negative (or vice versa)
    fleft = bernstein_eval(dc, left)
    fright = bernstein_eval(dc, right)
    assert fleft * fright < 0, (n,j,left,right,fleft,fright)
    for _ in range(90):
        mid = (left+right)/2
        fm = bernstein_eval(dc, mid)
        if (fm > 0) == (fleft > 0):
            left = mid
        else:
            right = mid
    return (left+right)/2


def check_exact_coefficients():
    for n in range(2, 17):
        for j in range(1, n+1):
            a = coeff(n, j)
            dc = deriv_coeff(n, j)
            assert a[0] == 0 and a[-1] == 1
            assert all(dc[k] > 0 if k == j-1 else dc[k] < 0
                       for k in range(n))
    assert coeff(2,1) == [F(0),F(5,4),F(1)]
    assert coeff(3,2) == [F(0),-F(7,27),F(34,27),F(1)]
    print('EXACT_BERNSTEIN_STEP_DERIVATIVE_SIGN_PATTERNS_PASS n=2..16')
    print('EXACT_TWO_AND_THREE_DEGREE_COEFFICIENTS_PASS')


def check_boundary_layer():
    aa = 1-exp(-1)
    u_star = e*log(2/aa)
    target = 1+2/e*(aa/2)**(e-1)
    vals=[]
    for n in (20, 50, 100, 200):
        # For j=1, the derivative has exactly one root and signs +,-.
        x = root_of_derivative(n,1, 0, 0.2, True)
        G = bernstein_eval(coeff(n,1),x)
        K = 2*G-1
        vals.append((n,n*x,K))
        assert K > 1
    # Boundary-layer numerics have a slow first-order correction.
    assert abs(vals[-1][2]-target) < 0.006
    assert abs(vals[-1][1]-u_star) < 0.35
    print('BOUNDARY_LAYER_FINITE_CHECKS_PASS',
          [(n,round(u,8),round(k,9)) for n,u,k in vals])
    print('LIMITING_LOCATION_AND_NORM',round(u_star,12),round(target,12))


def check_step_variation():
    for n in range(2, 11):
        for j in range(1, n+1):
            a = coeff(n,j)
            dc = deriv_coeff(n,j)
            grid = 150
            roots=[]
            for m in range(grid):
                lo,hi=m/grid,(m+1)/grid
                if bernstein_eval(dc,lo)*bernstein_eval(dc,hi)<0:
                    roots.append(root_of_derivative(n,j,lo,hi,False))
            # Root count is proved by Descartes in the accompanying proof.
            assert len(roots) == (1 if j in (1,n) else 2), (n,j,roots)
            vals=[bernstein_eval(a,z) for z in [0,*roots,1]]
            variation=sum(abs(v-w) for v,w in zip(vals[:-1],vals[1:]))
            assert abs(variation-(2*(max(vals)-min(vals))-1))<1e-9
            assert variation > 1
    print('NUMERIC_STEP_EXTREMA_AND_VARIATION_IDENTITIES_PASS n=2..10')

if __name__ == '__main__':
    check_exact_coefficients()
    check_step_variation()
    check_boundary_layer()
    print('ALL_BERNSTEIN_BOOLEAN_SUM_CHECKS_PASS')

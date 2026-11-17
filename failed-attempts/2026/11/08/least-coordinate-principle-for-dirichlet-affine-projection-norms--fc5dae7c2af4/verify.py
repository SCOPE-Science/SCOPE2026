#!/usr/bin/env python3
"""Exact rational checks for first-degree Dirichlet projection kernels.

Only finite parameter instances are tested; the theorem uses an analytic proof.
"""
from fractions import Fraction as F
from math import factorial, comb


def beta_tail(a, b, t):
    assert isinstance(t, F) and 0 < t < 1
    n = a + b - 1
    return sum((F(comb(n, j)) * t**j * (1-t)**(n-j) for j in range(a, n+1)), F(0))


def negative_mass_cdf(a, b):
    A = a + b
    t = F(a, A+1)
    return A*beta_tail(a, b, t) - (A+1)*beta_tail(a+1, b, t)


def negative_mass_integral(a, b):
    A = a + b
    t = F(a, A+1)
    inv_beta = F(factorial(A-1), factorial(a-1)*factorial(b-1))
    total = F(0)
    for j in range(b):
        coef = (-1)**j * comb(b-1, j)
        m = a+j
        total += coef * (t**m/F(m) - F(A+1, a)*t**(m+1)/F(m+1))
    return A*inv_beta*total


def dirichlet_moment(alpha, i, j):
    A = sum(alpha)
    return F(alpha[i]*(alpha[j] + (i == j)), A*(A+1))


def kernel_at(x, y, alpha):
    A = sum(alpha)
    return (A+1)*sum((F(A*x[i]*y[i], alpha[i]) for i in range(len(alpha))), F(0))-A


def test():
    count = 0
    for A in range(3, 25):
        last = None
        for a in range(1, A):
            b = A-a
            c1 = negative_mass_cdf(a,b)
            c2 = negative_mass_integral(a,b)
            assert c1 == c2, (a,b,c1,c2)
            assert 0 < c1 < A
            if last is not None:
                assert last > c1, (A,a,last,c1)
            last = c1
            count += 1
    print('EXACT_BETA_INTEGRAL_AND_STRICT_ORDER_OK',count)

    for alpha in [(1,1),(1,1,1),(1,2,3),(2,3,4,1),(4,5,2,7)]:
        d=len(alpha)
        A=sum(alpha)
        x=[F(i+1,sum(range(1,d+1))) for i in range(d)]
        # E[K(x,Y)] = 1, E[K(x,Y)Y_j] = x_j: reproduces each affine coordinate.
        for j in range(d):
            E_KY = (A+1)*sum((F(A*x[i],alpha[i])*dirichlet_moment(alpha,i,j) for i in range(d)), F(0))-F(alpha[j])
            assert E_KY == x[j], (alpha,j,E_KY,x[j])
        assert kernel_at(x,[F(v,A) for v in alpha],alpha) == 1
        for i in range(d):
            e=[F(k==i) for k in range(d)]
            for j in range(d):
                f=[F(k==j) for k in range(d)]
                assert kernel_at(e,f,alpha) == (F(A*(A+1),alpha[i])-A if i==j else -A)
    print('EXACT_DIRICHLET_AFFINE_REPRODUCTION_OK',5)

    for m in range(2,14):
        A=m
        c=negative_mass_cdf(1,A-1)
        expected=F(m)*(F(m,m+1)**(m-1))-1
        assert c==expected, (m,c,expected)
    print('UNIFORM_SIMPLEX_RECOVERY_OK',12)

    for A in range(3,25):
        vals=[1+2*negative_mass_cdf(a,A-a) for a in range(1,A)]
        assert vals==sorted(vals,reverse=True)
    print('ALL_DIRICHLET_AFFINE_CHECKS_OK')

if __name__=='__main__':
    test()

#!/usr/bin/env python3
"""Independent finite diagnostics for the trace-zero two-by-two Cartesian-radius formula.

Only the Python standard library is required. This is not a proof for general p.
"""
from fractions import Fraction as Q
from math import comb, factorial, pi, sin, cos, sqrt, isclose


def even_moment(r, s):
    """Average of cos(theta)^(2r) sin(theta)^(2s), exactly."""
    return Q(factorial(2*r) * factorial(2*s), 4**(r+s) * factorial(r) * factorial(s) * factorial(r+s))


def power_moment_direct(a, b, c, m):
    # a*cos^2 + b*sin^2 + 2*c*cos*sin, raised to integer m.
    out = Q(0)
    for i in range(m+1):
        for j in range(m-i+1):
            k = m-i-j
            if k % 2:
                continue
            coefficient = Q(factorial(m), factorial(i)*factorial(j)*factorial(k))
            out += coefficient*a**i*b**j*(2*c)**k*even_moment(i+k//2, j+k//2)
    return out


def power_moment_invariant(a, b, c, m):
    q = (a+b)/2
    rho2 = ((a-b)**2 + 4*c*c)/(a+b)**2
    series = Q(0)
    for k in range(m//2+1):
        j = 2*k
        series += Q(comb(m,j)*comb(2*k,k),4**k) * rho2**k
    return q**m*series


def dot(u, v):
    return sum((x*y for x,y in zip(u,v)), Q(0))


def test_exact():
    checks = 0
    for seed in range(1, 65):
        u = tuple(Q(((seed*(k+3)*7+k*k)%19)-9, k+2) for k in range(3))
        v = tuple(Q(((seed*(k+5)*11+2*k*k)%23)-11, k+4) for k in range(3))
        a,b,c = dot(u,u), dot(v,v), dot(u,v)
        assert a+b > 0
        assert (a-b)**2+4*c*c <= (a+b)**2
        checks += 2
        for m in range(1,6):
            assert power_moment_direct(a,b,c,m)==power_moment_invariant(a,b,c,m), (seed,m)
            checks += 1
        if m == 5:
            # The exact p=4 specialization in the finding.
            exact = power_moment_direct(a,b,c,2)
            F2 = 2*(a+b)
            detmod2 = (a-b)**2 + 4*c*c
            assert exact == F2**2/Q(16)+detmod2/Q(8)
            checks += 1
    return checks


def test_numeric():
    checks=0
    vectors = [((1.,2.,3.),(3.,1.,-2.)),((1.,0.,0.),(0.,1.,0.)),
               ((2.,-1.,3.),(1.,4.,-2.)),((2.,0.,0.),(1.,0.,0.)),
               ((3.,1.,1.),(2.,-1.,2.)), ((1.,0.,0.),(0.,0.,0.))]
    n=8192
    for u,v in vectors:
        a=sum(x*x for x in u);b=sum(x*x for x in v);c=sum(x*y for x,y in zip(u,v))
        rho=sqrt((a-b)**2+4*c*c)/(a+b)
        scale=sqrt((a+b)/2)
        for p in (1,3,5,7):
            actual = 0.
            formula= 0.
            for j in range(n):
                t=2*pi*j/n
                x=tuple(uu*cos(t)+vv*sin(t) for uu,vv in zip(u,v))
                actual += sum(z*z for z in x)**(p/2)
                formula += (1+rho*cos(2*t))**(p/2)
            actual=(actual/n)**(1/p)
            formula=scale*(formula/n)**(1/p)
            # For rho near one the trapezoidal error is still sub-1e-5 at 8192 samples.
            assert isclose(actual, formula, rel_tol=1e-6, abs_tol=1e-6), (u,v,p,actual,formula)
            checks+=1
    return checks

if __name__=='__main__':
    a=test_exact(); b=test_numeric()
    print(f'PASS: {a} exact rational tests and {b} numerical angular-integral tests')
    print('These finite checks do not certify the infinite p range.')

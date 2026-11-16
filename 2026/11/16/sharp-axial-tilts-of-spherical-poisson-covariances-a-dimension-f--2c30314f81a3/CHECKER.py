#!/usr/bin/env python3
"""Finite corroborative checks for sharp axial Poisson covariance formulas.
The analytic proof in RESULT.md, not these finite checks, covers all degrees.
Requires only the Python 3 standard library.
"""
import math
from fractions import Fraction as F


def add(a, b, scale=F(1)):
    c = a[:]
    if len(c) < len(b):
        c.extend([F(0)] * (len(b)-len(c)))
    for j, v in enumerate(b):
        c[j] += scale * v
    return c


def mult_x(a):
    return [F(0)] + a


def equal_polynomials(a, b):
    a = a + [F(0)] * max(0, len(b)-len(a))
    b = b + [F(0)] * max(0, len(a)-len(b))
    return a == b


def legendre_polys(N):
    out = [[F(1)], [F(0), F(1)]]
    for k in range(1, N):
        p = add(mult_x(out[k]), out[k-1], scale=-F(k, 2*k+1))
        p = [u * F(2*k+1, k+1) for u in p]
        out.append(p)
    return out[:N+1]


def gaussian_nodes(N):
    """Legendre nodes/weights on [-1,1] by Newton + exact derivative identity."""
    result = []
    for i in range(1, N+1):
        x = math.cos(math.pi*(i-0.25)/(N+0.5))
        for j in range(100):
            p0, p1 = 1.0, x
            for n in range(2, N+1):
                p0, p1 = p1, ((2*n-1)*x*p1-(n-1)*p0)/n
            pn, pm = (1.0, 0.0) if N == 0 else (p1, p0)
            dp = N*(x*pn-pm)/(x*x-1.0)
            newx = x-pn/dp
            if abs(newx-x)<3e-15:
                x=newx
                break
            x = newx
        weight = 2/((1-x*x)*dp*dp)
        result.append((x, weight))
    result.sort()
    return result


def dot(a,b):
    return sum(x*y for x,y in zip(a,b))


def spherical_poisson(r, a, b):
    return (1-r*r)/(1-2*r*dot(a,b)+r*r)**1.5


def factorization_tests():
    nodes=gaussian_nodes(64)
    x=(0.2,0.6,math.sqrt(0.60))
    y=(0.5,-0.4,math.sqrt(0.59))
    tests=0
    for r, theta in ((0.16,-1.0),(0.25,0.0),(0.36,0.75),(0.36,1.0)):
        q=math.sqrt(r)
        epsilon=theta*math.sqrt(r)/(1+r)
        approx=0.0
        for t,weight in nodes:
            sr=math.sqrt(max(0.0, 1-t*t))
            for k in range(128):
                p=2*math.pi*k/128
                z=(sr*math.cos(p),sr*math.sin(p),t)
                approx+=weight/(2*128)*(1+theta*t)*spherical_poisson(q,x,z)*spherical_poisson(q,z,y)
        exact=spherical_poisson(r,x,y)*(1+epsilon*(x[2]+y[2]))
        assert abs(exact-approx) < 3e-10, (r,theta,approx,exact)
        tests+=1
    return tests


def exact_tests():
    polys=legendre_polys(15)
    # Multiplication by latitude only couples adjacent spherical degrees:
    for k in range(1,14):
        rhs=add([v*F(k+1,2*k+1) for v in polys[k+1]],
                [v*F(k,2*k+1) for v in polys[k-1]])
        assert equal_polynomials(mult_x(polys[k]), rhs)
    # The zonal compressed Jacobi characteristic polynomial is monic Legendre.
    # Jacobi recurrence: det(xI-J_n)=x det(xI-J_{n-1}) - b_{n-1}^2 det(xI-J_{n-2}).
    D0=[F(1)]
    D1=[F(0),F(1)]
    for n in range(1,13):
        b2=F(n*n,(2*n-1)*(2*n+1))
        D2=add(mult_x(D1),D0,-b2)
        monic=[v / polys[n+1][-1] for v in polys[n+1]]
        assert equal_polynomials(D2,monic),(n,D2,monic)
        D0,D1=D1,D2
    # Exact supercritical S^2 witness at r=1/4, epsilon=9/20,
    # theta=9/8; g(t)=(1-t)^9 yields expectation -1/80.
    theta=F(9,8); m=9
    assert F(1)-theta*F(m,m+1)==-F(1,80)
    assert F(1)-2*F(9,20)==F(1,10)
    # Another exact witness theta=6/5,m=6.
    assert F(1)-F(6,5)*F(6,7)==-F(1,35)
    return 13+12+3

if __name__=='__main__':
    a=exact_tests()
    b=factorization_tests()
    print('PASS: %d rational Legendre/Jacobi/witness checks; %d Poisson factorization quadratures'%(a,b))

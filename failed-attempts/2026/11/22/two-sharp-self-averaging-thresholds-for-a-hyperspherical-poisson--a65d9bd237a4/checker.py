"""Reproducibility checks for the spherical Poisson-kernel self-averaging theorem.

Checks finite-dimensional exact kernel moment identities via numerical quadrature
and elementary algebraic and variational identities. The infinite-dimensional
probability statements require the mathematical proof and are not certified by
these numerical checks.
"""
from math import exp, log, sqrt, pi, isclose
import numpy as np
from scipy.special import roots_jacobi


def critical(r):
    return -0.25 * log(1-r*r)


def I(s):
    return -0.5*log(1-s*s)


def f(s, r):
    return -0.5*log(1+r*r-2*r*s)


def free(s, r):
    return f(s, r)-I(s)


def max_pair_inner(a):
    return sqrt(1-exp(-4*a))


def quadrature_moment(d, r, power, order=640):
    a=(d-3)/2
    nodes, weights=roots_jacobi(order, a, a)
    v=(1-r*r)/(1+r*r-2*r*nodes)**(d/2)
    return float(np.dot(weights, v**power)/sum(weights))


def run():
    checks=0
    for r in (0.2, 0.5, 0.75):
        for d in (2, 3, 5, 8, 12, 20):
            mean=quadrature_moment(d,r,1)
            second=quadrature_moment(d,r,2)
            theoretical=(1+r*r)/(1-r*r)**(d-1)
            assert abs(mean-1)<4e-9, (r,d,mean)
            assert abs(second/theoretical-1)<4e-9, (r,d,second,theoretical)
            checks+=2
    for r in (0.15,0.35,0.55,0.75,0.95):
        a=critical(r)
        a2=2*a
        assert a>0 and a2>a
        checks+=1
        assert isclose(I(r),2*a,rel_tol=1e-12)
        checks+=1
        for s in np.linspace(-0.99,0.99,199):
            lhs=(1+r*r-2*r*s)-(1-s*s)
            assert isclose(lhs,(s-r)**2,abs_tol=1e-12)
            assert free(float(s),r)<=1e-12
            checks+=2
        for fraction in (0.15,0.4,0.75,0.99):
            af=fraction*a
            t=max_pair_inner(af)
            assert t<r and free(t,r)<0
            assert isclose(I(t),2*af,rel_tol=1e-12)
            checks+=3
        for s in np.linspace(-0.9,0.99,90):
            s=float(s)
            derivative=(r-s)*(1-r*s)/((1-s*s)*(1+r*r-2*r*s))
            dx=1e-6
            finite=(free(s+dx,r)-free(s-dx,r))/(2*dx)
            assert abs(derivative-finite)<5e-7, (s,r,derivative,finite)
            checks+=1
        for fraction in (1.05,1.5,2.5,4):
            above=fraction*a
            b=r+(1-r)*min(.001,.001*(above/a-1))
            # This is strictly above rho, and local squared-moment rate is below 2alpha.
            vals=np.linspace(-0.999,b,20000)
            J=max(2*f(float(s),r)-I(float(s)) for s in vals)
            assert J<2*above,(r,above,b,J)
            checks+=1
    print('Passed',checks,'analytical and quadrature assertions')
    print('rho=0.5: alpha_c=',critical(.5),' alpha_2=',2*critical(.5))
    print('alpha=0.05: t=',max_pair_inner(.05),' L=',free(max_pair_inner(.05),.5))


if __name__=='__main__':
    run()

#!/usr/bin/env python3
"""Numerical reproduction of the sharp spectral-envelope constants.
The infinite-parameter theorem is established by the accompanying proof,
not by these finitely many numerical checks. Requires only Python stdlib.
"""
from math import exp, erf, sqrt, pi, isclose


def d(s):
    return (s**3+s/2)*exp(-s*s)-sqrt(pi)*erf(s)/4


def simpson(f, a=0., b=1., n=16384):
    assert n > 0 and n % 2 == 0
    h=(b-a)/n
    z=f(a)+f(b)
    for j in range(1,n):
        z+=(4 if j&1 else 2)*f(a+j*h)
    return z*h/3


def M(alpha):
    return 1. if alpha<=2 else sqrt(2/alpha)*exp(alpha/4-.5)


def G(u,alpha):
    return (1-2*u)*exp(alpha*u*(1-u))


def I(alpha):
    return simpson(lambda u:G(u,alpha)**2)

lo,hi=1.,2.
assert d(lo)>0 and d(hi)<0
for _ in range(110):
    mid=(lo+hi)/2
    if d(mid)>0:lo=mid
    else:hi=mid
s=(lo+hi)/2
alpha=2*s*s
m=exp(1)*s*s*exp(-s*s)
delta=exp(1-alpha/2)/(2*alpha)
assert 1.51121855<s<1.51121857
assert 4.56756304<alpha<4.56756306
assert 0.63257980<m<0.63257982
assert isclose(I(alpha)/(M(alpha)**2),m,rel_tol=1e-10)
assert isclose(delta*alpha**2*M(alpha)**2,1,rel_tol=1e-13)

for a in [-12.,-3.,-0.1,0.,.1,1.2,1.999,2.,2.001,3.,alpha,5.,9.,18.]:
    mm=M(a)
    integral=I(a)
    beta=integral/mm**2
    assert 0<beta<1
    if a<=2:
        want=simpson(lambda x:x*x*exp(a*(1-x*x)/2))
    else:
        t=sqrt(a/2)
        want=exp(1)/t*(sqrt(pi)*erf(t)/4-t*exp(-t*t)/2)
    assert isclose(beta,want,rel_tol=2e-10,abs_tol=2e-10)
    assert beta <= m+1e-10
    if abs(a)>0.001:
        eta=1/(a*a*mm*mm)
        for sign in [-1,1]:
            coupling=sign*eta*a*a
            assert isclose(abs(coupling)*mm*mm,1,rel_tol=2e-12)
            for u in [i/20 for i in range(21)]:
                for v in [i/20 for i in range(21)]:
                    assert 1+coupling*G(u,a)*G(v,a)>=-1e-12
            # Chapman-Kolmogorov at two steps, using quadrature
            u,v=.26,.68
            p1=lambda x,y:1+coupling*G(x,a)*G(y,a)
            two=simpson(lambda w:p1(u,w)*p1(w,v))
            expected=1+(coupling**2)*integral*G(u,a)*G(v,a)
            assert isclose(two,expected,rel_tol=2e-10,abs_tol=2e-10)
            # n-step coefficient, and the supremum at a signed extremizer
            for n in [1,2,3,5]:
                coeff=coupling**n*integral**(n-1)
                bound=m**(n-1)
                assert abs(coeff)*mm**2<=bound+1e-10

for a in [alpha-.5,alpha-.2,alpha-.01,alpha+.01,alpha+.2,alpha+.5]:
    assert I(a)/M(a)**2<m

print('PASS: unique-root bracketing, analytic-integral agreement,')
print('admissible density grids, Chapman-Kolmogorov quadrature,')
print('and sharp parameter envelope probes')
print('s* = %.15f' % s)
print('alpha* = %.15f' % alpha)
print('m* = %.15f' % m)
print('absolute delta* = %.15f' % delta)

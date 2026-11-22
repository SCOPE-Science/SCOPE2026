#!/usr/bin/env python3
"""Independent numerical/algebraic checks for a reflecting–absorbing diffusion theorem.
Uses the Python standard library only. Numerical checks supplement the written proof.
"""
from fractions import Fraction as F
from math import pi, gamma, sqrt, cosh, exp


def hyper0f1(b, t):
    # Direct convergent series for _0F_1(;b;t).
    acc = term = 1.0
    for n in range(1, 5000):
        term *= t / (n * (b + n - 1))
        acc += term
        if abs(term) < 1.e-15 * abs(acc):
            return acc
    raise RuntimeError('slow hypergeometric convergence')


def normalized_bessel_j_minus_third(z):
    # Positive prefactor times J_{-1/3}(z); only the sign/zero matters.
    return hyper0f1(2.0/3.0, -z*z/4.0)


def root():
    a, b = 1.72, 1.90
    assert normalized_bessel_j_minus_third(a) > 0
    assert normalized_bessel_j_minus_third(b) < 0
    for _ in range(65):
        c = (a+b)/2.0
        if normalized_bessel_j_minus_third(c)>0: a=c
        else: b=c
    return (a+b)/2


def ode_end(lam, delta, steps=2500):
    # Solve phi'' + lam/D(x) phi=0 with phi(0)=1, phi'(0)=0.
    integral = (2.0/3.0)*((1.0+delta)**1.5 - delta**1.5)
    C = 1.0/integral
    def f(x, y, v): return v, -lam*y/(C*sqrt(1.0-x+delta))
    h=1.0/steps
    y=1.0; v=0.0
    for k in range(steps):
        x=k*h
        a,b=f(x,y,v)
        c,d=f(x+h/2, y+h*a/2,v+h*b/2)
        e,g=f(x+h/2, y+h*c/2,v+h*d/2)
        j,l=f(x+h, y+h*e,v+h*g)
        y+=h*(a+2*c+2*e+j)/6
        v+=h*(b+2*d+2*g+l)/6
    return y


def shooting_root(delta):
    a,b=2.0,3.4
    assert ode_end(a,delta)>0 and ode_end(b,delta)<0
    for _ in range(35):
        c=(a+b)/2
        if ode_end(c,delta)>0:a=c
        else:b=c
    return (a+b)/2


def main():
    # Exact moments from reciprocal 0F1 Taylor series.
    c = F(8,27)
    b = F(2,3)
    m1=c/b
    m2=2*(c/b)**2 - c*c/(b*(b+1))
    var=m2-m1*m1
    assert m1==F(4,9)
    assert m2==F(128,405)
    assert var==F(16,135)
    assert var/m1**2==F(3,5)
    assert F(5,12)-F(1,4)==F(1,6)
    assert F(4,9)<F(1,2) and F(16,135)<F(1,6)

    t=(F(43,50))**2
    lower = 1 - F(3,2)*t + F(9,20)*t**2 - F(9,160)*t**3
    assert lower>F(11,100)
    assert F(27,32)*F(43,25)**2 > F(121,49)
    assert pi < 22/7
    j=root()
    eig=27*j*j/32
    assert 1.86<j<1.87
    assert eig>pi*pi/4

    for s in [1e-3,.01,.1,1.,10.,100.]:
        lap=1.0/hyper0f1(2.0/3.0, 8.0*s/27.0)
        hom=1.0/cosh(sqrt(s))
        if s<=10.: assert lap>hom
        else: assert lap<hom

    # Varadhan short-arrival action and normalized smooth regularizations.
    action=4.0/3.0*sqrt(2.0/3.0)
    assert abs(action**2-F(32,27))<1e-14
    assert F(8,27)>F(1,4)
    assert F(8,27)-F(1,4)==F(5,108)
    delta=1e-4
    integral=(2.0/3.0)*((1+delta)**1.5-delta**1.5)
    C=1/integral
    action_delta=(4.0/3.0)*((1+delta)**.75-delta**.75)/sqrt(C)
    # Early-arrival penalty, mean improvement and later-survival advantage persist.
    y1=1+delta
    mean_delta=((2.0/3.0)*(y1**1.5-delta**1.5)-2*delta*(sqrt(y1)-sqrt(delta)))/C
    eig_delta=shooting_root(delta)
    assert action_delta>1.0
    assert mean_delta<.5
    assert eig_delta>pi*pi/4
    print('PASS: exact moments, Bessel-root bracket, Laplace transform ordering at sample points,')
    print('      short-time action, principal eigenvalue, and positive regularization.')
    print('j[-1/3,1]=%.12f; lambda_star/D0=%.12f; lambda_hom/D0=%.12f' % (j,eig,pi*pi/4))
    print('regularization delta=%g: action=%.9f; mean=%.9f; lambda=%.9f' % (delta,action_delta,mean_delta,eig_delta))
    print('All computations normalize length and baseline diffusivity to one.')

if __name__=='__main__':main()

"""Standard-library-only numerical cross-checks for a hyperbolic cusp excursion law.
The analytic proof, not these finite tests, establishes the asymptotic theorem.
Run: python check_cusp_overshoot.py
"""
from math import sqrt, isclose
import random


def arc_apex(a, b, z):
    xc = (z*z+b*b-a*a)/(2*z)
    rad = sqrt(a*a+xc*xc)
    return rad if 0 < xc < z else max(a,b)


def simpson_weights(n):
    assert n % 2 == 0
    return [1 if i == 0 or i == n else (4 if i % 2 else 2)
            for i in range(n+1)]


def exact_tail_numeric(width, H, n=240):
    L = width/2
    assert H > sqrt(1+L*L)
    weights=simpson_weights(n)
    h=1/n
    total=0.0
    for i in range(n+1):
        s=i*h
        u=L*s
        si=s*(1-s)**3/(1-(u/H)**2)**1.5
        row=0.0
        for j in range(n+1):
            t=j*h
            v=L*(1-s)*t
            row+=weights[j]*t*(1-t)/(1-(v/H)**2)**1.5
        total+=weights[i]*si*row
    return L**4/H**6 * total*(h/3)**2


def two_terms(width, H):
    return width**4/(1920*H**6)+width**6/(17920*H**8)


def test_geometry():
    rng=random.Random(20261113)
    count=0
    for _ in range(80000):
        H=2+rng.random()*10
        z=0.01+rng.random()*6
        a=H-rng.random()*min(1.5,z*z/H)
        b=H-rng.random()*min(1.5,z*z/H)
        if a<=0 or b<=0:
            continue
        condition=sqrt(H*H-a*a)+sqrt(H*H-b*b)<z
        assert condition == (arc_apex(a,b,z)>H)
        count+=1
    print('geometry_equivalence_checks',count)


def test_asymptotic():
    for width in (1.0,2.0,4.0):
        errors=[]
        for H in (5.,10.,20.):
            exact=exact_tail_numeric(width,H)
            approx=two_terms(width,H)
            relative=abs(exact-approx)/exact
            errors.append(relative)
            print('width',width,'height',H,'probability',f'{exact:.14g}',
                  'two_term_relative_error',f'{relative:.5g}')
        assert errors[0]>errors[1]>errors[2]
        assert errors[-1]<3e-5


def test_mark_normalization():
    # r=z/L is Beta(5,1); conditional (u/z,v/z,1-(u+v)/z)
    # is Dirichlet(2,2,1). The limiting density is 120*r**4*s*t.
    assert isclose((1/5)*(1/24)*120,1.,rel_tol=1e-14)
    # E[r^2]=5/7, E[s^2+t^2]=2/5; compare the H^-8 coefficient.
    assert isclose((1/1920)*(3/2)*(5/7)*(2/5)*(1/4),
                   1/17920,rel_tol=1e-14)
    print('beta_dirichlet_moments_OK')

if __name__=='__main__':
    test_geometry()
    test_asymptotic()
    test_mark_normalization()
    print('HYPERBOLIC_CUSP_OVERSHOOT_CHECKS_OK')

#!/usr/bin/env python3
"""Independent numerical and exact-arithmetic diagnostics for the finite-noise Gaussian coupling theorem.

Analytic proof in RESULT.md establishes the theorem; finite checks do not prove infinite statements.
Run: python3 verify.py
Python standard library only.
"""
from fractions import Fraction as F
from math import sqrt
import random

checks = 0


def check(cond, context):
    global checks
    assert cond, context
    checks += 1


def var_poly(k, a, b, rho):
    return ((a*a)*(1+(k-1)*rho) + 2*(b*b)*(1+(k-1)*rho*rho)) / k


def exact_check():
    for k in range(2, 12):
        for a in range(-6, 7):
            for b in range(-5, 6):
                if b == 0:
                    continue
                aa, bb = F(a), F(b)
                rho = max(F(-1, k-1), -aa*aa/(4*bb*bb))
                check(F(-1, k-1) <= rho <= 0, ('feasible',k,a,b))
                vopt=var_poly(k,aa,bb,rho)
                check(vopt <= var_poly(k,aa,bb,F(-1,k-1)), ('endpoint',k,a,b))
                check(vopt <= var_poly(k,aa,bb,F(0)), ('independent',k,a,b))
                for q in range(101):
                    rr=F(-1,k-1)+F(q,100)*(F(1)+F(1,k-1))
                    check(vopt<=var_poly(k,aa,bb,rr), ('grid',k,a,b,q))
    a=F(3,2)
    q=F(8)
    r=F(-9,64)
    check(r == -a*a/(2*q), 'CV minimum correlation')
    v=lambda x: (a*a*(1+x)+q*(1+x*x))/2
    check(v(r) == F(5167,1024), 'CV rational optimum')
    check(v(F(-1)) == F(8), 'CV full-antithetic')
    check(v(F(0)) == F(41,8), 'CV iid')
    check(v(r)<v(F(0))<v(F(-1)), 'CV strict superiority')


def simulate_finite_cv():
    # Two Gaussian draws with target correlation, conditioned on each independent Y.
    seed=543219
    rng=random.Random(seed)
    N=120000
    c=.5
    alpha=4.
    sig=1.
    mu=0.
    expected={-1.:8.,0.:5.125,-9/64:5167/1024}
    for rho, truth in expected.items():
        raw=[]
        for _ in range(N):
            y=rng.gauss(mu,sig)
            z1=rng.gauss(0,1)
            z2=rng.gauss(0,1)
            w1=sig*z1
            w2=sig*(rho*z1+sqrt(1-rho*rho)*z2)
            score=sum(((c*(y+sqrt(alpha)*w)-(y-w/sqrt(alpha)))**2-w*w/alpha) for w in (w1,w2))/2
            raw.append((score,y))
        # Mean conditional score as a function of Y, known without coupling:
        # (c-1)^2 Y^2 +(c^2 alpha+2 c) sigma^2.
        residuals=[sc - ((c-1)**2*y*y+(c*c*alpha+2*c)*sig*sig) for sc,y in raw]
        empirical=sum(v*v for v in residuals)/N
        check(abs(empirical-truth)<.15, ('Monte Carlo CV',rho,empirical,truth))
        check(abs(sum(residuals)/N)<.06, ('conditional means',rho))


def nonexchangeable_matrix_stress():
    rng=random.Random(92811)
    for k in (3,4,7):
        for _ in range(300):
            # Gram correlation matrix of independently drawn unit vectors.
            u=[]
            for i in range(k):
                v=[rng.gauss(0,1) for _ in range(k+2)]
                d=sqrt(sum(x*x for x in v));u.append([x/d for x in v])
            r=[[sum(x*y for x,y in zip(ui,uj)) for uj in u] for ui in u]
            a,b=rng.uniform(-3,3),rng.uniform(.05,3)
            exact=(a*a*sum(sum(ri) for ri in r)+2*b*b*sum(x*x for ri in r for x in ri))/k**2
            rho=max(-1/(k-1),-a*a/(4*b*b))
            opt=var_poly(k,a,b,rho)
            check(exact+1e-9>=opt, ('nonexchangeable PSD optimum',k,exact,opt))


if __name__=='__main__':
    exact_check()
    nonexchangeable_matrix_stress()
    simulate_finite_cv()
    print(f'PASS: {checks} checks, exact fractions + nonexchangeable PSD samples + direct Monte Carlo CV')

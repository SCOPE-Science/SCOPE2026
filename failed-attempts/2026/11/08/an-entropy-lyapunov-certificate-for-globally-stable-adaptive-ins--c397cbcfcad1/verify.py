#!/usr/bin/env python3
"""Independent algebraic spot checks for an exact entropy Lyapunov identity.

No finite test is used as a substitute for the all-parameter mathematical proof.
Run with: python verify.py
"""
from fractions import Fraction as Q
from random import Random
from math import log, exp


def s(n, x):
    return sum((1-x)**k for k in range(n))


def field(n, x, a, d, delta, alpha, beta, u, eps):
    return (x*(1-x)*(-d+delta*a*s(n,x))/eps,
            (a-alpha)*(beta-a)*(u-(1+u)*x))


def rhs(n, x, a, delta, xstar, eps):
    return delta*a*(x-xstar)*(s(n,x)-s(n,xstar))/eps


def kl(p, q):
    return p*log(p/q)+(1-p)*log((1-p)/(1-q))


def energy(n, x, a, delta, alpha, beta, u, eps, d):
    xs=u/(1+u)
    ast=d/(delta*s(n,xs))
    return kl(xs,x)+delta*s(n,xs)/(eps*(1+u))*kl((ast-alpha)/(beta-alpha), (a-alpha)/(beta-alpha))


def check():
    rng=Random(1729)
    cases=0
    for n in range(2, 18):
        for i in range(150):
            u=Q(rng.randint(1,20), rng.randint(1,10))
            xs=u/(1+u)
            delta=Q(rng.randint(1,15),rng.randint(1,20))
            alpha=Q(1,4)
            beta=Q(7,2)
            ast=alpha+(beta-alpha)*Q(rng.randint(1,19),20)
            d=delta*ast*s(n,xs)
            eps=Q(rng.randint(1,40),rng.randint(1,20))
            x=Q(rng.randint(1,99),100)
            a=alpha+(beta-alpha)*Q(rng.randint(1,99),100)
            xd,ad=field(n,x,a,d,delta,alpha,beta,u,eps)
            vx=(x-xs)/(x*(1-x))
            va=(delta*s(n,xs)/(eps*(1+u)))*(a-ast)/((a-alpha)*(beta-a))
            derivative=vx*xd+va*ad
            expected=rhs(n,x,a,delta,xs,eps)
            assert derivative==expected, (n,i,derivative,expected)
            assert expected<=0
            assert (expected==0)==(x==xs)
            cases+=1
    print('EXACT_RATIONAL_IDENTITY_OK',cases)

    # All components of the parameter-specific instance are literal rationals.
    n=5;u=Q(2);r=Q(3);c=Q(1);delta=Q(1,5)
    alpha=Q(1,2);beta=Q(3);eps=Q(1,10)
    xs=u/(1+u);d=c*(1-r/n);ast=d/(delta*s(n,xs))
    assert xs==Q(2,3) and ast==Q(162,121)
    assert alpha<ast<beta
    for x in [Q(1,10),Q(1,2),Q(9,10)]:
        for a in [Q(3,4),Q(5,2)]:
            xd,ad=field(n,x,a,d,delta,alpha,beta,u,eps)
            direct=(x-xs)/(x*(1-x))*xd + delta*s(n,xs)/(eps*(1+u))*(a-ast)/((a-alpha)*(beta-a))*ad
            assert direct==rhs(n,x,a,delta,xs,eps)<0
    print('EXACT_EXAMPLE_OK',xs,ast)

    try:
        from scipy.integrate import solve_ivp
    except ImportError:
        print('NUMERICAL_INTEGRATION_SKIPPED (scipy absent)')
        return
    trajectories=0
    for e in [.05, .2, 1.0, 5.0, 25.0]:
        for x0, a0 in [(.03,.6), (.95,2.8), (.15,2.7), (.87,.7)]:
            def sigma(z):
                if z>=0:
                    return 1/(1+exp(-z))
                t=exp(z)
                return t/(1+t)
            def f(t,y):
                x=sigma(y[0]); a=float(alpha)+(float(beta)-float(alpha))*sigma(y[1])
                return [(-float(d)+float(delta)*a*s(n,x))/e,
                        (float(beta)-float(alpha))*(float(u)-(1+float(u))*x)]
            init_a=(a0-float(alpha))/(float(beta)-float(alpha))
            sol=solve_ivp(f,(0,15000),[log(x0/(1-x0)),log(init_a/(1-init_a))],method='DOP853',atol=2e-11,rtol=3e-10)
            assert sol.success
            final_x=sigma(sol.y[0,-1])
            final_a=float(alpha)+(float(beta)-float(alpha))*sigma(sol.y[1,-1])
            assert abs(final_x-float(xs))<2e-6,(e,x0,a0,sol.y[:,-1], final_x)
            assert abs(final_a-float(ast))<2e-6,(e,x0,a0,sol.y[:,-1], final_a)
            trajectories+=1
    print('NUMERICAL_TRAJECTORIES_OK',trajectories)
    print('VERIFY_OK')

if __name__=='__main__':
    check()

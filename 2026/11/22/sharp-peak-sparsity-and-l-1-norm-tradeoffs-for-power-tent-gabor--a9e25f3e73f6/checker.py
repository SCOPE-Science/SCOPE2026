"""Supplementary finite tests of the peak-capped power-tent dual formulas.

Requires Python >= 3.9 (standard library only). Run: python checker.py.
Finite checks supplement, but do not substitute for, the analytic proof.
"""
from fractions import Fraction as F
from math import log, isclose


def analytic_pair(r, beta, cap, x):
    a, b = (1.0-x)**r, x**r
    u = min(cap, beta/a)
    return u, (beta-a*u)/b


def vertex_minimum(a,b,beta,cap):
    # For nonnegative coefficients u,v, minimize u+v subject to
    # a*u+b*v=beta, 0<=u,v<=cap. Either u or v hits a bound.
    vertices = []
    for u in (F(0),cap):
        v = (beta-a*u)/b
        if 0 <= v <= cap:
            vertices.append((u+v,u,v))
    for v in (F(0),cap):
        u = (beta-b*v)/a
        if 0 <= u <= cap:
            vertices.append((u+v,u,v))
    if not vertices:
        return None
    return min(z[0] for z in vertices)


def check_exact_vertices():
    count = 0
    for r in (1,2,3):
        for j in range(1,50):
            x = F(j,100)
            a, b = (1-x)**r,x**r
            for k in range(20,101):
                cap = F(k,20)
                beta = F(1)
                if cap*(a+b)<beta:
                    continue
                u = min(cap,beta/a)
                v = (beta-a*u)/b
                assert 0 <= u <= cap and 0 <= v <= cap
                assert a*u+b*v==beta
                exact = vertex_minimum(a,b,beta,cap)
                assert exact is not None and u+v == exact
                count += 1
    return count


def integrate_simpson(fn,a,b,n=20000):
    h=(b-a)/n
    return h/3*(fn(a)+fn(b)+4*sum(fn(a+i*h) for i in range(1,n,2))+2*sum(fn(a+i*h) for i in range(2,n,2)))


def exact_curve(r,beta,cap):
    if cap< beta*max(1.0,2**(r-1)):
        raise ValueError('Infeasible peak bound')
    u = max(0.0,min(0.5,1-(beta/cap)**(1.0/r)))
    if cap >= beta*2**r:
        u=0.5
    left=integrate_simpson(lambda x: beta/(1-x)**r,0.0,u)
    if u >= 0.5:
        return 2*left
    def fn(x):
        if x==0.0 and cap==beta:
            return 2*beta if r==1 else beta
        return cap+(beta-cap*(1-x)**r)/x**r
    right=integrate_simpson(fn,u,0.5)
    return 2*(left+right)


def direct_curve(r,beta,cap):
    n=40000
    dx=0.5/n
    return 2*sum(sum(analytic_pair(r,beta,cap,(i+0.5)*dx))*dx for i in range(n))


def check_curves():
    count=0
    for r in (0.5,1.0,1.5,2.0,3.0):
        beta=0.35
        lo=beta*max(1.,2**(r-1))
        hi=beta*2**r
        for frac in (0.0,0.05,0.2,0.4,0.6,0.8,0.95,1.0,1.2):
            cap=lo+(hi-lo)*frac
            val=exact_curve(r,beta,cap)
            direct=direct_curve(r,beta,cap)
            assert isclose(val,direct,rel_tol=0,abs_tol=0.000015), (r,cap,val,direct)
            count+=1
    for t in (1.01,1.1,1.3,1.6,1.9,2.):
        beta=.35
        f=beta*(2*log(t)+4-2*t+2*(1-t)*log(t/(2*(t-1)))) if t<2 else 2*beta*log(2)
        assert abs(exact_curve(1,beta,beta*t)-f)<2e-9
        count+=1
    return count


def check_support():
    count=0
    for r in (.25,.5,1.,1.5,2.,3.):
        beta=.2
        lo=beta*max(1.,2**(r-1)); hi=beta*2**r
        for frac in (.0,.2,.5,.8,1.,1.3):
            cap=lo+(hi-lo)*frac
            predicted=max(1.,2*(beta/cap)**(1/r))
            occupied=0
            n=20000
            for i in range(n):
                x=.5*(i+.5)/n
                u,v=analytic_pair(r,beta,cap,x)
                assert u>0 and v> -1e-9 and max(u,v)<=cap+1e-9
                occupied+=1+(v>1e-12)
            observed=occupied/n
            assert abs(observed-predicted)<1e-3,(r,cap,predicted,observed)
            count+=1
    return count


if __name__=='__main__':
    a=check_exact_vertices()
    b=check_curves()
    c=check_support()
    print('PASS: rational fiber LP cases:',a)
    print('PASS: independent quadrature/closed-form comparisons:',b)
    print('PASS: measured support comparisons:',c)
    print('NOTE: These are finite tests; the accompanying manuscript supplies the all-parameter proof.')

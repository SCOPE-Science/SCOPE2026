"""Supplementary checks for a two-taxon seasonal Poisson surveillance theorem.
Standard-library-only; the analytic proof does not rely on finite testing.
"""
from math import exp, expm1, log, isclose
from random import Random


def dlog(B, alpha, beta, u, m):
    return B*u*(alpha/expm1(B*alpha*(1+u*m)) - beta/expm1(B*beta*(1-u*m)))


def prob(B, alpha, beta, u, m):
    return (-expm1(-B*alpha*(1+u*m)))*(-expm1(-B*beta*(1-u*m)))


def optimum(B, alpha, beta, u):
    if dlog(B, alpha, beta, u, 1)>=0:
        return 1.
    lo, hi = -1., 1.
    for _ in range(90):
        mid=(lo+hi)/2
        if dlog(B,alpha,beta,u,mid)>0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def critical(alpha, beta, u):
    if beta*(1-u)<=alpha*(1+u):return None
    lo,hi=0.,1.
    while dlog(hi,alpha,beta,u,1)<0:
        hi*=2
    for _ in range(90):
        mid=(lo+hi)/2
        if dlog(mid,alpha,beta,u,1)<0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def run():
    count=0
    # Three qualitative regions: finite saturation, boundary, permanent interior.
    regimes=[(1.,4.,.5),(1.,3.,.5),(1.,1.4,.5)]
    for a,b,u in regimes:
        crit=critical(a,b,u)
        mlist=[]
        for B in [.01,.1,.3,.8,1.,1.5,2.,3.,5.,8.,15.,30.]:
            m=optimum(B,a,b,u);mlist.append(m)
            assert 0 <m<=1
            assert prob(B,a,b,u,m)>=prob(B,a,b,u,0)-1e-12
            assert prob(B,a,b,u,m)>=prob(B,a,b,u,1)-1e-12
            for k in range(101):
                x=-1+2*k/100
                assert prob(B,a,b,u,m)>=prob(B,a,b,u,x)-2e-12
                count+=1
            if crit is not None and B>crit+1e-8:assert m==1
            count+=3
        assert all(y>=x-1e-10 for x,y in zip(mlist,mlist[1:]))
        if crit is not None:
            assert dlog(.5*crit,a,b,u,1)<0
            assert dlog(2*crit,a,b,u,1)>0
    # Certified root of the example polynomial z^4-4z^3+3.
    from fractions import Fraction as F
    def p(x):return x**4-4*x**3+3
    assert p(F(39,10))<0 and p(F(4))>0
    # General random stress tests: global maximizer by bisection, monotonicity with budget.
    r=Random(22571)
    for _ in range(500):
        a=10**r.uniform(-1,.4); b=a*10**r.uniform(.02,.55)
        u=r.uniform(.05,.95); B=10**r.uniform(-1.5,1.)
        m=optimum(B,a,b,u)
        for x in [-1.,-.75,-.5,-.25,0.,.25,.5,.75,1.]:
            assert prob(B,a,b,u,m)>=prob(B,a,b,u,x)-2e-12
            count+=1
        assert optimum(B*1.01,a,b,u)>=m-1e-9
        count+=1
    ex=critical(1.,4.,.5)
    print('checks_passed',count)
    print('critical_budget_alpha1_beta4_u0.5',format(ex,'.13f'))
    print('example_optimum_B1',format(optimum(1.,1.,4.,.5),'.13f'))
    print('example_optimum_B3',format(optimum(3.,1.,4.,.5),'.13f'))
    print('example_probability_at_B1',format(prob(1.,1.,4.,.5,optimum(1.,1.,4.,.5)),'.13f'))

if __name__=='__main__':run()

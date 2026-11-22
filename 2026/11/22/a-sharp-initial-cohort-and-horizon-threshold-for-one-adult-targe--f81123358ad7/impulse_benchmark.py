"""Reproduce the two-stage adult-removal timing theorem's numerical checks.

Only Python's standard library is needed. Analytical inequalities are proved
separately; these tests check implementations and sample parameters, not an
infinite parameter domain.
"""
import math
import random


def exprel(x):
    if abs(x) < 1e-7:
        return 1 + x/2 + x*x/6 + x*x*x/24 + x**4/120
    return math.expm1(x)/x


def H(t, mu):
    return -math.expm1(-mu*t)/mu


def A(t, a0, b, alpha, mu):
    return math.exp(-mu*t)*(a0 + b*t*exprel((mu-alpha)*t))


def D(t, a, alpha, mu):
    return a*math.exp((alpha-mu)*t) + t*exprel((alpha-mu)*t)


def optimum(T, a0, b, alpha, mu):
    assert T>0 and b>0 and alpha>=0 and mu>0 and a0>=0
    a=a0/b
    if a>=H(T,mu):
        return 0.0
    lo,hi=0.,T
    for _ in range(110):
        mid=(lo+hi)/2
        g=H(T-mid,mu)-D(mid,a,alpha,mu)
        if g>0:lo=mid
        else:hi=mid
    return (lo+hi)/2


def gain(s,T,a0,b,alpha,mu,kill=0.6):
    return kill*A(s,a0,b,alpha,mu)*H(T-s,mu)


def total_burden(s,T,a0,b,alpha,mu,kill=0.6):
    # Exact no-treatment integral: initial adults + developing cohort.
    no=a0*H(T,mu)
    # A(t) contribution from birth flux at t=u after future adult survival.
    # Numerical midpoint quadrature is used only for cross-checks.
    n=3000
    no+=sum(b*math.exp(-alpha*(k+0.5)*T/n)*H(T-(k+0.5)*T/n,mu)*T/n for k in range(n))
    return no-gain(s,T,a0,b,alpha,mu,kill)


def run():
    count=0
    r=random.Random(2024)
    for _ in range(300):
        T=r.uniform(0.15,5)
        mu=r.uniform(0.2,3)
        alpha=r.uniform(0.05,3)
        b=r.uniform(.4,3)
        a0=b*H(T,mu)*r.uniform(0,1.8)
        s=optimum(T,a0,b,alpha,mu)
        values=[gain(T*i/80,T,a0,b,alpha,mu) for i in range(81)]
        best=gain(s,T,a0,b,alpha,mu)
        assert best>=max(values)-1e-11
        count+=1
        for j in range(81):
            assert best>=values[j]-1e-11
            count+=1
        # Check the unperturbed ODE solution via a small explicit Euler step.
        n=10000
        dt=T/n
        L=b
        adult=a0
        best_times=[round(s/dt)]
        direct=0.
        for i in range(n):
            if i in best_times:adult*=0.4
            direct+=adult*dt
            oldL=L
            L+=(-alpha*L)*dt
            adult+=(oldL-mu*adult)*dt
        # Relative error depends on the time-discretization and pulse alignment.
        assert abs(direct-total_burden(s,T,a0,b,alpha,mu))<0.008
        count+=1
        if a0/b<H(T,mu)-1e-10:
            assert 0<s<T
            assert optimum(T,a0,b,alpha+0.3,mu)<s
            assert optimum(T,a0+0.01*b*H(T,mu),b,alpha,mu)<s
            count+=3
        else:
            assert s==0
            count+=1
    # Exact equal-rate example: threshold 1-e^-2 and interior root.
    s=optimum(2,.2,1,1,1)
    assert 0.56248<s<0.56249
    assert gain(s,2,.2,1,1,1)>1.91*gain(0,2,.2,1,1,1)
    assert optimum(2,.9,1,1,1)==0
    count+=3
    # Zero-loss mathematical boundary; exact half-horizon for no initial adults.
    for mu in (.2,1,2):
        for T in (.3,1,4):
            assert abs(optimum(T,0,1,0,mu)-T/2)<2e-12
            count+=1
    print('PASS',count,'finite supplementary assertions')


if __name__=='__main__':run()

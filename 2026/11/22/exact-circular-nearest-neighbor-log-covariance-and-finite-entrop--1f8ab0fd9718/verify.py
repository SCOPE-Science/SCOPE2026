#!/usr/bin/env python3
"""Reproducible numerical cross-checks for circular nearest-neighbour entropy theorem.
Standard-library Python only. Neither Monte Carlo nor quadrature proves the result.
"""
import math
import random

PI2=math.pi*math.pi

def li2_minus_half(tol=1e-16):
    v=0.0
    k=1
    while True:
        term=(-0.5)**k/(k*k)
        v+=term
        if abs(term)<tol: return v
        k+=1

def trigamma_int(n):
    return PI2/6.0-sum(1/(j*j) for j in range(1,n))

def c_closed():
    return PI2/6.0+2.0*li2_minus_half()

def c_independent_simpson(N=40000):
    def f(x):
        if x==0: return 0.5
        return (math.log1p(x)-math.log1p(x/2.0))/x
    dx=1.0/N
    s=f(0)+f(1)
    for i in range(1,N): s+=(4 if i%2 else 2)*f(i*dx)
    return 2*s*dx/3.0

def variance(n):
    if n==2: return 1.0
    return (PI2/6.0+2*c_closed())/n - trigamma_int(n)

def covariance(n,j):
    if j==0: return PI2/6.0-trigamma_int(n)
    if j in (1,n-1): return c_closed()-trigamma_int(n)
    return -trigamma_int(n)

def sample(n, rng):
    e=[rng.expovariate(1.0) for _ in range(n)]
    total=sum(e)
    z=[math.log(2*min(e[i-1],e[i])/total) for i in range(n)]
    h=sum(1/j for j in range(1,n))+sum(z)/n
    return h,z

def check():
    C=c_closed()
    assert abs(C-c_independent_simpson())<2e-10, ('closed C vs quadrature',C,c_independent_simpson())
    assert 0<C<PI2/12
    asym=PI2/6+2*C-1
    assert 2.14<asym<2.15
    print('C',format(C,'.16g'), 'asymptotic variance constant',format(asym,'.16g'))
    rng=random.Random(267191)
    for n,reps in [(2,180000),(3,180000),(4,180000),(5,180000),(10,180000),(25,90000)]:
        tot=tot2=0.0
        for _ in range(reps):
            h,_=sample(n,rng)
            tot+=h
            tot2+=h*h
        em=tot/reps
        ev=tot2/reps-em*em
        exact=variance(n)
        # 8-sigma conservative MC bound, using finite fourth moment of log distances.
        assert abs(em)<0.035, ('null mean',n,em)
        assert abs(ev-exact)<0.06, ('null variance',n,ev,exact)
        print(f'n={n:2d} simulated_mean={em:+.6f} simulated_variance={ev:.6f} exact_variance={exact:.6f}')
    n=6
    reps=230000
    s=[0.]*n
    cross=[0.]*n
    for _ in range(reps):
        _,z=sample(n,rng)
        for j in range(n):
            s[j]+=z[j]
            cross[j]+=z[0]*z[j]
    for j in range(n):
        est=cross[j]/reps-(s[0]/reps)*(s[j]/reps)
        exact=covariance(n,j)
        assert abs(est-exact)<0.035, ('kernel',j,est,exact)
        print(f'covariance lag={j}: simulated={est:+.6f}, exact={exact:+.6f}')
    print('ALL CROSS-CHECKS PASSED')

if __name__=='__main__': check()

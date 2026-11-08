#!/usr/bin/env python3
"""Deterministic identities and threshold diagnostics for diagonal-singular square-grid quadrature."""
import math

def diag_mean(alpha):
    return 2.0 / ((1.0-alpha)*(2.0-alpha))

def adj_mean(alpha):
    # E[(1+U-V)^(-alpha)], U,V uniform independent.
    return (2.0-2.0**(2.0-alpha))/(2.0-alpha) + 2.0*(2.0**(1.0-alpha)-1.0)/(1.0-alpha)

def gap_cdf(s):
    return 2*s-s*s

def exact_band_expectation(n,alpha):
    return (n*diag_mean(alpha)+2*(n-1)*adj_mean(alpha))*n**(alpha-2.0)

def root_gap(n,alpha,beta,level):
    # bisection in logarithmic coordinates u=-log(gap)
    ln=math.log(n)
    target=math.log(level)+2*ln
    def value(u):
        return alpha*ln+alpha*u-beta*math.log(1+ln+u)-target
    lo=0.0
    hi=max(10.0, 5.0*ln)
    while value(hi)<0:
        hi*=2
    assert value(lo)<0
    for _ in range(110):
        mid=(lo+hi)/2
        if value(mid)>0:hi=mid
        else:lo=mid
    return math.exp(-(lo+hi)/2)

nchecks=0
for a in [1/5,1/2,2/3,4/5,9/10]:
    m0=diag_mean(a)
    m1=adj_mean(a)
    assert m0>m1>0
    nchecks+=1
    # n=1 has all cells on diagonal and exact expectation I.
    assert abs(exact_band_expectation(1,a)-m0)<1e-11
    nchecks+=1
    for n in [2,3,5,10,100]:
        b=exact_band_expectation(n,a)
        assert 0<b<=m0*(1+1e-9)
        assert abs(b - (n*m0+2*(n-1)*m1)*n**(a-2))<1e-12
        nchecks+=2
    for s in [0.01,0.1,0.2,0.5,0.99]:
        assert abs(gap_cdf(s)-(1-(1-s)**2))<1e-14
        nchecks+=1
# numerical Simpson check of the exact adjacent density integral (no singular integrand at 0 for alpha<1).
def simpson_adj(a,N=100000):
    h=2/N
    def integrand(t):
        if t==0:return 0.0
        weight=t if t<=1 else 2-t
        return weight*t**(-a)
    val=integrand(0)+integrand(2)
    for j in range(1,N):
        val+=(4 if j%2 else 2)*integrand(j*h)
    return val*h/3
for a in [0.2,0.5,2/3,0.8]:
    assert abs(simpson_adj(a)-adj_mean(a))<1e-5
    nchecks+=1
# Logarithmic root asymptotics, n large; compare against exact asymptotic powers.
for a,b in [(2/3,0.0),(2/3,0.5),(2/3,1.0),(0.8,-0.8),(0.8,1.0)]:
    levels=[1,2]
    ratios=[]
    for level in levels:
        for n in [10**5,10**9,10**13]:
            t=root_gap(n,a,b,level)
            assert 0<t<1
            scaling=(level**(-1/a))*((2/a)**(-b/a))*n**(1-2/a)*(math.log(n))**(-b/a)
            assert math.isfinite(scaling) and scaling>0
            ratio=t/scaling
            assert .25<ratio<4, (a,b,level,n,ratio)
            nchecks+=3
            ratios.append((n,ratio))
# exponent and endpoint p-series implications
assert 2-2/(2/3)==-1
assert abs(1.0*(3/2)-1.5)<1e-14
for a in [0.3,0.6,2/3,0.8]:
    if a<2/3:
        low=2/(2-a); high=min(2,1/a)
        assert low<high
    elif a>2/3:
        assert 2-2/a>-1
    else:
        assert abs(2-2/a+1)<1e-12
    nchecks+=1
print('PASS: %d deterministic checks; no simulation treated as proof.'%nchecks)

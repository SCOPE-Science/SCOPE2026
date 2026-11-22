#!/usr/bin/env python3
"""Independent numerical checks for the two-phase upper-record extropy formula.

Uses only Python's standard library. Numerical quadrature is corroboration;
the exact identities and uniqueness proofs are analytic in RESULT.md.
"""
from math import exp, log


def ds(q):
    return (exp(-2*q)-exp(-4*q)*(8*q*q+4*q+1))/4


def g(q):
    return exp(-2*q)/2-8*q*q*exp(-4*q)


def bisect(f, lo, hi, n=65):
    f_lo=f(lo)
    assert f_lo*f(hi)<0
    for _ in range(n):
        mid=(lo+hi)/2
        if f_lo*f(mid)<=0:
            hi=mid
        else:
            lo=mid
            f_lo=f(mid)
    return (lo+hi)/2


def simpson(fun, left, right, intervals=8192):
    assert intervals % 2==0
    dx=(right-left)/intervals
    acc=fun(left)+fun(right)
    for j in range(1,intervals):
        acc+=(4 if j%2 else 2)*fun(left+j*dx)
    return acc*dx/3


def direct_j(a,b,q):
    # Directly integrate the density squares in physical time x.
    tau=q/a
    def sf(x):return exp(-a*x-b*max(x-tau,0.0))
    def dens(x):return (a+b*(x>=tau))*sf(x)
    def urec(x):return 4*(-log(sf(x)))*sf(x)*dens(x)
    # Endpoints need one-sided values, so calculate the two smooth pieces.
    def slice_j(j, left, right, hazard):
        def f(x):
            s=sf(x)
            val=hazard*s if j=='X' else 4*(-log(s))*s*(hazard*s)
            return val*val
        return simpson(f,left,right,32768)
    bound=tau+65/(a+b)
    return tuple(-0.5*(slice_j(which,0,tau,a)+slice_j(which,tau,bound,a+b)) for which in ('X','U'))


def smooth_ds(k,t,a=1,b=1):
    def fn(u):
        z=k*(u-t)
        sig=1/(1+exp(-z)) if z>=0 else exp(z)/(1+exp(z))
        return b*g(u)*sig
    return simpson(fn,0,30,12000)


def main():
    checks=0
    def check(cond, message=''):
        nonlocal checks
        assert cond,message
        checks+=1
    root=bisect(lambda q:exp(2*q)-(8*q*q+4*q+1),1,2)
    q_minus=bisect(lambda q:exp(q)-4*q,0.1,0.8)
    q_plus=bisect(lambda q:exp(q)-4*q,1.5,3)
    check(abs(root-1.7314429364718944)<2e-14,'zero')
    check(abs(q_minus-.3574029561813889)<2e-14,'minimum')
    check(abs(q_plus-2.15329236411035)<2e-14,'maximum')
    check(abs(ds(q_minus)+.08425249834277349)<1e-14)
    check(abs(ds(q_plus)-.001248267115581495)<1e-14)
    check(ds(.5)<0<ds(2.0))
    check(abs(ds(root))<1e-15)
    for a in (.8,1.0,2.4):
        for b in (.1, .7, 2.0):
            for q in (.1,.5,1,root,2,4):
                jx,ju=direct_j(a,b,q)
                check(abs(jx+(a+b*exp(-2*q))/4)<1e-10)
                check(abs(ju+a/4+b*exp(-4*q)*(2*q*q+q+.25))<1e-10)
                check(abs((ju-jx)-b*ds(q))<1.5e-10)
    for k in (16,32,64,128):
        check(smooth_ds(k,1)<0)
        check(smooth_ds(k,2)>0)
        t=bisect(lambda z:smooth_ds(k,z),1,2,n=38)
        check(abs(smooth_ds(k,t))<1e-12)
        check(abs(t-root)<(8.0/k))
        print('smooth',k,'root',format(t,'.12f'))
    print('step root',format(root,'.15f'))
    print('minimum location',format(q_minus,'.15f'),'normalized value',format(ds(q_minus),'.15f'))
    print('maximum location',format(q_plus,'.15f'),'normalized value',format(ds(q_plus),'.15f'))
    print('extrema magnitude ratio',format(-ds(q_minus)/ds(q_plus),'.12f'))
    print('verified checks',checks)

if __name__=='__main__':main()

#!/usr/bin/env python3
"""Exact finite identities and numerical limit diagnostics for Dirichlet coupon completion.
Only standard-library modules are required. Tests are finite diagnostics; limits use the proof.
"""
from fractions import Fraction
from math import factorial, comb, lgamma, exp, log, sqrt
from itertools import product

def rising(x, m):
    z=1
    for j in range(m): z*=x+j
    return z

def compositions(m,q):
    if q==1:
        yield (m,)
    else:
        for v in range(m+1):
            for suffix in compositions(m-v,q-1):
                yield (v,)+suffix

def pmf(counts, a):
    q=len(counts); m=sum(counts)
    v=Fraction(factorial(m),rising(q*a,m))
    for c in counts: v*=Fraction(rising(a,c), factorial(c))
    return v

def factorial_moment_exact(q,a,m,r):
    assert 0<=r<q
    return Fraction(factorial(q),factorial(q-r))*Fraction(rising((q-r)*a,m),rising(q*a,m))

def exact_checks():
    checks=0
    for q in range(2,6):
        for a in (1,2,3):
            for m in range(0,9):
                total=Fraction(0)
                moments=[Fraction(0) for _ in range(q)]
                for counts in compositions(m,q):
                    p=pmf(counts,a)
                    total+=p
                    u=sum(c==0 for c in counts)
                    for r in range(q):
                        fall=factorial(u)//factorial(u-r) if r<=u else 0
                        moments[r]+=fall*p
                assert total==1,(q,a,m,total)
                checks+=1
                for r in range(q):
                    rhs=factorial_moment_exact(q,a,m,r)
                    assert moments[r]==rhs,(q,a,m,r,moments[r],rhs)
                    checks+=1
    # Posterior Beta mean and variance of a coordinate after zero observations.
    for q in range(2,7):
        for a in (1,2,3):
            for m in range(0,9):
                mean=Fraction(a,q*a+m)
                second=Fraction(a*(a+1),(q*a+m)*(q*a+m+1))
                var=second-mean*mean
                assert var==Fraction(a*((q-1)*a+m),(q*a+m)**2*(q*a+m+1))
                checks+=1
    return checks

def asymptotic_diagnostics():
    # Stable product: avoid huge factorials or floating-point overflows.
    diags=[]
    for kappa in (0.5,1.0,2.0):
        for q in (100,500,2000,8000):
            a=kappa*log(q)
            scale=q*exp(log(q)/a)
            center=q*a*(exp(log(q)/a)-1)
            for x in (-1.0,0.0,1.0):
                m=int(center+scale*x)
                for r in (1,2,3):
                    log_e=sum(log(q-j) for j in range(r))
                    log_e+=sum(log(1-r*a/(q*a+j)) for j in range(m))
                    ratio=exp(log_e+r*x)
                    assert 0.5<ratio<2.5,(kappa,q,x,r,ratio)
                    diags.append((kappa,q,x,r,ratio))
    for k in (0.5,1.0,2.0):
        err_small=max(abs(t[4]-1) for t in diags if t[0]==k and t[1]==2000)
        err_large=max(abs(t[4]-1) for t in diags if t[0]==k and t[1]==8000)
        assert err_large<err_small,(k,err_small,err_large)
    return diags

if __name__=='__main__':
    c=exact_checks()
    d=asymptotic_diagnostics()
    print('PASS: exact rational assertions',c)
    print('PASS: finite-scale log-factorial-moment diagnostics',len(d))
    for k in (0.5,1.0,2.0):
        v=[abs(t[4]-1) for t in d if t[0]==k and t[1]==8000]
        print('kappa',k,'largest relative factorial-moment error at q=8000:',round(max(v),6))

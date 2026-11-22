#!/usr/bin/env python3
"""Independent high-precision finite diagnostics for the explicitly defined rational map.
Standard library only; the exact all-real-exponent assertions are proved in RESULT.md.
"""
from decimal import Decimal, localcontext

D=lambda x: Decimal(str(x))

def bisect(fn, lo, hi, steps=230):
    flo=fn(lo)
    assert flo*fn(hi)<0, (lo,hi,flo,fn(hi))
    for _ in range(steps):
        mid=(lo+hi)/2
        fm=fn(mid)
        if fm==0: return mid
        if fm*flo>0: lo,flo=mid,fm
        else: hi=mid
    return (lo+hi)/2

def investigate(beta,delta):
    b=D(beta)
    one=D(1)
    two=D(2)
    p=((one+8/(b+one)).sqrt()-one)/2
    rc=(one+p)/(one-p)**int(beta)
    L=(one+2*p)/((one-p)*(one+p)**2)
    C=(p+2)*(one+3*p+p*p-4*p**3)/(3*p*p*(one-p)**2*(one+p)**4)
    K=L/C
    assert p>0 and C>0 and L>0
    rho=rc*delta.exp()
    def fixed_eq(x): return rho*(one-x)**int(beta)/(one+x)-one
    pp=bisect(fixed_eq, p-D('0.05') if p>D('0.05') else p/2, p+D('0.05'))
    def f(x): return rho*x*(one-x)**int(beta)/(one+x)
    def fp(x):
        return rho*(one-x)**int(beta)/(one+x) * (one-x*b/(one-x)-x/(one+x))
    amplitude=(K*delta).sqrt()
    z=lambda x:f(f(x))-x
    lo=bisect(z,pp-2*amplitude,pp-amplitude/2)
    hi=bisect(z,pp+amplitude/2,pp+2*amplitude)
    assert abs(f(lo)-hi)<D('1e-53')
    assert abs(f(hi)-lo)<D('1e-53')
    ratio=((hi-lo)/2)**2/(K*delta)
    mul=fp(lo)*fp(hi)
    mult_ratio=(one-mul)/(4*L*delta)
    assert abs(ratio-1)<D('0.001'), (beta,delta,ratio)
    assert abs(mult_ratio-1)<D('0.001'),(beta,delta,mult_ratio)
    assert -1<mul<1
    # Independently reconstruct the second/third derivatives using log h.
    l1=one/p-b/(one-p)-one/(one+p)
    l2=-one/p**2-b/(one-p)**2+one/(one+p)**2
    l3=two/p**3-2*b/(one-p)**3-2/(one+p)**3
    A=p*(l1*l1+l2)/2
    C_from_log=p*(l1**3+3*l1*l2+l3)/6+A*A
    assert abs(C_from_log-C)<D('1e-47'),(beta,C_from_log,C)
    # First-flip multiplier and derivative of it with respect to log-rho.
    assert abs(p*l1+1)<D('1e-47')
    dpdlogrho=(one/(one+p)+b/(one-p))**(-1)
    dlamdp=-(one/(one+p)**2+b/(one-p)**2)
    assert abs(dlamdp*dpdlogrho+L)<D('1e-47')
    return (p,rc,L,C,K,ratio,mult_ratio)

with localcontext() as ctx:
    ctx.prec=75
    for beta in [2,3,4,10,100,1000]:
        p,rc,L,C,K,rat,mrat=investigate(beta,D('0.000001'))
        print('beta',beta,'rho_flip',str(rc)[:23],
              'amplitude_ratio',str(rat)[:19],
              'Floquet_ratio',str(mrat)[:19],
              'beta^2*K',str(D(beta)**2*K)[:19])
        assert D(1)<rc<D(8)
    for beta in [1000]:
        p,rc,L,C,K,_,_=investigate(beta,D('0.000001'))
        assert abs(D(beta)**2*K-6)<D('0.05')
    assert abs(investigate(2,D('0.000001'))[1]-D('4.9507461578603875'))<D('1e-14')
    assert abs(investigate(3,D('0.000001'))[1]-D('5.360967922884919'))<D('1e-14')
print('PASS: critical derivatives, nearby two-cycles, return multipliers, and scaling diagnostics')

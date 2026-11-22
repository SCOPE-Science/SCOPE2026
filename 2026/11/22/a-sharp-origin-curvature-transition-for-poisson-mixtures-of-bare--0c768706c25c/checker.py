#!/usr/bin/env python3
"""Reproduce exact normalized Barenblatt reset-mixture origin asymptotics."""
import mpmath as mp
mp.mp.dps=60

def params(sig):
    a=1/(sig+2); nu=1/sig
    I=mp.beta(mp.mpf('.5'),1+nu)
    return a,nu,I

def delta(sig,x,r=1,ell=1):
    a,nu,I=params(sig)
    s=(abs(x)/ell)**(1/a)
    F=lambda u: (mp.mpf(1) if u<=1 else 1-(1-u**(-2*a))**nu)
    term=mp.quad(lambda u: mp.exp(-r*s*u)*u**(-a)*F(u),[0,1,mp.inf])
    return r/(ell*I)*s**(1-a)*term

def coeff(sig,r=1,ell=1):
    a,nu,I=params(sig)
    if sig<1:
        J=nu/(1-a)*mp.beta((1-sig)/2,nu)
        return r*J/(ell**(sig+2)*I)
    if sig==1:
        return 3*r/(ell**3*I)
    return nu*mp.gamma(1-3*a)*r**(3*a)/(ell**3*I)

s=mp.mpf('0.5'); a,nu,I=params(s)
assert abs(I-mp.mpf(16)/15)<mp.mpf('1e-50')
assert abs(nu/(1-a)*mp.beta((1-s)/2,nu)-mp.mpf(32)/3)<mp.mpf('1e-50')
for sig in (mp.mpf('.5'),mp.mpf('1'),mp.mpf('2')):
    a,nu,I=params(sig)
    assert abs(mp.quad(lambda z:(1-z*z)**nu,[-1,1])-I)<mp.mpf('1e-42')
    eps=(mp.mpf('0.03'),mp.mpf('0.01'))
    vals=[]
    for x in eps:
        d=delta(sig,x)
        if sig<1: scale=x**(1+sig)
        elif sig==1: scale=x*x*mp.log(1/x)
        else: scale=x*x
        vals.append(d/scale)
    c=coeff(sig)
    assert abs(vals[1]-c)<abs(vals[0]-c), (sig,vals,c)
    assert abs(vals[1]/c-1)<mp.mpf('0.13'),(sig,vals,c)
    print('sigma',mp.nstr(sig,5),'pred',mp.nstr(c,14),'ratios',*[mp.nstr(v/c,11) for v in vals])
# Exact elementary critical integral, independent from compact-support kernel integration.
u=mp.mpf('0.01'); sigma=mp.mpf('1'); a,nuu,I=params(sigma)
s=u**3
exact=mp.quad(lambda v:mp.exp(-s*v)*v**(-a),[0,1])+mp.e1(s)
computed=mp.quad(lambda v:mp.exp(-s*v)*v**(-a),[0,1])+mp.quad(lambda v:mp.exp(-s*v)/v,[1,mp.inf])
assert abs(exact-computed)<mp.mpf('1e-43')
print('all checks passed')

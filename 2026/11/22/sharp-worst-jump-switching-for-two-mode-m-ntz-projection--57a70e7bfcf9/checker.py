#!/usr/bin/env python3
"""Reproducibility calculations for sharp two-mode power-space approximation.

Checks illustrate the analytic theorem; sampled grids do not certify global optimality.
Requires only Python's standard library.
"""
from math import sqrt, log, exp, isclose

def f(s, q):
    return s*(1-s) - ((2*q+1)/q**2)*(s-s**(q+1))**2

def fp(s, q):
    a = (2*q+1)/q**2
    return 1-(2+2*a)*s + 2*a*(q+2)*s**(q+1)-2*a*(q+1)*s**(2*q+1)

def optimum(q):
    assert q > 0
    if q == 1:
        return ((1-1/sqrt(3))/2, (1+1/sqrt(3))/2)
    lo, hi = ((0.0, .5) if q > 1 else (.5, 1.0))
    assert fp(lo,q)>0 and fp(hi,q)<0
    for _ in range(95):
        mid=(lo+hi)/2
        if fp(mid,q)>0: lo=mid
        else: hi=mid
    return ((lo+hi)/2,)

def simpson(g, a, b, n=3000):
    h=(b-a)/n
    return h/3*(g(a)+g(b)+4*sum(g(a+(2*j-1)*h) for j in range(1,n//2+1))+
               2*sum(g(a+2*j*h) for j in range(1,n//2)))

def exact_piece_integral_error(s,q):
    c=(2*q+1)*(q+1)/q**2*(s-s**(q+1))
    a=1-s-c/(q+1)
    return (a*a*s+2*a*c*s**(q+1)/(q+1)+c*c*s**(2*q+1)/(2*q+1)
          +(1-a)**2*(1-s)-2*(1-a)*c*(1-s**(q+1))/(q+1)
          +c*c*(1-s**(2*q+1))/(2*q+1))

def direct_step_projection_error(s,q):
    coeff=(2*q+1)*(q+1)/q**2 * (s-s**(q+1))
    proj=lambda x: 1-s+coeff*(x**q-1/(q+1))
    return simpson(lambda x:proj(x)**2,0,s)+simpson(lambda x:(1-proj(x))**2,s,1)

checks=0
for q in (.1,.2,.5,.75,.9,.99,1,1.01,1.1,2,3,10,100):
    opt=optimum(q)
    for s in (.07,.2,.4,.5,.66,.83,.97):
        assert abs(exact_piece_integral_error(s,q)-f(s,q))<3e-12,(q,s)
        checks+=1
        if q>=1:
            assert abs(direct_step_projection_error(s,q)-f(s,q))<2e-8,(q,s)
            checks+=1
    v=f(opt[0],q)
    for j in range(1,1200):
        s=j/1200
        assert f(s,q) <= v+3e-10,(q,s,v)
        checks+=1
    for s in opt:
        assert abs(fp(s,q))<1e-9, (q,s,fp(s,q))
        checks+=1
    if q !=1:
        assert (opt[0]<.5) == (q>1)
        checks+=1

slo,shi=optimum(1)
assert abs(f(slo,1)-1/12)<1e-13
assert abs(f(shi,1)-1/12)<1e-13
assert abs(f(.5,1)-1/16)<1e-13
checks+=3
j=lambda s:1/9+s*s*log(s)
assert -.03656 < j(shi) < -.03655
assert .04169 < j(slo) < .04171
for h in (1e-3, 1e-4, 1e-5):
    left=(f(optimum(1-h)[0],1-h)-1/12)/(-h)
    right=(f(optimum(1+h)[0],1+h)-1/12)/h
    assert abs(left-j(shi))<.001 and abs(right-j(slo))<.001
    checks+=2
for q in (10,30,100,300):
    s=optimum(q)[0]
    assert abs((.5-s)*q-1)<.45
    assert abs(f(s,q)-(.25-1/(2*q)))<5/(q*q)
    checks+=2
print('PASS:',checks,'finite numerical checks')
print('q=1 knots:',slo,shi,'sharp square:',f(slo,1))
print('left/right exponent derivatives:',j(shi),j(slo))
for q in (.5,1,2,10):
    s=optimum(q)[0]
    print('q=',q,'unique branch at',s,'squared constant=',f(s,q))

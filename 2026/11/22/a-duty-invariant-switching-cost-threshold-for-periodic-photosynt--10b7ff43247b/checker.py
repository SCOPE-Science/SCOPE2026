"""Deterministic diagnostic for a two-phase active-fraction model.

No finite computation substitutes for the analytical proof in RESULT.md.
Run with Python 3, requiring only its standard library.
"""
from math import exp, expm1, tanh, isclose
from random import Random

rng = Random(271828)
checks = 0

def phi(t, p, q):
    return (-expm1(-p*t))*(-expm1(-q*t))/(-expm1(-(p+q)*t))

def phi_prime(t, p, q):
    a=exp(-p*t); b=exp(-q*t); ab=a*b
    n=(1-a)*(1-b); den=1-ab
    return ((p*a*(1-b)+q*b*(1-a))*den-n*(p+q)*ab)/(den*den)

def production(t,u,v,d,f):
    k=u+d;p=k*f;q=v*(1-f)
    return f*u/k+d/(k*k)*phi(t,p,q)/t

def production_direct(t,u,v,d,f):
    k=u+d;el=exp(-k*f*t);ed=exp(-v*(1-f)*t)
    eq=u/k
    start=eq+(1-eq)*(1-ed)/(1-el*ed)
    return f*eq+(start-eq)*(1-el)/(k*t)

def root(g, left, right):
    for _ in range(85):
        mid=(left+right)/2
        if g(mid)>0: right=mid
        else: left=mid
    return (left+right)/2

for _ in range(1100):
    u=10**rng.uniform(-1.2,1.2)
    v=10**rng.uniform(-1.2,1.2)
    d=10**rng.uniform(-1.2,1.2)
    f=rng.uniform(.03,.97)
    k=u+d;p=k*f;q=v*(1-f)
    t=10**rng.uniform(-1,1.2)/max(p,q)
    K=d/(k*k)
    pp=phi(t,p,q)
    checks+=1
    assert isclose(pp,2*tanh(p*t/2)*tanh(q*t/2)/(tanh(p*t/2)+tanh(q*t/2)),rel_tol=1e-11,abs_tol=1e-11)
    checks+=1
    assert isclose(production(t,u,v,d,f),production_direct(t,u,v,d,f),rel_tol=1e-9,abs_tol=1e-10)
    fast=f*(u*f+v*(1-f))/(k*f+v*(1-f))
    slow=f*u/k
    checks+=1
    assert slow<production(t,u,v,d,f)<fast
    H=pp-t*phi_prime(t,p,q)
    checks+=1
    assert 0<H<1
    c=K*rng.uniform(.05,.95)
    tstar=root(lambda x:phi(x,p,q)-x*phi_prime(x,p,q)-c/K,1e-6/max(p,q),150/min(p,q))
    def objective(x):return production(x,u,v,d,f)-c/x
    checks+=1
    assert objective(tstar)>objective(.7*tstar)+1e-10
    checks+=1
    assert objective(tstar)>objective(1.3*tstar)+1e-10
    checks+=1
    assert objective(tstar)>slow
    checks+=1
    assert isclose(objective(tstar)-slow,K*phi_prime(tstar,p,q),rel_tol=1e-8,abs_tol=1e-9)
    for cc in (K,1.5*K,3*K):
        checks+=1
        assert production(2*t,u,v,d,f)-cc/(2*t)>production(t,u,v,d,f)-cc/t

for p,q in ((1,1),(.3,2),(6,.8),(1,.02)):
    for c in (1e-5,1e-4,1e-3):
        K=1.2
        ts=root(lambda x:phi(x,p,q)-x*phi_prime(x,p,q)-c/K,1e-8/max(p,q),150/min(p,q))
        approximation=(6*(p+q)*c/(K*p*p*q*q))**(1/3)
        checks+=1
        assert abs(ts/approximation-1)<.24

print(f"PASS: {checks} deterministic formula and optimization diagnostics")

#!/usr/bin/env python3
"""Deterministic supplementary numerical tests of the steady mixing/oxygen theorem.

Only standard-library dependencies. The analytic proof in RESULT.md, not finite tests,
establishes statements for all positive real parameters.
"""
import math
import random

def root_positions(p, q):
    assert p > 1 and q > 4*p/(p-1)**2
    disc=q*(q*(p-1)**2-4*p)
    lo=(q*(p-1)-2-math.sqrt(disc))/(2*(q+1))
    hi=(q*(p-1)-2+math.sqrt(disc))/(2*(q+1))
    assert 0<lo<hi<p-1
    return lo**(1/p),hi**(1/p)

def deficit(x,p,q):
    return 1/x + q*x**(p-1)/(1+x**p)

def oxygen_derivative(x,p,q):
    z=x**p
    return ((q+1)*z*z+(2-q*(p-1))*z+1)/(x*x*(1+z)**2)

def oxygen_derivative_direct(x,p,q):
    z=x**p
    return 1/(x*x)-q*x**(p-2)*(p-1-z)/(1+z)**2

def bisect(fun, left, right, increasing=True):
    fl=fun(left);fr=fun(right)
    assert (fl<0<fr) if increasing else (fl>0>fr)
    for _ in range(160):
        mid=(left+right)/2
        if (fun(mid)<0) == increasing:
            left=mid
        else:
            right=mid
    return (left+right)/2

def test():
    checks=0
    rng=random.Random(76591844)
    for p in [0.125,0.5,1.0,1.01,1.125,1.5,2,3,4,6.5,12]:
        qc=4*p/(p-1)**2 if p>1 else math.inf
        for q in [0.001,0.5,1,5,9,40,200, qc*0.5 if p>1 else 5,
                  qc if p>1 else 10, qc*1.1 if p>1 else 20]:
            if not math.isfinite(q): continue
            for x in [0.03,0.07,0.2,0.5,0.9,1.0,2.1,5.0,10.0]:
                a=oxygen_derivative(x,p,q)
                b=oxygen_derivative_direct(x,p,q)
                assert abs(a-b)<2e-10*(1+abs(a)+abs(b))
                checks+=1
                if p<=1 or q<=qc*(1-1e-12):
                    assert a>0
                    checks+=1
            if p>1 and q>qc*(1+1e-8):
                a,b=root_positions(p,q)
                for x,want in [(a/2,+1),((a+b)/2,-1),(2*b,+1)]:
                    assert oxygen_derivative(x,p,q)*want>0
                    checks+=1
                assert deficit(a,p,q)<deficit(b,p,q)
                checks+=1
    for _ in range(20000):
        p=0.2+10*rng.random()
        x=math.exp(rng.uniform(-3,2))
        q=math.exp(rng.uniform(-4,5))
        a=oxygen_derivative(x,p,q)
        b=oxygen_derivative_direct(x,p,q)
        assert abs(a-b)<2e-10*(1+abs(a)+abs(b))
        checks+=1
    # Explicit p=2, q=12, r0=K=1, Cs=10, threshold=3.1
    p,q=2.,12.
    a,b=root_positions(p,q)
    assert abs(a-0.34372376933344034)<1e-12
    assert abs(b-0.8068982213550734)<1e-12
    assert abs((10-deficit(a,p,q))-3.401826132568024)<1e-12
    assert abs((10-deficit(b,p,q))-2.896191048800809)<1e-12
    target=6.9
    roots=[bisect(lambda x:deficit(x,p,q)-target,0.1,a,increasing=False),
           bisect(lambda x:deficit(x,p,q)-target,a,b,increasing=True),
           bisect(lambda x:deficit(x,p,q)-target,b,5,increasing=False)]
    targets=[0.23861248681671143,0.5591007603286322,1.0863447238691482]
    for x,y in zip(roots,targets):
        assert abs(x-y)<1e-12
        checks+=1
    # critical root has horizontal tangent but no sign reversal
    for p in [1.25,1.5,2,3,4,9]:
        qc=4*p/(p-1)**2
        x0=((p-1)/(p+1))**(1/p)
        assert abs(oxygen_derivative(x0,p,qc))<1e-9
        for x in [x0/2,x0*.99,x0*1.01,x0*2]:
            assert oxygen_derivative(x,p,qc)>0
            checks+=1
    # square-root splitting coefficient, checked asymptotically
    for p in [1.25,1.5,2.,3.,4.,8.]:
        qc=4*p/(p-1)**2
        pref=2*(p-1)**2/(math.sqrt(p)*(p+1)**2)*((p-1)/(p+1))**(1/p-1)
        a,b=root_positions(p,qc+1e-5)
        assert abs((b-a)/math.sqrt(1e-5)-pref)<2e-4*max(1,pref)
        checks+=1
    return checks

if __name__=='__main__':
    print('CHECKS_PASSED',test())

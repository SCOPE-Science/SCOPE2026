"""Finite reproducible diagnostics for a sharp qubit-renewal-purity theorem.

This program does not certify arbitrary probability distributions or the proof.
Install NumPy and run: python3 verify_qubit_purity.py
"""
import math
import numpy as np

PI=math.pi
rng=np.random.default_rng(17039071)
checks=0

def near(a,b,tol=3e-10):
    global checks
    assert abs(a-b) <= tol * max(1.0,abs(a),abs(b)), (a,b)
    checks+=1

def law(x,w,m):
    x=np.asarray(x,float)
    w=np.asarray(w,float)
    assert min(x)>0 and min(w)>=0 and len(x)==len(w)
    near(sum(w),1.0)
    near(np.dot(x,w),m)
    u=np.dot(w,np.exp(1j*x))
    chi=(u-1)/(1j*m)
    return abs(chi)**2

def g(m):
    return 2*math.sin(m/2) if m<=PI else 2.

def upper(m):
    return (g(m)/m)**2

def odd_law(m):
    if m<=PI:return [m],[1.]
    k=max(0,int(math.floor((m-PI)/(2*PI))))
    a=PI*(2*k+1)
    b=a+2*PI
    return [a,b],[(b-m)/(b-a),(m-a)/(b-a)]

def even_law(m):
    assert m>=2*PI
    k=max(1,int(math.floor(m/(2*PI))))
    a=2*PI*k
    b=a+2*PI
    return [a,b],[(b-m)/(b-a),(m-a)/(b-a)]

# Check both optimizers across small/boundary/large means.
means=[0.01,0.2,1.,PI/2,PI-1e-6,PI,PI+1e-6,4.,2*PI-1e-6,2*PI,2*PI+1e-6,9.,31.]
for m in means:
    x,w=odd_law(m)
    near(law(x,w,m),upper(m))
    if m>=2*PI:
        x,w=even_law(m)
        near(law(x,w,m),0.,tol=1e-13)
    else:
        for eps in [min(0.01,m/10),min(0.001,m/100),min(1e-5,m/1000)]:
            q=(m-eps)/(2*PI-eps)
            y=law([eps,2*PI],[1-q,q],m)
            assert y<upper(m)+1e-9
            checks+=1

# Explicit strict nonattainment approximations converge quadratically in epsilon.
for m in [0.5,PI,5.]:
    vals=[]
    for e in [1e-2,1e-3,1e-4]:
        q=(m-e)/(2*PI-e)
        vals.append(law([e,2*PI],[1-q,q],m))
    assert vals[-1]<vals[-2]<vals[0]
    checks+=1

# Independent numerical stationary-age integrals for finitely supported laws.
for m in [0.3,2.,PI,4.,8.]:
    raw=rng.uniform(0.1,7.,6)
    w=rng.dirichlet(np.ones(6))
    x=raw*m/np.dot(raw,w)
    z1=np.dot(w,np.expm1(1j*x))/(1j*m)
    z2=np.dot(w, np.sin(x)+1j*(1-np.cos(x)))/m
    near(abs(z1)**2,abs(z2)**2)
    near(law(x,w,m),abs(z1)**2)

# Random laws, including highly heterogeneous supports and broad means.
for m in means:
    for _ in range(175):
        k=int(rng.integers(2,22))
        w=rng.dirichlet(rng.uniform(0.25,2.,k))
        x=np.exp(rng.uniform(-8.,8.,k))
        x=x*m/np.dot(x,w)
        val=law(x,w,m)
        assert val>=-1e-12 and val<=upper(m)+1e-10,(m,val,upper(m))
        checks+=1

# Analytically scaled examples for mixed and pure reset states.
for p,cabs in [(0.5,0.5),(0.2,0.4),(0.75,0.25)]:
    assert cabs*cabs<=p*(1-p)+1e-15
    base=p*p+(1-p)*(1-p)
    for m in means:
        x,w=odd_law(m)
        purity=base+2*cabs*cabs*law(x,w,m)
        near(purity,base+2*cabs*cabs*upper(m))

print('PASS',checks,'finite diagnostics; not an infinite-distribution certificate')

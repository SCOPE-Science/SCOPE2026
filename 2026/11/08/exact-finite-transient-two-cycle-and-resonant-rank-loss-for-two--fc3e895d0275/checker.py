#!/usr/bin/env python3
"""Exact and numerical checks of the two-row isotropic PolarGrad phase classification."""
from fractions import Fraction as F
import numpy as np

def exact_step(a,b,alpha):
    mean=(abs(a)+abs(b))/2
    s=lambda x: F(1) if x>0 else (F(-1) if x<0 else F(0))
    return (a-alpha*mean*s(a), b-alpha*mean*s(b))

def exact_contrast(a,b):
    x,y=sorted((abs(a),abs(b)),reverse=True)
    return (x-y)/(x+y) if x+y else F(0)

# Two-step scalar recurrence on the invariant nonresonant contrast interval.
for alpha in (F(3,10), F(7,10), F(13,10), F(17,10)):
    c=abs(1-alpha)
    r=(1+c)/2
    a,b=F(1)+r,F(1)-r
    z=exact_step(*exact_step(a,b,alpha),alpha)
    assert z==((1-alpha)*a,(1-alpha)*b), (alpha,z)
    assert exact_contrast(*exact_step(a,b,alpha))==c/r

# Exact rank-loss resonances: r=c^k reaches rank one exactly at update k.
alpha=F(7,10)
c=F(3,10)
for k in range(1,6):
    r=c**k
    a,b=F(1)+r,F(1)-r
    for j in range(k):
        assert a!=0 and b!=0
        a,b=exact_step(a,b,alpha)
    assert (a==0) != (b==0), (k,a,b)
    a1,b1=exact_step(a,b,alpha)
    assert (a1,b1)==((1-alpha/2)*a,(1-alpha/2)*b)

# Equal-singular-value start stays on its exactly invariant ray.
for alpha in (F(1,10), F(7,10), F(13,10)):
    a,b=F(3),F(-3)
    for j in range(5):
        assert a==F(3)*(1-alpha)**j
        assert b==-F(3)*(1-alpha)**j
        a,b=exact_step(a,b,alpha)

def numeric_update(e,alpha):
    u,s,vt=np.linalg.svd(e,full_matrices=False)
    active=s>1e-11*max(1,float(s[0]))
    if not np.any(active):
        return np.zeros_like(e)
    return e-(alpha/2)*float(np.sum(s[active]))*(u[:,active]@vt[active,:])

# Orthogonal singular frames and extra columns do not affect the two-step law.
rng=np.random.default_rng(261030280)
count=0
maxerr=0.0
for n in (2,3,8):
    for alpha in (0.21,0.67,1.24,1.76):
        c=abs(1-alpha)
        for j in range(25):
            r=c+(1-c)*rng.uniform(.03,.95)
            u,_=np.linalg.qr(rng.standard_normal((2,2)))
            v,_=np.linalg.qr(rng.standard_normal((n,n)))
            e=u@np.diag([1+r,1-r])@v[:2,:]
            e2=numeric_update(numeric_update(e,alpha),alpha)
            err=np.linalg.norm(e2-(1-alpha)*e,'fro')/max(1,np.linalg.norm(e,'fro'))
            assert err < 1e-11, (n,alpha,j,err)
            maxerr=max(maxerr,err)
            count+=1
print(f"VERIFY_OK exact rank-loss and two-step rational checks; {count} random-frame cases; max residual {maxerr:.3e}")

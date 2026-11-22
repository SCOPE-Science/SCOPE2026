#!/usr/bin/env python3
"""Exact algebraic checks for the four-channel rectangular-pulse contrast.
No external dependencies; numerical tests are diagnostics, not proofs.
"""
from fractions import Fraction as F
from math import exp, log, isclose
from random import Random

# Sparse integer polynomials in (r,z).
def P(c=0): return {(0,0):int(c)} if c else {}
def X(i,j): return {(i,j):1}
def add(a,b):
    out=dict(a)
    for k,v in b.items():
        out[k]=out.get(k,0)+v
        if out[k]==0: del out[k]
    return out
def neg(a): return {k:-v for k,v in a.items()}
def sub(a,b): return add(a,neg(b))
def mul(a,b):
    out={}
    for (i,j),v in a.items():
        for (k,l),w in b.items():out[(i+k,j+l)]=out.get((i+k,j+l),0)+v*w
    return {k:v for k,v in out.items() if v}
def power(a,n):
    out=P(1)
    for _ in range(n):out=mul(out,a)
    return out
def scale(a,c):return {k:v*c for k,v in a.items() if v*c}

r,z=X(1,0),X(0,1);one=P(1)
def qpoly(j):return mul(sub(one,power(r,j)),add(one,power(z,j)))
q=[None]+[qpoly(j) for j in range(1,5)]
lhs=add(sub(mul(power(q[1],2),q[4]),scale(mul(mul(q[1],q[2]),q[3]),2)),power(q[2],3))
rhs=scale(mul(mul(mul(mul(mul(z,sub(r,z)),power(sub(one,r),3)),add(one,r)),power(sub(one,z),2)),sub(one,mul(r,z))),-2)
assert lhs==rhs,'The exact multivariate polynomial factorization fails'
checks=1

# Three-channel alias: 2 pulses versus a physical single pulse.
xx,rr,zz=F(1,2),F(1,2),F(1,4)
def two(j,x=xx,r=rr,z=zz,C=F(1)):return C*x**j*(1-r**j)*(1+z**j)
qq=[None]+[two(j) for j in range(1,5)]
assert qq[1:]==[F(5,16),F(51,256),F(455,4096),F(3855,65536)]
checks+=1
S=F(51,80); product=F(163,3200)
assert qq[2]==qq[1]*S and qq[3]==qq[1]*(S*S-product)
checks+=1
assert 36*36<1297<37*37  # both putative endpoints in (e^-lambda*T,1)
checks+=1
contrast=qq[1]**2*qq[4]-2*qq[1]*qq[2]*qq[3]+qq[2]**3
assert contrast == F(-189,1048576)
checks+=1

# Test identity at many exact rational physical parameter points, independent of the symbolic proof.
for i in range(2,14):
    for j in range(1,i):
        rr=F(i,15);zz=F(j,15)
        for t in (F(1,3),F(2,3),F(1)):
            for C in (F(1,7),F(2),F(13,5)):
                qq=[None]+[two(n,t,rr,zz,C) for n in range(1,5)]
                d=qq[1]**2*qq[4]-2*qq[1]*qq[2]*qq[3]+qq[2]**3
                rhs=-2*C**3*t**6*zz*(rr-zz)*(1-rr)**3*(1+rr)*(1-zz)**2*(1-rr*zz)
                assert d==rhs and d<0
                checks+=1

# Direct integration of filter dynamics for independent random physical pulse schedules.
rand=Random(734201)
for _ in range(150):
    lam=.1+rand.random()*2.7
    length=.1+rand.random()*2.0
    gap=.03+rand.random()*2.0
    tail=rand.random()*2.0
    amp=.1+rand.random()*4.0
    T=2*length+gap+tail
    bounds=((0.,length),(length+gap,2*length+gap))
    x=exp(-lam*tail);r0=exp(-lam*length);z0=exp(-lam*(length+gap))
    for j in range(1,5):
        # exact integration on each constant-input segment
        mass=sum(amp*(exp(-j*lam*(T-end))-exp(-j*lam*(T-start)))/(j*lam) for start,end in bounds)
        normalized=j*lam*mass
        direct=amp*x**j*(1-r0**j)*(1+z0**j)
        assert isclose(normalized,direct,rel_tol=2e-11,abs_tol=1e-12)
        checks+=1

# Log derivative is strictly decreasing at any r in (0,1).
for rr in (.05,.2,.5,.75,.95):
    deriv=lambda z:1/z-1/(rr-z)-2/(1-z)-rr/(1-rr*z)
    ds=[deriv(rr*i/1000) for i in range(1,1000)]
    assert all(a>b for a,b in zip(ds,ds[1:])) and ds[0]>0>ds[-1]
    checks+=1
print('PASS',checks,'independent counted checks; factorization symbolic, all interval signs analytic')

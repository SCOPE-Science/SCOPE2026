#!/usr/bin/env python3
"""Reproducible numerical and algebraic checks for local-time threshold absorption.
Only the Python standard library is needed. Tests corroborate, rather than replace, proofs.
"""
import math
import random
from decimal import Decimal, getcontext

getcontext().prec = 64
D = Decimal

def L(s, r, x, h, diffusivity):
    q = ((r+s)/diffusivity).sqrt()
    e = (x*q).exp()
    g = (r+s)/(r+s*e)
    phi = q*s*e/(r+s*e)
    return g.ln() - h*phi

def moments(r,x,h,dr):
    z=x*(r/dr).sqrt(); E=z.exp(); lam=h/x
    m=x*x/dr*((E-1)/z**2+lam*E/z)
    v=(x*x/dr)**2*((E**2-1-z*E)/z**4 + lam*E*(2*E-z-1)/z**3)
    return m,v

def rootopt(lam):
    lo,hi=D(1),D(2)
    for _ in range(210):
        z=(lo+hi)/2
        E=z.exp()
        sign=(z-2)+2/E + lam*z*(z-1)
        if sign>0:hi=z
        else:lo=z
    return (lo+hi)/2

def assert_rel(a,b,rtol=D('2e-16')):
    assert abs(a-b)<=rtol*max(D(1),abs(a),abs(b)),(a,b)

rng = random.Random(4141)
count=0
for i in range(32):
    r=D(str(10**rng.uniform(-1,1)))
    x=D(str(10**rng.uniform(-0.5,0.4)))
    h=D(str(10**rng.uniform(-1.5,0.6)))
    dr=D(str(10**rng.uniform(-0.7,0.7)))
    step=D('1e-17')
    f0=L(D(0),r,x,h,dr)
    fp=L(step,r,x,h,dr); fm=L(-step,r,x,h,dr)
    ma=-(fp-fm)/(2*step)
    va=(fp+fm-2*f0)/step**2
    m,v=moments(r,x,h,dr)
    assert_rel(ma,m,D('3e-20'))
    assert_rel(va,v,D('2e-16'))
    count+=2

z0=rootopt(D(0))
assert D('1.59')<z0<D('1.60'); count+=1
for j in range(60):
    lam=D(str(10**rng.uniform(-4,3)))
    z=rootopt(lam)
    assert D(1)<z<z0
    E=z.exp(); r=z*z
    h=lam
    m,v=moments(r,D(1),h,D(1))
    assert_rel(v, m*m - (lam*E/z)**2,D('2e-50'))
    assert D(0)<v<m*m
    # The FPT mean is larger on both sides of the uniquely optimal rate.
    def mean_at(zz):return (zz.exp()-1)/zz**2+lam*zz.exp()/zz
    for scale in (D('0.8'),D('0.96'),D('1.04'),D('1.25')):
        assert mean_at(z*scale)>mean_at(z)
    # Compared with erasing local-time progress at each reset, the optimizer is higher.
    assert z>z0/(1+lam)
    count+=8
# Large and small threshold limits
for lam in [D('1e-5'), D('1e-6')]:
    z=rootopt(lam)
    coeff=z0*(z0*z0+2*z0-2)/(2*(z0-1))
    rem=abs((z-(z0-z0*lam+coeff*lam*lam))/lam**2)
    assert rem < D('0.004')
    count+=1
for lam in [D('1e5'),D('1e6')]:
    z=rootopt(lam)
    assert abs((z-1)*lam - (1-2/Decimal(1).exp()))<D('0.00002')
    count+=1
print('PASS',count,'independent numerical derivative, optimizer, variance, and boundary checks')
print('z0:',z0)

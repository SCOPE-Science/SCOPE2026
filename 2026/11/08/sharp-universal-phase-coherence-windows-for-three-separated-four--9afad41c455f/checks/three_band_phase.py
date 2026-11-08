"""Finite consistency checks for the three-band signed-kernel phase diagram."""
import math, random
from collections import Counter

def pred(w,T,d):
    delta=w*T
    x=d*T
    return delta<=1/3+1e-12 and any(x>=k+delta-1e-12 and x<=k+(1-delta)/2+1e-12 for k in range(30))

def lobe(w,T,d):
    delta=w*T
    if d<=w or delta>=1:
        return False,[]
    labs=[]
    for dv in (d,2*d):
        lo,hi=T*(dv-w),T*(dv+w)
        if (math.floor(lo+1e-10)==math.floor(hi-1e-10)):
            labs.append(math.floor((lo+hi)/2))
        else:
            return False,[]
    return labs[1]%2==0,labs

random.seed(816)
cnt=Counter()
for i in range(20000):
    T=10**random.uniform(-1,1)
    w=random.uniform(.0003,.7)/T
    d=(w+random.uniform(.001,10/T))
    a=pred(w,T,d); b,l=lobe(w,T,d)
    if a!=b:
        raise AssertionError((w,T,d,a,b,l))
    cnt[str(a)]+=1
print('THREE_BAND_PHASE_DIAGRAM_PASS',sum(cnt.values()),dict(cnt))
# Finite quadrature of the actual positive Gram kernel in the coherent cases:
import numpy as np
rng=np.random.default_rng(20261103)
for width,d,sgn in [(0.2,1.2,-1),(0.2,2.2,1),(0.2,.6,None),(0.35,1.35,None)]:
    n=12
    freqs=np.concatenate([np.linspace(j*d-width/2,j*d+width/2,n) for j in range(3)])
    diff=freqs[:,None]-freqs[None,:]
    K=np.sinc(diff)
    h=np.abs(rng.normal(size=3*n))+.1
    if sgn is not None:
        ph=np.repeat([1,sgn,1],n)
        ref=np.dot(h*ph,K@(h*ph))
        for k in range(20):
            rand=np.exp(1j*rng.uniform(-math.pi,math.pi,size=3*n))
            val=np.real(np.vdot(h*rand,K@(h*rand)))
            assert ref>=val-1e-9
    else:
        if width == .2:
            # Adjacent sinc signs positive; outer sinc sign negative:
            # no three constant band phases satisfy all three edges.
            adj=float(np.sinc(d)); outer=float(np.sinc(2*d))
            assert adj > 0 and outer < 0 and (np.sign(adj)**2)*np.sign(outer) < 0
        else:
            # The far-band difference interval straddles the integer 3,
            # hence demands both cross-band phase signs simultaneously.
            assert np.sinc(2*d-width)>0 and np.sinc(2*d+width)<0
print('THREE_BAND_NUMERICS_PASS')

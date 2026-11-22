"""Reproducibility checks for weighted-triangle spectral fractional heat."""
import math
import random
import numpy as np
from scipy.linalg import expm
from scipy.optimize import brentq


def data(a,b,c):
    s=a+b+c
    d=math.sqrt(max(0,s*s-3*(a*b+a*c+b*c)))
    lmin,lmax=s-d,s+d
    m=min(a,b,c)
    crit=(math.log((lmax/3-m)/(lmin/3-m))/math.log(lmax/lmin)
          if lmax-lmin>1e-9 and lmin/3-m>1e-9 else math.inf)
    return lmin,lmax,crit


def spec_power(a,b,c,alpha):
    L=np.array([[a+b,-a,-b],[-a,a+c,-c],[-b,-c,b+c]])
    z,U=np.linalg.eigh(L)
    z[0]=0.0  # mathematical zero eigenvalue; suppress roundoff before fractional power
    return (U * np.maximum(z,0)**alpha) @ U.T


def kernel_edge(w,lmin,lmax,alpha,t):
    if abs(lmax-lmin)<1e-11:
        return -math.expm1(-t*lmin**alpha)/3
    gap=lmax-lmin
    Pplus=(lmin/3-w)/gap
    Pminus=(w-lmax/3)/gap
    # stable near t=0: sum of offdiagonal projections is -1/3
    return Pplus*math.expm1(-t*lmax**alpha)+Pminus*math.expm1(-t*lmin**alpha)


rng=random.Random(724321)
checks=0
for trial in range(150):
    a,b,c=[math.exp(rng.uniform(-1.8,1.8)) for _ in range(3)]
    lam,high,critical=data(a,b,c)
    for alpha in [0.33,0.91,1.,1.2,2.,3.,4.5]:
        Q=spec_power(a,b,c,alpha)
        for (i,j,w) in [(0,1,a),(0,2,b),(1,2,c)]:
            actual=Q[i,j]
            if high-lam>1e-8:
                predicted=((lam/3-w)*high**alpha+(w-high/3)*lam**alpha)/(high-lam)
            else:
                predicted=-w*high**(alpha-1)
            assert abs(actual-predicted)<=5e-8*max(1,abs(actual),abs(predicted))
            checks+=1
        for t in [0.001,0.03,0.2,1.]:
            E=expm(-t*Q)
            for (i,j,w) in [(0,1,a),(0,2,b),(1,2,c)]:
                exact=kernel_edge(w,lam,high,alpha,t)
                assert abs(E[i,j]-exact)<2e-8
                checks+=1
            assert np.max(np.abs(E.sum(axis=1)-1))<3e-9
            checks+=1
    # Unique weakest edge: generator sign threshold and all other entries nonpositive
    if len(set(round(v,8) for v in [a,b,c]))==3:
        weak=min(a,b,c)
        for alp in [max(0.1,critical-0.1),critical+0.1]:
            Q=spec_power(a,b,c,alp)
            vals=dict(zip([a,b,c], [Q[0,1],Q[0,2],Q[1,2]]))
            assert (vals[weak]>0)==(alp>critical)
            assert all(v<0 for w,v in vals.items() if w!=weak), (a,b,c,alp,critical,vals)
            checks+=1

# Time crossing and exact transient infinity norm, moderate numerically stable parameters.
for a,b,c,alpha in [(0.5,1.,2.,2.1), (0.4,1.3,3.,2.),(0.9,1.,1.,18.),(0.3,0.8,1.4,3.)]:
    low,hi,crit=data(a,b,c)
    if alpha<=crit:continue
    w=min(a,b,c)
    rate_high=hi**alpha; rate_low=low**alpha
    C=(low/3-w)/(hi-low)
    A=(hi/3-w)/(hi-low)
    peak=math.log(C*rate_high/(A*rate_low))/(rate_high-rate_low)
    fun=lambda t: kernel_edge(w,low,hi,alpha,t)
    # bracket away from the t=0 root
    lo=peak
    assert fun(lo)<0
    ub=max(10*peak,10/rate_low)
    root=brentq(fun,lo,ub,xtol=5e-15)
    assert root>peak
    weights={(0,1):a,(0,2):b,(1,2):c}
    for t in [peak/2,peak, (peak+root)/2,root+1/rate_low]:
        Q=spec_power(a,b,c,alpha)
        E=expm(-t*Q)
        actual=float(np.max(np.sum(np.abs(E),axis=1)))
        expected=1-2*min(0,fun(t))
        assert abs(actual-expected)<3e-9
        checks+=1

# Two sharply different critical-exponent divergences.
for eps in (1e-2,1e-3,1e-4):
    low,hi,crit=data(1-eps,1,1)
    formula=math.log(3)/math.log(3/(3-2*eps))
    assert abs(crit-formula)<1e-7*max(1,crit)
    checks+=1
for delta in (1e-2,1e-3,1e-4):
    C=3.
    low,hi,crit=data(1-delta,1,C)
    asym=(math.log(1/delta)+math.log(4*(C-1)/3))/math.log((2*C+1)/3)
    assert abs(crit-asym)<0.04
    checks+=1

print(f"PASS: {checks} independent spectral, heat-kernel, and asymptotic comparisons")

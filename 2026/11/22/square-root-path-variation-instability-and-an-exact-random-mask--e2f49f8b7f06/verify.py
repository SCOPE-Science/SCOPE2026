#!/usr/bin/env python3
"""Finite checks for Walsh spectral shrinkage and open-path variation.
No external packages; does not certify asymptotic arguments.
"""
from math import sqrt, comb, pi
from random import Random

def fwht(values):
    a=list(values)
    n=len(a); step=1
    while step<n:
        for i in range(0,n,2*step):
            for j in range(i,i+step):
                u,v=a[j],a[j+step]
                a[j]=u+v; a[j+step]=u-v
        step*=2
    return a

def proj(x, mask):
    n=len(x)
    spectral=fwht(x)
    return [z/n for z in fwht([b*m for b,m in zip(spectral,mask)])]

def tv(x):
    return sum(abs(a-b) for a,b in zip(x,x[1:]))

def soft(x,lam):
    n=len(x)
    spectrum=fwht(x)
    spectrum=[c if i==0 else (max(c-lam*sqrt(n),0) if c>0 else min(c+lam*sqrt(n),0)) for i,c in enumerate(spectrum)]
    return [v/n for v in fwht(spectrum)]

def mask_from_code(n,code):
    return [1]+[(code>>(j-1))&1 for j in range(1,n)]

def exact_mean(n):
    m=n//2
    return 0.5+(n-2)/n*(m*comb(m,m//2)/2**m) if m%2==0 else 0.5

for n in (2,4,8):
    best=(-1,None,None)
    tot=0.0
    for code in range(1<<(n-1)):
        mask=mask_from_code(n,code)
        single=proj([1]+[0]*(n-1),mask)
        tot+=tv(single)
        for k in range(n-1):
            x=[0]*(k+1)+[1]*(n-k-1)
            gain=tv(proj(x,mask))
            if gain>best[0]:best=(gain,k,code)
    obs=tot/(1<<(n-1))
    formula=0.5 if n==2 else exact_mean(n)
    assert abs(obs-formula)<1e-10,(n,obs,formula)
    assert best[0] <= 2*(sqrt(n)-1)/(sqrt(2)-1)+1e-10
    print('EXHAUSTIVE_MASKS_STEPS_AND_EXACT_FIRST_MOMENT_PASS',n,'count',1<<(n-1),'mean',round(obs,10),'sharp',best)

rng=Random(20261117)
for n in (16,32,64,128):
    upper=2*(sqrt(n)-1)/(sqrt(2)-1)
    for _ in range(140):
        mask=[1]+[rng.randint(0,1) for _ in range(n-1)]
        k=rng.randrange(n-1)
        h=[0]*(k+1)+[1]*(n-k-1)
        assert tv(proj(h,mask))<=upper+1e-8
        # Every spectral mask can be realized as a strict chamber of soft thresholding.
        lam=1.0
        fw=[0.0]+[2*lam*sqrt(n) if m else 0.0 for m in mask[1:]]
        center=[v/n for v in fwht(fw)]
        epsilon=1e-3
        x=[a+epsilon*b for a,b in zip(center,h)]
        delta=[(a-b)/epsilon for a,b in zip(soft(x,lam),soft(center,lam))]
        ph=proj(h,mask)
        assert max(abs(a-b) for a,b in zip(delta,ph))<1e-8
    print('RANDOM_MASK_HAAR_BOUND_AND_STRICT_CHAMBER_PASS',n,'upper',round(upper,6),'random_trials',140)

for n in (4,8,16,32,64,128):
    print('EXACT_MASK_EXPECTATION_FORMULA',n,round(exact_mean(n),10),'scaled',round(exact_mean(n)/sqrt(n),10))
print('ALL_WALSH_PATH_BV_CHECKS_PASS')

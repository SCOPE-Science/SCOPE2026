#!/usr/bin/env python3
"""Independent scalar spectral-root and finite-difference checks for Leslie-plus sensitivity thresholds.
Requires only Python >=3.9 standard library. Run: python check.py
"""
import random
import math

rng = random.Random(1102026)
checks = 0

def root(ss, t, fs):
    n = len(fs)
    assert len(ss) == n-1 and 0 <= t < 1 and fs[-1] > 0
    def reproduction(lam):
        p = 1.0
        result = fs[0]
        for j in range(1,n-1):
            p *= ss[j-1]/lam
            result += fs[j]*p
        p *= ss[n-2]/(lam-t)
        result += fs[n-1]*p
        return result
    lo = t + 1e-13
    hi = 2.0
    while hi <= reproduction(hi):
        hi *= 2
    for _ in range(110):
        mid = (lo+hi)/2
        if mid > reproduction(mid):
            hi=mid
        else:
            lo=mid
    return (lo+hi)/2

def weights(ss,t,lam):
    n=len(ss)+1
    w=[1.0]
    for j in range(n-2):
        w.append(w[-1]*ss[j]/lam)
    w.append(w[-1]*ss[-1]/(lam-t))
    return w

for _ in range(700):
    n = rng.randint(3, 9)
    ss = [rng.uniform(.35,.99) for k in range(n-1)]
    t = rng.uniform(.1,.95)
    fs = [rng.uniform(1.2,3.0) for k in range(n)]
    lam=root(ss,t,fs)
    assert lam>1
    w=weights(ss,t,lam)
    assert all(w[j] > w[j+1] for j in range(n-2))
    checks+=n-2
    for j in range(n-1):
        prod=math.prod(ss[j:])
        formula=prod / (lam**(n-j-2)*(lam-t)) # index j=0 corresponds age 1
        assert math.isclose(w[-1]/w[j],formula,rel_tol=2e-12,abs_tol=2e-12)
        checks+=1
    # Direct implicit root differentiation, not relying on eigenvectors.
    h=1e-5
    diff=[]
    for j in range(n):
        up=fs.copy(); dn=fs.copy();up[j]+=h;dn[j]-=h
        diff.append((root(ss,t,up)-root(ss,t,dn))/(2*h))
    for j in range(n):
        assert math.isclose(diff[j]/diff[0],w[j]/w[0],rel_tol=2e-5,abs_tol=2e-5)
        checks+=1

n=4
ss=[.9,.9,.9]
t=.95
p=math.prod(ss)
threshold_lam=[]
threshold_F=[]
for j in range(1,n):
    P=math.prod(ss[j-1:])
    lo,hi=1.0,4.0
    for _ in range(120):
        z=(lo+hi)/2
        if z**(n-j-1)*(z-t)<P:lo=z
        else:hi=z
    critical=(lo+hi)/2
    threshold_lam.append(critical)
    F=critical**(n-1)*(critical-t)/p
    threshold_F.append(F)
    L=root(ss,t,[0]*(n-1)+[F])
    assert abs(L-critical)<1e-10
    w=weights(ss,t,L)
    assert math.isclose(w[-1],w[j-1],rel_tol=1e-10)
    checks+=2
assert threshold_lam[0]<threshold_lam[1]<threshold_lam[2]
assert threshold_F[0]<threshold_F[1]<threshold_F[2]
checks+=2
for F in [0.2,0.9,1.5,3.0,9.0]:
    lam=root(ss,t,[0]*(n-1)+[F])
    if lam>1:
        w=weights(ss,t,lam)
        age_rank=sorted(range(1,n+1),key=lambda age:-w[age-1])
        # Every age relative to final follows the unique crossing budget.
        for j,T in enumerate(threshold_F,1):
            assert (w[-1]>w[j-1]) == (F<T)
            checks+=1
print('PASS:',checks,'independent numerical assertions; n=4 critical lambdas =',threshold_lam,'critical fecundities =',threshold_F)

"""Finite numerical stress tests for sharp fixed-area endpoint averaging bounds.

All conclusions about arbitrary measurable sets use the separate analytical proof.
"""
import math
import random

INF = float('inf')

def conj(p):
    if p == 1:
        return INF
    if p == INF:
        return 1.
    return p/(p-1)

def mean(a):
    return sum(a)/len(a)

def indicator_norm(m, p, q):
    inner = [((v**(1/q)) if q != INF else (1. if v>0 else 0.)) for v in m]
    if p == INF:
        return max(inner)
    return mean([v**p for v in inner])**(1/p)

def rank_one(m,p,q):
    return indicator_norm(m,p,q)*indicator_norm(m,conj(p),conj(q))/mean(m)

cases=[(1,1),(INF,INF),(1,2),(INF,2),(2,1),(2,INF),(1,INF),(INF,1),(1,4),(4,1),(4,INF),(INF,4)]
random.seed(73)
count=0
for p,q in cases:
    for _ in range(250):
        m=[random.random() for i in range(80)]
        t=mean(m)
        delta=abs((0 if p==INF else 1/p)-(0 if q==INF else 1/q))
        assert rank_one(m,p,q)<=t**(-delta)*(1+2e-12)
        count+=1

# For each non-corner endpoint, exhibit a two-height sequence that approaches the
# sharp constant at a specified nontrivial area t.
t=.37
for p,q in [(1,2),(INF,2),(1,4),(INF,4),(2,1),(2,INF),(4,1),(4,INF)]:
    delta=abs((0 if p==INF else 1/p)-(0 if q==INF else 1/q))
    vals=[]
    for eps in [0.002,0.0002,0.00002]:
        if p in (1,INF):
            # This discretized high-spike profile is a two-atom probability law.
            weights=[eps,1-eps]
            heights=[1.,(t-eps)/(1-eps)]
        else:
            weights=[t-eps,1-t+eps]
            heights=[1.,eps/(1-t+eps)]
        def power_mean(alpha):
            return sum(w*h**alpha for w,h in zip(weights,heights))
        sup=max(heights)
        support=sum(w for w,h in zip(weights,heights) if h>0)
        if p==1:
            exact=power_mean(1/q)*sup**(1/conj(q))/t
        elif p==INF:
            exact=sup**(1/q)*power_mean(1/conj(q))/t
        elif q==1:
            exact=power_mean(p)**(1/p)*support**(1/conj(p))/t
        else:
            exact=support**(1/p)*power_mean(conj(p))**(1/conj(p))/t
        vals.append(exact/(t**(-delta)))
    assert all(0<v<=1+1e-10 for v in vals)
    assert vals[-1]>.9998, (p,q,vals)
    assert vals[0]<vals[1]<vals[2], (p,q,vals)

# In opposite corners, exact equality holds for positive a.e. sections and a
# set of positive outer measure where the section has full length.
for p,q in [(1,INF),(INF,1)]:
    m=[1.]+[.2]*999
    t=mean(m)
    assert abs(rank_one(m,p,q)-1/t)<1e-9

print(f"PASS: {count} finite-grid upper-bound probes; eight two-height limiting families; two corner equality probes")

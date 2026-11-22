"""Reproducibility checks for coordinatewise sensitivity of mixed-norm ball projection."""
from itertools import combinations, product
from fractions import Fraction as F
import random
import numpy as np


def formula(sizes):
    d=sorted(sizes, reverse=True)
    if len(d)<3:
        return F(1)
    v=F(1)
    s=F(0)
    for k in range(1,len(d)):
        s+=F(1,d[k-1])
        if k>=2:
            v=max(v,1+F(k-1)/(1+s))
    return v


def enumerate_faces(sizes):
    m=len(sizes)
    result=F(1)
    for r in range(1,m+1):
        for active in combinations(range(m),r):
            for ks in product(*[range(1,sizes[g]+1) for g in active]):
                H=sum([F(1,k) for k in ks],F(0))
                for kg in ks:
                    result=max(result, F(1)+F(r-2)/(kg*H)) if r>=2 else result
    return result


def t_lambda(y, lam):
    a=np.abs(np.asarray(y,dtype=float))
    if lam>=sum(a):return 0.
    lo,hi=0.,max(a)
    for _ in range(55):
        md=(lo+hi)/2
        if np.maximum(a-md,0).sum()>lam:lo=md
        else:hi=md
    return (lo+hi)/2


def project(groups, radius):
    arr=[np.asarray(g,dtype=float) for g in groups]
    if sum(max(abs(a)) for a in arr)<=radius:
        return [a.copy() for a in arr]
    lo=0.;hi=max(sum(abs(a)) for a in arr)
    for _ in range(55):
        mid=(lo+hi)/2
        if sum(t_lambda(a,mid) for a in arr)>radius:lo=mid
        else:hi=mid
    lam=(lo+hi)/2
    return [np.clip(a,-t_lambda(a,lam),t_lambda(a,lam)) for a in arr]


def sharp_example(sizes, target, others, radius=3.):
    active=[target]+list(others)
    r=len(active)
    lam=0.7
    ts=radius/r
    ks={g:(1 if g==target else sizes[g]) for g in active}
    y=[]
    h=[]
    for g,d in enumerate(sizes):
        if g not in ks:
            y.append(np.zeros(d));h.append(np.zeros(d));continue
        k=ks[g]
        b=np.zeros(d);b[:k]=ts+lam/k
        y.append(b)
        h.append(np.r_[np.full(k,1. if g==target else -1.),np.zeros(d-k)])
    p=project(y,radius)
    assert max(np.max(abs(p[g][:ks[g]]-ts)) for g in active)<1e-8
    eps=min(.01, lam/(100*max(sizes)))
    q=project([a+eps*b for a,b in zip(y,h)], radius)
    actual=max(np.max(abs(a-b)) for a,b in zip(p,q))/eps
    desired=float(F(1)+F(r-2)/(1+sum((F(1,sizes[g]) for g in others),F(0))))
    return actual,desired


def run():
    cnt=0
    for m in range(1,5):
        for d in product(range(1,5), repeat=m):
            assert formula(d)==enumerate_faces(d),(d,formula(d),enumerate_faces(d))
            cnt+=1
    print('Exact face-enumeration comparisons:', cnt)
    rr=random.Random(23)
    examples=0
    for _ in range(120):
        m=rr.randint(3,7)
        d=tuple(rr.randint(1,9) for _ in range(m))
        order=sorted(range(m),key=lambda g:d[g],reverse=True)
        best=(0,None,None)
        for k in range(2,m):
            target=order[k];other=order[:k]
            v=1+(k-1)/(1+sum(1/d[g] for g in other))
            if v>best[0]:best=(v,target,other)
        observed,wanted=sharp_example(d,best[1],best[2],radius=3.)
        assert abs(observed-wanted)<5e-8,(d,observed,wanted)
        assert abs(wanted-float(formula(d)))<1e-10
        examples+=1
    print('Constructed sharp finite-pair tests:',examples)
    for d, target, others in [((1,4,4),0,[1,2]),((1,100,100),0,[1,2]),((1,100,100,100),0,[1,2,3]),((1,1,1),0,[1,2])]:
        got,wanted=sharp_example(d,target,others)
        print('example',d,'coefficient',formula(d),'finite two-input ratio',got)
    r=rr
    for _ in range(120):
        m=r.randint(1,6)
        d=tuple(r.randint(1,6) for __ in range(m))
        rad=r.uniform(.1,9.)
        y=[np.array([r.uniform(-5,5) for __ in range(j)]) for j in d]
        z=[np.array([r.uniform(-5,5) for __ in range(j)]) for j in d]
        p,q=project(y,rad),project(z,rad)
        left=max(float(np.max(abs(a-b))) for a,b in zip(p,q))
        right=float(formula(d))*max(float(np.max(abs(a-b))) for a,b in zip(y,z))
        assert left<=right+1e-8,(d,left,right)
    print('Independent random two-input inequalities: 120')

if __name__=='__main__':run()

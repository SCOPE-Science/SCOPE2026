#!/usr/bin/env python3
"""Exhaustive independent residual-language checks for cyclic distinct-run words.
Scientific input is a vector of positive run lengths; it contains no workflow data.
"""
from itertools import product
from collections import defaultdict
from random import Random


def downset(word):
    s={''}
    for c in word:
        s |= {v+c for v in tuple(s)}
    return s

def data(v):
    q=len(v)
    w=''.join(str(i)*a for i,a in enumerate(v))
    rotations={w[i:]+w[:i] for i in range(len(w))}
    closure=set().union(*(downset(t) for t in rotations))
    return w,rotations,closure

def residuals(lang):
    r=defaultdict(set)
    for s in lang:
        for k in range(len(s)+1):
            r[s[:k]].add(s[k:])
    return r

def predict_residual(v,z):
    q=len(v);n=sum(v)
    if not z:
        return data(v)[2]
    i=int(z[0]);p=len(z)-len(z.lstrip(str(i)))
    if len(set(z))==1:
        rest=''.join(str((i+h)%q)*v[(i+h)%q] for h in range(1,q))
        return set().union(*(downset(str(i)*t+rest+str(i)*(v[i]-p-t))
                           for t in range(v[i]-p+1)))
    j=int(z[-1]);r=len(z)-len(z.rstrip(str(j)))
    if i==j:
        assert p+r<=v[i],(v,z)
        return downset(str(i)*(v[i]-p-r))
    t=str(j)*(v[j]-r)
    k=(j+1)%q
    while k!=i:
        t+=str(k)*v[k]; k=(k+1)%q
    t+=str(i)*(v[i]-p)
    return downset(t)

def conjugacy_classes(C):
    return 1+len({frozenset(sufs) for sufs in residuals(C).values()})

def check(v):
    n=sum(v);w,C,D=data(v)
    R=residuals(D)
    expect=n*n-sum(a*a for a in v)+3
    actual=1+len({frozenset(x) for x in R.values()})
    csc=conjugacy_classes(C)
    assert actual==expect and csc==expect,(v,expect,actual,csc)
    for z,suffixes in R.items():
        pred=predict_residual(v,z)
        assert pred==suffixes,(v,z,sorted(pred),sorted(suffixes))
    return len(R),len(D)

def main():
    conf=[]
    for q in range(2,6):
        maxval={2:5,3:3,4:2,5:2}[q]
        conf.extend(product(range(1,maxval+1),repeat=q))
    rng=Random(20261107)
    for _ in range(180):
        q=rng.randint(2,5)
        v=tuple(rng.randint(1, min(6,max(1,12//q))) for _ in range(q))
        if sum(v)<=12:conf.append(v)
    total_pre=total_lang=0
    for v in conf:
        a,b=check(v);total_pre+=a;total_lang+=b
    print('VERIFY_OK configurations=%d residuals=%d accepted_words=%d'%(len(conf),total_pre,total_lang))
if __name__=='__main__':main()

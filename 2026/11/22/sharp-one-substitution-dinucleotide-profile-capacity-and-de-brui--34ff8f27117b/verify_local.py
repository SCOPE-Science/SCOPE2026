#!/usr/bin/env python3
"""Exact local-change census and constructive saturation checks."""
from itertools import product
from collections import defaultdict

def vector(q, additions, removals):
    a=[0]*(q*q)
    for x,y in additions:a[q*x+y]+=1
    for x,y in removals:a[q*x+y]-=1
    return tuple(a)

def local_change(q,a,b,c,d):
    return vector(q,[(a,d),(d,c)],[(a,b),(b,c)])

def debruijn(q,order=3):
    # Fredricksen--Kessler--Maiorana algorithm: cyclic de Bruijn sequence.
    arr=[0]*(q*order+1)
    out=[]
    def db(t,p):
        if t>order:
            if order%p==0:out.extend(arr[1:p+1])
        else:
            arr[t]=arr[t-p]
            db(t+1,p)
            for j in range(arr[t-p]+1,q):
                arr[t]=j
                db(t+1,t)
    db(1,1)
    return tuple(out)+tuple(out[:order-1])

def direct_ball(q,w):
    profiles=set()
    for i,b in enumerate(w):
        for d in range(q):
            if b==d:continue
            new=w[:i]+(d,)+w[i+1:]
            profile=[0]*(q*q)
            for a,c in zip(new,new[1:]):profile[a*q+c]+=1
            profiles.add(tuple(profile))
    return profiles

for q in range(2,9):
    change_to_contexts=defaultdict(set)
    for a,b,c,d in product(range(q),repeat=4):
        if b!=d:change_to_contexts[local_change(q,a,b,c,d)].add((a,b,c,d))
    formula=q*(q-1)*(q*q-1)
    assert len(change_to_contexts)==formula,(q,len(change_to_contexts),formula)
    collisions=[v for v in change_to_contexts.values() if len(v)>1]
    assert len(collisions)==q*(q-1) and all(len(c)==2 for c in collisions)
    for v in collisions:
        (a,b,c,d),(ap,bp,cp,dp)=sorted(v)
        assert b==bp and d==dp and {(a,c),(ap,cp)}=={(b,d),(d,b)}
    if q>=3:
        for a,b,c in product(range(q),repeat=3):
            assert any(len(change_to_contexts[local_change(q,a,b,c,d)])==1
                       for d in range(q) if b!=d)
    w=debruijn(q)
    assert len(w)==q**3+2
    assert len({w[i:i+3] for i in range(len(w)-2)})==q**3
    actual=len(direct_ball(q,w))
    predicted=formula+2*(q-1)
    assert actual==predicted,(q,actual,predicted)
    print('q=%d interior=%d collision_pairs=%d capacity=%d witness_length=%d verified' %
          (q,formula,len(collisions),actual,len(w)))
print('LOCAL_CHECK_PASS')

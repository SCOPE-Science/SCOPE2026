#!/usr/bin/env python3
"""Exhaustive two-neighbor graph bootstrap census, PG(2,q), q=2,3,4."""
import itertools
from collections import Counter
from math import comb

def field(q):
    def multiply(a,b):
        if q!=4: return (a*b)%q
        out=0
        for i in range(2):
            for j in range(2):
                if ((a>>i)&1) and ((b>>j)&1): out^=1<<(i+j)
        if out&4: out^=7
        return out
    add=lambda a,b:(a^b if q==4 else (a+b)%q)
    return add,multiply

def incidence(q):
    add,mul=field(q)
    labels=set()
    for x in itertools.product(range(q),repeat=3):
        if not any(x):continue
        leading=next(t for t in x if t)
        inv=next(t for t in range(1,q) if mul(t,leading)==1)
        labels.add(tuple(mul(t,inv) for t in x))
    vectors=sorted(labels)
    v=len(vectors); assert v==q*q+q+1
    neighbors=[]
    for x in vectors:
        neighbors.append(sum(1<<(v+j) for j,y in enumerate(vectors) if add(add(mul(x[0],y[0]),mul(x[1],y[1])),mul(x[2],y[2]))==0))
    for y in vectors:
        neighbors.append(sum(1<<i for i,x in enumerate(vectors) if add(add(mul(x[0],y[0]),mul(x[1],y[1])),mul(x[2],y[2]))==0))
    return neighbors,v

def closure(neighbors,mask):
    rounds=0
    while True:
        next_mask=mask
        for idx,nei in enumerate(neighbors):
            if not (mask>>idx)&1 and ((mask&nei).bit_count()>=2):next_mask|=1<<idx
        if next_mask==mask:return mask,rounds
        mask=next_mask
        rounds+=1

def census(q,k):
    nb,v=incidence(q)
    all_ones=(1<<(2*v))-1
    count=Counter()
    time_profile=Counter()
    for combi in itertools.combinations(range(2*v),k):
        mask=sum(1<<j for j in combi)
        out,steps=closure(nb,mask)
        if out==all_ones:
            shore=sum(j<v for j in combi)
            count[shore]+=1
            time_profile[(shore,steps)]+=1
    return count,time_profile

def main():
    expected={2:{0:7,1:28,3:28,4:7},3:{0:234,1:936,3:936,4:234},4:{0:11088,1:55440,2:100800,3:100800,4:55440,5:11088}}
    for q in (2,3,4):
        k=4 if q in (2,3) else 5
        neg,_=census(q,k-1)
        assert sum(neg.values())==0
        c,t=census(q,k)
        assert dict(c)==expected[q],(q,c)
        print('q',q,'min',k,'total',sum(c.values()),'shore',sorted(c.items()))
        print('rounds',sorted(t.items()))
    print('VERIFY_OK')
if __name__=='__main__':main()

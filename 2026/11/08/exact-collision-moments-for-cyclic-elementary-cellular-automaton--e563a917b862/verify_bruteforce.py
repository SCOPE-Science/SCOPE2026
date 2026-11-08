#!/usr/bin/env python3
"""Exhaustive cyclic Rule-4 output fibres, independently of transfer methods."""
from collections import Counter

def successor(x,n):
    z=0
    for i in range(n):
        if ((x>>i)&1) and not ((x>>((i-1)%n))&1) and not ((x>>((i+1)%n))&1):
            z|=1<<i
    return z

def fibfree(length):
    total=0
    for b in range(1<<length):
        s=[i for i in range(length) if (b>>i)&1]
        if all((i>0 and (b>>(i-1))&1) or (i+1<length and (b>>(i+1))&1) for i in s):
            total+=1
    return total

def expected_nonzero(y,n,sequence):
    sites=[i for i in range(n) if (y>>i)&1]
    assert sites
    d=[(sites[(k+1)%len(sites)]-sites[k])%n for k in range(len(sites))]
    if len(sites)==1:d=[n]
    assert min(d)>=2
    r=1
    for v in d:r*=sequence[max(v-3,0)]
    return r

if __name__=='__main__':
    sq=[fibfree(k) for k in range(17)]
    assert sq[:6]==[1,1,2,4,7,12]
    for n in range(3,17):
        fibres=Counter(successor(x,n) for x in range(1<<n))
        assert sum(fibres.values())==1<<n
        assert all(successor(y,n)==y for y in fibres)
        forbidden=sum(1 for y in range(1<<n) if successor(y,n)==0)
        assert fibres[0]==forbidden
        for y,c in fibres.items():
            if y:assert c==expected_nonzero(y,n,sq),(n,y,c)
        moment=sum(c*c for c in fibres.values())
        print(f'n={n:2} outputs={len(fibres):5} zero_fibre={fibres[0]:6} moment={moment:12}')
    print('PASS: all cyclic configurations through n=16; exact fibres and collision moments')

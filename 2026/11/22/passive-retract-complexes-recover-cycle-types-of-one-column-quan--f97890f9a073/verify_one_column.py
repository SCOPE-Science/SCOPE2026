#!/usr/bin/env python3
"""Exhaustive small-order checks of retractions omitting the active column."""
from collections import Counter
from itertools import product
from math import prod

def parts(n, lo=1):
    if n == 0:
        yield ()
    for i in range(lo, n+1):
        for p in parts(n-i,i):
            yield (i,)+p

def perm_from_parts(d):
    out=[0]
    a=1
    for k in d:
        for j in range(k):
            out.append(a+(j+1)%k)
        a+=k
    return out

def expected(d):
    r=len(d); p={}
    for mask in range(1,1<<r):
        s=mask.bit_count()
        count=prod(d[i] for i in range(r) if (mask>>i)&1)
        p[s]=p.get(s,0)+count*s**(r-s+1)
    return p

def brute(d):
    n=sum(d); p=perm_from_parts(d)
    def op(x,y): return p[x] if y==0 else x
    cnt=Counter()
    for v in product(range(1,n+1),repeat=n+1):
        if any(v[v[x]]!=v[x] for x in range(n+1)):
            continue
        if any(v[op(x,y)]!=op(v[x],v[y]) for x in range(n+1) for y in range(n+1)):
            continue
        cnt[len(set(v))]+=1
    return dict(cnt)

def main():
    cases=0
    for n in range(2,6):
        for d in parts(n):
            if all(x==1 for x in d):
                continue
            b=brute(d); e=expected(d)
            assert b==e,(d,b,e)
            cases+=1
    print('ONE_COLUMN_RETRACTION_EXHAUSTIVE_PASSED',cases)
if __name__=='__main__': main()

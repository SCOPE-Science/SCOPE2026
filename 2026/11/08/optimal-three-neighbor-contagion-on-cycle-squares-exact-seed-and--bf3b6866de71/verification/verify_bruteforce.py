#!/usr/bin/env python3
"""Independent graph-and-dynamics enumeration for cycle-square 3-bootstrap sets.
Uses no characterization of cyclic gaps. Enumerates all subsets for 5 <= n <= 18.
"""
from collections import Counter
from itertools import combinations

def stat(n):
    nbr=[{(i+d)%n for d in (-2,-1,1,2)} for i in range(n)]
    assert all(len(x)==4 for x in nbr)
    for size in range(n+1):
        times=Counter()
        for seeds in combinations(range(n),size):
            active=set(seeds)
            t=0
            while len(active)<n:
                new={v for v in range(n) if v not in active and len(nbr[v]&active)>=3}
                if not new:break
                active.update(new)
                t+=1
            if len(active)==n:times[t]+=1
        if times:return (size,times)
    raise AssertionError('no percolating set')

def predicted(n):
    k=n//3
    if n%3==0:return (k+1,Counter({k:n*k}))
    if n%3==1:return (k+1,Counter({k:n}))
    out=Counter({k:n*(k*k+k+2)//2})
    for t in range((k+1)//2,k):
        if t*2<k:continue
        out[t]=n//2 if 2*t==k else n
    return (k+2,out)

if __name__=='__main__':
    for n in range(5,19):
        got=stat(n)
        exp=predicted(n)
        assert got==exp,(n,got,exp)
        print(f'n={n} minimum_seed_size={got[0]} time_census={dict(sorted(got[1].items()))} PASS')
    print('PASS: exhaustive independent activation process 5..18')

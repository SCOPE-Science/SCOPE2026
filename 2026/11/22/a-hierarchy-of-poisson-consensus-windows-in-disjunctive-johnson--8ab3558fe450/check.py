"""Finite checks for disjunctive dynamics on Johnson graphs.
Run: python check.py
Requires only Python standard library.
"""
from itertools import combinations
from random import Random
from math import comb

def setup(n,k):
    vertices=[sum(1<<i for i in a) for a in combinations(range(n),k)]
    adj=[sum(1<<j for j,w in enumerate(vertices) if (v&w).bit_count()==k-1) for v in vertices]
    return vertices,adj

def step(state,adj):
    out=0
    for i,a in enumerate(adj):
        if a & state: out |= 1<<i
    return out

def covered(state, vertices, k, t):
    # Distance balls (t>=2 only); for the all-zero state return zero.
    out=0
    seeds=[v for j,v in enumerate(vertices) if state>>j&1]
    for i,v in enumerate(vertices):
        if any((v&s).bit_count()>=k-t for s in seeds):out|=1<<i
    return out

def test(n,k,trials,seed):
    vs,adj=setup(n,k); N=len(vs); rng=Random(seed)
    cases=[0,(1<<N)-1]+[(1<<i) for i in range(N)]
    for j in range(trials):
        if j%4==0: cases.append(1<<rng.randrange(N))
        elif j%4==1: cases.append(sum(1<<rng.randrange(N) for _ in range(1+ j%9)))
        else: cases.append(rng.getrandbits(N))
    checked=0
    for st in cases:
        x=st
        for t in range(1,k+1):
            x=step(x,adj)
            if t>=2:
                y=covered(st,vs,k,t)
                assert x==y,(n,k,t,st,x,y)
                if 2<=k-t<=k-2:
                    r=k-t
                    # all-k-set shadow witness iff all t-updated vertices active
                    seen=set()
                    for i,v in enumerate(vs):
                        if st>>i&1:
                            bits=[a for a in range(n) if v>>a&1]
                            seen.update(combinations(bits,r))
                    bad=0
                    for v in vs:
                        bits=[a for a in range(n) if v>>a&1]
                        if all(a not in seen for a in combinations(bits,r)):bad+=1
                    assert (x==(1<<N)-1)==(bad==0),(n,k,t,st,bad)
            checked+=1
    return checked,len(cases),N

if __name__=='__main__':
    total=0
    for n,k,trials in [(6,3,1400),(8,4,2000),(10,5,1000),(12,6,300)]:
        checks,cases,N=test(n,k,trials,n*100+k)
        print(f'PASS n={n} k={k} vertices={N} initial_states={cases} update_checks={checks}')
        total+=checks
    print('PASS total_update_checks',total)

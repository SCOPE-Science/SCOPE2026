#!/usr/bin/env python3
"""Exact complex rank certificate for three-term signed convolution on A5.

Requires numpy 2.3.5. A pair of prime-field rank tests and a Hadamard bound
proves every claimed characteristic-zero rank, not just lower bounds.
"""
from itertools import permutations
from collections import Counter
from math import comb
from pathlib import Path
import csv
import numpy as np

PRIMES=(1000000007,1000000009)
assert PRIMES[0]*PRIMES[1] > 2*3**30

def even(p):
    return sum(p[i]>p[j] for i in range(5) for j in range(i+1,5)) % 2 == 0

G=[p for p in permutations(range(5)) if even(p)]
S=list(permutations(range(5)))
assert len(G)==60 and len(S)==120 and G[0]==tuple(range(5))
ids={g:i for i,g in enumerate(G)}
compose=lambda x,y: tuple(x[y[k]] for k in range(5))
mult=np.array([[ids[compose(x,y)] for y in G] for x in G],dtype=np.int16)
inverse=np.array([next(j for j in range(60) if mult[i,j]==0) for i in range(60)])
conjugates=np.array([[ids[compose(compose(s,g),tuple(s.index(t) for t in range(5)))] for g in G] for s in S],dtype=np.int16)

def orbit(a,b):
    out=set()
    for s in range(120):
        out.add((int(conjugates[s,a]),int(conjugates[s,b])))
        out.add((int(conjugates[s,inverse[a]]),int(conjugates[s,mult[inverse[a],b]])))
    return out

# Basic arithmetic invariants and the split order-five conjugacy flag.
def element_order(a):
    x=0
    for n in range(1,61):
        x=int(mult[x,a])
        if x==0:return n
    raise AssertionError('invalid element order')
orders=[element_order(a) for a in range(60)]
assert Counter(orders)==Counter({1:1,2:15,3:20,5:24})
seed=orders.index(5)
five_class={int(conjugates[j,seed]) for j,h in enumerate(S) if even(h)}
assert len(five_class)==12
assert all((int(inverse[g]) in five_class)==(g in five_class) for g in range(60) if orders[g]==5)

def subgroup_size(a,b):
    reached={0};todo=[0]
    steps=(a,b,int(inverse[a]),int(inverse[b]))
    while todo:
        x=todo.pop()
        for s in steps:
            y=int(mult[x,s])
            if y not in reached:
                reached.add(y);todo.append(y)
    return len(reached)

def intrinsic_rank(a,b):
    e=int(mult[inverse[a],b])
    r=orders[a];st=tuple(sorted((orders[b],orders[e])))
    h=subgroup_size(a,b)
    if (r,st,h)==(3,(2,2),6):return 40
    if (r,st,h)==(3,(3,3),12):return 45
    if (r,st,h)==(3,(5,5),60) and ((b in five_class)==(e in five_class)):
        return 49
    if (r,st,h)==(2,(5,5),60):return 54
    if (r,st,h)==(5,(2,5),60):return 55
    if (r,st,h) in ((5,(2,3),60),(5,(3,3),60)):return 56
    return 60

def exact_mod_rank(a,b,p):
    # Matrix entry (x,y) is k(xy^{-1}), k=1_e+1_a-1_b.
    M=np.zeros((60,60),dtype=np.int64)
    for x in range(60):
        M[x,x]+=1
        M[x,int(mult[inverse[a],x])]+=1
        M[x,int(mult[inverse[b],x])]-=1
    M%=p
    rank=0
    for col in range(60):
        options=np.flatnonzero(M[rank:,col])
        if len(options)==0:
            continue
        pivot=rank+int(options[0])
        if pivot!=rank:
            M[[rank,pivot]]=M[[pivot,rank]]
        M[rank,col:]=(M[rank,col:]*pow(int(M[rank,col]),-1,p))%p
        affected=np.flatnonzero(M[rank+1:,col])+rank+1
        if len(affected):
            M[affected,col:]=(M[affected,col:]-M[affected,col,None]*M[rank,col:])%p
        rank+=1
        if rank==60: break
    return rank

def main():
    rows=list(csv.DictReader((Path(__file__).parent/'orbit_table.csv').open(encoding='utf-8')))
    assert len(rows)==23
    remaining={(a,b) for a in range(1,60) for b in range(1,60) if a!=b}
    by_pair={}
    total=Counter()
    for entry in rows:
        a,b=int(entry['a']),int(entry['b'])
        actual=orbit(a,b)
        assert actual <= remaining and (a,b)==min(actual)
        assert len(actual)==int(entry['normalized_pairs'])
        assert len(actual)*30 == int(entry['signed_kernels'])
        remaining-=actual
        for x,y in actual: by_pair[(x,y)]=int(entry['rank'])
        total[int(entry['rank'])]+=len(actual)*30
    assert not remaining and len(by_pair)==59*58
    # Explicitly test every normalized signed mask and the intrinsic test.
    for (a,b),expected in by_pair.items():
        assert intrinsic_rank(a,b)==expected,(a,b,'intrinsic',expected)
        for p in PRIMES:
            assert exact_mod_rank(a,b,p)==expected,(a,b,p,expected)
    assert sum(total.values())==comb(60,2)*58
    assert total==Counter({40:1800,45:3600,49:3600,54:3600,55:7200,56:10800,60:72060})
    print('EXACT PASS: all 3422 normalized kernels at both primes; 23 classes; 102660 signed kernels')
    print('RANK HISTOGRAM',sorted(total.items()))
    print('BOUNDS:',3**30, PRIMES[0]*PRIMES[1]);

if __name__=='__main__':main()

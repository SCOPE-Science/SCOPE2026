#!/usr/bin/env python3
"""Independent labelled-state checker, no symbolic quotient dependency."""
from itertools import product
from collections import Counter

def update(s,m):
    a=s[:m];b=s[m:]
    cnta=[a.count(i) for i in range(4)]
    cntb=[b.count(i) for i in range(4)]
    return tuple(((c+1)%4 if cntb[(c+1)%4]>=2 else c) for c in a)+tuple(
           ((c+1)%4 if cnta[(c+1)%4]>=2 else c) for c in b)

def entry_period(s,m):
    seen={};t=0
    while s not in seen:
        seen[s]=t
        s=update(s,m)
        t+=1
        assert t<64
    return seen[s],t-seen[s]

def from_counts(v):
    return tuple(c for c,t in enumerate(v) for _ in range(t))

def main():
    samples={}
    for m,n in ((1,1),(1,4),(2,3),(3,4),(4,4)):
        cp=Counter()
        for s in product(range(4),repeat=m+n):
            d,p=entry_period(s,m)
            assert d<=5 and p in (1,4,6)
            t=s
            for j in range(17):
                if j==5: at5=t
                t=update(t,m)
            assert at5==t
            cp[p]+=1
        samples[f'{m},{n}']=dict(sorted(cp.items()))
    s=from_counts((0,2,2,2))+from_counts((2,2,0,2))
    assert entry_period(s,6)==(0,6)
    s=from_counts((1,1,2,2))+from_counts((2,2,1,1))
    assert entry_period(s,6)==(1,6)
    s=from_counts((0,1,2,2))+from_counts((2,2,1,1))
    assert entry_period(s,5)==(5,1)
    print('exhaustive_labelled_counts='+str(samples),flush=True)
    print('direct_period_six_witnesses=2_passed',flush=True)
    print('direct_sharp_entry_five_witness=passed',flush=True)
    print('PASS',flush=True)
if __name__=='__main__':main()

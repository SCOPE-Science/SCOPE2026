#!/usr/bin/env python3
"""Independent finite Grassmannian comparison-trace and online-rank checks."""
from itertools import permutations, combinations
from collections import Counter
from functools import lru_cache

EXPECTED={2:[1,1],3:[1,3,2],4:[1,6,10],5:[1,10,30,6],6:[1,15,70,41],7:[1,21,140,161,10],8:[1,28,252,476,89]}

def permutations_one_descent(n):
    return [p for p in permutations(range(1,n+1)) if sum(p[i]>p[i+1] for i in range(n-1))<=1]

def analyze(n, online=True):
    qs=list(combinations(range(n),2))
    ps=permutations_one_descent(n)
    masks=[sum((p[i]>p[j])<<r for r,p in enumerate(ps)) for i,j in qs]
    full=(1<<len(ps))-1
    states=[((),[full])]
    poly=[1]
    while states:
        nxt=[]
        for selected, classes in states:
            for i in range(selected[-1]+1 if selected else 0,len(qs)):
                yes=masks[i]
                children=[c&yes for c in classes]+[c&~yes for c in classes]
                if all(children):nxt.append((selected+(i,),children))
        if not nxt:break
        poly.append(len(nxt))
        states=nxt
    assert poly == EXPECTED[n], (n,poly)
    if n==6:
        # independently check the critical local obstructions for every support up to size four
        for r in [3,4]:
            for ids in combinations(range(len(qs)),r):
                degrees=Counter(x for idx in ids for x in qs[idx])
                if r==3 and max(degrees.values())<3 and sum(d>=2 for d in degrees.values())<2:
                    continue
                if r==4:
                    pass
                traces={sum(((p[qs[i][0]]>p[qs[i][1]])<<j) for j,i in enumerate(ids)) for p in ps}
                assert len(traces)<(1<<r), (r,ids)
    print('n',n,'concepts',len(ps),'VC',len(poly)-1,'polynomial',poly,flush=True)
    if online:
        @lru_cache(None)
        def ldim(active):
            if active.bit_count()<2:return 0
            return max((1+min(ldim(active&mask),ldim(active&~mask)) for mask in masks if active&mask and active&~mask),default=0)
        ld=ldim(full)
        assert ld == n-1,(n,ld)
        print('Ldim',ld,'visited',ldim.cache_info().currsize,flush=True)

for n in range(2,9):analyze(n)
print('verified')

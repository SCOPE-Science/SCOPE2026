#!/usr/bin/env python3
"""Exact finite checks for rank-two local masks and adjacency overlaps."""
from itertools import permutations
from collections import Counter, defaultdict
from math import factorial

def signature(orders):
    n=len(orders[0]); r=len(orders)
    adj=[]
    for order in orders:
        adj.append({(order[i],order[i+1]) for i in range(n-1)})
    def mask(x,y):
        return tuple((i,sgn) for i,E in enumerate(adj) for sgn,a,b in ((1,x,y),(-1,y,x)) if (a,b) in E)
    types=frozenset(frozenset(mask(x,y) for y in range(n) if y!=x) for x in range(n))
    masks=frozenset(mask(x,y) for x in range(n) for y in range(n) if x!=y)
    counts=[sum((x,y) in adj[0] and ((x,y) if s==1 else (y,x)) in adj[1] for x in range(n) for y in range(n) if x!=y) for s in (1,-1)]
    endpoints={v for order in orders for v in (order[0],order[-1])}
    rare_pairs=[tuple(sorted((x,y))) for x in range(n) for y in range(x+1,n) if sum(((x,y) in e or (y,x) in e) for e in adj)>=2]
    rare_vertices=[v for x,y in rare_pairs for v in (x,y)]
    clean=(len(endpoints)==2*r and len(set(rare_vertices))==len(rare_vertices) and not(endpoints & set(rare_vertices)) and n>len(endpoints)+len(rare_vertices))
    support=tuple(z>0 for z in counts)
    return support,(types,masks),clean,counts

def run():
    for n in range(3,8):
        id_order=tuple(range(n)); counter=Counter(); grouped=defaultdict(set); clean_ct=0
        for p in permutations(range(n)):
            support,sig,clean,counts=signature((id_order,p))
            counter[tuple(counts)]+=1
            if clean:
                grouped[support].add(sig)
                clean_ct+=1
        for support,sigs in grouped.items():
            assert len(sigs)==1,(n,support,len(sigs))
        assert sum(counter.values())==factorial(n)
        meanpos=sum(key[0]*cnt for key,cnt in counter.items())/factorial(n)
        meanneg=sum(key[1]*cnt for key,cnt in counter.items())/factorial(n)
        assert abs(meanpos-(n-1)/n)<1e-12 and abs(meanneg-(n-1)/n)<1e-12
        print(n,'perms',factorial(n),'clean',clean_ct,'support_classes',len(grouped),'distinct_distributions',len(counter))
    print('RANK_TWO_SUCCESSOR_EXHAUSTIVE_OK')
if __name__=='__main__': run()

#!/usr/bin/env python3
"""Independent pair-of-one-factor enumeration of cycle-type orbit weights."""
import json
import itertools
from math import comb, prod, factorial
from collections import Counter


def perfect_matchings(items):
    if len(items) == 0:
        yield ()
    else:
        a=items[0]
        for j in range(1,len(items)):
            b=items[j]
            for m in perfect_matchings(items[1:j]+items[j+1:]):
                yield ((a,b),)+m

def partition_profile(P,Q,order):
    adj={v:set() for v in order}
    for a,b in P+Q:
        adj[a].add(b);adj[b].add(a)
    unseen=set(order);parts=[]
    while unseen:
        root=min(unseen); seen={root};todo=[root];unseen.remove(root)
        for v in todo:
            for w in adj[v]:
                if w not in seen:
                    seen.add(w);unseen.remove(w);todo.append(w)
        assert len(seen)%2==0
        parts.append(len(seen)//2)
    return tuple(sorted(parts))

def fodd(h):return prod(range(1,2*h,2))

def partitions(n,minimum=1):
    if n==0: yield ()
    else:
        for v in range(minimum,n+1):
            for rest in partitions(n-v,v):yield (v,)+rest

def weighted_orbit(n,k,lam):
    h=(n-k)//2
    cc=Counter(lam)
    z=prod(t**m*factorial(m) for t,m in cc.items())
    return comb(n,k)*fodd(h)*factorial(h)*2**(h-len(lam))//z

if __name__=='__main__':
    for n in range(3,9):
        total=0;degree_freq=Counter();types=0
        for h in range(n//2+1):
            k=n-2*h
            pairings=tuple(perfect_matchings(tuple(range(2*h))))
            actual=Counter(partition_profile(P,Q,tuple(range(2*h))) for P in pairings for Q in pairings)
            assert sum(actual.values())==fodd(h)**2
            for lam in partitions(h):
                count=comb(n,k)*actual[lam]
                prediction=weighted_orbit(n,k,lam)
                assert count==prediction,(n,k,lam,count,prediction)
                degree=2*h*(h-1)+comb(k,2)+lam.count(1)
                degree_freq[degree]+=count
                total+=count;types+=1
        assert sum(d*count for d,count in degree_freq.items())%2==0
        print(json.dumps({'n':n,'matchings':total,'flip_edges':sum(d*c for d,c in degree_freq.items())//2,'orbit_count':types,'degree_distribution':dict(sorted(degree_freq.items()))},sort_keys=True,separators=(',',':')))

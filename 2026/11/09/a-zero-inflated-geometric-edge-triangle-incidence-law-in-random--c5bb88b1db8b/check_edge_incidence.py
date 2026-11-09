#!/usr/bin/env python3
"""Finite consistency checks for the uniform simplex-attachment edge co-degree law.
This program tests finite transition identities; it does not prove asymptotics.
"""
from collections import Counter
from itertools import combinations
from math import sqrt
from random import Random

checks=0

def require(cond, msg):
    global checks
    assert cond, msg
    checks += 1

def cod_counts(n,edges):
    nbr=[set() for _ in range(n)]
    for a,b in edges:
        nbr[a].add(b);nbr[b].add(a)
    counts=Counter(len(nbr[a]&nbr[b]) for a,b in edges)
    return counts

def next_state(n, edges, item):
    e=set(edges)
    if isinstance(item,int):
        e.add((item,n))
    else:
        a,b=item
        e.add((a,n));e.add((b,n))
    return tuple(sorted(e))

states={tuple()}
for n in range(1,8):
    new_states=set()
    for edges in states:
        ecount=len(edges); H=n+ecount
        before=cod_counts(n,edges)
        require(sum(before.values())==ecount,(n,'edge identity',edges))
        require(sum(k*v for k,v in before.items())==3*(ecount-n+1),(n,'incidence identity',edges))
        all_items=list(range(n))+list(edges)
        sums=Counter()
        for item in all_items:
            dest=next_state(n,edges,item)
            after=cod_counts(n+1,dest)
            for k in set(before)|set(after):
                sums[k]+=after[k]-before[k]
            if isinstance(item,int):
                require(len(dest)==ecount+1,('vertex edge count',n,edges))
            else:
                require(len(dest)==ecount+2,('edge edge count',n,edges))
            new_states.add(dest)
        require(sums[0]==n-before[0],('k0 drift',n,edges,sums[0]))
        require(sums[1]==2*ecount+before[0]-before[1],('k1 drift',n,edges,sums[1]))
        for k in range(2,ecount+3):
            require(sums[k]==before[k-1]-before[k],('k>=2 drift',n,edges,k,sums[k]))
    print('states at n=',n,len(states))
    states=new_states

phi=(1+sqrt(5))/2
r=1/(phi+2)
q0=(3*sqrt(5)-5)/10
q1=3/5
require(abs(q0+q1/(1-r)-1)<1e-13,'normalization')
require(abs(q1/(1-r)**2-3*(phi-1)/phi)<1e-13,'mean incidence')
require(abs(q0-(1/(phi*(phi+2))))<1e-13,'q0 identities')
require(abs(q1-((2*phi+r)*r/phi))<1e-13,'q1 identities')

rng=Random(7462026)
n=1
c=[]
N=150000
while n<N:
    if rng.randrange(n+len(c))<n:
        c.append(0)
    else:
        chosen=rng.randrange(len(c));c[chosen]+=1;c.extend((1,1))
    n+=1
cnt=Counter(c)
require(abs(len(c)/N-phi)<0.025,'edge density sample')
require(abs(cnt[0]/len(c)-q0)<0.02,'q0 sample')
for k in range(1,7):
    require(abs(cnt[k]/len(c)-q1*r**(k-1))<0.02,('q sample',k))
require(sum(k*v for k,v in cnt.items())==3*(len(c)-N+1),'simulation incidence identity')
print('final n',N,'edges',len(c),'q0',cnt[0]/len(c),'q1',cnt[1]/len(c))
print('PASSED',checks,'checks')

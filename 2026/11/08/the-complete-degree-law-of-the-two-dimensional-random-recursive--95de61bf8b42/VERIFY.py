#!/usr/bin/env python3
"""Exact enumeration and numerical checks of RRSC(2) degree-increment identities."""
from fractions import Fraction
from collections import Counter,defaultdict
from math import sqrt, gamma
import random

def ncounts(edges, n):
    d=[0]*n
    for u,v in edges:d[u]+=1;d[v]+=1
    return Counter(d)

def next_state(edges,n,choice):
    # New vertex n attaches to chosen vertex or chosen old edge.
    if choice < n:
        add=((choice,n),)
    else:
        u,v=edges[choice-n]
        add=((u,n),(v,n))
    return tuple(sorted(edges+add))

def check_state(edges,n):
    c=ncounts(edges,n)
    den=n+len(edges)
    predicted={1:Fraction(n-2*c[1],den),
               2:Fraction(len(edges)+2*c[1]-3*c[2],den)}
    for k in range(3,n+2):
        predicted[k]=Fraction(k*c[k-1]-(k+1)*c[k],den)
    agg=Counter()
    for choice in range(den):
        cc=ncounts(next_state(edges,n,choice),n+1)
        for k in predicted:agg[k]+=cc[k]-c[k]
    for k in predicted:
        assert Fraction(agg[k],den)==predicted[k],(n,edges,k,agg[k],predicted[k])
    # total increment of degrees = twice number of new edges
    assert sum(k*(ncounts(next_state(edges,n,ch),n+1)[k]-c[k]) for ch in range(den) for k in range(1,n+2)) == 2*n + 4*len(edges), (n,edges)
    return den

states={((0,1),):Fraction(1)}
assertion_count=0
for n in range(2,8):
    states_new=defaultdict(Fraction)
    for edges,prob in states.items():
        assertion_count+=check_state(edges,n)
        den=n+len(edges)
        for ch in range(den):states_new[next_state(edges,n,ch)]+=prob/den
    assert sum(states.values())==1
    print('n',n,'states',len(states),'checks',assertion_count)
    states=states_new
assert sum(states.values())==1

phi=(1+sqrt(5))/2
pk=[0.,1/(phi+3.)]
pk.append((phi+2*pk[1])/(phi+4))
for k in range(3,100001):pk.append(k*pk[k-1]/(phi+k+2))
assert abs(sum(pk)-1)<1.e-10
assert abs(sum(k*x for k,x in enumerate(pk))-2*phi)<1.e-5
assert abs(pk[1]-(7-sqrt(5))/22)<1.e-15
assert abs(pk[2]-(45+14*sqrt(5))/209)<1.e-15

# Repeatable simulation of the actual *simplicial* process, not a degree-only surrogate.
rng=random.Random(41729)
n=90000
edges=[]
D=[0]
N=1
for step in range(1,n):
    choice=rng.randrange(N+len(edges))
    if choice<N:
        D[choice]+=1
        D.append(1)
        edges.append((choice,N))
    else:
        u,v=edges[choice-N]
        D[u]+=1;D[v]+=1
        D.append(2)
        edges.append((u,N));edges.append((v,N))
    N+=1
assert len(D)==n
assert sum(D)==2*len(edges)
print('edge_ratio',len(edges)/n,'phi',phi)
for k in range(1,9):
    freq=D.count(k)/n
    print('degree',k,'empirical',freq,'theoretical',pk[k])
    assert abs(freq-pk[k])<0.025
assert abs(len(edges)/n-phi)<0.03
print('PASSED',assertion_count,'exact transition terms and distribution/simulation sanity checks')

#!/usr/bin/env python3
"""Independent finite checks for threshold-half three-state excitation.
Runs all states on four small graphs; no third-party packages required.
"""
from itertools import product
from collections import Counter

def cycle(n):
    return [tuple(sorted({(i-1)%n, (i+1)%n})) for i in range(n)]

def disjoint(g,h):
    n=len(g)
    return g+[tuple(n+j for j in nbr) for nbr in h]

def complete_tripartite(a,b,c):
    parts=(range(a), range(a,a+b), range(a+b,a+b+c))
    return [tuple(w for j,p in enumerate(parts) if i!=j for w in p) for i,p0 in enumerate(parts) for v in p0]

def step(x,neighbors,theta):
    out=[]
    for v,z in enumerate(x):
        if z==1: out.append(2)
        elif z==2: out.append(0)
        else: out.append(1 if sum(x[w]==1 for w in neighbors[v])>=theta else 0)
    return tuple(out)

def orbit_period(x,neighbors,theta):
    seen={}
    t=0
    while x not in seen:
        seen[x]=t
        x=step(x,neighbors,theta)
        t+=1
    return seen[x],t-seen[x]

def census(graph,theta):
    n=len(graph)
    assert all(len(nbr)==2*theta for nbr in graph)
    counts=Counter()
    for state in product((0,1,2),repeat=n):
        entry,period=orbit_period(state,graph,theta)
        counts[period]+=1
        assert 12%period==0, (state,period)
    return dict(sorted(counts.items()))

if __name__=='__main__':
    tests=[('triangle',cycle(3),1),('square',cycle(4),1),
           ('disjoint_triangle_square',disjoint(cycle(3),cycle(4)),1),
           ('octahedron',complete_tripartite(2,2,2),2)]
    for name,g,theta in tests:
        print(name,'states',3**len(g),'eventual-period-state-populations',census(g,theta))
    witness=(0,1,2)+(0,0,1,2)
    seq=[]
    g=disjoint(cycle(3),cycle(4))
    x=witness
    for _ in range(13):
        seq.append(''.join(map(str,x)))
        x=step(x,g,1)
    assert seq[0]==seq[12]
    assert all(seq[i]!=seq[0] for i in range(1,12))
    print('primitive_twelve_witness',' -> '.join(seq))
    # C5 is 2-regular but its spectrum is not integral and supports period five.
    g=cycle(5)
    x=(0,0,0,1,2)
    seen=[]
    for i in range(5):
        seen.append(x)
        x=step(x,g,1)
    assert x==seen[0] and len(set(seen))==5
    print('nonintegral_C5_primitive_five_witness',seen[0])

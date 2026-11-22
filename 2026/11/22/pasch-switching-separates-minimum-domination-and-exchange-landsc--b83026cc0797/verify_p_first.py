#!/usr/bin/env python3
"""Independent point-subset-first exhaustive verification for STS(13) Levi graphs.
Uses only the Python standard library. Run: python3 verify_p_first.py
"""
from itertools import combinations
from collections import Counter
from hashlib import sha256

def designs():
    n=13
    starter=((1,3,9),(2,5,6))
    cyclic=sorted({tuple(sorted((x+t)%n for x in b)) for b in starter for t in range(n)})
    deleted={(2,4,10),(2,5,6),(4,6,12),(5,10,12)}
    inserted={(2,4,6),(2,5,10),(4,10,12),(5,6,12)}
    assert deleted.issubset(cyclic)
    return [('cyclic',cyclic),('switched',sorted((set(cyclic)-deleted)|inserted))]

def check_design(blocks):
    assert len(blocks)==26 and len(set(blocks))==26
    pair_count=Counter(pair for b in blocks for pair in combinations(b,2))
    assert len(pair_count)==78 and set(pair_count.values())=={1}
    return [sum(1<<x for x in b) for b in blocks]

def enumerate_p_first(blocks):
    B=check_design(blocks)
    ALL=(1<<13)-1
    states={}; layers=Counter()
    for P in range(1<<13):
        p=P.bit_count()
        if not 5<=p<=7:continue
        mandatory=[j for j,b in enumerate(B) if not b&P]
        extra=9-p-len(mandatory)
        if extra<0:continue
        allowed=[j for j,b in enumerate(B) if b&P]
        for E in combinations(allowed,extra):
            Q=tuple(sorted((*mandatory,*E)))
            covered=P
            for j in Q:covered|=B[j]
            if covered!=ALL:continue
            key=P|sum(1<<(13+j) for j in Q)
            assert key not in states
            states[key]=(p,extra==0)
            layers[p,extra==0]+=1
    return states,layers

def summary(states):
    keys=set(states)
    adjacency={x:[] for x in keys}
    for x in keys:
        elements=[i for i in range(39) if x>>i&1]
        absent=[i for i in range(39) if not x>>i&1]
        for i in elements:
            for j in absent:
                y=x^(1<<i)^(1<<j)
                if y in keys:adjacency[x].append(y)
    assert all(x in adjacency[y] for x in keys for y in adjacency[x])
    E=sum(map(len,adjacency.values()))//2
    components=[];seen=set()
    for x in keys:
        if x in seen:continue
        seen.add(x); todo=[x]; size=0
        while todo:
            z=todo.pop();size+=1
            for y in adjacency[z]:
                if y not in seen:seen.add(y);todo.append(y)
        components.append(size)
    digest=sha256(''.join(f'{x:010x}\n' for x in sorted(keys)).encode()).hexdigest()
    return E,Counter(components),Counter(map(len,adjacency.values())),digest

EXPECTED={
 'cyclic':(1456,{(5,True):195,(6,True):624,(6,False):507,(7,True):130},2652,{1:117,17:39,676:1}),
 'switched':(1511,{(5,True):195,(6,True):574,(6,False):612,(7,True):130},3192,{1:82,10:9,24:6,48:3,17:3,936:1,51:1,13:1}),
}
if __name__=='__main__':
    for name,blocks in designs():
        states,types=enumerate_p_first(blocks)
        edges,components,degrees,digest=summary(states)
        N,T,EE,CC=EXPECTED[name]
        assert len(states)==N and types==T and edges==EE and components==CC
        print(name,'N',len(states),'point-neat distribution',dict(sorted(types.items())),
              'edges',edges,'component sizes',dict(sorted(components.items())),
              'degrees',dict(sorted(degrees.items())), 'state SHA256',digest)
    print('PASS: both STS(13) types, exact optimum sets, and exchanges')

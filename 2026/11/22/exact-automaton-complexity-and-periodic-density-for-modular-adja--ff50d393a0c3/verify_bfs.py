#!/usr/bin/env python3
"""Independent breadth-first state construction and right-language refinement."""
from collections import deque, defaultdict
from itertools import product

def analyze(q,m):
    initial=('start',)
    dead=('dead',)
    def step(st, a):
        if st==initial:
            return (0,(0,)*(q*q)) if a==0 else dead
        if st==dead:return dead
        old,vec=st
        nxt=list(vec)
        nxt[old*q+a]=(nxt[old*q+a]+1)%m
        return (a,tuple(nxt))
    states=[initial]
    index={initial:0}
    todo=deque([initial])
    while todo:
        state=todo.popleft()
        for a in range(q):
            other=step(state,a)
            if other not in index:
                index[other]=len(states)
                states.append(other)
                todo.append(other)
    edges=[[index[step(state,a)] for a in range(q)] for state in states]
    accepting={i for i,st in enumerate(states) if len(st)==2 and isinstance(st[0],int) and st[0]==0 and not any(st[1])}
    partition=[set(accepting),set(range(len(states)))-accepting]
    rounds=0
    while True:
        cls={i:j for j,b in enumerate(partition) for i in b}
        refined=[]
        for block in partition:
            split=defaultdict(set)
            for x in block:
                split[tuple(cls[y] for y in edges[x])].add(x)
            refined.extend(split.values())
        if len(refined)==len(partition):break
        partition=refined
        rounds+=1
    d=q*q-q+1
    expectation=q*m**d+2
    assert len(states)==len(partition)==expectation
    assert len(accepting)==1
    # Direct word oracle checks every word of length <= 8, including empty.
    for n in range(9 if q==2 else 7):
        for word in product(range(q),repeat=n):
            at=0
            for a in word:at=edges[at][a]
            brute=(n>0 and word[0]==word[-1]==0 and all(sum(word[i]==x and word[i+1]==y for i in range(n-1))%m==0 for x in range(q) for y in range(q)))
            assert (at in accepting)==brute, (q,m,word)
    print(f'q={q} m={m} exponent={d} reachable={len(states)} minimal={len(partition)} refinement_rounds={rounds} direct_oracle=PASS')
    return edges,next(iter(accepting))

for q,m in ((2,2),(2,3),(2,4),(3,2)):
    analyze(q,m)

# Exact length-dependent density on alphabet size two; rational exact arithmetic.
edges,accept=analyze(2,2)
counts=[0]*len(edges)
counts[0]=1
for n in range(1,82):
    nxt=[0]*len(edges)
    for i,t in enumerate(edges):
        if counts[i]:
            for j in t:nxt[j]+=counts[i]
    counts=nxt
    if n in (1,3,5,9,15,25,41,81):
        from fractions import Fraction
        p=Fraction(counts[accept],2**n)
        print(f'length={n} accepted={counts[accept]} probability={float(p):.12f} exact={p}')

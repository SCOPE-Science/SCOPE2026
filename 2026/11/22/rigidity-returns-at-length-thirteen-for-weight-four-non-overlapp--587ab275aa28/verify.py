#!/usr/bin/env python3
"""Standalone exhaustive check for the binary weight-four length-13 nonoverlapping code."""
from itertools import combinations
from collections import defaultdict, Counter
from math import comb
from pathlib import Path

N, W = 13, 4

def rotations(s):
    return [s[i:] + s[:i] for i in range(len(s))]

def unbordered(s):
    return all(s[:k] != s[-k:] for k in range(1, len(s)))

def compatible(a, b):
    return all(a[:k] != b[-k:] and b[:k] != a[-k:] for k in range(1, N))

def build():
    groups = defaultdict(list)
    for ones in combinations(range(N), W):
        w = ''.join('1' if i in ones else '0' for i in range(N))
        if w[0] != '1' or w[-1] != '0' or not unbordered(w):
            continue
        groups[min(rotations(w))].append(w)
    return dict(sorted((neck, tuple(sorted(ws))) for neck,ws in groups.items()))

def exhaustive():
    groups=build()
    assert len(groups)==55
    assert Counter(map(len,groups.values()))=={1:24,2:28,3:3}
    assert sum(map(len, groups.values()))==89
    # Unique cross-bifix-free maximal size 55 must contain one member from each necklace.
    # Every compatible word starts with 1 and ends with 0 (or the reverse),
    # so this orientation covers all solutions modulo word reversal.
    opts={i:set(v) for i,v in enumerate(groups.values())}
    nodes=[0];sol=[]
    def search(domains, chosen):
        nodes[0]+=1
        while True:
            singleton=[(g,next(iter(v))) for g,v in domains.items() if len(v)==1]
            if not singleton:break
            g,w=singleton[0]
            del domains[g]
            if any(not compatible(w,x) for x in chosen):return
            chosen=chosen+(w,)
            # All other groups must retain at least one word compatible with w.
            for h in tuple(domains):
                domains[h]={v for v in domains[h] if compatible(w,v)}
                if not domains[h]:return
        if not domains:
            sol.append(tuple(sorted(chosen)));return
        g=min(domains,key=lambda x:(len(domains[x]),x))
        for w in sorted(domains[g]):
            nd={h:set(v) for h,v in domains.items() if h!=g}
            nd[g]={w}
            search(nd,chosen)
    search(opts,tuple())
    return groups,sol,nodes[0]

def main():
    groups,solutions,nodes=exhaustive()
    assert len(solutions)==1,(len(solutions),nodes)
    code=solutions[0]
    assert len(code)==55
    assert all(w.count('1')==W and len(w)==N and unbordered(w) for w in code)
    assert all(compatible(x,y) for x in code for y in code)
    assert len({min(rotations(w)) for w in code})==55
    # Named explicit threshold code with one-positions p1=1,p2<=4,p3<=7,p4<=10.
    threshold=tuple(sorted(''.join('1' if p+1 in (1,*vals) else '0' for p in range(N))
           for vals in combinations(range(2,11),3) if vals[0]<=4 and vals[1]<=7))
    assert code==threshold
    assert comb(N,W)//N==55
    # Independently replay the accompanying finite forcing certificate:
    # each row must have exactly one still feasible representative in its orbit.
    lines=Path(__file__).with_name('forcing.tsv').read_text(encoding='utf-8').splitlines()
    assert lines[0]=='necklace\tforced_word\toriginal_candidates'
    trace=[tuple(row.split('\t')) for row in lines[1:]]
    assert len(trace)==55
    active={neck:set(values) for neck,values in groups.items()}
    replay=[]
    for necklace,word,multiplicity in trace:
        assert necklace in active
        assert len(groups[necklace])==int(multiplicity)
        assert active[necklace]=={word}, (necklace,active[necklace])
        replay.append(word)
        del active[necklace]
        for key in active:
            active[key]={v for v in active[key] if compatible(word,v)}
            assert active[key]
    assert not active and tuple(sorted(replay))==code
    print('VERIFY_OK',len(code),'unique_oriented_optimum',len(solutions),'nodes',nodes)
if __name__=='__main__': main()

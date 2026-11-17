#!/usr/bin/env python3
"""Independent exact verifier via perfect matchings and two-factor decompositions."""
from collections import Counter
import itertools
import json
import pathlib

HERE=pathlib.Path(__file__).resolve().parent
cert=json.loads((HERE/'certificate.json').read_text(encoding='utf-8'))
N=20
raw=[]
for i in range(10):
    raw += [(i,(i+1)%10),(i,10+i),(10+i,10+(i+3)%10)]
E=sorted(set(tuple(sorted((u,v))) for u,v in raw))
assert len(E)==30
incident=[[] for _ in range(N)]
for i,(u,v) in enumerate(E):incident[u].append(i);incident[v].append(i)
matchings=[]
def enumerate_matchings(mask, chosen):
    if not mask:
        matchings.append(frozenset(chosen))
        return
    lowest=(mask & -mask).bit_length()-1
    for j in incident[lowest]:
        u,v=E[j]
        other=v if u==lowest else u
        if mask & (1<<other):
            enumerate_matchings(mask ^ (1<<lowest) ^ (1<<other), chosen+(j,))
enumerate_matchings((1<<N)-1,())
assert len(matchings)==60
ALL=frozenset(range(30))

def even_cycles(edges):
    """Trace disjoint cycles of a 2-factor, returning ordered edge-index tuples."""
    nbrs=[[] for _ in range(N)]
    for j in edges:
        u,v=E[j]
        nbrs[u].append((v,j));nbrs[v].append((u,j))
    assert all(len(x)==2 for x in nbrs)
    cycles=[];seen=set()
    for root in range(N):
        if root in seen:continue
        row=[];v=root;prev=-1
        while v not in seen:
            seen.add(v)
            available=[(w,e) for w,e in nbrs[v] if w!=prev]
            assert len(available)==(2 if prev==-1 else 1)
            w,j=min(available)
            row.append(j)
            prev,v=v,w
        assert v==root and len(row)%2==0
        cycles.append(tuple(row))
    return cycles

def key_triple(three):
    return tuple(sorted(tuple(sorted(m)) for m in three))

factorizations=set(); types=Counter()
for M in matchings:
    cycles=even_cycles(ALL-M)
    types[tuple(sorted(map(len,cycles)))]+=1
    for phases in itertools.product((0,1),repeat=len(cycles)):
        A=set();B=set()
        for cyc,p in zip(cycles,phases):
            A.update(cyc[p::2]);B.update(cyc[1-p::2])
        assert len(A)==len(B)==10 and A.isdisjoint(B)
        factorizations.add(key_triple((M,A,B)))
assert types=={(10,10):36,(20,):24},types
assert len(factorizations)==32,len(factorizations)

# Separately interpret every supplied colour string as an unordered triple of matchings.
read_states=[]
for s in cert['colourings']:
    assert len(s)==30
    colour_sets=[]
    for k in range(3):
        m={i for i,v in enumerate(s) if int(v)==k}
        assert len(m)==10 and all(len({i for i in m if i in incident[v]})==1 for v in range(N))
        colour_sets.append(m)
    read_states.append(key_triple(colour_sets))
assert len(read_states)==len(set(read_states))==32
assert set(read_states)==factorizations
state_index={s:i for i,s in enumerate(read_states)}

# Direct matching toggles; this is independent of the first verifier's colour-swap routine.
switch_edges=set()
for i,T in enumerate(read_states):
    for a,b in ((0,1),(0,2),(1,2)):
        A,B=frozenset(T[a]),frozenset(T[b])
        for cyc in even_cycles(A|B):
            toggle=frozenset(cyc)
            transformed=[frozenset(m) for m in T]
            transformed[a]=A^toggle
            transformed[b]=B^toggle
            j=state_index[key_triple(transformed)]
            if j!=i: switch_edges.add(tuple(sorted((i,j))))
assert len(switch_edges)==36
assert sorted([list(x) for x in switch_edges])==cert['switch_edges']
# Compare an explicit 20-state vertex bijection with the original Desargues edge set.
iso=dict(cert['large_component_to_GP'])
translated={tuple(sorted((iso[a],iso[b]))) for a,b in switch_edges if a in iso and b in iso}
assert translated==set(E)
assert len(cert['other_components'])==6
print('PERFECT_MATCHING_ENUMERATION_PASS 60 matchings=(36 double-10,24 Hamilton)')
print('MATCHING_TOGGLE_PASS 32 factorisations, 36 moves, 20-state GP(10,3), six K2')

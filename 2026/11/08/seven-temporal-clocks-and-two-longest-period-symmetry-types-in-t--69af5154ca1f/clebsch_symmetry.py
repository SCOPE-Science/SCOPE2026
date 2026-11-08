"""Graph automorphism orbit classification of primitive periodic orbits.
Uses only finite-state trajectories, graph automorphisms, no linear theory.
"""
import itertools
from collections import Counter
from pathlib import Path

ROOT=Path(__file__).parent
pow3=[3**i for i in range(16)]
gens=[1,2,4,8,15]

def successor(state):
    digits=[]
    for _ in range(16):
        digits.append(state%3)
        state//=3
    ret=0
    for i,d in enumerate(digits):
        if d==1: nd=2
        elif d==2: nd=0
        else: nd=int(any(digits[i^j]==1 for j in gens))
        ret+=pow3[i]*nd
    return ret

def canon_orbit(state, period):
    best=state; curr=state
    for _ in range(period-1):
        curr=successor(curr); best=min(best,curr)
    assert successor(curr)==state
    return best

def graph_automorphism_affine(perm, shift):
    # perm permutes the 5 generators, with the fifth equal to xor of first four.
    columns=[gens[perm[i]] for i in range(4)]
    vertex_map=[]
    for x in range(16):
        y=shift
        for i in range(4):
            if x>>i & 1:y^=columns[i]
        vertex_map.append(y)
    assert len(set(vertex_map))==16
    return vertex_map

def apply(state, vmap):
    out=0
    for i in range(16):
        out+=(state%3)*pow3[vmap[i]]
        state//=3
    return out

def validate_automorphisms():
    elements=set()
    for perm in itertools.permutations(range(5)):
        for shift in range(16):
            img=tuple(graph_automorphism_affine(perm,shift))
            elements.add(img)
            for u in range(16):
                assert {img[u^j] for j in gens}=={img[u]^j for j in gens}
    assert len(elements)==1920
    print("GRAPH: 1920 distinct affine automorphisms, all edge-preserving")

def analyze(period):
    f=ROOT/f'period{period}_reps.txt'; reps=sorted(set(map(int,f.read_text().splitlines())))
    assert len(reps)==(2400 if period==16 else 9600)
    lookup=set(reps)
    perms=[]
    for j in range(4):
        p=list(range(5));p[j],p[j+1]=p[j+1],p[j]
        perms.append(graph_automorphism_affine(p,0))
    for bit in [1,2,4,8]:perms.append(graph_automorphism_affine(list(range(5)),bit))
    unseen=set(reps);orbits=[]
    while unseen:
        first=min(unseen);unseen.remove(first);work=[first];orbit={first}
        for x in work:
            for pm in perms:
                y=canon_orbit(apply(x,pm),period)
                assert y in lookup,(period,x,y)
                if y not in orbit:
                    orbit.add(y);unseen.remove(y);work.append(y)
        orbits.append((first,len(orbit)))
    orbits.sort(key=lambda t:(t[1],t[0]))
    print(f'PERIOD {period}: cycles={len(reps)} symmetry_classes={len(orbits)} orbit_size_distribution={sorted(Counter(x[1] for x in orbits).items())}')
    print(f'PERIOD {period}: symmetry_orbit_representatives={orbits}')
    return orbits

if __name__=='__main__':
    validate_automorphisms()
    analyze(13)
    analyze(16)

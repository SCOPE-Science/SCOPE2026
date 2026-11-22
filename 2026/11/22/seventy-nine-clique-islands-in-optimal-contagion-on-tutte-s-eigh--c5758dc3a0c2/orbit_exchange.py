#!/usr/bin/env python3
"""Reproducible six-symbol orbits and single-vertex exchanges of tree complements."""
from collections import Counter
from itertools import permutations
from pathlib import Path

optima={int(s) for s in Path('optima.txt').read_text().splitlines()}
assert len(optima)==12780 and all(s.bit_count()==8 and 0<=s<(1<<30) for s in optima)
full=(1<<30)-1

def neighbors(s):
    x=s
    while x:
        a=x&-x;x-=a
        z=full^s
        while z:
            b=z&-z;z-=b
            y=s^a^b
            if y in optima:yield a,y

deg=Counter();total_arcs=0
for s in optima:
    moves=Counter(a for a,_ in neighbors(s))
    assert len(moves)==8 and set(moves.values())=={1},(s,moves)
    deg[sum(moves.values())]+=1
    total_arcs+=sum(moves.values())
assert deg=={8:12780} and total_arcs==102240
seen=set();components=[]
for seed in sorted(optima):
    if seed in seen:continue
    stack=[seed]; seen.add(seed); c={seed}
    while stack:
        s=stack.pop()
        for _,n in neighbors(s):
            if n not in seen:
                seen.add(n); c.add(n);stack.append(n)
    components.append(c)
assert Counter(map(len,components))=={9:70,12150:1}
shapes=Counter(tuple(Counter((x&32767).bit_count() for x in c)[j] for j in range(9)) for c in components if len(c)==9)
assert shapes=={(9,0,0,0,0,0,0,0,0):15,
               (0,0,0,0,0,0,0,0,9):15,
               (0,0,3,6,0,0,0,0,0):20,
               (0,0,0,0,0,6,3,0,0):20}

D=[(a,b) for a in range(6) for b in range(a+1,6)]
did={x:i for i,x in enumerate(D)}
M=[]
def rec(avail,cur):
    if not avail:
        M.append(tuple(sorted(cur))); return
    a=min(avail)
    for b in sorted(avail-{a}):
        rec(avail-{a,b},cur+[did[(a,b)]])
rec(set(range(6)),[])
mid={x:i for i,x in enumerate(M)}
assert len(M)==15
perm_maps=[]
for pi in permutations(range(6)):
    pm=[did[tuple(sorted((pi[a],pi[b])))] for a,b in D]
    pm.extend(15+mid[tuple(sorted(pm[e] for e in m))] for m in M)
    perm_maps.append(pm)

def transform(s, pm):
    y=0
    while s:
        a=s&-s;s-=a
        y|=1<<pm[a.bit_length()-1]
    return y

left=set(optima);sizes=Counter();orbits=[]
while left:
    rep=min(left)
    orbit={transform(rep,p) for p in perm_maps}
    assert orbit<=left
    left-=orbit
    sizes[len(orbit)]+=1
    orbits.append((rep,len(orbit),(rep&32767).bit_count()))
assert len(orbits)==40
assert sizes==Counter({15:2,60:2,90:3,120:4,180:4,360:19,720:6})
for j, expected in enumerate([225,720,1860,2280,2610,2280,1860,720,225]):
    assert sum(n for _,n,k in orbits if k==j)==expected
print('EXCHANGE_AND_ORBITS_OK','vertices',len(optima),'edges',total_arcs//2,'components',Counter(map(len,components)),'S6_orbits',len(orbits),'orbit_sizes',dict(sorted(sizes.items())))
print('island_profiles',dict(shapes))
print('orbit_representatives_as_decimal_bit_masks (mask, size, number_of_duads):')
for row in sorted(orbits):print(*row)

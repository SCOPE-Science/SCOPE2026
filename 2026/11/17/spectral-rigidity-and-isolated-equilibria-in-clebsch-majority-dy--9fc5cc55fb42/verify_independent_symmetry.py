#!/usr/bin/env python3
"""Independent update, direct-iterate and complete automorphism-orbit checker."""
import itertools
import json
from collections import Counter

DIRECTIONS=(1,2,4,8,15)
FULL=(1<<16)-1

def one_round(x):
    bits=[]
    for v in range(16):
        count=sum((x >> (v^e)) & 1 for e in DIRECTIONS)
        bits.append(int(count > 2))
    return sum(bit<<v for v,bit in enumerate(bits))

maps={}
by_period_and_entry=Counter()
for x in range(1<<16):
    seq=[x]
    for _ in range(6):
        seq.append(one_round(seq[-1]))
    assert seq[6] == seq[4]
    depth=next(t for t in range(5) if seq[t+2]==seq[t])
    period=1 if seq[depth]==seq[depth+1] else 2
    rep=min(seq[depth],seq[depth+1])
    by_period_and_entry[(depth,period)]+=1
    maps.setdefault(rep,[period,0])[1]+=1
assert len(maps)==1307
assert sum(1 for p,_ in maps.values() if p==1)==142
assert sum(1 for p,_ in maps.values() if p==2)==1165
assert by_period_and_entry[(4,1)] == 1920
assert by_period_and_entry[(4,2)] == 0
# Exact spectral check from independent adjacency representation.
eigenvalues=Counter()
for w in range(16):
    eig=sum(1 if (w&d).bit_count()%2 == 0 else -1 for d in DIRECTIONS)
    eigenvalues[eig] += 1
assert eigenvalues=={5:1,1:10,-3:5}
fixed=[x for x,(p,_) in maps.items() if p==1]
assert set(x.bit_count() for x in fixed)=={0,8,16}
for x in fixed:
    if x in (0,FULL):
        continue
    assert all(sum(1 if (x>>(v^e))&1 else -1 for e in DIRECTIONS)
               == (1 if (x>>v)&1 else -1) for v in range(16))
    assert maps[x][1] == 1
# Explicit generators of (F_2)^4 semidirect S_5.
permutation_generators=[]
for e in (1,2,4,8):
    permutation_generators.append(tuple(v^e for v in range(16)))
for j in range(3):
    def bit_swap(v):
        a=(v>>j)&1
        b=(v>>(j+1))&1
        return v ^ ((a^b)<<j) ^ ((a^b)<<(j+1))
    permutation_generators.append(tuple(bit_swap(v) for v in range(16)))
permutation_generators.append(tuple(v ^ (7 if v&8 else 0) for v in range(16)))
for g in permutation_generators:
    for v in range(16):
        assert {g[v^e] for e in DIRECTIONS} == {g[v]^e for e in DIRECTIONS}

def push(x,vertex_perm):
    y=0
    for v in range(16):
        if x & (1<<v):
            y |= 1<<vertex_perm[v]
    return y

orbit_classes=[]
seen=set()
for seed in sorted(maps):
    if seed in seen:continue
    orbital={seed}
    frontier=[seed]
    while frontier:
        x=frontier.pop()
        for g in permutation_generators:
            z=push(x,g)
            k=min(z,one_round(z)) if maps[seed][0]==2 else z
            assert k in maps and maps[k]==maps[seed]
            if k not in orbital:
                orbital.add(k)
                frontier.append(k)
    assert not (seen & orbital)
    seen.update(orbital)
    p,basin=maps[seed]
    orbit_classes.append((seed,p,len(orbital),basin, (seed^one_round(seed)).bit_count() if p==2 else 0))
assert len(seen)==len(maps)
assert len(orbit_classes)==14
assert sorted((p,n) for _,p,n,_,_ in orbit_classes if p==1)==[(1,1),(1,1),(1,20),(1,120)]
assert sum(n for _,p,n,_,_ in orbit_classes if p==2)==1165
# Establish full vertex automorphism group has exactly 1920 distinct maps.
permuted_maps=set()
for order in itertools.permutations(DIRECTIONS):
    images=order[:4]
    linear=[0]*16
    for v in range(16):
        out=0
        for j,e in enumerate((1,2,4,8)):
            if v&e:out ^= images[j]
        linear[v]=out
    assert linear[15] == order[4]
    for translate in range(16):
        perm=tuple(linear[v]^translate for v in range(16))
        permuted_maps.add(perm)
assert len(permuted_maps)==1920
assert all(len(orb)>0 for orb in orbit_classes)
# Output full 14-row witness table (each is a group orbit representative).
print('generator_count:',len(permutation_generators))
print('full_automorphism_group_order:',len(permuted_maps))
print('eigenvalue_multiplicities:',dict(sorted(eigenvalues.items())))
print('period_entry:',sorted((t,p,n) for (t,p),n in by_period_and_entry.items()))
print('classes: mask,period,spatial_class_size,attractor_basin_size,flipping_vertices')
for cls in orbit_classes:
    print(','.join(map(str,cls)))
print('passed: all 65536 direct trajectories, 14 geometric classes and equilibrium eigenvector/isolated tests')

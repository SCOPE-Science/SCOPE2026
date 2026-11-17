#!/usr/bin/env python3
"""Exact finite certificate for the affine-symplectic homology character of the Kummer biplane block complex."""
from collections import Counter
from itertools import combinations, product
from math import comb

F = lambda x: ((x & 1) ^ ((x >> 1) & 1) ^ ((x & 1) & ((x >> 1) & 1)))
Q = lambda x: F(x & 3) ^ F((x >> 2) & 3)
D = frozenset(x for x in range(16) if Q(x))
BLOCKS = [frozenset(u ^ d for d in D) for u in range(16)]
B = lambda a, b: Q(a ^ b) ^ Q(a) ^ Q(b)
FACES = sorted({tuple(sorted(s)) for block in BLOCKS for k in range(1,7)
                for s in combinations(sorted(block), k)}, key=lambda s:(len(s),s))
assert len(FACES) == 808
assert Counter(map(len,FACES)) == {1:16, 2:120, 3:320, 4:240, 5:96, 6:16}
assert all(sum(x in block and y in block for block in BLOCKS) == 2
           for x in range(16) for y in range(x+1,16))

# Basis-image enumeration of all symplectic linear maps, avoiding group libraries.
def linear_maps():
    count=0
    for images in product(range(1,16), repeat=4):
        if len(set(images)) < 4:
            continue
        table = [0]*16
        for x in range(1,16):
            bit = (x & -x).bit_length()-1
            table[x] = table[x ^ (1<<bit)] ^ images[bit]
        if len(set(table)) != 16:
            continue
        if any(B(images[i], images[j]) != B(1<<i, 1<<j)
               for i in range(4) for j in range(i+1, 4)):
            continue
        image_D = frozenset(table[x] for x in D)
        shifts = [s for s in range(16) if BLOCKS[s] == image_D]
        assert len(shifts) == 1
        count += 1
        yield table, shifts[0]
    assert count == 720

def fixed_cycles(perm):
    seen=set()
    cycles=[]
    for x in range(16):
        if x in seen: continue
        cycle=[]; y=x
        while y not in seen:
            seen.add(y); cycle.append(y); y=perm[y]
        cycles.append(cycle)
    return cycles

def closed_formula(perm, blockperm):
    cycles=fixed_cycles(perm)
    fixed={c[0] for c in cycles if len(c)==1}
    pairs=[frozenset(c) for c in cycles if len(c)==2]
    ff=len(fixed)
    result=ff-comb(ff,2)+len(pairs)-1
    for u in range(16):
        if blockperm[u] == u:
            fb=len(fixed & BLOCKS[u])
            tb=sum(p <= BLOCKS[u] for p in pairs)
            result+=1-fb+comb(fb,2)-tb
    return result

def signed_simplex_trace(perm):
    # Deliberately independent direct chain-level computation. Fixed oriented
    # simplices contribute the sign of the restriction and the dimension parity.
    total=0
    for face in FACES:
        image=[perm[x] for x in face]
        if set(image) != set(face):
            continue
        parity=0
        for j in range(len(image)):
            for k in range(j+1,len(image)):
                parity ^= int(image[j]>image[k])
        total += (-1 if (len(face)-1+parity)&1 else 1)
    return total-1  # H_0=Q; H_2 is the only positive rational homology.

traces=Counter(); n=0; total=0; trans=0; direct_diffs=0
for lin,shift in linear_maps():
    for t in range(16):
        perm=[lin[x]^t for x in range(16)]
        # Because image_D = shift + D, induced block map u -> L(u)+t+shift.
        blockperm=[lin[u]^t^shift for u in range(16)]
        assert all(frozenset(perm[x] for x in BLOCKS[u]) == BLOCKS[blockperm[u]]
                   for u in range(16))
        exact=closed_formula(perm,blockperm)
        direct=signed_simplex_trace(perm)
        assert exact==direct,(lin,shift,t,exact,direct)
        traces[exact]+=1; total+=exact; n+=1
        if lin==list(range(16)):
            trans+=exact
assert n==11520
assert dict(traces)=={-5:240,-1:4230,0:2304,1:4640,7:105,55:1}
assert total==0 and trans==160
print('KUMMER_CHARACTER_VERIFIED')
print('vertices=16 blocks=16 faces=808 linear_group=720 affine_group=11520')
print('character_distribution='+repr(sorted(traces.items())))
print('full_invariants=0 translation_invariants=10')
print('direct_signed_face_trace_checked_for_all_11520_elements')

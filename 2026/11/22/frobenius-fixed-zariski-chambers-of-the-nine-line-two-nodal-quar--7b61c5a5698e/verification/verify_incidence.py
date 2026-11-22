#!/usr/bin/env python3
"""Independent combinatorial chamber-support verifier (standard library only)."""
from itertools import permutations,combinations
from collections import Counter

# Exceptional curves e0..e4, roots A/B, cross-line curves L13,L14,L23,L24.
roots=(5,6); lines=((1,3),(1,4),(2,3),(2,4))

def admissible(mask):
    chosen=lambda i: bool(mask&(1<<i))
    # No two selected (-1)-curves may intersect.
    for a,b in combinations(tuple(range(5))+tuple(range(7,11)),2):
        intersects=(a<5 and b>=7 and a in lines[b-7]) or (b<5 and a>=7 and b in lines[a-7])
        if a>=7 and b>=7:intersects=(set(lines[a-7]).isdisjoint(lines[b-7]))
        if chosen(a) and chosen(b) and intersects:return False
    if chosen(5) and sum(chosen(i) for i in (0,1,2))>1:return False
    if chosen(6) and sum(chosen(i) for i in (0,3,4))>1:return False
    if chosen(5) and chosen(6) and chosen(0):return False
    return True

valid={m for m in range(1<<11) if admissible(m)}
assert len(valid)==221

def mapcurve(p):
    perm=list(p)
    perm+= [5 if {p[i] for i in (0,1,2)}=={0,1,2} else 6,
            6 if {p[i] for i in (0,3,4)}=={0,3,4} else 5]
    perm += [7+lines.index(tuple(sorted((p[a],p[b])))) for a,b in lines]
    assert len(perm)==11 and sorted(perm)==list(range(11))
    return perm

def transform(m,perm):return sum(1<<perm[i] for i in range(11) if m>>i&1)
reps={'identity':(0,1,2,3,4),'single_inner_swap':(0,2,1,3,4),
      'double_inner_swap':(0,2,1,4,3),'exchange_pairs':(0,3,4,1,2),
      'order_four':(0,3,4,2,1)}
expected={'identity':221,'single_inner_swap':61,'double_inner_swap':17,'exchange_pairs':23,'order_four':5}
for name,p in reps.items():
    fixed={m for m in valid if transform(m,mapcurve(p))==m}
    assert len(fixed)==expected[name],(name,len(fixed))
    poly=Counter((m.bit_count(),bool(m&(1<<5))+bool(m&(1<<6))) for m in fixed)
    print(name,sorted((k[0],k[1],v) for k,v in poly.items()))
G=[(0,)+a for a in permutations((1,2,3,4)) if {frozenset(a[:2]),frozenset(a[2:])}=={frozenset((1,2)),frozenset((3,4))}]
assert len(G)==8
acts=[mapcurve(p) for p in G]
fixed_sum=sum(sum(transform(m,p)==m for m in valid) for p in acts)
assert fixed_sum==416
print('burnside_orbits',fixed_sum//8)
assert fixed_sum//8==52
print('TWO_NODAL_QUARTIC_INCIDENCE_OK')

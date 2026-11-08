#!/usr/bin/env python3
"""Independent affine-plane classification and reconfiguration checks.

Constructs incidence from F_3^2 and the three available direction classes;
does not use the explicit labelled Pappus edge list or the direct verifier.
"""
from itertools import combinations
from collections import Counter
P=[(x,y) for x in range(3) for y in range(3)]
# full affine plane: 4 direction classes; missing class x+y=c.
classes=[]
for mode in range(4):
    group=[]
    for c in range(3):
        if mode==0: line=frozenset((x,y) for x,y in P if x==c)
        elif mode==1: line=frozenset((x,y) for x,y in P if y==c)
        elif mode==2: line=frozenset((x,y) for x,y in P if (y-x)%3==c)
        else: line=frozenset((x,y) for x,y in P if (x+y)%3==c)
        group.append(line)
    classes.append(group)
LINES=sum(classes[:3],[])
assert len(set(LINES))==9
POINT_ID={p:i for i,p in enumerate(P)}
LINE_ID={line:9+i for i,line in enumerate(LINES)}
NEIGH=[set() for _ in range(18)]
for line,idx in LINE_ID.items():
    for p in line:
        j=POINT_ID[p];NEIGH[j].add(idx);NEIGH[idx].add(j)
assert all(len(s)==3 for s in NEIGH)

def feasible(code):
    for v in range(18):
        if not (NEIGH[v]&code):return False
    obs=[frozenset(NEIGH[v]&code) for v in range(18) if v not in code]
    return len(obs)==len(set(obs))

codes=set(); keys={}
for W in classes[3]:
    for d,D in enumerate(classes[:3]):
        for E in D:
            q=next(iter(W&E))
            choices_p=E-W
            choices_l=[line for line in LINES if line not in D and q in line]
            assert len(choices_p)==2 and len(choices_l)==2
            choices=[]
            for p in choices_p:
                for line in choices_l:
                    code=frozenset({POINT_ID[x] for x in W}|{POINT_ID[p]}|
                                   {LINE_ID[t] for t in D}|{LINE_ID[line]})
                    assert len(code)==8 and feasible(code)
                    choices.append(code)
                    codes.add(code)
            assert len(set(choices))==4
            keys[(tuple(sorted(W)),d,tuple(sorted(E)))]=set(choices)
assert len(codes)==108 and len(keys)==27
assert set().union(*keys.values())==codes
assert sum(len(v) for v in keys.values())==108
# Independently scan all (4,4) point-line selections (126^2), and no others at weight 8.
full_codes=set()
for ps in combinations(range(9),4):
    for ls in combinations(range(9,18),4):
        c=frozenset(ps+ls)
        if feasible(c):full_codes.add(c)
assert full_codes==codes,(len(full_codes),len(codes))
# Counting argument: 3-point covers must be a missing-direction line, and
# a 3-line cover is a full available parallel class.
three_point_covers=[a for a in combinations(range(9),3) if all(any(POINT_ID[p] in a for p in l) for l in LINES)]
assert len(three_point_covers)==3
assert all(tuple(sorted(a)) in [tuple(sorted(POINT_ID[p] for p in W)) for W in classes[3]] for a in three_point_covers)
# All four-point covers and four-line covers have the geometric forms claimed.
Acover={frozenset(a) for a in combinations(range(9),4) if all(any(POINT_ID[p] in a for p in l) for l in LINES)}
Aform={frozenset({POINT_ID[p] for p in W}|{POINT_ID[p]}) for W in classes[3] for p in set(P)-W}
assert Acover==Aform and len(Acover)==18
Bcover={frozenset(b) for b in combinations(range(9,18),4) if all(any(idx in b for idx in NEIGH[POINT_ID[p]]) for p in P)}
Bform={frozenset({LINE_ID[l] for l in D}|{LINE_ID[l]}) for D in classes[:3] for l in set(LINES)-set(D)}
assert Bcover==Bform and len(Bcover)==18
# A one-token jump fixes W and D and changes precisely one of two local choices.
for block in keys.values():
    for s in block:
        assert sum(len(s^t)==2 for t in block if t!=s)==2
        assert not any(len(s^t)==2 and next(iter(t-s)) in NEIGH[next(iter(s-t))] for t in block if t!=s) # no adjacent relocation
for s in codes:
    other=[t for t in codes if len(s^t)==2]
    assert len(other)==2
    assert any(s in block and set(other)<block for block in keys.values())
print('GEOMETRY: affine-plane model, 27 blocks x 4 codes = 108')
print('GEOMETRY: all 18 four-point covers and 18 four-line covers classified')
print('GEOMETRY: all 4+4 feasible configurations coincide with geometric form')
print('GEOMETRY: exactly two token jumps per code, none between blocks')
print('GEOMETRY: PASS')

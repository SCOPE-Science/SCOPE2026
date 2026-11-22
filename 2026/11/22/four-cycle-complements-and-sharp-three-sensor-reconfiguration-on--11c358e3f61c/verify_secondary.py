#!/usr/bin/env python3
"""Independent set-based verification of one-erasure identifying codes on H(5,2)."""
from itertools import combinations, permutations
from collections import Counter,deque

# The labels of vertices are Python frozensets, entirely separate from bitmask
# incidence implementation in verify_main.cpp.
root = frozenset(range(5))
levels = [frozenset(c) for k in (2,3) for c in combinations(range(5),k)]
vertex_index = {x:i for i,x in enumerate(levels)}
closed=[]
for x in levels:
    closed.append(frozenset([x] + [y for y in levels if len(x)!=len(y) and (x<y or y<x)]))
assert len(levels)==20 and all(len(r)==4 for r in closed)
# Store each signature as a small bitmask; unique nonempty signatures after
# deletion of any single detector is an independent direct definition.
B=[sum(1<<vertex_index[z] for z in r) for r in closed]
FULL=(1<<20)-1
# Every rejected set has at least one violated local inequality; this method
# tests the failure of one-deletion identification by comparing post-deletion
# signatures rather than using the 2-distinguishing lemma.
def valid(m):
    signatures=[m&row for row in B]
    if any(x.bit_count()<2 for x in signatures): return False
    for i in range(20):
        if not (m>>i&1):continue
        one=m^(1<<i)
        seen=set()
        for row in B:
            code=one&row
            if code==0 or code in seen: return False
            seen.add(code)
    return True
# Downward closure of non-detector sets means checking all 9-deletions
# excludes all larger omissions. Test all 8-omissions and 9-omissions exactly.
optima=[]
for k in (8,9):
    count=0
    for omission in combinations(range(20),k):
        s=FULL
        for i in omission:s^=1<<i
        if valid(s):
            count+=1
            if k==8:optima.append(s)
    assert count==(15 if k==8 else 0),(k,count)

# Geometric predicted omissions: C_4 in K_5 with both points representing
# its edges and complementary triples representing its edges.
expected=set()
for four in combinations(range(5),4):
    four=frozenset(four)
    edges={frozenset(e) for e in combinations(four,2)}
    for diags in combinations(sorted(edges,key=lambda t:tuple(sorted(t))),2):
        if not diags[0].isdisjoint(diags[1]):continue
        squares=edges-set(diags)
        omit = squares | {root-e for e in squares}
        s=FULL
        for x in omit:s^=1<<vertex_index[x]
        expected.add(s)
assert len(expected)==15 and set(optima)==expected

# Each optimum must retain identification after each of its twelve detector
# positions is deleted; these 180 individual checks are already within valid().
# A separate complete finite enumeration evaluates the two-multiplicity
# criterion with Python integers, without the C++ certificate as input.
# This also verifies the complete weight polynomial and TAR threshold.
separations=[B[i]^B[j] for i in range(20) for j in range(i+1,20)]
hist=Counter()
all_codes=set()
for s in range(FULL+1):
    if any((s & row).bit_count()<2 for row in B):continue
    if any((s & row).bit_count()<2 for row in separations):continue
    hist[s.bit_count()]+=1
    all_codes.add(s)
assert hist==Counter({12:15,13:120,14:680,15:1824,16:2155,
                     17:940,18:190,19:20,20:1})
assert len(all_codes)==5945

def reach(b):
    start=min(optima)
    seen={start};q=deque([start])
    while q:
        s=q.popleft()
        for i in range(20):
            t=s^(1<<i)
            if t.bit_count()<=b and t in all_codes and t not in seen:
                seen.add(t);q.append(t)
    return len(seen.intersection(optima))
assert tuple(reach(b) for b in (12,13,14,15))==(1,1,1,15)
print('INDEPENDENT_DIRECT_ERASURE_OK',len(expected),'optima and zero size-11 codes')
print('INDEPENDENT_ALL_WEIGHT_AND_TAR_OK',len(all_codes))

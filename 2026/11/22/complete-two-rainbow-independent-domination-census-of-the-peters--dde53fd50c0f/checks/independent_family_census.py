#!/usr/bin/env python3
"""Different exact method: independent-edge-family pairs and uncovered-edge test."""
from itertools import combinations
from collections import Counter
from hashlib import sha256
edges = list(combinations(range(5), 2))
edge_masks = [(1<<a)|(1<<b) for a,b in edges]
nonintersect = [sum(1<<j for j in range(10) if edge_masks[i]&edge_masks[j]==0) for i in range(10)]
allmask = (1<<10)-1
families=[]
for mask in range(1,1<<10):
    ids = [j for j in range(10) if mask>>j&1]
    if any(nonintersect[j]&mask for j in ids):continue
    families.append((mask, ids))
assert len(families) == 75

def ftype(ids):
    n=len(ids)
    if n<3: return str(n)
    common=31
    for i in ids: common &= edge_masks[i]
    return str(n)+('S' if common else 'T')
assert Counter(ftype(ids) for _,ids in families)=={'1':10,'2':30,'3S':20,'3T':10,'4S':5}
counts=Counter(); ledger=bytearray(3**10)
for A, aids in families:
    for B, bids in families:
        if A&B:continue
        Z=allmask^(A|B)
        # Equivalence: every zero edge is disjoint from at least one member of EACH class.
        if any((nonintersect[i]&A)==0 or (nonintersect[i]&B)==0 for i in range(10) if Z>>i&1):continue
        counts[(ftype(aids),ftype(bids))]+=1
        idx=0
        for v in range(10): idx=3*idx+(1 if A>>v&1 else 2 if B>>v&1 else 0)
        assert not ledger[idx]
        ledger[idx]=1
assert counts=={('3T','3T'):30,('3S','4S'):20,('4S','3S'):20,('3T','4S'):20,('4S','3T'):20},counts
assert sum(ledger)==110
print('EXACT_FAMILY_OK', sorted(counts.items()))
print('membership_sha256',sha256(ledger).hexdigest())

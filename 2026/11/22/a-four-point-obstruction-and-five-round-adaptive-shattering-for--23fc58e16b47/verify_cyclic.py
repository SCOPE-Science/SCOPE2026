#!/usr/bin/env python3
"""Separate cyclic-difference-set model of the order-three projective plane.
No use of certificate.json or coordinates; Python 3.10+ only.
"""
from collections import Counter
from functools import lru_cache
from itertools import combinations
D=(0,1,3,9)
assert Counter((a-b)%13 for a in D for b in D if a!=b)==Counter({j:1 for j in range(1,13)})
lines=[sum(1<<((i+d)%13) for d in D) for i in range(13)]
concepts=[lines[a]^lines[b] for a,b in combinations(range(13),2)]
assert len(set(concepts))==78
assert all(c.bit_count()==6 for c in concepts)
counts=[0]*14
facets_by_size=Counter()
shattered=set()
for s in range(1<<13):
    seen={sum((c>>j&1)<<r for r,j in enumerate(t for t in range(13) if s>>t&1)) for c in concepts}
    if len(seen)==1<<s.bit_count():
        shattered.add(s)
        counts[s.bit_count()]+=1
for s in shattered:
    if not any(s|1<<j in shattered for j in range(13) if not s>>j&1):
        facets_by_size[s.bit_count()]+=1
assert counts[:6]==[1,13,78,286,702,0]
assert all(v==0 for v in counts[5:])
assert facets_by_size==Counter({4:702})
for s in range(1<<13):
    if s.bit_count()==4:
        assert (s in shattered)==all((s&l)!=l for l in lines)

# Recursive Littlestone feasibility, independent of the displayed witness tree.
positive=[sum(1<<h for h,c in enumerate(concepts) if c>>j&1) for j in range(13)]
@lru_cache(None)
def full_tree(h,d):
    if d==0: return h!=0
    if h.bit_count()<1<<d:return False
    return any(full_tree(h&p,d-1) and full_tree(h&~p,d-1) for p in positive)
allhypotheses=(1<<78)-1
assert full_tree(allhypotheses,5)
assert not full_tree(allhypotheses,6)
assert Counter(sum(bool(c>>j&1) for c in concepts) for j in range(13))==Counter({36:13})
print('TERNARY_TWO_LINE_XOR_CYCLIC_PASS concepts=78 VC=4 Ldim=5 facets=702')

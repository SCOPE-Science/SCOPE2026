#!/usr/bin/env python3
"""Exact finite topology certificate for a six-vertex cyclic multipartite digraph.
The input graph and every face are generated here; no external files or packages.
"""
from collections import Counter, defaultdict, deque

VERTICES = range(6)
ARCS = tuple((2*i+a, 2*((i+1)%3)+b)
             for i in range(3) for a in range(2) for b in range(2))
PIVOT_ORDER = (1,9,8,5,10,2,3,7,4,0,11,6)

def faces():
    valid = set()
    for mask in range(1 << len(ARCS)):
        es = [arc for j, arc in enumerate(ARCS) if mask & (1 << j)]
        if len({a for a,b in es}) != len(es) or len({b for a,b in es}) != len(es):
            continue
        nxt = dict(es)
        has_cycle = False
        for start in nxt:
            seen = set()
            node = start
            while node in nxt and node not in seen:
                seen.add(node)
                node = nxt[node]
            if node in seen:
                has_cycle = True
                break
        if not has_cycle:
            valid.add(mask)
    return valid

F = faces()
assert len(ARCS)==12
assert Counter(f.bit_count() for f in F) == {0:1,1:12,2:54,3:104,4:84,5:24}
assert all(f & (f-1) in F for f in F if f)
PRESENT = F - {0}

# First available pivot per simplex: a complete lexicographic acyclic matching.
remaining = set(PRESENT)
pairs = []
for vertex in PIVOT_ORDER:
    bit = 1 << vertex
    for lower in sorted((x for x in remaining if not x & bit),
                        key=lambda x:x.bit_count(), reverse=True):
        higher = lower | bit
        if lower in remaining and higher in remaining:
            remaining.remove(lower)
            remaining.remove(higher)
            pairs.append((lower,higher))
assert len(pairs)==134
assert len(remaining)==10
assert Counter(f.bit_count()-1 for f in remaining)=={0:1,2:1,3:4,4:4}

# Check the Forman orientation of the ENTIRE face-incidence graph is acyclic.
partner = dict(pairs)
out, indegree = defaultdict(list), {f:0 for f in PRESENT}
incidences = 0
for higher in PRESENT:
    for i in range(len(ARCS)):
        if not higher & (1<<i):
            continue
        lower = higher ^ (1<<i)
        if lower == 0:
            continue
        incidences+=1
        start, end = ((lower,higher) if partner.get(lower)==higher else (higher,lower))
        out[start].append(end)
        indegree[end]+=1
queue=deque(f for f,d in indegree.items() if not d)
visited=0
while queue:
    vertex=queue.popleft(); visited+=1
    for to in out[vertex]:
        indegree[to]-=1
        if indegree[to]==0:queue.append(to)
assert visited==len(PRESENT), 'gradient cycle'

# Integral algebraic Morse cancellations; all pivots are units, so the
# reduced chain complex is chain-homotopy equivalent over Z to the original.
boundary={}
for simplex in PRESENT:
    indices=[i for i in range(len(ARCS)) if simplex & (1<<i)]
    boundary[simplex]={}
    if len(indices)>1:
        for position,i in enumerate(indices):
            boundary[simplex][simplex ^ (1<<i)]=(-1)**position
live=set(PRESENT)
unused=set(pairs)
cancellations=0
while unused:
    pair=next(((a,b) for a,b in sorted(unused)
               if a in live and b in live and abs(boundary[b].get(a,0))==1),None)
    assert pair is not None, 'no unit-pivot order'
    lower,higher=pair
    factor=boundary[higher][lower]
    col=boundary[higher].copy()
    for other in list(live):
        if other in pair:continue
        coefficient=boundary[other].get(lower,0)
        if coefficient:
            for face, val in col.items():
                new=boundary[other].get(face,0)-coefficient*factor*val
                if new:boundary[other][face]=new
                else:boundary[other].pop(face,None)
        boundary[other].pop(lower,None)
        boundary[other].pop(higher,None)
    live.remove(lower);live.remove(higher)
    unused.remove(pair)
    cancellations+=1
assert live==remaining
assert all(not boundary[f] for f in remaining), 'nonzero integral Morse boundary'
assert cancellations==134
print('FACES_0_TO_4=12,54,104,84,24')
print('HASSE_INCIDENCES=%d' % incidences)
print('MATCHED_PAIRS=134 CRITICAL_0_2_3_4=1,1,4,4')
print('INTEGRAL_MORSE_BOUNDARIES_ZERO')
print('ALL_VERIFY_OK')

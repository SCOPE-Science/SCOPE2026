#!/usr/bin/env python3
"""Independent, stdlib-only verification of a finite graph-Hom collapse certificate.
Usage: python verify_hom.py collapse_pairs.json
"""
import collections
import itertools
import json
import sys

N = 11
E = set()
for i in range(5):
    E.add(tuple(sorted((i, (i+1)%5))))
    for j in ((i-1)%5, (i+1)%5):
        E.add(tuple(sorted((i+5,j))))
    E.add((i+5,10))
assert len(E)==20
ADJ = [set() for _ in range(N)]
for i,j in E:
    ADJ[i].add(j)
    ADJ[j].add(i)
assert all(not (ADJ[i] & ADJ[j]) for i,j in E)  # triangle-free
assert not any(i != j and ADJ[i] <= ADJ[j] for i in range(N) for j in range(N))  # no target folds
assert all(b in ADJ[a] for a,b in [(0,6),(6,10),(10,9),(9,0)])  # a square

def compatible(box):
    return all(all(b in ADJ[a] for a in bits(box[i]) for b in bits(box[(i+1)%5])) for i in range(5))

def bits(mask):
    return [k for k in range(N) if mask & (1<<k)]

def dimension(box):
    return sum(x.bit_count()-1 for x in box)

def codimension_one(box):
    ans=[]
    for j,mask in enumerate(box):
        if mask.bit_count()>=2:
            for a in bits(mask):
                smaller=list(box)
                smaller[j]^=1<<a
                ans.append(tuple(smaller))
    return ans

# Every graph homomorphism from the five-cycle is a length-5 closed walk.
# Every multi-homomorphism can be reached from one singleton map by
# successively adding elements to coordinate sets: each intermediate box
# remains a multi-homomorphism.
zero = set()
for walk in itertools.product(range(N),repeat=5):
    if all(walk[(i+1)%5] in ADJ[walk[i]] for i in range(5)):
        zero.add(tuple(1<<k for k in walk))
assert len(zero)==310
# Independent numerical cross-check: trace of the fifth adjacency power.
a = [[int(j in ADJ[i]) for j in range(N)] for i in range(N)]
power=[[int(i==j) for j in range(N)] for i in range(N)]
for _ in range(5):
    power=[[sum(power[i][k]*a[k][j] for k in range(N)) for j in range(N)] for i in range(N)]
assert sum(power[i][i] for i in range(N))==310

all_boxes = set(zero)
frontier=set(zero)
while frontier:
    next_frontier=set()
    for box in frontier:
        for k in range(5):
            common=set(range(N))
            for j in ((k-1)%5,(k+1)%5):
                for b in bits(box[j]):
                    common &= ADJ[b]
            for b in common:
                if not box[k] & (1<<b):
                    larger=list(box)
                    larger[k]|=1<<b
                    next_frontier.add(tuple(larger))
    next_frontier-=all_boxes
    all_boxes.update(next_frontier)
    frontier=next_frontier

cells = {d: {x for x in all_boxes if dimension(x)==d} for d in range(3)}
assert len(all_boxes)==960
assert [len(cells[d]) for d in range(3)]==[310,500,150]
assert all(dimension(x)<=2 for x in all_boxes)
assert all(sum(x.bit_count()==2 for x in sq)==2 for sq in cells[2])
assert all(len(codimension_one(sq))==4 for sq in cells[2])
assert all(compatible(x) for x in all_boxes)
assert all(c in cells[1] for sq in cells[2] for c in codimension_one(sq))
assert all(c in cells[0] for e in cells[1] for c in codimension_one(e))

with open(sys.argv[1],encoding='utf-8') as f:
    certificate=json.load(f)
assert certificate['format']=='graph-hom-2cell-free-edge-collapses-v1'
pairs=certificate['pairs']
assert len(pairs)==150
remain2=set(cells[2]); remain1=set(cells[1])
for step,pair in enumerate(pairs):
    edge=tuple(pair['edge']);square=tuple(pair['square'])
    assert edge in remain1 and square in remain2, ('missing',step)
    assert edge in codimension_one(square), ('not facet',step)
    containing=[s for s in remain2 if edge in codimension_one(s)]
    assert containing==[square], ('not free',step)
    remain2.remove(square);remain1.remove(edge)
assert not remain2 and len(remain1)==350
# Remaining 1-skeleton: every 1-cell is an interval with two distinct endpoints.
neighbor=collections.defaultdict(set)
for edge in remain1:
    ends=codimension_one(edge)
    assert len(ends)==2 and ends[0]!=ends[1]
    neighbor[ends[0]].add(ends[1]);neighbor[ends[1]].add(ends[0])
start=min(cells[0]);seen={start};todo=[start]
for vertex in todo:
    for nxt in sorted(neighbor[vertex]):
        if nxt not in seen:
            seen.add(nxt);todo.append(nxt)
assert seen==cells[0], ('disconnected',len(seen))
assert len(todo)==310  # supplies a spanning tree of 309 edges
beta1=len(remain1)-len(cells[0])+1
assert beta1==41
print('GRAPH: 11 vertices, 20 edges; triangle-free with a 4-cycle')
print('HOM(C5,G): f-vector (310, 500, 150), dimension 2')
print('INDEPENDENT CHECK: trace(A^5)=310')
print('CERTIFICATE: 150 valid elementary free-edge square collapses')
print('RESIDUAL GRAPH: 310 vertices, 350 edges, connected')
print('HOMOTOPY TYPE: wedge of 41 circles')
print('STATUS: PASS')

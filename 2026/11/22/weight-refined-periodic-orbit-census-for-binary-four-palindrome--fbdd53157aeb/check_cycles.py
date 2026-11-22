#!/usr/bin/env python3
"""Exact elementary-cycle determinant certificate for a binary avoidance shift.

No external packages are required.
"""
from collections import defaultdict
from itertools import combinations

V=range(8)
edges={v:[] for v in V}
for v in V:
    for b in (0,1):
        word=f'{2*v+b:04b}'
        if word!=word[::-1]:
            edges[v].append(((2*v+b)%8,b))

cycles=[]
for start in V:
    def visit(path,bits):
        for endpoint,bit in edges[path[-1]]:
            if endpoint==start and len(path)>1:
                if start==min(path):
                    cycles.append((tuple(path),tuple(bits+[bit])))
            elif endpoint not in path and endpoint>start:
                visit(path+[endpoint],bits+[bit])
    visit([start],[])
assert len(cycles)==6
assert sorted((len(v),sum(bits)) for v,bits in cycles)==[(2,1),(4,1),(4,3),(6,3),(8,4),(8,4)]

# A determinant is a signed sum over vertex-disjoint directed-cycle families.
poly=defaultdict(int)
poly[(0,0)]=1
families=[]
for r in range(1,7):
    for indices in combinations(range(6),r):
        used=[]
        for i in indices: used.extend(cycles[i][0])
        if len(set(used))!=len(used): continue
        exponent=(sum(len(cycles[i][0]) for i in indices),
                  sum(sum(cycles[i][1]) for i in indices))
        poly[exponent]+=(-1)**r
        families.append((indices,exponent))
expected={(0,0):1,(2,1):-1,(4,1):-1,(4,3):-1,(6,3):-1}
assert {k:v for k,v in poly.items() if v}==expected
print('ELEMENTARY CYCLES')
for vertices,bits in cycles:
    print('vertices',vertices,'length',len(vertices),'ones',sum(bits))
print('NONEMPTY DISJOINT FAMILIES',families)
print('DETERMINANT TERMS',dict(sorted((k,v) for k,v in poly.items() if v)))

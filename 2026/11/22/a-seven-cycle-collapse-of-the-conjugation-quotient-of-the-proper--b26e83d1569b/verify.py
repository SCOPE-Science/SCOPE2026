#!/usr/bin/env python3
"""Exhaustive finite verification of a subgroup-poset orbit-space collapse."""
import json,sys
from itertools import permutations
from collections import deque,Counter

def main(cert):
    group=list(permutations(range(4)))
    lookup={p:i for i,p in enumerate(group)}
    identity=lookup[tuple(range(4))]
    m=len(group)
    multiply=[[lookup[tuple(a[b[k]] for k in range(4))] for b in group] for a in group]
    inverses=[next(j for j in range(m) if multiply[i][j]==identity) for i in range(m)]
    def closure(gens):
        elements={identity}|set(gens)
        while True:
            old=len(elements)
            elements|={multiply[a][b] for a in tuple(elements) for b in tuple(elements)}
            if len(elements)==old:return frozenset(elements)
    found={frozenset({identity})}; queue=deque(found)
    while queue:
        subgroup=queue.popleft()
        for g in range(m):
            if g in subgroup:continue
            enlarged=closure(set(subgroup)|{g})
            if enlarged not in found:
                found.add(enlarged);queue.append(enlarged)
    assert len(found)==30
    subgroups=sorted((h for h in found if 1<len(h)<m),key=lambda h:(len(h),tuple(sorted(h))))
    idx={h:i for i,h in enumerate(subgroups)}
    strict={(i,j) for i in range(len(subgroups)) for j in range(len(subgroups)) if subgroups[i]<subgroups[j]}
    chains={0:{(i,) for i in range(len(subgroups))},1:strict,2:set()}
    for i,j in strict:
        for k in range(len(subgroups)):
            if subgroups[j]<subgroups[k]:chains[2].add((i,j,k))
    assert list(map(lambda d:len(chains[d]),range(3)))==[28,63,24]
    acts=[[idx[frozenset(multiply[multiply[g][x]][inverses[g]] for x in h)] for h in subgroups] for g in range(m)]
    def orbit(chain):return min(tuple(act[i] for i in chain) for act in acts)
    cells={d:sorted({orbit(c) for c in chains[d]}) for d in range(3)}
    assert [len(cells[d]) for d in range(3)]==[9,15,6]
    index={d:{c:i for i,c in enumerate(cells[d])} for d in range(3)}
    faces={d:[tuple(index[d-1][orbit(c[:j]+c[j+1:])] for j in range(d+1)) for c in cells[d]] for d in (1,2)}
    for j,face_ids in enumerate(faces[2]):
        boundary={}
        for k,e in enumerate(face_ids):
            a,b=faces[1][e]
            boundary[b]=boundary.get(b,0)+(-1)**k
            boundary[a]=boundary.get(a,0)-(-1)**k
        assert all(t==0 for t in boundary.values()),j
    active={d:set(range(len(cells[d]))) for d in range(3)}
    assert len(cert['collapses'])==8
    for d,upper,lower in cert['collapses']:
        assert d in (1,2) and upper in active[d] and lower in active[d-1]
        assert lower in faces[d][upper]
        containing=[e for e in active[d] if lower in faces[d][e]]
        assert containing==[upper],(d,upper,lower,containing)
        if d==1:
            assert not any(upper in faces[2][t] for t in active[2])
        active[d].remove(upper);active[d-1].remove(lower)
    assert [len(active[d]) for d in range(3)]==[7,7,0]
    degree=Counter()
    adjacency={v:set() for v in active[0]}
    for e in active[1]:
        a,b=faces[1][e]
        assert a!=b and a in active[0] and b in active[0]
        degree[a]+=1;degree[b]+=1
        adjacency[a].add(b);adjacency[b].add(a)
    assert all(degree[v]==2 for v in active[0])
    reached={next(iter(active[0]))};todo=list(reached)
    while todo:
        for n in adjacency[todo.pop()]:
            if n not in reached:reached.add(n);todo.append(n)
    assert reached==active[0]
    assert sorted(active[1])==cert['final_edge_indices']
    assert sorted(active[0])==cert['final_vertex_indices']
    print('S4_SUBGROUP_CONJUGACY_QUOTIENT_SEVEN_CYCLE_OK',len(found),[len(cells[d]) for d in range(3)])
if __name__=='__main__':
    with open(sys.argv[1],encoding='utf-8') as f:cert=json.load(f)
    main(cert)

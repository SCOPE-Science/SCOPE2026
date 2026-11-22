#!/usr/bin/env python3
"""Exact integral chain verification for wheel-forest symmetry quotients.

Run with Python >=3.9; only standard-library modules are used.
"""
from collections import Counter, defaultdict
from functools import lru_cache
from itertools import product
import heapq
import json

N = 5
# Rim edges e_i={i,i+1}, then spoke edges s_i={i,hub}, indexed 0..9.
EDGES = [(i, (i + 1) % N) for i in range(N)] + [(i, N) for i in range(N)]
GROUPS = {"rotation": [(a, 0) for a in range(N)],
          "reflection": [(0, 0), (0, 1)],
          "dihedral": [(a, b) for a in range(N) for b in (0, 1)]}
EXPECTED = {
    "rotation": ([93, 1358, 4992, 6624, 2904], [1, 0, 0, 0, 6]),
    "reflection": ([244, 3432, 12504, 16560, 7260], [1, 0, 0, 0, 15]),
    "dihedral": ([60, 716, 2520, 3312, 1452], [1, 0, 0, 0, 3]),
}


def forest(mask):
    parent = list(range(N + 1))
    def root(v):
        while parent[v] != v:
            v = parent[v]
        return v
    for j, (a, b) in enumerate(EDGES):
        if mask & (1 << j):
            a, b = root(a), root(b)
            if a == b:
                return False
            parent[a] = b
    return True


FACES = tuple(m for m in range(1, 1 << (2*N))
              if m.bit_count() <= N and forest(m))
assert Counter(m.bit_count() for m in FACES) == {1:10, 2:45, 3:115, 4:170, 5:121}


def action(a, b):
    # Reflection maps the rim edge starting i to that starting a-i-1.
    return tuple(([((a-i-1)%N if b else (a+i)%N) for i in range(N)] +
                  [N + ((a-i)%N if b else (a+i)%N) for i in range(N)]))


def mask_image(m, perm):
    ans = 0
    while m:
        bit = m & -m
        ans |= 1 << perm[bit.bit_length() - 1]
        m ^= bit
    return ans


def build(typ):
    perms = [action(a,b) for a,b in GROUPS[typ]]
    face_set = set(FACES)
    assert all(mask_image(m,perm) in face_set for m in FACES for perm in perms)
    assert len(set(perms)) == len(perms)
    assert all(tuple(p[q[i]] for i in range(2*N)) in perms for p in perms for q in perms)
    @lru_cache(None)
    def canonical(flag):
        return min(tuple(mask_image(m,p) for m in flag) for p in perms)
    cells = [set() for _ in range(N)]
    def traverse(top,flag):
        cells[len(flag)-1].add(canonical(flag))
        sub = (top-1)&top
        while sub:
            traverse(sub,(sub,)+flag)
            sub = (sub-1)&top
    for top in FACES:
        traverse(top,(top,))
    cells = [sorted(layer) for layer in cells]
    ix = [{f:j for j,f in enumerate(layer)} for layer in cells]
    bd = [None]
    for d in range(1,N):
        matrix = {}
        for j, flag in enumerate(cells[d]):
            col=defaultdict(int)
            for i in range(d+1):
                face = canonical(flag[:i]+flag[i+1:])
                col[ix[d-1][face]] += (-1)**i
            matrix[j] = {r:v for r,v in col.items() if v}
        bd.append(matrix)
    return cells, bd


def check_d_squared(bd):
    for d in range(2,N):
        lower,upper=bd[d-1],bd[d]
        for c,col in upper.items():
            out=defaultdict(int)
            for mid,a in col.items():
                for r,b in lower[mid].items():
                    out[r] += a*b
            assert all(v==0 for v in out.values()), (d,c,out)


def cancel_units(cells,boundaries):
    gens=[set(range(len(layer))) for layer in cells]
    bd=boundaries
    rowsets=[None]+[defaultdict(set) for _ in range(N)]
    for d in range(1,N):
        for j,col in bd[d].items():
            for i in col: rowsets[d][i].add(j)
    counts=[0]*N
    for d in range(1,N):
        heap=[]
        def queue(row,col):
            if col not in bd[d] or abs(bd[d][col].get(row,0))!=1:
                return
            score=(len(rowsets[d][row])-1)*(len(bd[d][col])-1)
            heapq.heappush(heap,(score,row,col))
        for col,entries in bd[d].items():
            for row in entries: queue(row,col)
        while heap:
            score,row,col=heapq.heappop(heap)
            if col not in bd[d] or abs(bd[d][col].get(row,0))!=1:
                continue
            current=(len(rowsets[d][row])-1)*(len(bd[d][col])-1)
            if current>score:
                queue(row,col)
                continue
            pivot=bd[d][col]
            unit=pivot[row]
            assert abs(unit)==1
            affected=set()
            for other in tuple(rowsets[d][row]):
                if other==col: continue
                vec=bd[d][other]
                multiple=vec[row]//unit
                for i,v in pivot.items():
                    old=vec.get(i,0)
                    new=old-multiple*v
                    if new:
                        vec[i]=new
                        if not old:rowsets[d][i].add(other)
                    elif old:
                        del vec[i]
                        rowsets[d][i].discard(other)
                affected.add(other)
            for i in pivot:
                rowsets[d][i].discard(col)
            del bd[d][col]
            gens[d].remove(col)
            gens[d-1].remove(row)
            if d>1:
                for i in bd[d-1].pop(row):
                    rowsets[d-1][i].discard(row)
            if d<N-1:
                for other in tuple(rowsets[d+1].get(col,())):
                    bd[d+1][other].pop(col)
                rowsets[d+1].pop(col,None)
            counts[d]+=1
            for other in affected:
                for i in bd[d][other]:queue(i,other)
            for i in pivot:
                for other in rowsets[d][i]:queue(i,other)
    assert not any(vec for d in range(1,N) for vec in bd[d].values())
    assert all(len(x)==(len(cells[d])-counts[d]- (counts[d+1] if d+1<N else 0))
               for d,x in enumerate(gens))
    return [len(x) for x in gens],counts


def rooted_forest_orbit_witness():
    # Kook's edge-rooted forest indexing set for the coned pentagon.
    rooted=set()
    for m in range(1,1<<N):
        if m==(1<<N)-1:continue
        picked={i for i in range(N) if m>>i&1}
        if any(not ({j,(j-1)%N}&picked) for j in range(N)):
            continue
        todo=set(picked)
        components=[]
        while todo:
            stack=[todo.pop()]; component=[]
            while stack:
                j=stack.pop();component.append(j)
                for k in ((j-1)%N,(j+1)%N):
                    if k in todo:todo.remove(k);stack.append(k)
            components.append(component)
        for chosen in product(*components):
            rooted.add((tuple(sorted(picked)),tuple(sorted(chosen))))
    assert len(rooted)==30
    def transform(f,a,b):
        p=action(a,b)
        return (tuple(sorted(p[i] for i in f[0])),
                tuple(sorted(p[i] for i in f[1])))
    fixed={str((a,b)):sum(transform(f,a,b)==f for f in rooted)
           for a,b in GROUPS['dihedral']}
    assert fixed['(0, 0)']==30 and all(v==0 for k,v in fixed.items() if k!='(0, 0)')
    assert len({min(transform(f,a,b) for a,b in GROUPS['dihedral']) for f in rooted})==3
    return fixed


def main():
    outcome={}
    for typ in ('rotation','reflection','dihedral'):
        cells,bd=build(typ)
        check_d_squared(bd)
        vector,counts=cancel_units(cells,bd)
        expected_cells,expected_vector=EXPECTED[typ]
        assert list(map(len,cells))==expected_cells,(typ,list(map(len,cells)))
        assert vector==expected_vector,(typ,vector)
        assert sum((-1)**d*len(cells[d]) for d in range(N)) == 1+vector[4]
        outcome[typ]={'cells':expected_cells,'unimodular_cancellations':counts[1:],
                      'reduced_chain_ranks':vector, 'integer_homology':'torsion_free'}
    outcome['trivial']={'face_counts_by_cardinality':[10,45,115,170,121],
                        'wedge_s4':30, 'basis_rooted_forest_fixed_counts':rooted_forest_orbit_witness()}
    print(json.dumps(outcome,sort_keys=True,separators=(',',':')))
    print('VERIFY_OK')

if __name__=='__main__':main()

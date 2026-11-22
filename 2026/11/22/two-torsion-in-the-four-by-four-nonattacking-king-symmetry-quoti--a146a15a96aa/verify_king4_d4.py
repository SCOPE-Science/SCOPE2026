#!/usr/bin/env python3
"""Exact integer homology of a dihedral quotient of a king-placement complex.

Reproducible using Python 3 and its standard library only. All arithmetic is
integral. The orbit chains are formed after barycentric subdivision.
"""
from collections import Counter, defaultdict
from math import gcd
from functools import reduce

N = 4
vertices = [(i, j) for i in range(N) for j in range(N)]
faces = {0}
for b, (r, c) in enumerate(vertices):
    bad = sum(1 << j for j, (x, y) in enumerate(vertices[:b])
              if max(abs(x-r), abs(y-c)) <= 1)
    faces.update(f | 1 << b for f in list(faces) if not f & bad)
faces.discard(0)
assert len(faces) == 313
assert Counter(f.bit_count()-1 for f in faces) == {0:16,1:78,2:140,3:79}

perms = []
for rot in range(4):
    for refl in (False, True):
        images = []
        for r, c in vertices:
            if refl:
                c = N-1-c
            for _ in range(rot):
                r, c = c, N-1-r
            images.append(vertices.index((r, c)))
        perms.append(tuple(images))
assert len(set(perms)) == 8

def move(face, p):
    result = 0
    while face:
        bit = face & -face
        result |= 1 << p[bit.bit_length()-1]
        face ^= bit
    return result

def transform(flag, p):
    return tuple(move(f, p) for f in flag)

def canon(flag):
    return min(transform(flag, p) for p in perms)

raw_flags = defaultdict(set)
for full in faces:
    def generate(upper, flag):
        raw_flags[len(flag)-1].add(flag)
        sub = (upper-1) & upper
        while sub:
            generate(sub, (sub,)+flag)
            sub = (sub-1) & upper
    generate(full, (full,))

cells = {d: sorted(set(canon(f) for f in raw))
         for d, raw in raw_flags.items()}
assert [len(cells[d]) for d in range(4)] == [50, 283, 471, 237]
assert sum((-1)**d*len(cells[d]) for d in cells) == 1
for d, raw in raw_flags.items():
    fixed = [sum(transform(flag,p)==flag for flag in raw) for p in perms]
    assert sum(fixed)//8 == len(cells[d]) and sum(fixed)%8 == 0

index = {d: {cell:i for i, cell in enumerate(cells[d])} for d in cells}
matrices = {}
for d in range(1,4):
    columns = []
    for flag in cells[d]:
        col = defaultdict(int)
        for j in range(d+1):
            col[canon(flag[:j]+flag[j+1:])] += (-1)**j
        columns.append({k:v for k,v in col.items() if v})
    matrices[d] = columns
for d in (2,3):
    for col in matrices[d]:
        comp = defaultdict(int)
        for target, coef in col.items():
            for lower, val in matrices[d-1][index[d-1][target]].items():
                comp[lower] += coef*val
        assert not any(comp.values()), 'boundary composition must vanish'

def unimodular_units(columns, lower_basis):
    """Integer row-column pivoting; remaining entries give residual Smith data.

    A unit pivot of sign a reduces other entries via A[k,h]-A[k,j]*A[i,h]*a.
    Thus each step uses only unimodular integral operations.
    """
    row_ids = {cell: i for i, cell in enumerate(lower_basis)}
    rows = defaultdict(dict)
    cols = defaultdict(dict)
    for j, column in enumerate(columns):
        for facet, value in column.items():
            i = row_ids[facet]
            rows[i][j] = value
            cols[j][i] = value
    pivots = 0
    while True:
        best = None
        for i, row in rows.items():
            for j, a in row.items():
                if abs(a)==1:
                    cost = (len(row)-1)*(len(cols[j])-1)
                    if best is None or cost < best[0]:
                        best = (cost,i,j,a)
                    if cost == 0: break
            if best is not None and best[0] == 0: break
        if best is None: break
        _,i,j,a = best
        pivot_row = list(rows[i].items())
        pivot_col = list(cols[j].items())
        for k,b in pivot_col:
            if k==i: continue
            for h,c in pivot_row:
                if h==j: continue
                value=rows[k].get(h,0)-b*c*a
                if value:
                    rows[k][h] = value
                    cols[h][k] = value
                else:
                    rows[k].pop(h,None)
                    cols[h].pop(k,None)
        for h,_ in pivot_row: cols[h].pop(i,None)
        for k,_ in pivot_col: rows[k].pop(j,None)
        del rows[i]
        del cols[j]
        pivots += 1
    remain = {j: {i:a for i,a in col.items() if a} for j,col in cols.items() if col}
    return pivots, remain

pivots={}; residual={}
for d in (1,2,3):
    pivots[d], residual[d] = unimodular_units(matrices[d],cells[d-1])
assert pivots == {1:49,2:234,3:236}
assert not residual[1] and not residual[2]
assert len(residual[3])==1
last_entries = list(next(iter(residual[3].values())).values())
assert last_entries and reduce(gcd,map(abs,last_entries))==2
assert all(a%2==0 for a in last_entries)
assert len(cells[3])-pivots[3]==1
ranks={1:49,2:234,3:237}
def rank_mod_prime(columns, basis, prime):
    # Independent finite-field check, with row dictionaries keyed by orbit IDs.
    rows = {face:i for i,face in enumerate(basis)}
    reduced = {}
    rank = 0
    for column in columns:
        vec = {rows[k]:v%prime for k,v in column.items() if v%prime}
        while vec:
            lead=min(vec)
            if lead not in reduced:
                inverse=pow(vec[lead],-1,prime)
                reduced[lead]={i:(v*inverse)%prime for i,v in vec.items() if v}
                rank += 1
                break
            pivot=reduced[lead];scalar=vec[lead]
            for i,v in pivot.items():
                n=(vec.get(i,0)-scalar*v)%prime
                if n:vec[i]=n
                else:vec.pop(i,None)
    return rank

for prime, expected in [(2,{1:49,2:234,3:236}), (3,{1:49,2:234,3:237})]:
    observed={d:rank_mod_prime(matrices[d],cells[d-1],prime) for d in (1,2,3)}
    assert observed==expected, (prime, observed)
assert (len(cells[0])-ranks[1],
        len(cells[1])-ranks[1]-ranks[2],
        len(cells[2])-ranks[2]-ranks[3],
        len(cells[3])-ranks[3])==(1,0,0,0)
print('KING4_D4_QUOTIENT_INTEGRAL_HOMOLOGY_OK')
print('face_counts', dict(sorted(Counter(f.bit_count()-1 for f in faces).items())))
print('quotient_cell_counts', [len(cells[d]) for d in range(4)])
print('boundary_ranks',ranks)
print('unit_pivots',pivots, 'last_smith_invariant',2)
print('homology', 'H_0=Z H_1=0 H_2=Z/2 H_3=0; no other degrees')

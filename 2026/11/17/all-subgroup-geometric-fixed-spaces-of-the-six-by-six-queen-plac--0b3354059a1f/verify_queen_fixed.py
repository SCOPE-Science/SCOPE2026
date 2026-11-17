#!/usr/bin/env python3
"""Exact standalone certificate for fixed sets of the six-board queen complex."""
from itertools import combinations
from collections import Counter
from hashlib import sha256
import json

N = 6
SQUARES = tuple((i, j) for i in range(N) for j in range(N))
I = {p: i for i, p in enumerate(SQUARES)}

def r(p):
    x, y = p
    return (y, N - 1 - x)

def s(p):
    x, y = p
    return (x, N - 1 - y)

def move(p, a, b):
    if b:
        p = s(p)
    for _ in range(a):
        p = r(p)
    return p

G = tuple((a, b) for a in range(4) for b in range(2))
perms = {g: tuple(I[move(p, *g)] for p in SQUARES) for g in G}
perm_to_g = {v: g for g, v in perms.items()}
assert len(perm_to_g) == 8
identity = (0, 0)

def mul(a, b):
    p, q = perms[a], perms[b]
    return perm_to_g[tuple(p[q[i]] for i in range(36))]

def subgroup(gens):
    a = set(gens) | {identity}
    while True:
        b = a | {mul(x, y) for x in a for y in a}
        if a == b:
            return frozenset(a)
        a = b

all_subgroups = {subgroup([g]) for g in G}
all_subgroups |= {subgroup([a, b]) for a in G for b in G}
assert len(all_subgroups) == 10

def compatible(x, y):
    a, b = SQUARES[x]
    c, d = SQUARES[y]
    return a != c and b != d and abs(a - c) != abs(b - d)

def faces_from_orbits(H):
    remaining = set(range(36))
    O = []
    while remaining:
        x = min(remaining)
        orb = tuple(sorted({perms[g][x] for g in H}))
        remaining.difference_update(orb)
        if all(compatible(i, j) for i, j in combinations(orb, 2)):
            O.append(orb)
    edge = {(i, j) for i in range(len(O)) for j in range(i+1, len(O))
            if all(compatible(x, y) for x in O[i] for y in O[j])}
    fs = {()}
    for k in range(1, len(O)+1):
        layer = {c for c in combinations(range(len(O)), k)
                 if all((i, j) in edge for i, j in combinations(c, 2))}
        if not layer:
            break
        fs.update(layer)
    return O, fs

# Independent construction: recursively enumerate the original nonattacking placements.
orig = {frozenset()}
for x in range(36):
    orig |= {F | {x} for F in tuple(orig) if all(compatible(x, y) for y in F)}
assert len(orig) == 2635
assert [sum(len(f)==k for f in orig) for k in range(7)] == [1,36,340,1024,982,248,4]

rows = []
for H in sorted(all_subgroups, key=lambda h: (len(h), sorted(h))):
    O, fs = faces_from_orbits(H)
    index = {e: i for i,e in enumerate(O)}
    # Independently recover orbit simplices by testing invariance of each original face.
    fixed = set()
    for F in orig:
        if all({perms[g][i] for i in F} == F for g in H):
            support = frozenset(F)
            fixed.add(tuple(sorted(index[e] for e in O if set(e) <= support)))
    assert fs == fixed, (H, fs ^ fixed)
    f = [sum(len(c)==k for c in fs) for k in range(1+max(map(len,fs)))]
    red_euler = sum((-1 if k == 0 else (-1)**(k-1)) * count for k,count in enumerate(f))
    row = {'subgroup': sorted([f'r{a}s{b}' for a,b in H]),
           'order':len(H), 'f_by_cardinality':f, 'reduced_euler':red_euler}
    rows.append(row)

    if H == frozenset({identity, (2,0)}):
        assert f == [1,12,22,4]
        triangles = [face for face in fs if len(face)==3]
        edges = {face for face in fs if len(face)==2}
        assert len(triangles)==4
        incidences = Counter(e for t in triangles for e in combinations(t, 2))
        certificates=[]
        for t in sorted(triangles):
            free = [e for e in combinations(t,2) if incidences[e]==1]
            assert free
            e=min(free)
            edges.remove(e)
            certificates.append((t,e))
        assert len(edges)==18
        seen={0}
        todo=[0]
        tree=[]
        while todo:
            x=todo.pop()
            for y,z in sorted(edges):
                nxt = z if y == x else y if z == x else -1
                if nxt not in seen and nxt>=0:
                    seen.add(nxt)
                    todo.append(nxt)
                    tree.append((x,nxt))
        assert len(seen)==12 and len(tree)==11
        assert len(edges)-len(O)+1==7
        row['free_collapses']=[{'triangle':list(t),'free_edge':list(e)} for t,e in certificates]
        row['spanning_tree']=[list(e) for e in tree]
        row['vertex_orbits']=[[list(SQUARES[v]) for v in orb] for orb in O]
    if len(H)==4 and (1,0) in H:
        assert f==[1,6]
    if len(H)==2 and any(g in H for g in [(1,1),(3,1)]):
        assert f==[1,6]
    if len(H)>1 and (2,0) not in H and (1,0) not in H and len(H)!=2:
        raise AssertionError('unexpected subgroup')

assert len([r for r in rows if r['f_by_cardinality']==[1]])==5
assert len([r for r in rows if r['f_by_cardinality']==[1,6]])==3
assert len([r for r in rows if r['f_by_cardinality']==[1,12,22,4]])==1
assert len([r for r in rows if r['f_by_cardinality']==[1,36,340,1024,982,248,4]])==1

# Compare all eight reduced Lefschetz numbers against independent signed simplex traces.
def sign_perm(sequence):
    return (-1)**sum(a>b for i,a in enumerate(sequence) for b in sequence[i+1:])
char={}
for g in G:
    reduced=0
    p=perms[g]
    for face in orig:
        if {p[i] for i in face} == face:
            ordered=sorted(face)
            target=[p[i] for i in ordered]
            sign=sign_perm(target)
            reduced += (-1 if not face else (-1)**(len(face)-1)) * sign
    h=subgroup([g])
    expected = next(row['reduced_euler'] for row in rows
                    if set(row['subgroup']) == {f'r{a}s{b}' for a,b in h})
    assert reduced == expected, (g,reduced,expected)
    char[f'r{g[0]}s{g[1]}'] = -reduced  # degree-three rational homology is known to be the only one

print('ORIGINAL_FACE_COUNTS 1,36,340,1024,982,248,4')
print('ALL_SUBGROUPS',len(rows),'ALL_SUBGROUP_ORBIT_FACES_RECONSTRUCTED')
for row in rows:
    print('SUBGROUP',','.join(row['subgroup']),'F',','.join(map(str,row['f_by_cardinality'])))
print('LEFSCHETZ_COMPATIBLE_EIGHT_ELEMENTS',json.dumps(char,sort_keys=True))
print('HALF_TURN_FREE_COLLAPSES',json.dumps(next(row['free_collapses'] for row in rows if row['f_by_cardinality']==[1,12,22,4]),sort_keys=True))
print('SIX_BY_SIX_QUEEN_ALL_D4_FIXED_SPACES_PASS')

#!/usr/bin/env python3
"""Exact simplicial-collapse, fundamental-group, and integral-boundary verifier.

Usage: python3 check.py [--generate]
No nonstandard packages are needed. The input graph is P_3 Cartesian C_6.
The certificates are explicit integer masks/indices; ordinary mode checks them.
"""
from collections import Counter, defaultdict
from itertools import combinations
from pathlib import Path
import sys

ROOT = Path(__file__).resolve().parent
CERT = ROOT / 'certificates'
GENERATE = sys.argv[1:] == ['--generate']
assert sys.argv[1:] in ([], ['--generate'])


def vertices(mask):
    while mask:
        bit = mask & -mask
        yield bit
        mask ^= bit


def graph():
    n = 6
    edges = set()
    for r in range(3):
        for c in range(n):
            u = r*n+c
            v = r*n + (c+1) % n
            edges.add(tuple(sorted((u,v))))
    for r in range(2):
        for c in range(n):
            edges.add((r*n+c,(r+1)*n+c))
    return sorted(edges)


def matchings(edges):
    incident = defaultdict(list)
    for i,(u,v) in enumerate(edges):
        incident[u].append((v,i));incident[v].append((u,i))
    full = (1<<18)-1
    def visit(covered, chosen):
        if covered == full:
            yield tuple(sorted(chosen)); return
        v = next(k for k in range(18) if not covered & (1<<k))
        for w,i in incident[v]:
            if not covered & (1<<w):
                yield from visit(covered | (1<<v) | (1<<w), chosen + (i,))
    return sorted(set(visit(0,())))


def immediate_subfaces(a):
    if a.bit_count() == 1: return []
    return [a ^ bit for bit in vertices(a)]


def read_lines(name):
    return [tuple(map(int,line.split())) for line in (CERT/name).read_text().splitlines() if line.strip()]


def write_lines(name,rows):
    (CERT/name).write_text(''.join(' '.join(map(str,row))+'\n' for row in rows))


def collapse(faces):
    active = set(faces)
    co = {a:set() for a in faces}
    for a in faces:
        for b in immediate_subfaces(a): co[b].add(a)
    if GENERATE:
        from collections import deque
        queue = deque(sorted(a for a in faces if len(co[a]) == 1))
        sequence = []
        while queue:
            a = queue.popleft()
            if a not in active or len(co[a]) != 1: continue
            b = next(iter(co[a]))
            sequence.append((a,b))
            for x in (a,b):
                active.remove(x)
                for y in immediate_subfaces(x):
                    if y in active:
                        co[y].remove(x)
                        if len(co[y]) == 1: queue.append(y)
        write_lines('collapse_pairs.tsv', sequence)
    else:
        sequence = read_lines('collapse_pairs.tsv')
        for a,b in sequence:
            assert a in active and b in active
            assert a.bit_count()+1 == b.bit_count() and a&b == a
            assert co[a] == {b}, (a,b)
            assert len(co[b]) == 0, (a,b)
            for x in (a,b):
                active.remove(x)
                for y in immediate_subfaces(x):
                    if y in active: co[y].remove(x)
        assert not any(len(co[a]) == 1 for a in active)
    assert len(sequence) == 14436
    assert len(active) == 1481
    assert dict(sorted(Counter(a.bit_count() for a in active).items())) == {1:30,2:270,3:694,4:487}
    assert all(all(y in active for y in immediate_subfaces(x)) for x in active)
    return active


def pi1_triviality(by):
    parent = {a:a for a in by[1]}
    def root(a):
        while parent[a] != a: a = parent[a]
        return a
    tree = []
    for e in by[2]:
        a,b = list(vertices(e)); ra,rb=root(a),root(b)
        if ra != rb:
            parent[ra] = rb
            tree.append(e)
    assert len(tree) == 29
    if GENERATE:
        known = set(tree);proof=[]
        while len(known) < len(by[2]):
            progress = False
            for t in by[3]:
                sides = immediate_subfaces(t)
                unknown = [e for e in sides if e not in known]
                if len(unknown) == 1:
                    e = unknown[0]
                    known.add(e);proof.append((t,e));progress = True
            assert progress, 'Triangle relations do not suffice'
        write_lines('pi1_relations.tsv', [(e,) for e in tree] + proof)
    else:
        seq = read_lines('pi1_relations.tsv')
        assert len(seq) == 270 and seq[:29] == [(e,) for e in tree]
        known = set(tree)
        faces3 = set(by[3]);faces2 = set(by[2])
        for t,e in seq[29:]:
            assert t in faces3 and e in faces2 and e not in known
            assert set(immediate_subfaces(t)) - known == {e}
            known.add(e)
        assert known == faces2
    return len(tree), len(by[2]) - len(tree)


def smith_unit_pivots(by):
    idx={a:i for i,a in enumerate(by[3])}
    rows=[{} for _ in by[3]]
    cols=[{} for _ in by[4]]
    for j,a in enumerate(by[4]):
        for k,bit in enumerate(vertices(a)):
            i = idx[a^bit]
            v = 1 if k%2 == 0 else -1
            rows[i][j] = v
            cols[j][i] = v
    # Check simplicial boundary-square identity explicitly for each 3-cell.
    edgeset=set(by[2])
    for a in by[4]:
        twice=defaultdict(int)
        for k,bit in enumerate(vertices(a)):
            t=a^bit
            for s,b2 in enumerate(vertices(t)):
                edge=t^b2
                assert edge in edgeset
                twice[edge] += (-1)**(k+s)
        assert all(x==0 for x in twice.values())
    if GENERATE:
        pivots=[]
    else:
        pivots=read_lines('unit_pivots.tsv')
        assert len(pivots)==453
    steps = 453
    for t in range(steps):
        if GENERATE:
            _,i,j = min((len(rows[i])*len(cols[j]),i,j)
                        for i,r in enumerate(rows) for j,v in r.items() if abs(v)==1)
            pivots.append((i,j))
        else:
            i,j=pivots[t]
        assert abs(rows[i].get(j,0)) == 1, (t,i,j)
        v=rows[i][j]
        r=list(rows[i].items()); c=list(cols[j].items())
        for k,a in c:
            if k==i: continue
            for l,b in r:
                if l==j: continue
                value=rows[k].get(l,0)-a*b//v
                if value:
                    rows[k][l]=value;cols[l][k]=value
                else:
                    rows[k].pop(l,None);cols[l].pop(k,None)
        for l,_ in r:cols[l].pop(i,None)
        for k,_ in c:rows[k].pop(j,None)
        rows[i].clear(); cols[j].clear()
    assert all(not r for r in rows)
    assert all(not c for c in cols)
    if GENERATE:write_lines('unit_pivots.tsv',pivots)
    return steps


def main():
    edges=graph()
    assert len(edges)==30
    pms=matchings(edges)
    assert len(pms)==108 and len(set(pms))==108
    assert all(len(p)==9 and len(set(sum((list(edges[i]) for i in p),[])))==18 for p in pms)
    faces=set()
    for pm in pms:
        for length in range(1,10):
            for subset in combinations(pm,length):
                faces.add(sum(1<<i for i in subset))
    assert len(faces)==30353
    assert dict(sorted(Counter(a.bit_count() for a in faces).items())) == {1:30,2:363,3:2194,4:6258,5:9144,6:7600,7:3684,8:972,9:108}
    core=collapse(faces)
    by={k:sorted(a for a in core if a.bit_count()==k) for k in range(1,5)}
    tree, relations=pi1_triviality(by)
    pivots=smith_unit_pivots(by)
    assert pivots==453 and relations==241 and tree==29
    # The exact cellular boundary d_2 has rank 241 because the triangular
    # elimination kills all edge generators after contracting the tree.
    # d_3 has 453 integral unit Smith factors and no other factors.
    assert len(by[3])-relations-pivots==0
    assert len(by[4])-pivots==34
    print('PASS: graph vertices=18 edges=30, perfect matchings=108')
    print('PASS: nonempty faces=30353, elementary collapses=14436')
    print('PASS: core f-vector=(30,270,694,487)')
    print('PASS: fundamental group=1, via 29 tree edges and 241 triangle relations')
    print('PASS: degree-3 boundary Smith diagonal=453 ones and 34 zeros')
    print('PASS: integral homology H_2=0, H_3=Z^34; homotopy wedge of 34 S^3')

if __name__=='__main__': main()

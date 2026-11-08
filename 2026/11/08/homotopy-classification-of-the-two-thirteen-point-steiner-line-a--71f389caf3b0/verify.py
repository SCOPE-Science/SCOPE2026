#!/usr/bin/env python3
"""Exact, standard-library verification for line-avoiding complexes of STS(13)."""
from collections import Counter, defaultdict, deque
from itertools import combinations
from math import comb
from functools import lru_cache

N = 13
BASES = ((0, 1, 4), (0, 2, 7))
OLD = {(0, 1, 4), (0, 2, 7), (1, 7, 9), (2, 4, 9)}
NEW = {(0, 1, 7), (0, 2, 4), (1, 4, 9), (2, 7, 9)}


def designs():
    a = {tuple(sorted((v+t) % N for v in b))
         for b in BASES for t in range(N)}
    assert len(a) == 26 and OLD <= a
    b = (a - OLD) | NEW
    for blocks in (a, b):
        pair_count = Counter(p for triple in blocks for p in combinations(triple, 2))
        assert len(blocks) == 26 and len(pair_count) == comb(N, 2)
        assert set(pair_count.values()) == {1}
    old_pairs = Counter(p for triple in OLD for p in combinations(triple, 2))
    new_pairs = Counter(p for triple in NEW for p in combinations(triple, 2))
    assert old_pairs == new_pairs
    return a, b


def facets(blocks):
    bm = {sum(1 << i for i in b) for b in blocks}
    # Independent implementations: direct bitmask and recursive extension.
    faces = {s for s in range(1 << N) if not any((s & b) == b for b in bm)}
    recursive = {0}
    for v in range(N):
        recursive |= {s | (1 << v) for s in tuple(recursive)
                      if not any(((s | (1 << v)) & b) == b for b in bm)}
    assert faces == recursive
    for f in faces:
        assert f == 0 or all(f & ~(1 << j) in faces for j in range(N) if f >> j & 1)
    return faces


def boundary(s):
    vertices = [i for i in range(N) if s >> i & 1]
    return {s & ~(1 << i): (-1 if k % 2 else 1)
            for k, i in enumerate(vertices)}


def topological_count(nodes, arrows):
    adj = {s: [] for s in nodes}
    indeg = {s: 0 for s in nodes}
    for a, b in arrows:
        adj[a].append(b); indeg[b] += 1
    todo = deque(s for s in nodes if indeg[s] == 0)
    count = 0
    while todo:
        a = todo.popleft(); count += 1
        for b in adj[a]:
            indeg[b] -= 1
            if not indeg[b]:
                todo.append(b)
    assert count == len(nodes), 'non-acyclic matching'


def toggle_morse(faces):
    remaining = set(faces); lower = {}; upper = {}
    for i in range(N):
        for s in sorted(faces):
            t = s | (1 << i)
            if not (s & (1 << i)) and s in remaining and t in remaining:
                lower[s] = t; upper[t] = s
                remaining.remove(s); remaining.remove(t)
    # Augmented matching's empty-singleton pair is removed from the actual CW matching.
    assert 0 in lower and lower[0] == 1
    del lower[0]; del upper[1]
    ordinary = faces - {0}
    unmatched = (remaining - {0}) | {1}
    directed = []
    for s in ordinary:
        if s.bit_count() == 1: continue
        for t in boundary(s):
            directed.append((t, s) if lower.get(t) == s else (s, t))
    topological_count(ordinary, directed)
    assert len(directed) == sum(s.bit_count() for s in ordinary if s.bit_count()>1)
    return lower, unmatched, len(directed)


def morse_matrix(lower, unmatched):
    critical3 = sorted(s for s in unmatched if s.bit_count() == 4)
    critical4 = sorted(s for s in unmatched if s.bit_count() == 5)
    lows = {s for s in lower if s.bit_count() == 4}
    edges = [(s, t) for s in lows for t in boundary(lower[s]) if t != s and t in lows]
    # A lower matched 3-face precedes all other matched 3-faces in the boundary of its partner.
    adj = {s: [] for s in lows}; indeg = {s: 0 for s in lows}
    for s, t in edges:
        adj[s].append(t); indeg[t] += 1
    q = deque(s for s in lows if indeg[s] == 0); order = []
    while q:
        s=q.popleft(); order.append(s)
        for t in adj[s]:
            indeg[t] -= 1
            if indeg[t] == 0: q.append(t)
    assert len(order) == len(lows)
    cols = []
    for u in critical4:
        z = defaultdict(int, boundary(u))
        for s in order:
            coeff = z[s]
            if coeff:
                upper = lower[s]; db = boundary(upper)
                assert db[s] in (-1, 1)
                mult = coeff // db[s]
                for t, a in db.items(): z[t] -= mult*a
                assert z[s] == 0
        assert all(z[s] == 0 for s in lows)
        cols.append([z[t] for t in critical3])
    return [[col[r] for col in cols] for r in range(len(critical3))], critical3, critical4


def independent_morse_matrix(lower, unmatched):
    # Separate memoized gradient recursion; no coefficient-elimination loop.
    crit3 = sorted(s for s in unmatched if s.bit_count() == 4)
    crit4 = sorted(s for s in unmatched if s.bit_count() == 5)
    positions = {s:i for i,s in enumerate(crit3)}
    @lru_cache(None)
    def reduce_face(s):
        if s in positions:
            return tuple(int(j == positions[s]) for j in range(len(crit3)))
        if s not in lower:
            return (0,) * len(crit3)
        tau = lower[s]; bd = boundary(tau); a = bd[s]
        ans = [0]*len(crit3)
        for t,c in bd.items():
            if t != s:
                row=reduce_face(t)
                for i in range(len(ans)):ans[i] -= c * row[i] // a
        return tuple(ans)
    result = []
    for u in crit4:
        row = [0]*len(crit3)
        for s,sgn in boundary(u).items():
            v = reduce_face(s)
            for i in range(len(row)):
                row[i] += sgn*v[i]
        result.append(row)
    return [[column[r] for column in result] for r in range(len(crit3))]


def det_bareiss(a):
    a = [list(row) for row in a]; n = len(a)
    if n == 0: return 1
    sign=1; previous=1
    for k in range(n-1):
        r=next((j for j in range(k,n) if a[j][k]), None)
        if r is None: return 0
        if r != k: a[r],a[k]=a[k],a[r]; sign=-sign
        p=a[k][k]
        for i in range(k+1,n):
            for j in range(k+1,n):
                v=a[i][j]*p-a[i][k]*a[k][j]
                assert v%previous==0
                a[i][j]=v//previous
            a[i][k]=0
        previous=p
    return sign*a[-1][-1]


def find_unit_minor(matrix):
    m=len(matrix); n=len(matrix[0]); assert m<=n
    for cols in combinations(range(n),m):
        d=det_bareiss([[matrix[i][j] for j in cols] for i in range(m)])
        if abs(d)==1: return cols,d
    raise AssertionError('No full-rank unimodular minor')


def mod2_ranks(faces):
    by_dim={d:sorted(s for s in faces if s.bit_count() == d+1) for d in range(N)}
    ranks = {}; pivot = {}
    for d in range(1,N):
        src=by_dim[d]
        if not src:continue
        rows={f:i for i,f in enumerate(by_dim[d-1])}
        basis={}
        for s in src:
            col=0
            for t in boundary(s):col ^= (1 << rows[t])
            while col:
                i=col.bit_length()-1
                if i in basis:col ^= basis[i]
                else:basis[i]=col;break
        ranks[d]=len(basis)
    betti = {}
    for d, faces_d in by_dim.items():
        if not faces_d: continue
        betti[d] = len(faces_d)-ranks.get(d,0)-ranks.get(d+1,0)
    return ranks, betti


def test_case(name,blocks,expect_faces,expect_crit,expect_wedge):
    faces=facets(blocks)
    fvec=tuple(sum(s.bit_count()==k for s in faces) for k in range(7))
    assert fvec==expect_faces,(name,fvec,expect_faces)
    five=[s for s in faces if s.bit_count()==5]
    six=[s for s in faces if s.bit_count()==6]
    maximal_five=sum(not any((t & u)==t for u in six) for t in five)
    assert maximal_five == (117 if name == 'cyclic' else 132)
    lower,critical,coverings=toggle_morse(faces)
    crit=Counter(s.bit_count()-1 for s in critical)
    assert dict(crit)==expect_crit,(name,crit)
    m,c3,c4=morse_matrix(lower,critical)
    assert m == independent_morse_matrix(lower,critical)
    minor,det=find_unit_minor(m)
    assert len(c4)-len(c3)==expect_wedge
    ranks,betti=mod2_ranks(faces)
    assert betti == {0:1,1:0,2:0,3:0,4:expect_wedge,5:0},betti
    euler=sum((-1)**(k-1)*fvec[k] for k in range(1,7))
    assert euler==expect_wedge+1
    print(name,'f=[%s]'%(','.join(map(str,fvec))),'ordinary_coverings=',coverings,
          'matched_pairs=',len(lower),'critical=',sorted(crit.items()),
          'morse_boundary_shape=',(len(c3),len(c4)),
          'unit_minor_columns_zero_based=',minor,'unit_minor_det=',det,
          'maximal_five=',maximal_five, 'mod2_betti=',sorted(betti.items()),'wedge_S4=',expect_wedge)
    return minor,det,m


def main():
    a,b=designs()
    aa=test_case('cyclic',a,(1,13,78,260,455,312,39),{0:1,3:6,4:18},12)
    bb=test_case('Pasch_switched',b,(1,13,78,260,455,312,34),{0:1,3:4,4:21},17)
    print('ALL_CHECKS_PASS')
    return aa,bb

if __name__=='__main__':main()

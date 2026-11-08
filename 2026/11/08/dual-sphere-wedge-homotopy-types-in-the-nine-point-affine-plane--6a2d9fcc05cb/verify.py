#!/usr/bin/env python3
"""Reproducible exact face-poset and integral-Morse checks for affine order-three line and theta complexes."""
from collections import Counter, defaultdict, deque

N = 9
FULL = (1 << N) - 1
POINTS = [(x, y) for x in range(3) for y in range(3)]


def lines():
    ans = set()
    for dx, dy in ((1, 0), (0, 1), (1, 1), (1, 2)):
        for x, y in POINTS:
            pts = {((x + t * dx) % 3, (y + t * dy) % 3) for t in range(3)}
            ans.add(sum(1 << POINTS.index(p) for p in pts))
    assert len(ans) == 12 and all(u.bit_count() == 3 for u in ans)
    assert all(sum(u >> k & 1 for u in ans) == 4 for k in range(9))
    assert all(sum((u >> a & 1) and (u >> b & 1) for u in ans) == 1
               for a in range(9) for b in range(a+1, 9))
    return sorted(ans)


def face_sets(L):
    X = {s for s in range(1 << N) if all((s & ell) != ell for ell in L)}
    T = {s for s in range(1 << N) if any((s & ell) == 0 for ell in L)}
    # Independent second enumeration: union of all subfaces of facets.
    theta_via_facets = set()
    for ell in L:
        facet = FULL ^ ell
        sub = facet
        while True:
            theta_via_facets.add(sub)
            if sub == 0:
                break
            sub = (sub - 1) & facet
    assert T == theta_via_facets
    assert T == {s for s in range(1 << N) if (FULL ^ s) not in X}
    return X, T


def match_faces(faces):
    remaining = set(faces)
    pairs = []
    for vertex in range(N):
        bit = 1 << vertex
        for a in sorted(remaining):
            b = a | bit
            if (a & bit) == 0 and b in remaining:
                pairs.append((a, b))
                remaining.remove(a)
                remaining.remove(b)
    assert len(pairs) * 2 + len(remaining) == len(faces)
    assert (0, 1) in pairs
    return pairs, remaining


def orientation_test(faces, pairs):
    # Directed Hasse: upward for paired cover, downward otherwise.
    up = {(a, b) for a, b in pairs if a}
    cells = sorted(faces - {0})
    arcs = defaultdict(list)
    incoming = {x: 0 for x in cells}
    edges = 0
    for b in cells:
        for bit in (1 << v for v in range(N) if b >> v & 1):
            a = b ^ bit
            if a == 0:
                continue
            source, target = (a, b) if (a, b) in up else (b, a)
            arcs[source].append(target)
            incoming[target] += 1
            edges += 1
    Q = deque(x for x in cells if not incoming[x])
    count = 0
    while Q:
        u = Q.popleft()
        count += 1
        for v in arcs[u]:
            incoming[v] -= 1
            if incoming[v] == 0:
                Q.append(v)
    assert count == len(cells), (count, len(cells))
    return edges


def integer_morse_boundary(faces, pairs, critical):
    # Exact integral algebraic Morse cancellation, with oriented incidence ±1.
    # Remove only pairs with nonempty lower member; preserve an actual vertex.
    columns = {}
    for b in faces:
        if b == 0: continue
        co = {}
        support = [v for v in range(N) if b >> v & 1]
        for j, v in enumerate(support):
            a = b ^ (1 << v)
            if a:
                co[a] = (-1) ** j
        columns[b] = co
    for low, high in pairs:
        if not low:
            continue
        assert low in columns and high in columns
        col = columns[high]
        pivot = col.get(low, 0)
        assert abs(pivot) == 1, (low, high, pivot)
        # Schur complement at a unit pivot in the integral chain complex.
        for b, c in columns.items():
            if b == high or b.bit_count() != high.bit_count():
                continue
            coeff = c.pop(low, 0)
            if coeff:
                factor = coeff * pivot
                for a, value in col.items():
                    if a == low: continue
                    c[a] = c.get(a, 0) - factor * value
                    if c[a] == 0: del c[a]
        for b, c in columns.items():
            if b.bit_count() == high.bit_count() + 1:
                c.pop(high, None)
        del columns[high]
        del columns[low]
    expected = {c for c in critical if c}
    expected.add(1)
    assert set(columns) == expected, (set(columns), expected)
    nz = {hex(b):{hex(a):v for a,v in c.items()} for b,c in columns.items() if c}
    assert not nz, nz
    return len(columns)


def mod2_ranks(faces):
    by_n = {k: sorted(s for s in faces if s.bit_count() == k) for k in range(1, 7)}
    ranks = []
    for k in range(2, 7):
        if not by_n[k]:
            continue
        pos = {s:i for i,s in enumerate(by_n[k-1])}
        piv = {}
        for cell in by_n[k]:
            col = 0
            for v in range(N):
                if cell >> v & 1:
                    col ^= 1 << pos[cell ^ (1 << v)]
            while col:
                h = col.bit_length()-1
                if h not in piv:
                    piv[h] = col
                    break
                col ^= piv[h]
        ranks.append((k-1,len(piv)))
    return ranks


def main():
    L = lines()
    X, T = face_sets(L)
    print('lines', len(L))
    for label, F, expected in [('line-free',X,{2:1,3:11}),('theta',T,{3:11,4:1})]:
        P, critical = match_faces(F)
        # Nonempty-face discrete Morse has one selected critical vertex.
        nonaugmented_critical = set(critical) | {1}
        assert Counter(c.bit_count()-1 for c in nonaugmented_critical) == Counter({0:1,**expected})
        edges = orientation_test(F,P)
        remaining = integer_morse_boundary(F,P,critical)
        dims = Counter(s.bit_count()-1 for s in F)
        ranks = mod2_ranks(F)
        print(label,'faces_with_empty',len(F),'face_vector',dict(sorted(dims.items())),
              'pair_count_without_empty',len(P)-1,'critical',dict(sorted(Counter(s.bit_count()-1 for s in nonaugmented_critical).items())),
              'Hasse_relations',edges,'acyclic',True,'integer_Morse_boundary_nonzero',0,
              'mod2_boundary_ranks',ranks,'remaining_cells',remaining)
    print('ALL_CHECKS_PASS')

if __name__=='__main__': main()

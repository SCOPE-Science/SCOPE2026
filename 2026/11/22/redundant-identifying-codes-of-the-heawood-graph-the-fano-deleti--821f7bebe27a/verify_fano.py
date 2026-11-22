#!/usr/bin/env python3
"""Reproduce the redundant identifying-code census on the Fano incidence graph.

Uses only the Python standard library. Vertex labels 0..6 are points;
7..13 are lines, where line 7+j contains j,j+1,j+3 mod 7.
"""
from collections import Counter
from itertools import combinations, permutations

P = range(7)
L = range(7, 14)
lines = [{j % 7, (j + 1) % 7, (j + 3) % 7} for j in P]
assert len({frozenset(a) for a in lines}) == 7
assert all(sum(p in ell for ell in lines) == 3 for p in P)
N = [1 << i for i in range(14)]
for j, ell in enumerate(lines):
    for p in ell:
        N[p] |= 1 << (7 + j)
        N[7 + j] |= 1 << p
assert all(n.bit_count() == 4 for n in N)


def valid_deleted(t):
    """Direct two-domination and symmetric-difference conditions on S=V\\T."""
    s = ((1 << 14) - 1) ^ t
    return (all((v & s).bit_count() >= 2 for v in N)
            and all(((N[i] ^ N[j]) & s).bit_count() >= 2
                    for i in range(14) for j in range(i)))


def classified(t):
    """Independent finite-geometric conditions on deleted point/line vertices."""
    pts = [i for i in P if t >> i & 1]
    lns = [j for j in P if t >> (7 + j) & 1]
    k = len(pts) + len(lns)
    if k <= 2:
        return True
    if k >= 5:
        return False
    if k == 3:
        if len(pts) == 3:
            return not any(set(pts) == ell for ell in lines)
        if len(lns) == 3:
            return not any(all(p in lines[j] for j in lns) for p in P)
        if len(pts) == 1:
            return sum(pts[0] in lines[j] for j in lns) == 1
        if len(lns) == 1:
            return sum(p in lines[lns[0]] for p in pts) == 1
    if k == 4:
        if len(pts) == 4:
            return any(set(pts) == set(P) - ell for ell in lines)
        if len(lns) == 4:
            return any(set(lns) == set(P) - {j for j in P if p in lines[j]} for p in P)
        if len(pts) == 2:
            return all(sum(p in lines[j] for j in lns) == 1 for p in pts) and all(sum(p in lines[j] for p in pts) == 1 for j in lns)
    return False

codes = Counter()
triples = []
quads = []
for t in range(1 << 14):
    direct = valid_deleted(t)
    geometry = classified(t)
    assert direct == geometry, (hex(t), direct, geometry)
    if direct:
        codes[14 - t.bit_count()] += 1
        if t.bit_count() == 3:
            triples.append(t)
        if t.bit_count() == 4:
            quads.append(t)
assert dict(codes) == {10: 98, 11: 224, 12: 91, 13: 14, 14: 1}, codes
assert len(triples) == 224 and len(quads) == 98
# Each valid deletion triple extends; every smaller deletion extends too.
for t in range(1 << 14):
    if valid_deleted(t):
        assert any(q & t == t for q in quads), hex(t)

# Full automorphism group from the 168 collineations and one point-line duality.
line_lookup = {frozenset(ell): j for j, ell in enumerate(lines)}
automorphisms = []
for pi in permutations(P):
    image = [line_lookup.get(frozenset(pi[p] for p in ell)) for ell in lines]
    if any(j is None for j in image):
        continue
    phi = list(pi) + [7 + image[j] for j in P]
    automorphisms.append(phi)
assert len(automorphisms) == 168
# Correlation: p_i maps to L_{-i}, and L_j to p_{-j}.
dual = [7 + ((-i) % 7) for i in P] + [(-j) % 7 for j in P]
for phi in list(automorphisms):
    automorphisms.append([dual[phi[i]] for i in range(14)])
assert len({tuple(a) for a in automorphisms}) == 336
for phi in automorphisms:
    assert all(sum(1 << phi[k] for k in range(14) if N[i] >> k & 1) == N[phi[i]] for i in range(14))

def orbits(states):
    remaining = set(states)
    result = []
    while remaining:
        t = min(remaining)
        orb = {sum(1 << a[i] for i in range(14) if t >> i & 1)
               for a in automorphisms}
        assert orb <= remaining
        remaining.difference_update(orb)
        result.append((len(orb), t))
    return sorted(result)

orb4 = orbits(quads)
orb3 = orbits(triples)
assert [r for r, _ in orb4] == [14, 84], orb4
assert [r for r, _ in orb3] == [56, 168], orb3
print('VERIFY_FANO_OK')
print('redundant_polynomial:', ' + '.join(f'{codes[k]}z^{k}' for k in sorted(codes)))
print('deleted_4_orbits:', orb4, 'deleted_3_orbits:', orb3)

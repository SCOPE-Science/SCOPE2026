#!/usr/bin/env python3
"""Independent Fano-collineation enumeration of Heawood matching-complex character."""
from itertools import permutations
from collections import Counter

P = tuple(range(1, 8))
L = {ell: frozenset(p for p in P if (p & ell).bit_count() % 2 == 0) for ell in P}
assert len(set(L.values())) == 7
# Line-major order: different from a point-major verification.
E = [(p, ell) for ell in P for p in sorted(L[ell])]
index = {e: j for j, e in enumerate(E)}
face_masks = [0]
for mask in range(1, 1 << len(E)):
    used_p = used_l = 0
    admissible = True
    for k, (p, ell) in enumerate(E):
        if mask & (1 << k):
            if used_p & (1 << p) or used_l & (1 << ell):
                admissible = False
                break
            used_p |= 1 << p
            used_l |= 1 << ell
    if admissible:
        face_masks.append(mask)
assert len(face_masks) == 3462
face_lists = [tuple(i for i in range(21) if mask & (1 << i)) for mask in face_masks]
# Every collineation is determined by a permutation of the seven Fano points.
line_label = {support: ell for ell, support in L.items()}
collineations = []
for images in permutations(P):
    sigma = dict(zip(P, images))
    if not all(frozenset(sigma[p] for p in L[ell]) in line_label for ell in P):
        continue
    tau = {ell: line_label[frozenset(sigma[p] for p in L[ell])] for ell in P}
    collineations.append((sigma, tau))
assert len(collineations) == 168

def order(perm):
    img = list(range(21))
    for t in range(1, 17):
        img = [perm[i] for i in img]
        if img == list(range(21)):
            return t
    raise AssertionError('unexpected element order')

def lefschetz(perm):
    # Reduced simplicial Lefschetz number. The empty face contributes -1.
    total = -1
    for oriented in face_lists[1:]:
        images = [perm[i] for i in oriented]
        if set(images) != set(oriented):
            continue
        inversions = sum(images[i] > images[j]
                         for i in range(len(images)) for j in range(i + 1, len(images)))
        total += (-1) ** (len(oriented) - 1 + inversions)
    return total

# A factorization partitions all 21 edges into three disjoint perfect matchings.
all_edges = (1 << 21) - 1
perfect = {m for m in face_masks if m.bit_count() == 7}
assert len(perfect) == 24
factorizations = set()
for a in perfect:
    for b in perfect:
        if a < b and not a & b:
            c = all_edges ^ a ^ b
            if c in perfect:
                factorizations.add(frozenset((a, b, c)))
assert len(factorizations) == 8

def transfer(mask, permutation):
    return sum(1 << permutation[i] for i in range(21) if mask & (1 << i))

profile = Counter()
factorization_profile = Counter()
all_traces = []
perm_char_inner = 0
residual_norm = 0
cross_term = 0
for sigma, tau in collineations:
    for dual in (0, 1):
        # The polarity (p,ell) -> (ell,p) reverses the bipartition.
        edge_image = [(sigma[ell], tau[p]) if dual else (sigma[p], tau[ell]) for p, ell in E]
        perm = [index[e] for e in edge_image]
        key = (dual, order(perm), lefschetz(perm))
        profile[key] += 1
        all_traces.append(key[2])
        fixed = sum(frozenset(transfer(m, perm) for m in partition) == partition
                    for partition in factorizations)
        factorization_profile[(dual, order(perm), fixed)] += 1
        rem = key[2] - fixed
        perm_char_inner += fixed * fixed
        residual_norm += rem * rem
        cross_term += fixed * rem
expected = {
    (0, 1, 16): 1, (0, 2, 0): 21, (0, 3, 1): 56,
    (0, 4, 0): 42, (0, 7, 2): 48,
    (1, 2, 4): 28, (1, 6, 1): 56, (1, 8, 0): 84,
}
assert profile == expected, (profile, expected)
assert len(all_traces) == 336
assert sum(all_traces) == 336  # full-group invariant dimension = 1
assert sum(x * x for x in all_traces) == 3 * 336
assert factorization_profile == {
    (0, 1, 8): 1, (0, 2, 0): 21, (0, 3, 2): 56,
    (0, 4, 0): 42, (0, 7, 1): 48,
    (1, 2, 2): 28, (1, 6, 2): 56, (1, 8, 0): 84,
}
assert perm_char_inner == 2 * 336
assert residual_norm == 336
assert cross_term == 0
print('OK: 336 graph symmetries; complete eight-type character table.')
print('OK: eight perfect-matching factorizations, their permutation character,')
print('and an orthogonal irreducible degree-eight residual representation.')

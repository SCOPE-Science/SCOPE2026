#!/usr/bin/env python3
"""Finite exact-rational illustration of atom separation; not an infinite proof."""
from fractions import Fraction as Q

lam = Q(1, 2)
gap = Q(1, 2)
length = Q(1)
# On [0,3/5) use x/2+7/10; on (3/5,1] use x/2-3/10.
branches = [((Q(0), Q(3, 5)), Q(7, 10)),
            ((Q(3, 5), Q(1)), Q(-3, 10))]
atoms = [(Q(0), Q(1))]
checks = 0
for n in range(1, 17):
    nxt = []
    for start, stop in atoms:
        for (lo, hi), shift in branches:
            left, right = max(start, lo), min(stop, hi)
            if left <= right:
                nxt.append((lam * left + shift, lam * right + shift))
    atoms = sorted(set(nxt))
    assert len(atoms) == len(nxt), 'distinct words produced equal atoms'
    assert atoms
    for left, right in atoms:
        assert left <= right
        assert right - left <= length * lam**n
        checks += 2
    for j in range(len(atoms) - 1):
        assert atoms[j + 1][0] - atoms[j][1] >= gap * lam**(n - 1)
        checks += 1
    assert all(Q(0) <= a <= b <= Q(1) for a, b in atoms)
    checks += 1
print('PASS: finite exact-rational atom checks:', checks,
      'levels: 1–16; final atoms:', len(atoms))

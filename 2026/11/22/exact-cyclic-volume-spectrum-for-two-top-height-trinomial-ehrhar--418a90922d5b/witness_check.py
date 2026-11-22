"""Exact witness heights for cyclic two-high Ehrhart simplices."""
from math import gcd

WITNESSES = {4: (1, 2, 2, 3), 5: (2, 4, 4),
             6: (2, 5, 5), 8: (4, 5, 7), 10: (5, 6, 9)}
for m, residues in WITNESSES.items():
    assert gcd(m, *residues) == 1
    h = []
    for j in range(m):
        t = sum((j * r) % m for r in residues)
        assert t % m == 0
        h.append(t // m)
    assert sorted(h) == [0] + [1] * (m - 3) + [2, 2]
    print('PASS order', m, 'heights', h)
print('WITNESS_CHECK_PASS')

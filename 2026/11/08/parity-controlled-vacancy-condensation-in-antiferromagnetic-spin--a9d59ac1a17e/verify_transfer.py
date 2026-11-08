"""Independent boundary-state contraction for the spin-one wheel model.

Run: python verify_transfer.py
Computes the least bond energy and its multiplicity at each exact occupancy.
"""
from collections import defaultdict
from fractions import Fraction


def record(table, key, energy, mult):
    old = table.get(key)
    if old is None or energy < old[0]:
        table[key] = (energy, mult)
    elif energy == old[0]:
        table[key] = (old[0], old[1] + mult)


def occupancy_sectors(n):
    full = {}
    for hub in (-1, 0, 1):
        for first in (-1, 0, 1):
            # Boundary state (last spin, occupied count).
            v = {(first, int(hub != 0) + int(first != 0)):
                 (hub * first, 1)}
            for j in range(1, n):
                w = {}
                for (last, occupied), (energy, count) in v.items():
                    for new in (-1, 0, 1):
                        record(w, (new, occupied + int(new != 0)),
                               energy + last * new + hub * new, count)
                v = w
            for (last, occupied), (energy, count) in v.items():
                record(full, occupied, energy + last * first, count)
    return full


def claimed_sector(n, occupied):
    if n % 2 == 0:
        if occupied == 0: return (0, 1)
        if occupied == n: return (-n, 2)
        if occupied == n + 1: return (-n, 4)
    else:
        if occupied == 0: return (0, 1)
        if occupied == n - 1: return (-(n - 2), 4*n)
        if occupied == n + 1: return (-(n - 1), 2*n)
    return None


def check(n):
    table = occupancy_sectors(n)
    assert len(table) == n + 2
    for q in range(n + 2):
        e, c = table[q]
        assert c >= 1
        if n % 2 == 0:
            assert e >= -min(q, n)  # Local triangle lower bound.
        else:
            if q == 0: assert e == 0
            elif q < n: assert e >= 1-q
            elif q == n: assert e >= -(n-2)
            else: assert e >= -(n-1)
        claimed = claimed_sector(n, q)
        if claimed is not None:
            assert (e, c) == claimed, (n, q, (e, c), claimed)
    # Independently recover the phase envelope by minimizing all n+2 sectors.
    if n % 2:
        brks = [Fraction(1, 2), Fraction(n-2,n-1)]
        endpoints = [(0,1), (n-1,4*n), (n+1,2*n)]
    else:
        brks = [Fraction(0), Fraction(1)]
        endpoints = [(0,1), (n,2), (n+1,4)]
    ds = sorted(set([Fraction(-3), Fraction(3)] + brks +
                    [(x+y)/2 for x,y in zip([-3]+brks, brks+[3])]))
    for d in ds:
        min_energy = min(e + d*q for q,(e,c) in table.items())
        desired = min(table[q][0] + d*q for q,c in endpoints)
        assert min_energy == desired, (n, d, min_energy, desired)
        count = sum(c for q,(e,c) in table.items() if e + d*q == min_energy)
        count_expected = sum(c for q,c in endpoints
                             if table[q][0] + d*q == desired)
        assert count == count_expected, (n, d, count, count_expected)
    print(f"rim={n}: exact-sector DP and boundary multiplicities PASS")


if __name__ == '__main__':
    for size in range(3, 71):
        check(size)
    print('TRANSFER PASS')

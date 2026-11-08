"""Exact integer check of finite cyclic two-sided halo saturation.
Run: python3 VERIFY.py
This is finite corroboration; the proof in RESULT.md covers all N.
"""
from itertools import combinations

def masks(n):
    out = {}
    for length in range(1, n + 1):
        for start in range(n):
            bitmask = sum(1 << ((start + j) % n) for j in range(length))
            out[bitmask] = length
    return list(out.items())

def halo(n, subset, level_numer=2, level_denom=3, arcs=None):
    arcs = masks(n) if arcs is None else arcs
    covered = 0
    for arc, length in arcs:
        # integer implementation of |E cap I|/|I| > level_numer/level_denom
        if level_denom * (arc & subset).bit_count() > level_numer * length:
            covered |= arc
    return covered

def predicted(n):
    return n // 2 + 1 + (n % 4 == 3)

def check():
    exhaustive = 0
    for n in range(3, 15):
        arcs = masks(n)
        allbits = (1 << n) - 1
        least = None
        for k in range(1, n + 1):
            count = 0
            for choices in combinations(range(n), k):
                subset = sum(1 << j for j in choices)
                count += halo(n, subset, arcs=arcs) == allbits
            if count:
                least = k
                break
        assert least == predicted(n), (n, least, predicted(n))
        exhaustive += 1
    constructed = 0
    for n in range(3, 201):
        k = predicted(n)
        subset = (1 << k) - 1
        assert halo(n, subset) == (1 << n) - 1, (n, k)
        constructed += 1
    checkerboard = 0
    for n in range(4, 101, 2):
        subset = sum(1 << j for j in range(0, n, 2))
        assert halo(n, subset, 2, 3) != (1 << n) - 1
        assert halo(n, subset, 199, 300) == (1 << n) - 1
        checkerboard += 1
    print(f'VERIFY_OK exhaustive_orders={exhaustive} contiguous_constructions={constructed} checkerboard_thresholds={checkerboard}')

if __name__ == '__main__':
    check()

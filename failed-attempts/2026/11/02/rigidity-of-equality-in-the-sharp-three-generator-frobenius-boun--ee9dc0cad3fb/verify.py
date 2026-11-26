#!/usr/bin/env python3
"""Finite diagnostic for equality in the 3-generator Frobenius bound.
Not an infinite proof: the accompanying proof gives the universal result.
"""
from math import gcd
import heapq
import sys


def frobenius_apery(a: int, b: int, c: int) -> int:
    """Least nonnegative costs by residue modulo c, using generators a,b."""
    infinity = c * c * c + c
    distance = [infinity] * c
    distance[0] = 0
    q = [(0, 0)]
    while q:
        total, residue = heapq.heappop(q)
        if total != distance[residue]:
            continue
        for step in (a, b):
            dest = (residue + step) % c
            nd = total + step
            if nd < distance[dest]:
                distance[dest] = nd
                heapq.heappush(q, (nd, dest))
    assert max(distance) < infinity
    return max(distance) - c


def expected_equality(a: int, b: int, c: int) -> bool:
    return (a >= 2 and b == a + 1 and c == 2 * a) or (a == 1 and b == 2 and c % 2 == 0)


def run(max_c: int = 95) -> None:
    checked = equalities = 0
    for c in range(3, max_c + 1):
        for b in range(2, c):
            for a in range(1, b):
                if gcd(gcd(a, b), c) != 1:
                    continue
                checked += 1
                f = frobenius_apery(a, b, c)
                bound = b * ((c + 1) // 2) - c - 1
                assert f <= bound, (a, b, c, f, bound)
                actual = f == bound
                wanted = expected_equality(a, b, c)
                assert actual == wanted, (a, b, c, f, bound, wanted)
                equalities += actual
    print(f"PASS: checked {checked} coprime triples, {equalities} equality cases, 3<=c<={max_c}")

if __name__ == '__main__':
    run(int(sys.argv[1]) if len(sys.argv) > 1 else 95)

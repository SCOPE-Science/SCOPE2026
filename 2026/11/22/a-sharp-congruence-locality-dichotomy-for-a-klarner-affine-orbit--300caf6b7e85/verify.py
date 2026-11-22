#!/usr/bin/env python3
"""Independent finite verification of a modular affine-orbit theorem."""
from collections import deque


def orbit_mod(m):
    assert m >= 1
    seen = bytearray(m)
    queue = deque([0])
    seen[0] = 1
    while queue:
        x = queue.popleft()
        for y in ((2*x) % m, (3*x+2) % m, (6*x+3) % m):
            if not seen[y]:
                seen[y] = 1
                queue.append(y)
    return seen


def check(limit=2000):
    for m in range(1,limit+1):
        seen = orbit_mod(m)
        full = all(seen)
        expected = m%6 != 0
        assert full == expected, (m, sum(seen), expected)
        if m%6 == 0:
            assert not seen[1], m
    print(f'PASS: all {limit} moduli, exact all-class criterion m%6 != 0')
    for m in (1, 6, 12, 18, 36, 72, 100, 125, 243, 625, 1024):
        print(f'm={m:4d} classes_reached={sum(orbit_mod(m)):4d}/{m}')


if __name__ == '__main__':
    check()

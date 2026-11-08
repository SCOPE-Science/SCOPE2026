#!/usr/bin/env python3
"""Independent exact enumeration of finite cyclic Rule 90 necklaces."""
from collections import defaultdict


def rotate(x, n, k):
    k %= n
    if k == 0:
        return x
    mask = (1 << n) - 1
    return ((x << k) | (x >> (n - k))) & mask


def necklace(x, n):
    return min(rotate(x, n, k) for k in range(n))


def update(x, n):
    # Direct per-cell implementation, including n=1 and n=2.
    y = 0
    for i in range(n):
        left = (x >> ((i - 1) % n)) & 1
        right = (x >> ((i + 1) % n)) & 1
        y |= (left ^ right) << i
    return y


def primitive_period(x, n):
    for p in range(1, n + 1):
        if n % p == 0 and all(((x >> i) & 1) == ((x >> (i % p)) & 1) for i in range(n)):
            return p
    raise AssertionError('unreachable')


def theorem_degree(y, n):
    p = primitive_period(y, n)
    t = n // p
    root = [(y >> i) & 1 for i in range(p)]
    if n % 2:
        return 2 if y.bit_count() % 2 == 0 else 0
    if p % 2:
        e = sum(root) % 2
        return 3 if e == 0 else (1 if t % 4 == 0 else 0)
    a = sum(root[0::2]) % 2
    b = sum(root[1::2]) % 2
    if a == b == 0:
        return 4
    return 2 if t % 2 == 0 else 0


def exhaustive(max_n=16):
    total_necklaces = 0
    for n in range(1, max_n + 1):
        predecessors = defaultdict(set)
        all_necklaces = set()
        for x in range(1 << n):
            source = necklace(x, n)
            all_necklaces.add(source)
            predecessors[necklace(update(x, n), n)].add(source)
        for y in all_necklaces:
            actual = len(predecessors.get(y, set()))
            predicted = theorem_degree(y, n)
            if actual != predicted:
                raise AssertionError((n, y, actual, predicted))
        total_necklaces += len(all_necklaces)
    return total_necklaces


def witnesses():
    n = 8
    examples = {
        '00000001': 0, '11111111': 1, '00010001': 2,
        '00000000': 3, '00000101': 4,
    }
    for w, degree in examples.items():
        assert theorem_degree(int(w, 2), n) == degree
    return len(examples)


if __name__ == '__main__':
    count = exhaustive()
    example_count = witnesses()
    print(f'VERIFY_OK lengths=1..16 necklaces={count} witnesses={example_count}')

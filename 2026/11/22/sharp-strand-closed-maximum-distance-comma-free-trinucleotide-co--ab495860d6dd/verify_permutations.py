#!/usr/bin/env python3
"""Exact permutation enumeration for strand-closed 3-letter comma-free codes.

Alphabet: 0..q-1, with Watson-Crick pairing 0<->1, 2<->3, ... .
For an optimal q-word distance-three code indexed by the first coordinate,
f is its middle-coordinate permutation and g = c f^{-1} c f its last one.
"""
from itertools import permutations


def is_valid(code, q):
    complement = lambda i: i ^ 1
    s = set(code)
    assert len(s) == len(code)
    if any(tuple(complement(x) for x in w[::-1]) not in s for w in code):
        return False
    for i, a in enumerate(code):
        for b in code[i + 1:]:
            if sum(x != y for x, y in zip(a, b)) != 3:
                return False
    return all(a[k:] + b[:k] not in s for a in code for b in code for k in (1, 2))


def count_full(q):
    count = 0
    sample = None
    for f in permutations(range(q)):
        inverse = [0] * q
        for i, x in enumerate(f):
            inverse[x] = i
        g = tuple(inverse[(f[i] ^ 1)] ^ 1 for i in range(q))
        if all(g[i] != f[f[i]] for i in range(q)):
            code = tuple((i, f[i], g[i]) for i in range(q))
            assert is_valid(code, q)
            count += 1
            sample = code
    return count, sample


def block_union(*codes):
    out = []
    offset = 0
    for code in codes:
        q = len(code)
        out += [tuple(v + offset for v in w) for w in code]
        offset += q
    assert is_valid(out, offset)
    return out


def main():
    expected = {2: 0, 4: 6, 6: 160, 8: 8988}
    samples = {}
    for q, answer in expected.items():
        found, sample = count_full(q)
        assert found == answer, (q, found, answer)
        if sample is not None:
            samples[q] = sample
        print(f'q={q}: {found} optimal codes')
    for sizes in [(4, 4), (4, 6), (6, 6), (4, 4, 6)]:
        code = block_union(*(samples[s] for s in sizes))
        print('block_union', sizes, 'size', len(code), 'valid')
    print('PASS: permutation characterization and block constructions')


if __name__ == '__main__':
    main()

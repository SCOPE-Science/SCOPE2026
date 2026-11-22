#!/usr/bin/env python3
"""Exhaustive binary square-root order test for the sharp initial boundary."""
from itertools import product


def embeds(pattern, text):
    j = 0
    for letter in text:
        if j < len(pattern) and pattern[j] == letter:
            j += 1
    return j == len(pattern)


def square_roots(word):
    roots = set()
    for k in range(1, len(word) // 2 + 1):
        for tup in product('01', repeat=k):
            root = ''.join(tup)
            if embeds(root + root, word):
                roots.add(root)
    return roots


def is_maximal(root, roots):
    return not any(len(other) > len(root) and embeds(root, other)
                   for other in roots)


def deficient_mixed_roots(word):
    roots = square_roots(word)
    optimum = max(map(len, roots), default=0)
    return sorted((r for r in roots if len(set(r)) == 2 and
                   len(r) < optimum and is_maximal(r, roots)),
                  key=lambda r: (len(r), r))


def main():
    threshold_hosts = []
    for n in range(0, 8):
        hits = []
        for bits in product('01', repeat=n):
            word = ''.join(bits)
            defect = deficient_mixed_roots(word)
            if defect:
                hits.append((word, defect))
        print(f'n={n}: qualifying_hosts={len(hits)}')
        if n < 7:
            assert not hits
        else:
            threshold_hosts = hits
    expected = ['0010101', '0101001', '0101011', '0110101',
                '1001010', '1010100', '1010110', '1101010']
    assert [w for w, _ in threshold_hosts] == expected
    for w, roots in threshold_hosts:
        assert roots in (['01'], ['10'])
        print(f'  {w}: maximal_mixed_roots={roots}')
    complement = str.maketrans('01', '10')
    unseen = set(expected)
    orbits = []
    while unseen:
        w = min(unseen)
        orbit = {w, w[::-1], w.translate(complement),
                 w[::-1].translate(complement)}
        assert orbit <= set(expected)
        orbits.append(sorted(orbit))
        unseen -= orbit
    print('symmetry_orbits=', orbits)
    assert len(orbits) == 2 and all(len(orb) == 4 for orb in orbits)
    print('PASS: complete length-zero-to-seven enumeration')


if __name__ == '__main__':
    main()

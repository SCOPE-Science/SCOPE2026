#!/usr/bin/env python3
"""Independent word-level enumeration of four-base DNA maximizers.

Does not use the permutation characterization or the associated counting code.
"""
from itertools import combinations, permutations, product


def direct_code_ok(words):
    words = frozenset(words)
    n = 3
    return (all(sum(a[t] != b[t] for t in range(n)) == n
                for a, b in combinations(words, 2))
            and all(a[k:] + b[:k] not in words
                    for a in words for b in words for k in range(1, n)))


def solutions(q):
    complement = lambda x: x ^ 1
    words = list(product(range(q), repeat=3))
    pairs = sorted({tuple(sorted((w, tuple(complement(x) for x in w[::-1]))))
                    for w in words})
    assert all(len(p) == 2 for p in pairs)
    found = []
    for p, r in combinations(pairs, 2):
        code = frozenset(p + r)
        if len(code) == 4 and direct_code_ok(code):
            found.append(code)
    return found


def main():
    sol = solutions(4)
    assert len(sol) == 6, len(sol)
    assert len(set(sol)) == 6
    group = [p for p in permutations(range(4))
             if all(p[i ^ 1] == (p[i] ^ 1) for i in range(4))]
    assert len(group) == 8
    unseen = set(sol)
    sizes = []
    while unseen:
        x = next(iter(unseen))
        orbit = {frozenset(tuple(p[t] for t in w) for w in x) for p in group}
        assert orbit <= set(sol)
        unseen -= orbit
        sizes.append(len(orbit))
    assert sorted(sizes) == [2, 4]
    for c in sorted(sol, key=lambda x: sorted(x)):
        print(' '.join(''.join(str(v) for v in w) for w in sorted(c)))
    print('q=4: 32 reverse-complement pairs, 496 candidate pair selections')
    print('q=4: exactly 6 optimal four-word codes; orbit sizes 2 and 4')
    # For q=2 the only possible nonempty strand-closed full-distance
    # code has two words, hence is one reverse-complement pair.
    binary_pairs = sorted({tuple(sorted((w, tuple(x ^ 1 for x in w[::-1]))))
                           for w in product(range(2), repeat=3)})
    assert len(binary_pairs) == 4
    assert all(not direct_code_ok(pair) for pair in binary_pairs)
    print('q=2: no nonempty admissible code')
    print('PASS: direct exhaustive word-level verification')


if __name__ == '__main__':
    main()

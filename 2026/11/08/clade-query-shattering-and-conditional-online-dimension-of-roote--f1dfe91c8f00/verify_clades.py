#!/usr/bin/env python3
"""Finite independent checks for the stated cluster-membership theorem.

No external dependencies. The general theorem is proved in RESULT.md;
this script only checks the indicated finite ranges.
"""
from functools import lru_cache
from itertools import combinations
from collections import Counter

@lru_cache(maxsize=None)
def trees(mask):
    """Return distinct sets of proper nontrivial clades of rooted binary trees."""
    if mask.bit_count() == 1:
        return (frozenset(),)
    low = mask & -mask
    answers = set()
    s = (mask - 1) & mask
    while s:
        if s & low:
            t = mask ^ s
            for a in trees(s):
                for b in trees(t):
                    c = a | b
                    if s.bit_count() > 1:
                        c = c | {s}
                    if t.bit_count() > 1:
                        c = c | {t}
                    answers.add(frozenset(c))
        s = (s - 1) & mask
    return tuple(sorted(answers, key=lambda f: tuple(sorted(f))))


def laminar(support):
    for a, b in combinations(support, 2):
        if a & b and (a & b) != a and (a & b) != b:
            return False
    return True


def shatters(support, concepts):
    support = tuple(support)
    traces = set()
    for tree in concepts:
        traces.add(sum((1 << i) for i, q in enumerate(support) if q in tree))
        if len(traces) == (1 << len(support)):
            return True
    return len(traces) == (1 << len(support))


def associated_stirling(m, k):
    @lru_cache(None)
    def a(v, j):
        if v == 0:
            return int(j == 0)
        if j < 1 or v < 2*j:
            return 0
        return j*a(v-1, j) + (v-1)*a(v-2, j-1)
    return a(m, k)


def exact_ldim(concepts, queries):
    concepts = tuple(concepts)
    N = len(concepts)
    masks = [sum(1 << i for i, c in enumerate(concepts) if q in c) for q in queries]
    @lru_cache(None)
    def rank(state):
        best = 0
        for pos in masks:
            a = state & pos
            b = state & ~pos
            if a and b:
                best = max(best, 1 + min(rank(a), rank(b)))
        return best
    return rank((1 << N) - 1)


def main():
    count_laminar = 0
    count_conditional = 0
    for n in range(2, 7):
        concept_set = trees((1 << n) - 1)
        expected_trees = 1
        for k in range(3, 2*n-1, 2):
            expected_trees *= k
        assert len(concept_set) == expected_trees, (n, len(concept_set))
        possible = tuple(q for q in range(1, 1 << n)
                         if 2 <= q.bit_count() < n)
        faces = {frozenset()}
        for tree in concept_set:
            q = tuple(tree)
            for count in range(1, len(q)+1):
                for sub in combinations(q, count):
                    faces.add(frozenset(sub))
        assert all(laminar(face) for face in faces)
        for face in faces:
            assert shatters(face, concept_set), ('unshattered laminar', n, face)
            count_laminar += 1
        counts = Counter(map(len, faces))
        for k in range(n-1):
            assert counts[k] == associated_stirling(n+k, k+1), (n, k, counts)
        if n <= 4 or n == 5:
            # Exhaustive conditional checks through n=4; nontrivial constrained n=5 cases.
            for positive in faces:
                if n == 5 and len(positive) < 2:
                    continue
                filtered = tuple(c for c in concept_set if positive <= c)
                assert filtered
                assert exact_ldim(filtered, possible) == n-2-len(positive), (n, positive)
                count_conditional += 1
        print('n=', n, 'trees=', len(concept_set), 'faces=', len(faces),
              'polynomial=', [counts[i] for i in range(n-1)])
    print('PHYLO_CLADE_SHATTER_PASS', 'faces=', count_laminar,
          'conditional_Ldim_cases=', count_conditional)

if __name__ == '__main__':
    main()

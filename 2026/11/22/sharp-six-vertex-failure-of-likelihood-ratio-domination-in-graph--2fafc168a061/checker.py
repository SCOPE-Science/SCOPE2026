#!/usr/bin/env python3
"""Exact, standalone certificate for the likelihood-ratio boundary in finite graph parking."""
from collections import Counter, defaultdict
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import factorial


def edge_masks(n):
    pairs = tuple(combinations(range(n), 2))
    for code in range(1 << len(pairs)):
        yield code, tuple(pair for i, pair in enumerate(pairs) if (code >> i) & 1)


def neighbors(n, edges):
    adjacent = [0] * n
    for i, j in edges:
        adjacent[i] |= 1 << j
        adjacent[j] |= 1 << i
    return adjacent


def maximal_independent_cardinalities(n, adj):
    cnt = Counter()
    full = (1 << n) - 1
    for mask in range(1 << n):
        independent = all((adj[i] & mask) == 0 for i in range(n) if mask & (1 << i))
        if not independent:
            continue
        dominated = mask
        for i in range(n):
            if mask & (1 << i):
                dominated |= adj[i]
        if dominated == full:
            cnt[mask.bit_count()] += 1
    total = sum(cnt.values())
    assert total > 0
    return {k: Fraction(v, total) for k, v in cnt.items()}


def sequential_by_recursion(n, adj):
    full = (1 << n) - 1
    @lru_cache(None)
    def distribution(available):
        if available == 0:
            return {0: Fraction(1)}
        chosen = [i for i in range(n) if available & (1 << i)]
        counts = defaultdict(Fraction)
        for i in chosen:
            rest = available & ~(adj[i] | (1 << i))
            for k, probability in distribution(rest).items():
                counts[k+1] += probability / len(chosen)
        return dict(counts)
    return distribution(full)


def sequential_by_permutations(n, adj):
    counts = Counter()
    for order in permutations(range(n)):
        occupied = 0
        for i in order:
            if (occupied & adj[i]) == 0:
                occupied |= (1 << i)
        counts[occupied.bit_count()] += 1
    return {k: Fraction(v, factorial(n)) for k, v in counts.items()}


def ratio_ordered(seq, static):
    # Both models have exactly the same positive support:
    # every maximal independent set has positive sequential probability.
    ks = sorted(static)
    assert set(seq) == set(static)
    return all(seq[a]*static[b] <= seq[b]*static[a]
               for a, b in zip(ks, ks[1:]))


def first_order(seq, static):
    total_seq = total_stat = Fraction(0)
    for k in sorted(static):
        total_seq += seq[k]
        total_stat += static[k]
        if total_seq > total_stat:
            return False
    return True


def main():
    graph_cases = 0
    order_checks = 0
    permutation_comparisons = 0
    for n in range(1, 6):
        by_n = 0
        for _, edges in edge_masks(n):
            adj = neighbors(n, edges)
            stat = maximal_independent_cardinalities(n, adj)
            seq = sequential_by_recursion(n, adj)
            per = sequential_by_permutations(n, adj)
            assert sum(stat.values()) == sum(seq.values()) == 1
            assert per == seq, (n, edges, per, seq)
            permutation_comparisons += 1
            assert ratio_ordered(seq, stat), (n, edges, seq, stat)
            order_checks += max(len(stat)-1, 0)
            graph_cases += 1
            by_n += 1
        assert by_n == 2 ** (n*(n-1)//2)
        print('n=%d labeled_graphs=%d' % (n, by_n))
    # Sharp six-vertex witness: universal vertex 0, a disjoint K2, and a P3.
    witness = tuple((0, v) for v in range(1, 6)) + ((1, 2), (3, 4), (3, 5))
    adj = neighbors(6, witness)
    seq = sequential_by_recursion(6, adj)
    stat = maximal_independent_cardinalities(6, adj)
    assert seq == {1: Fraction(1,6),2: Fraction(5,18),3: Fraction(5,9)}
    assert stat == {1: Fraction(1,5),2: Fraction(2,5),3: Fraction(2,5)}
    assert sequential_by_permutations(6, adj) == seq
    assert first_order(seq, stat) and not ratio_ordered(seq, stat)
    # Test exact family formulas against distinct finite graph instances.
    for m in range(2, 16):
        n = m+4
        edges = [(0,i) for i in range(1,n)] + [(1,2)] + [(3,j) for j in range(4,n)]
        s = sequential_by_recursion(n, neighbors(n, edges))
        expected = {1: Fraction(1, m+4),
                    2: Fraction(m+3,(m+4)*(m+1)),
                    m+1: Fraction(m*(m+3),(m+4)*(m+1))}
        assert s == expected, (m, s, expected)
        assert not ratio_ordered(s, {1:Fraction(1,5), 2:Fraction(2,5), m+1:Fraction(2,5)})
    print('EXACT PASS:',graph_cases,'labeled graphs through five vertices,',
          order_checks,'adjacent-support order inequalities,',
          permutation_comparisons,'independent exhaustive permutation comparisons,',
          'one sharp six-vertex witness, and fourteen family instances')

if __name__ == '__main__':
    main()

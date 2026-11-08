"""Exact reproduction of a five-site monomer-adsorption edge-augmentation theorem.

Run: python3 verify.py
Only Python standard library is required. All numerical comparisons are rational.
"""
from fractions import Fraction
from functools import lru_cache
from itertools import combinations, permutations
from math import comb, factorial


def bits_graph(n, edge_bits):
    pairs = list(combinations(range(n), 2))
    nb = [1 << i for i in range(n)]
    for k, (i, j) in enumerate(pairs):
        if (edge_bits >> k) & 1:
            nb[i] |= 1 << j
            nb[j] |= 1 << i
    return nb


def expected_recursion(n, edge_bits):
    nb = bits_graph(n, edge_bits)
    @lru_cache(None)
    def f(remaining):
        if remaining == 0:
            return Fraction(0)
        total, todo = Fraction(0), remaining
        while todo:
            vbit = todo & -todo
            todo ^= vbit
            i = vbit.bit_length() - 1
            total += f(remaining & ~nb[i])
        return 1 + total / remaining.bit_count()
    return f((1 << n) - 1)


def prefix_means_permutations(n, edge_bits):
    nb = bits_graph(n, edge_bits)
    sums = [0] * (n + 1)
    for order in permutations(range(n)):
        occupied = 0
        for k, v in enumerate(order):
            sums[k] += occupied.bit_count()
            if not (nb[v] & occupied):
                occupied |= 1 << v
        sums[n] += occupied.bit_count()
    return [Fraction(v, factorial(n)) for v in sums]


def connected(n, edge_bits):
    nb = bits_graph(n, edge_bits)
    discovered = 1
    while True:
        enlarged = discovered
        for v in range(n):
            if (discovered >> v) & 1:
                enlarged |= nb[v]
        if enlarged == discovered:
            return discovered == (1 << n) - 1
        discovered = enlarged


def edge_mask(n, edges):
    pairs = list(combinations(range(n), 2))
    wanted = {tuple(sorted(edge)) for edge in edges}
    assert wanted.issubset(set(pairs))
    return sum(1 << k for k, p in enumerate(pairs) if p in wanted)


def pair_class(n, before, added_index, representatives):
    pairs = list(combinations(range(n), 2))
    after = before | (1 << added_index)
    for cls, (ref_before, ref_added) in enumerate(representatives):
        ref_after = ref_before | (1 << ref_added)
        for order in permutations(range(n)):
            remap = {}
            for k, (u, v) in enumerate(pairs):
                a, b = sorted((order[u], order[v]))
                remap[k] = pairs.index((a, b))
            perm_before = sum(1 << remap[k] for k in range(len(pairs)) if (before >> k) & 1)
            perm_after = sum(1 << remap[k] for k in range(len(pairs)) if (after >> k) & 1)
            if perm_before == ref_before and perm_after == ref_after:
                return cls
    return None


def bernstein_to_power(means):
    n = len(means) - 1
    output = [Fraction(0) for _ in range(n + 1)]
    for k, a in enumerate(means):
        for r in range(n-k+1):
            output[k+r] += a * comb(n, k) * comb(n-k, r) * (-1)**r
    return output


def run():
    # Consecutive graphs: P5, a C4 with a pendant vertex, and K_{2,3}.
    p5 = [(0,2),(0,4),(1,2),(1,3)]
    e01 = (0,3)
    e12 = (1,4)
    g0 = edge_mask(5, p5)
    g1 = edge_mask(5, p5 + [e01])
    g2 = edge_mask(5, p5 + [e01,e12])
    cases = (g0,g1,g2)
    expected_means = [
        [Fraction(0),Fraction(1),Fraction(8,5),Fraction(2),Fraction(34,15),Fraction(37,15)],
        [Fraction(0),Fraction(1),Fraction(3,2),Fraction(19,10),Fraction(67,30),Fraction(38,15)],
        [Fraction(0),Fraction(1),Fraction(7,5),Fraction(9,5),Fraction(11,5),Fraction(13,5)],
    ]
    for g,m in zip(cases, expected_means):
        assert prefix_means_permutations(5,g) == m
        assert expected_recursion(5,g) == m[-1]
    polynomials = [bernstein_to_power(row) for row in expected_means]
    gain = [Fraction(0),Fraction(0),Fraction(-1),Fraction(2),Fraction(-7,6),Fraction(7,30)]
    assert [b-a for a,b in zip(polynomials[0],polynomials[1])] == gain
    assert [b-a for a,b in zip(polynomials[1],polynomials[2])] == gain
    # Independent complete 5! permutation check of the 2^10 labeled graphs.
    # This also checks the recurrence on every graph, not just the witness trio.
    for n in range(1,6):
        total = 1 << comb(n,2)
        all_expectations = []
        for mask in range(total):
            recurrence = expected_recursion(n,mask)
            permutation = prefix_means_permutations(n,mask)[-1]
            assert recurrence == permutation, (n,mask)
            all_expectations.append(recurrence)
        positive = []
        cnt = [0,0]
        pairs = list(combinations(range(n),2))
        for mask in range(total):
            if not connected(n,mask):
                continue
            for edge_index in range(len(pairs)):
                if mask >> edge_index & 1:
                    continue
                difference = all_expectations[mask | 1<<edge_index] - all_expectations[mask]
                if difference > 0:
                    positive.append((mask,edge_index,difference))
                    assert n == 5
                    assert difference == Fraction(1,15)
                    cls = pair_class(5,mask,edge_index,[(g0, pairs.index(tuple(sorted(e01)))),
                                                            (g1, pairs.index(tuple(sorted(e12))))])
                    assert cls is not None
                    cnt[cls] += 1
        if n < 5:
            assert len(positive) == 0
        else:
            assert len(positive) == 180
            assert cnt == [120,60]
        print('vertices',n,'labeled_graphs',total,'positive_connected_augmentations',len(positive), 'class_counts',cnt)
    # The crossover follows since 21p^2-70p+60 is positive on R
    # (discriminant -140). Evaluate the cubic at exact rational endpoints.
    def cubic(x):
        return 7*x**3 - 35*x**2 + 60*x - 30
    assert cubic(Fraction(849,1000)) < 0 < cubic(Fraction(850,1000))
    assert cubic(Fraction(0)) < 0 < cubic(Fraction(1))
    print('gains_at_jamming',Fraction(1,15),Fraction(1,15))
    print('time_polynomial_difference_power_coefficients',gain)
    print('unique_p_crossover_in_interval',(Fraction(849,1000),Fraction(850,1000)))
    print('PASS exact finite classification and time-dependent law')


if __name__ == '__main__':
    run()

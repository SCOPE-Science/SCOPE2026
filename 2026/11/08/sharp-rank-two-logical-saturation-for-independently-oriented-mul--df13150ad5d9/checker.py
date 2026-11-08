"""Finite reproducibility checks for multitournament local-profile saturation.

All computations use exact integer or rational arithmetic. They check finite
instances only; the proof of the limiting law is mathematical, not computational.
"""
from itertools import product
from fractions import Fraction
from math import comb


def saturation_witness(k):
    """Return local orientation signatures for an optimal (2**k+1)-point model."""
    q = 1 << k
    n = q + 1
    s = [[None] * n for _ in range(n)]
    for d in range(1, q // 2 + 1):
        label = d - 1                 # canonical representative of complement pair
        for i in range(n):
            j = (i + d) % n
            assert s[i][j] is None and s[j][i] is None
            s[i][j] = label
            s[j][i] = (q - 1) ^ label
    return s


def deficient(s, v, q):
    return len({s[v][w] for w in range(len(s)) if w != v}) != q


def single_defect_probability(q, n):
    # Inclusion-exclusion for an n-1-sample coupon collector.
    return sum(((-1) ** (j + 1)) * comb(q, j) *
               Fraction((q - j) ** (n - 1), q ** (n - 1))
               for j in range(1, q + 1))


def conditional_defect_probability(q, n):
    # Conditioning on one known incident label leaves q-1 other labels.
    if n < 2:
        raise ValueError('n must be >= 2')
    return sum(((-1) ** (j + 1)) * comb(q - 1, j) *
               Fraction((q - j) ** (n - 2), q ** (n - 2))
               for j in range(1, q))


def enumerate_tournaments(k, n):
    q = 1 << k
    edges = [(i, j) for i in range(n) for j in range(i + 1, n)]
    count = 0
    defective = [0] * n
    pair_defective = [[0] * n for _ in range(n)]
    triple_defective = 0
    all_saturated = 0
    for labels in product(range(q), repeat=len(edges)):
        signatures = [[None] * n for _ in range(n)]
        for (i, j), color in zip(edges, labels):
            signatures[i][j] = color
            signatures[j][i] = (q - 1) ^ color
        defects = [deficient(signatures, v, q) for v in range(n)]
        count += 1
        all_saturated += not any(defects)
        for v in range(n):
            defective[v] += defects[v]
            for w in range(v + 1, n):
                pair_defective[v][w] += defects[v] and defects[w]
        if n >= 3:
            triple_defective += all(defects[:3])
    return count, defective, pair_defective, triple_defective, all_saturated


def main():
    # The explicit cyclic-factor construction attains the lower size q+1.
    for k in range(1, 7):
        s = saturation_witness(k)
        q = 1 << k
        n = q + 1
        assert all(s[i][j] ^ s[j][i] == q - 1
                   for i in range(n) for j in range(n) if i != j)
        assert all(not deficient(s, v, q) for v in range(n))
        assert all(sum((s[i][j] == a) for j in range(n) if i != j) == 1
                   for i in range(n) for a in range(q))
    checked = 0
    for k, n_values in [(1, [2, 3, 4, 5]), (2, [2, 3, 4])]:
        q = 1 << k
        for n in n_values:
            count, defective, pair, triple, saturated = enumerate_tournaments(k, n)
            p = single_defect_probability(q, n)
            assert p == conditional_defect_probability(q, n)
            for i in range(n):
                assert Fraction(defective[i], count) == p
                for j in range(i + 1, n):
                    assert Fraction(pair[i][j], count) == p * p
            if n < q + 1:
                assert saturated == 0
            if k == 1 and n == 3:
                # Pairwise independence does not imply mutual independence.
                assert Fraction(triple, count) == 0
                assert p ** 3 == Fraction(1, 8)
            checked += count
    print('ALL_CHECKS_OK finite_structures=', checked,
          'cyclic_witness_sizes=', [2 ** k + 1 for k in range(1, 7)])


if __name__ == '__main__':
    main()

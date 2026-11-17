"""Exact finite checks for Euclidean projections onto Hamming codeword polytopes.

Standard library only. The infinite-family theorem is analytical; these tests are
finite consistency checks of its candidate and supporting hyperplane.
"""

from fractions import Fraction
from itertools import combinations
import random


def syndrome(word, m):
    value = 0
    while word:
        lowbit = word & -word
        value ^= lowbit.bit_length()  # coordinate column indices 1..2**m-1
        word ^= lowbit
    return value


def enumerate_code(m):
    n = (1 << m) - 1
    return [word for word in range(1 << n) if syndrome(word, m) == 0]


def check_order(m):
    n = (1 << m) - 1
    codewords = enumerate_code(m)
    assert len(codewords) == 1 << (n - m)
    assert all(w.bit_count() >= 3 for w in codewords if w)
    total_equal = 0
    for i in range(n):
        triples = [w for w in codewords if w.bit_count() == 3 and ((w >> i) & 1)]
        assert len(triples) == (n - 1) // 2
        assert all(sum((w >> j) & 1 for w in triples) == 1
                   for j in range(n) if j != i)
        for w in codewords:
            dot_num = 6 * ((w >> i) & 1) - 2 * w.bit_count()
            assert dot_num <= 0
            is_equal = not w or (w.bit_count() == 3 and ((w >> i) & 1))
            assert (dot_num == 0) == bool(is_equal)
            total_equal += dot_num == 0
        # The projection coordinates have denominator n+3.
        proj_num = [n - 1 if j == i else 2 for j in range(n)]
        residual_num = [4 if j == i else -2 for j in range(n)]
        assert sum(proj_num[j] * residual_num[j] for j in range(n)) == 0
        assert Fraction(sum(t*t for t in residual_num), (n + 3)**2) == Fraction(4, n+3)
    return n, len(codewords), n * len(codewords), total_equal


def check_random(m, trials=2000):
    n = (1 << m) - 1
    rng = random.Random(93071 + m)
    parity_positions = [1 << j for j in range(m)]
    info_positions = [j for j in range(1, n + 1) if j not in parity_positions]
    for _ in range(trials):
        word = sum(1 << (j-1) for j in info_positions if rng.randrange(2))
        target = syndrome(word, m)
        for j in parity_positions:
            if target & j:
                word ^= 1 << (j-1)
        assert syndrome(word, m) == 0
        assert word == 0 or word.bit_count() >= 3
        i = rng.randrange(n)
        assert 6 * ((word >> i) & 1) - 2 * word.bit_count() <= 0
    return n, trials


def main():
    finite = [check_order(m) for m in (2, 3, 4)]
    sampled = [check_random(m) for m in (5, 6, 7)]
    assert finite == [(3,2,6,6),(7,16,112,28),(15,2048,30720,120)]
    print('HAMMING_HULL_EXACT_PASS finite=(n,codewords,noncode_vertices,face_equalities):', finite,
          ' sampled:', sampled)


if __name__ == '__main__':
    main()

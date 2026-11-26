"""Standalone exact finite checks for adjacent-swap radius-two balls.

The unbounded mathematical assertions require the proof in RESULT.md;
these exhaustive tests check finite cases and construction/normalization.
"""
from itertools import product
from fractions import Fraction
from math import comb


def brute_ball(word):
    reached = {word}
    layer = {word}
    for _ in range(2):
        layer = {
            w[:i] + (w[i + 1], w[i]) + w[i + 2:]
            for w in layer for i in range(len(w) - 1)
            if w[i] != w[i + 1]
        }
        reached |= layer
    return reached


def local_formula(word):
    n = len(word)
    boundaries = [i for i in range(n - 1) if word[i] != word[i + 1]]
    disjoint_pairs = sum(
        int(j >= i + 2)
        for k, i in enumerate(boundaries)
        for j in boundaries[k + 1:]
    )
    overlapping = sum(
        int(word[i] != word[i + 2])
        + int(len({word[i], word[i + 1], word[i + 2]}) == 3)
        for i in range(n - 2)
    )
    return 1 + len(boundaries) + disjoint_pairs + overlapping


def expected_mean(q, n):
    if n == 1:
        return Fraction(1)
    return (Fraction(1) + Fraction((n - 1) * (q - 1), q)
            + Fraction((n - 2) * (n + 1) * (q - 1) ** 2, 2 * q * q))


def binary_max(n):
    if n == 1:
        return 1
    if n == 2:
        return 2
    if n == 3:
        return 3
    if n == 4:
        return 6
    return (n * n - 3 * n + 6) // 2


def extremizer_constraint(word):
    return (all(word[i] != word[i + 1] for i in range(len(word) - 1))
            and all(word[i] != word[i + 2] for i in range(len(word) - 2)))


def check():
    test_counts = 0
    for q, max_n in [(2, 11), (3, 8), (4, 6)]:
        for n in range(1, max_n + 1):
            count = 0
            total = 0
            optimum = -1
            best_words = []
            for word in product(range(q), repeat=n):
                computed = len(brute_ball(word))
                assert computed == local_formula(word), (q, n, word, computed)
                total += computed
                count += 1
                if computed > optimum:
                    optimum, best_words = computed, [word]
                elif computed == optimum:
                    best_words.append(word)
            assert count == q ** n
            assert Fraction(total, count) == expected_mean(q, n), (q, n, total)
            if q == 2:
                assert optimum == binary_max(n), (q, n, optimum)
                if n >= 6:
                    assert len(best_words) == 2 and all(
                        word[i] != word[i + 1]
                        for word in best_words for i in range(n - 1))
                elif n == 5:
                    assert set(best_words) == {
                        tuple(int(c) for c in w)
                        for w in ('01001', '01010', '01101', '10010', '10101', '10110')
                    }
                elif n == 4:
                    assert set(best_words) == {(0,1,1,0), (1,0,0,1)}
            elif n >= 2:
                assert optimum == comb(n+1, 2)-1, (q, n, optimum)
                assert all(extremizer_constraint(word) for word in best_words)
                assert len(best_words) == q*(q-1)*(q-2)**(n-2)
            test_counts += count
            print('PASS q=%d n=%d words=%d sum=%d max=%d extremizers=%d' %
                  (q, n, count, total, optimum, len(best_words)))
    # Binary maximum proof's exact local reduction: check all boundary words of length <= 13.
    for N in range(1, 14):
        for bits in product(range(2), repeat=N):
            word = [0]
            for bit in bits:
                word.append(word[-1] ^ bit)
            b = sum(bits)
            s = sum(bits[i] * bits[i + 1] for i in range(N - 1))
            h = sum(bits[i] != bits[i + 1] for i in range(N - 1))
            f = 1 + b + comb(b, 2) - s + h
            z = N - b
            E = (not bits[0]) + (not bits[-1])
            C0 = sum(not bits[i] and not bits[i + 1] for i in range(N - 1))
            baseline = 2 + comb(N, 2)
            assert 2 * (f - baseline) == z*(z+7-2*N)-4*E-6*C0
            assert f == local_formula(tuple(word))
    print('VERIFY_OK total_direct_centers=%d' % test_counts)

if __name__ == '__main__':
    check()

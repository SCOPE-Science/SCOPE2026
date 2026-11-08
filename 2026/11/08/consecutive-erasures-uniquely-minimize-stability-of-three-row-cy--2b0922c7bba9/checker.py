"""Finite diagnostic for an exact three-row harmonic-frame erasure theorem."""
import itertools
import math
import numpy as np


def max_gram(N, erased):
    matrix = np.array(
        [[(1 + 2 * math.cos(2 * math.pi * (j - k) / N)) / 3
          for k in erased] for j in erased], dtype=float)
    return float(np.linalg.eigvalsh(matrix)[-1])


def consecutive(N, mask):
    return any(set(mask) == {(j + k) % N for k in range(3)} for j in range(N))


def expected(N):
    a = (1 + 2 * math.cos(2 * math.pi / N)) / 3
    b = (1 + 2 * math.cos(4 * math.pi / N)) / 3
    return 1 + (b + math.sqrt(b * b + 8 * a * a)) / 2


def main():
    count = 0
    for N in range(6, 37):
        best = expected(N)
        assert 1 - 3 * best / N > 0
        winners = []
        for mask in itertools.combinations(range(N), 3):
            actual = max_gram(N, mask)
            count += 1
            assert actual <= best + 1.e-10, (N, mask, actual, best)
            if abs(actual - best) < 1.e-10:
                winners.append(mask)
        assert len(winners) == N, (N, winners)
        assert all(consecutive(N, mask) for mask in winners)
    a = 2 / 3
    assert abs(expected(6) - (1 + a * math.sqrt(2))) < 1.e-13
    assert abs(max_gram(6, (0, 1, 3)) - (1 + math.sqrt(5) / 3)) < 1.e-13
    a = (1 + 2 * math.cos(2 * math.pi / 7)) / 3
    c = -(1 + 2 * math.cos(6 * math.pi / 7)) / 3
    assert 0 < c < (math.sqrt(2) - 1) * a
    print(f"THREE_ROW_ERASURE_PASS orders=31 masks={count} exact_equalities=31")


if __name__ == "__main__":
    main()

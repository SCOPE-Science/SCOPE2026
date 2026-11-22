"""Exact finite checks for the comparability-graded one-point type theorem.
Run: python3 checks/verify.py (from the result package root).
Only Python's standard library is required.
"""
from itertools import product


def partitions(n, low=1):
    """Each nondecreasing tuple of positive parts summing to n, exactly once."""
    if n == 0:
        yield ()
    else:
        for first in range(low, n + 1):
            for tail in partitions(n - first, first):
                yield (first,) + tail


def predicted(parts):
    """One-point comparability distribution from the extension bijection."""
    p = [1]
    for length in parts:
        q = [0] * (len(p) + length)
        for i, value in enumerate(p):
            for j in range(length + 1):
                q[i + j] += value
        p = q
    answer = [2 * value for value in p]
    answer[0] -= 1
    for length in parts:
        for degree in range(2, length + 1):
            answer[degree] += degree - 1
    return answer


def independent_brute(parts):
    """Enumerate every trichotomy of a new point versus named parameters.
    This implementation uses no generating functions or chain-formula cases.
    """
    n = sum(parts)
    less = set()
    start = 0
    for size in parts:
        for i in range(start, start + size):
            for j in range(i + 1, start + size):
                less.add((i, j))
        start += size
    count = [0] * (n + 1)
    # status -1 = x<old, +1 = old<x, 0 = incomparable.
    for status in product((-1, 0, 1), repeat=n):
        # Old comparisons force the lower/upper sets to be ideals/filters.
        if any((status[i] == -1 and status[j] != -1) or
               (status[j] == 1 and status[i] != 1)
               for i, j in less):
            continue
        # Any old points on opposite sides of x were already ordered.
        if any(status[i] == 1 and status[j] == -1 and (i, j) not in less
               for i in range(n) for j in range(n)):
            continue
        count[sum(s != 0 for s in status)] += 1
    return count


def unimodal(coeff):
    peak = 0
    while peak + 1 < len(coeff) and coeff[peak] <= coeff[peak + 1]:
        peak += 1
    return all(coeff[i] >= coeff[i + 1]
               for i in range(peak, len(coeff) - 1))


def log_concave(coeff):
    return all(coeff[i] * coeff[i] >= coeff[i - 1] * coeff[i + 1]
               for i in range(1, len(coeff) - 1))


def main():
    counts = []
    for n in range(1, 9):
        ps = list(partitions(n))
        bad_u, bad_l = [], []
        for parts in ps:
            guess = predicted(parts)
            actual = independent_brute(parts)
            assert guess == actual, (parts, guess, actual)
            if not unimodal(guess):
                bad_u.append(parts)
            if not log_concave(guess):
                bad_l.append(parts)
        counts.append((n, len(ps), bad_u, bad_l))
    assert [num for _, num, _, _ in counts] == [1, 2, 3, 5, 7, 11, 15, 22]
    assert [bad for _, _, bad, _ in counts] == [[], [], [], [], [], [], [], [(3, 5)]]
    assert counts[5][3] == [(2, 4), (3, 3)]
    assert all(not bad for _, _, _, bad in counts[:5])
    for a in range(1, 81):
        for b in range(a, 81):
            coeff = predicted((a, b))
            u_expected = (a <= 2 or b <= a + 1)
            l_expected = (a == 1 or (a == 2 and b in (2, 3)))
            assert unimodal(coeff) == u_expected, (a, b, 'unimodal')
            assert log_concave(coeff) == l_expected, (a, b, 'log-concave')
    assert predicted((3, 5)) == [1, 4, 8, 12, 11, 12, 6, 4, 2]
    assert predicted((2, 4)) == [1, 4, 8, 8, 9, 4, 2]
    assert predicted((3, 3)) == [1, 4, 8, 12, 6, 4, 2]
    for n, count, bad_u, bad_l in counts:
        print(f'n={n}: partitions={count}; nonunimodal={bad_u}; nonlogconcave={bad_l}')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()

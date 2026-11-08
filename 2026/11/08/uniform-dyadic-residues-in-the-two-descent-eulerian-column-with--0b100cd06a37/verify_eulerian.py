#!/usr/bin/env python3
"""Independent exact finite checks for the fixed-two-descent Eulerian residue theorem."""
from collections import Counter


def initial(k):
    return max(3, 2 * ((k + 1) // 2) - 1)


def value(n, k):
    q = 1 << k
    return (pow(3, n, q) - (n + 1) * pow(2, n, q)
            + n * (n + 1) // 2) % q


def core(n, k):
    q = 1 << k
    return (pow(3, n, q) + n * (n + 1) // 2) % q


def nu2(n):
    assert n != 0
    return (abs(n) & -abs(n)).bit_length() - 1


def verify():
    # The independent Eulerian triangle checks the closed formula.
    prev = [1]
    rowchecks = 0
    for n in range(2, 401):
        row = [0] * n
        for j in range(n):
            row[j] = (j + 1) * (prev[j] if j < len(prev) else 0) + (n - j) * (prev[j - 1] if j else 0)
        prev = row
        if n >= 3:
            expected = 3**n - (n + 1) * 2**n + n * (n + 1) // 2
            assert row[2] == expected, (n, row[2], expected)
            rowchecks += 1
    blocks = 0
    cells = 0
    for k in range(1, 13):
        q = 1 << k
        P = q << 1
        N = initial(k)
        assert N >= 3
        for a in (N, N + 1, N + 10):
            first = Counter()
            second = Counter()
            for n in range(a, a + P):
                v = value(n, k)
                assert v == core(n, k), (k, n)
                (first if n % 2 == 0 else second)[v] += 1
                cells += 1
            assert len(first) == len(second) == q
            assert all(first[y] == 1 and second[y] == 1 for y in range(q))
            blocks += 1
        assert value(N, k) == value(N + P, k)
        assert value(N, k) != value(N + P // 2, k)
        if N > 3:
            assert value(N - 1, k) != value(N - 1 + P, k)
            assert (N - 1) + nu2(N) < k
    valchecks = 0
    for k in range(1, 13):
        q = 1 << k
        for epsilon in (0, 1):
            for t in range(0, 145, 3):
                n = epsilon + 2 * t
                for h in (1, 2, 3, 4, 5, 7, 8, 16, 31, 32, 63, 64, 127):
                    m = n + 2 * h
                    delta = (core(m, k) - core(n, k)) % q
                    if nu2(h) < k:
                        assert delta != 0 and nu2(delta) == nu2(h), (k, n, h)
                    else:
                        assert delta == 0
                    valchecks += 1
    print('VERIFY_OK', 'Eulerian_recurrence_rows='+str(rowchecks),
          'dyadic_levels=1..12', 'complete_blocks='+str(blocks),
          'residue_inputs='+str(cells), 'isometry_pairs='+str(valchecks),
          'sharp_preperiod=PASS', 'least_period=PASS',
          'one_per_parity_fiber=PASS')


if __name__ == '__main__':
    verify()

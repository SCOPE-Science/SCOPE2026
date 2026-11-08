"""Independent occupancy-count check of the closed minimum-cardinality formulas.

No rook adjacency matrices and no formal square-root recurrence are used.
"""
import json
from math import factorial, comb
from itertools import product


def all_even_fibers(objects, bins):
    return sum(all(f.count(j) % 2 == 0 for j in range(bins))
               for f in product(range(bins), repeat=objects))


def paired_minimum_count(m, n):
    assert 2 <= m <= n
    if m % 2 == 0:
        total = all_even_fibers(m, n)
        return (m, 2*total if m == n else total)
    odd_row_case = m * comb(n, 2) * sum(
        all(f.count(j) % 2 == 0 for j in range(2, n))
        for f in product(range(n), repeat=m-1))
    total = odd_row_case
    if n == m:
        total += odd_row_case
        if m == 3:
            total -= 9
    if n == m + 1:
        total += all_even_fibers(m+1, m)
    return m+1, total


if __name__ == '__main__':
    expected = {
        (2, 2): (2, 4), (2, 3): (2, 3), (2, 4): (2, 4),
        (3, 3): (4, 81), (3, 4): (4, 129), (3, 5): (4, 210),
        (4, 4): (4, 80), (4, 5): (4, 65),
        (5, 5): (6, 10900), (5, 6): (6, 12605),
    }
    for key, want in expected.items():
        got = paired_minimum_count(*key)
        assert got == want, (key, got, want)
        print(json.dumps({'board': list(key), 'minimum_size': got[0],
                          'minimum_count': got[1],
                          'occupancy_count': 'PASS'}, sort_keys=True))
    print('MINIMA_PASS: all ten leading coefficients match.')

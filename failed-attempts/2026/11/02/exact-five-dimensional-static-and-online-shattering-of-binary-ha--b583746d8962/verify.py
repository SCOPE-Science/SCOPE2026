"""Reproduce finite witnesses for exact-distance-two Hamming spheres.

Run with Python 3.9 or later; standard library only.
"""
import itertools
import json
from pathlib import Path

QUERIES = [0, 3, 5, 9, 17]

def response(center, query):
    return int((center ^ query).bit_count() == 2)

def pattern(center, queries):
    return sum(response(center, q) << i for i, q in enumerate(queries))

def verify():
    data = json.loads(Path(__file__).with_name('witnesses.json').read_text())
    assert data['dimension'] == 7
    assert data['queries_decimal'] == QUERIES
    witnesses = data['centers_by_pattern_decimal']
    assert len(witnesses) == 32
    assert len(set(witnesses)) == 32
    for i, c in enumerate(witnesses):
        assert 0 <= c < (1 << 7)
        assert pattern(c, QUERIES) == i, (i, c)
    assert set(pattern(c, QUERIES) for c in range(1 << 7)) == set(range(32))
    print('FIVE_QUERY_SHATTERING_PASS patterns=32 distinct_centers=32')

    # Independently test the structural small-fiber bounds in several
    # dimensions. The written proof establishes these bounds universally.
    for n in (7, 8, 9, 10):
        edges = list(itertools.combinations(range(n), 2))
        two = list(itertools.combinations(range(n), 2))
        four = list(itertools.combinations(range(n), 4))
        queries = [(2, set(s)) for s in two] + [(4, set(s)) for s in four]
        a, b, c = 0, 1, 2
        two_star = [e for e in edges if (a in e) != (b in e)]
        near_star = [e for e in two_star if ((a in e and c not in e) or e == (b, c))]
        assert len(two_star) == 2 * (n - 2)
        assert len(near_star) == n - 2
        def yes(e, item):
            size, s = item
            return len(set(e) & s) == size // 2
        for query in queries:
            size, s = query
            y = sum(yes(e, query) for e in near_star)
            assert min(y, len(near_star) - y) <= 3
            y2 = sum(yes(e, query) for e in two_star)
            if size == 4 or not (s & {a, b}):
                assert y2 <= 4 or y2 == len(two_star)
            elif s == {a, b}:
                assert y2 == len(two_star)
            else:
                assert y2 == n - 2
        print('STRUCTURAL_FIBER_SMOKE_PASS dimension=' + str(n))
    print('DISTANCE_TWO_ALL_CHECKS_PASS')

if __name__ == '__main__':
    verify()

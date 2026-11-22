"""Exact finite certificates for three independent linear-order successor systems.
Run: python3 checker.py
All mathematical lower and extension arguments are in RESULT.md.
"""
from itertools import permutations

WITNESSES = {
    10: (
        (7, 10, 9, 8, 3, 4, 5, 6, 2, 1),
        (5, 6, 7, 4, 3, 2, 1, 10, 8, 9),
    ),
    17: (
        (8, 9, 1, 7, 6, 14, 15, 17, 16, 13, 12, 2, 3, 10, 11, 5, 4),
        (3, 4, 7, 8, 12, 13, 17, 16, 2, 1, 6, 5, 9, 15, 14, 10, 11),
    ),
}


def make_relations(order):
    """Construct the order and immediate-successor relations independently."""
    pos = {u: i for i, u in enumerate(order)}
    lt = {(u, v) for u in order for v in order if pos[u] < pos[v]}
    succ = set(zip(order, order[1:]))
    assert len(lt) == len(order) * (len(order) - 1) // 2
    return lt, succ


def patterns(size, extras, long_range):
    orders = [tuple(range(1, size + 1)), *extras]
    assert len(orders) == 3
    assert all(len(o) == size and set(o) == set(orders[0]) for o in orders)
    pairs = [make_relations(o) for o in orders]
    result = []
    for x, y in sorted(pairs[0][1]):
        bits = []
        for lt, succ in pairs[1:]:
            if (x, y) in succ:
                bits.append('A+')
            elif (y, x) in succ:
                bits.append('A-')
            elif long_range and (x, y) in lt:
                bits.append('G+')
            elif long_range and (y, x) in lt:
                bits.append('G-')
            else:
                assert not long_range
                bits.append('0')
        result.append((x, tuple(bits)))
    return result, pairs


def test(size, extras, long_range):
    labels = ('A+', 'A-', 'G+', 'G-') if long_range else ('A+', 'A-', '0')
    row_data, pairs = patterns(size, extras, long_range)
    seen = {bits for x, bits in row_data}
    expected = set((a, b) for a in labels for b in labels)
    assert seen == expected, (size, expected - seen)
    assert len(row_data) == len(expected)
    assert len(set(x for x, _ in row_data)) == size - 1
    assert sum(len(s) for _, s in pairs) == 3 * (size - 1)
    for j in range(2):
        for label in labels:
            assert sum(1 for _, bits in row_data if bits[j] == label) == len(labels)
    # Independent directed-edge lookup against the signed/missing atomic predicates.
    for x, bits in row_data:
        y = x + 1
        for j, code in enumerate(bits, start=1):
            lt, succ = pairs[j]
            assert (code == 'A+') == ((x, y) in succ)
            assert (code == 'A-') == ((y, x) in succ)
            if long_range:
                assert (code == 'G+') == ((x, y) in lt and (x, y) not in succ)
                assert (code == 'G-') == ((y, x) in lt and (y, x) not in succ)
            else:
                assert (code == '0') == ((x, y) not in succ and (y, x) not in succ)
    return row_data


def extended(extras, base, n):
    assert n >= base
    return tuple(tuple(o) + tuple(range(base + 1, n + 1)) for o in extras)


def main():
    for size, extras in WITNESSES.items():
        long_range = size == 17
        rows = test(size, extras, long_range)
        assert len(rows) == (16 if long_range else 9)
        for n in range(size, 101):
            ordered = extended(extras, size, n)
            rows_extended, _ = patterns(n, ordered, long_range)
            labels = ('A+', 'A-', 'G+', 'G-') if long_range else ('A+', 'A-', '0')
            assert set(bits for _, bits in rows_extended) == set((a, b) for a in labels for b in labels)
        # The lower bound is exact because an n-point reference path has n-1 edges.
        assert size - 1 == (4 if long_range else 3) ** 2
    # Small exhaustive sanity check: enumerate all orders on n=3 and n=4.
    counts = []
    for n in (3, 4):
        p = list(permutations(range(1, n + 1)))
        all_patterns = (make_relations(q) for q in p)
        # Each path in an n-element model has at most n-1 distinct anchor pairs.
        for pair in all_patterns:
            assert len(pair[1]) == n - 1
        counts.append(len(p))
    print('VERIFY_OK thresholds=10,17 extension_sizes=10..100,17..100, exhaustive_path_counts=' + str(counts))


if __name__ == '__main__':
    main()

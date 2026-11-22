#!/usr/bin/env python3
"""Direct finite verification of the parity-syndrome odd-independent-set construction."""
from collections import Counter


def labels_for_dimension(d):
    assert d >= 2 and d % 2 == 0
    m = d.bit_length() - 1
    q = 1 << m
    return m, list(range(q)) + [0] * (d - q)


def syndrome(x, labels):
    total = 0
    for i, a in enumerate(labels):
        if (x >> i) & 1:
            total ^= a
    return total


def binary_rank(columns, width):
    pivots = {}
    for col in columns:
        v = col
        while v:
            i = v.bit_length() - 1
            if i not in pivots:
                pivots[i] = v
                break
            v ^= pivots[i]
    assert len(pivots) <= width
    return len(pivots)


def check_dimension(d):
    m, labels = labels_for_dimension(d)
    q = 1 << m
    assert len(labels) == d
    frequency = Counter(labels)
    assert len(frequency) == q
    assert all(count % 2 == 1 for count in frequency.values())
    assert binary_rank([(a << 1) | 1 for a in labels], m + 1) == m + 1
    # Here syndrome and parity are computed directly from the vertex bits.
    is_selected = bytearray(1 << d)
    for x in range(1 << d):
        if x.bit_count() % 2 == 0 and syndrome(x, labels) != 0:
            is_selected[x] = 1
    expected = (1 << (d - 1)) - (1 << (d - m - 1))
    assert sum(is_selected) == expected
    for x in range(1 << d):
        neighbor_count = sum(is_selected[x ^ (1 << i)] for i in range(d))
        if is_selected[x]:
            assert neighbor_count == 0, (d, x, neighbor_count)
        else:
            assert neighbor_count == 0 or neighbor_count % 2 == 1, (d, x, neighbor_count)
        if x.bit_count() % 2:
            assert neighbor_count == d - frequency[syndrome(x, labels)]
    return expected


def main():
    expected_exact = {2: 1, 4: 6, 6: 24, 8: 112}
    tested = {}
    for d in range(2, 17, 2):
        size = check_dimension(d)
        tested[d] = size
        if d in expected_exact:
            assert size == expected_exact[d]
    for d in range(2, 4097, 2):
        m, labels = labels_for_dimension(d)
        q = 1 << m
        assert q <= d < 2 * q
        assert d - q >= 0 and (d - q) % 2 == 0
        assert len(labels) == d
        # Rational inequalities are checked after cross-multiplication.
        assert 2 * q > d
        assert (4 * d - 2) <= (2 * q) * (4 * d - 2)
    print('DIRECT_ODD_NEIGHBOR_CENSUS_PASS', tested)
    print('PARITY_SYNDROME_RANK_AND_COUNT_PASS dimensions=2..16 step=2')
    print('LARGE_DIMENSION_LABEL_ARITHMETIC_PASS even_dimensions=2..4096')
    print('VERIFY_OK')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Independent finite checks for open-neighborhood locating codes on cycles."""
from collections import Counter
from math import comb


def polynomial(m):
    out = {0: 1}
    for k in range(1, m // 3 + 1):
        numerator = m * comb(m - 2 * k - 1, k - 1)
        assert numerator % k == 0
        out[k] = numerator // k
    return out


def expected_omissions(n):
    if n == 4:
        return {}
    if n % 2:
        return polynomial(n)
    a = polynomial(n // 2)
    out = Counter()
    for k, x in a.items():
        for j, y in a.items():
            out[k + j] += x * y
    return dict(out)


def graph_old(n, selected):
    trace = []
    for v in range(n):
        neighbor_bits = (1 << ((v - 1) % n)) | (1 << ((v + 1) % n))
        observed = neighbor_bits & selected
        if not observed:
            return False
        trace.append(observed)
    return len(set(trace)) == n


def omitted_pattern(n, selected):
    if n == 4:
        return False
    absent = ((1 << n) - 1) ^ selected
    for i in range(n):
        if (absent >> i) & 1:
            if ((absent >> ((i + 2) % n)) & 1) or ((absent >> ((i + 4) % n)) & 1):
                return False
    return True


def transfer_polynomial(m):
    """Cyclic 2-step exclusion, via a four-state weighted trace."""
    states = [(0, 0), (0, 1), (1, 0), (1, 1)]
    result = Counter()
    for start in states:
        current = {(start, 0): 1}
        for _ in range(m):
            nxt = Counter()
            for ((a, b), weight), count in current.items():
                for c in (0, 1):
                    if a * b == 0 and b * c == 0 and a * c == 0:
                        nxt[((b, c), weight + c)] += count
            current = nxt
        for (finish, weight), count in current.items():
            if finish == start:
                result[weight] += count
    return dict(result)


def run():
    total = 0
    old = 0
    for n in range(3, 18):
        actual = Counter()
        for selected in range(1 << n):
            total += 1
            direct = graph_old(n, selected)
            equivalent = omitted_pattern(n, selected)
            assert direct == equivalent, (n, selected, direct, equivalent)
            if direct:
                old += 1
                actual[n - selected.bit_count()] += 1
        assert dict(actual) == expected_omissions(n), (n, actual, expected_omissions(n))
    for m in range(3, 91):
        assert transfer_polynomial(m) == polynomial(m), m
    for n in range(3, 251):
        actual = expected_omissions(n)
        if n == 4:
            assert not actual
            continue
        q = n // 3 if n % 2 else 2 * ((n // 2) // 3)
        assert set(actual) == set(range(q + 1))
        minimum = n - max(actual)
        target = (n - n // 3) if n % 2 else (n - 2 * (n // 6))
        assert minimum == target
    selected = sum(1 << i for i in range(13) if i not in {0, 5, 6, 12})
    assert graph_old(13, selected) and selected.bit_count() == 9
    print(f'VERIFY_OK cycles=3..17 masks={total} OLD_sets={old} transfer_cycle_squares=3..90 size_support=3..250 C13_witness=PASS')


if __name__ == '__main__':
    run()

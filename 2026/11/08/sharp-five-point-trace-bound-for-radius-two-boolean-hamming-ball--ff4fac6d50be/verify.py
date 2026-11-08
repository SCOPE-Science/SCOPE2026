#!/usr/bin/env python3
"""Finite exhaustive certificate for radius-two Boolean Hamming-ball traces.

Every five distinct points contained in a radius-two ball translate to five
rows of weight at most two. The nonzero coordinate columns are nonempty masks
on five rows, each with multiplicity at most two. This enumerates ALL such
column multisets without geometric or probabilistic sampling.
"""
from itertools import combinations
from math import comb


def trace_masks_for_rows(rows, n, radius=2):
    seen = 0
    for center in range(1 << n):
        trace = sum(1 << i for i, x in enumerate(rows)
                    if (center ^ x).bit_count() <= radius)
        seen |= 1 << trace
    return seen


def finite_template_certificate():
    degree = [0] * 5
    columns = []
    total = 0
    distinct = 0
    maximum = 0
    sharp_columns = None
    full = 0
    histogram = {}

    def inspect():
        nonlocal total, distinct, maximum, sharp_columns, full
        total += 1
        u = len(columns)
        rows = [sum(1 << j for j, column in enumerate(columns)
                    if (column >> i) & 1) for i in range(5)]
        if len(set(rows)) != 5:
            return
        distinct += 1
        # Four formally available all-zero columns saturate every possible
        # nonempty trace; centers of weight >4 always have empty trace.
        # Only active coordinate masks with weight <=4 are necessary.
        seen = 0
        for active_center in range(1 << u):
            weight = active_center.bit_count()
            if weight > 4:
                continue
            for spare_weight in range(5 - weight):
                trace = 0
                for i, row in enumerate(rows):
                    if (active_center ^ row).bit_count() + spare_weight <= 2:
                        trace |= 1 << i
                seen |= 1 << trace
        ntraces = seen.bit_count()
        histogram[ntraces] = histogram.get(ntraces, 0) + 1
        if ntraces > maximum:
            maximum = ntraces
            sharp_columns = tuple(columns)
        full += ntraces == 32

    def enumerate_columns(mask=1):
        if mask == 32:
            inspect()
            return
        enumerate_columns(mask + 1)  # zero copies
        for copies in (1, 2):
            for i in range(5):
                if (mask >> i) & 1:
                    degree[i] += 1
            feasible = max(degree) <= 2
            # For two copies, first copy increment above; second below.
            if copies == 2:
                for i in range(5):
                    if (mask >> i) & 1:
                        degree[i] += 1
                feasible = max(degree) <= 2
            if feasible:
                columns.extend([mask] * copies)
                enumerate_columns(mask + 1)
                del columns[-copies:]
            for i in range(5):
                if (mask >> i) & 1:
                    degree[i] -= copies
            # Restore input degree before next branch.
    enumerate_columns()
    assert (total, distinct, full, maximum) == (14778, 7260, 0, 27), (total, distinct, full, maximum)
    print('TEMPLATE_CERTIFICATE_PASS', total, distinct, full, maximum)
    print('TRACE_HISTOGRAM', sorted(histogram.items()))
    return sharp_columns


def basic_dimensions():
    # Independent direct trace table, not the symbolic column machinery.
    expected = {1: 0, 2: 0, 3: 1, 4: 3, 5: 4, 6: 4}
    for d, goal in expected.items():
        n = 1 << d
        ranges = [sum(1 << x for x in range(n)
                      if (x ^ c).bit_count() <= 2) for c in range(n)]
        possible = [False] * (goal + 2)
        # Translate any full-witness center to zero: for k>=1 it suffices
        # to enumerate supports inside B_2(0), since other full centers
        # are translates of this one. The empty support is always shattered.
        local = [x for x in range(n) if x.bit_count() <= 2]
        for k in range(1, goal + 2):
            if k > len(local):
                continue
            for S in combinations(local, k):
                traces = {sum(1 << i for i, x in enumerate(S)
                              if (ranges[c] >> x) & 1) for c in range(n)}
                if len(traces) == 1 << k:
                    possible[k] = True
                    if k == goal + 1:
                        raise AssertionError(('unexpected shattering', d, S))
                    # For smaller k only one witness is required.
                    break
        actual = max([0] + [k for k in range(1, len(possible)) if possible[k]])
        assert actual == goal, (d, actual, goal)
        print('DIRECT_DIMENSION_PASS', d, actual)


def sharp_five_trace_example():
    # Every point has Hamming weight one or two and lies in B_2(0).
    S = [16, 3, 5, 6, 24]  # Five points in Q_6.
    mask = trace_masks_for_rows(S, 6)
    assert mask.bit_count() == 27
    missing = [t for t in range(32) if not ((mask >> t) & 1)]
    assert missing == [15, 19, 21, 25, 30], missing
    print('SHARP_27_TRACE_WITNESS_PASS', S, missing)


def four_shattered_example():
    S = [1, 2, 4, 8]  # Four coordinate unit vectors in Q_5.
    assert trace_masks_for_rows(S, 5).bit_count() == 16
    print('FOUR_SHATTERED_WITNESS_PASS', S)


if __name__ == '__main__':
    finite_template_certificate()
    basic_dimensions()
    sharp_five_trace_example()
    four_shattered_example()
    print('ALL_RADIUS_TWO_CUBE_CERTIFICATES_PASS')

#!/usr/bin/env python3
"""Direct labelled-state verification of sequential binary parity on triangular books."""
from collections import Counter
from itertools import permutations
from math import factorial


def expected(k, t):
    if k % 2:
        return {1: 1 << k, 2: 1 << k, 4: 1 << (k + 1)}
    return {1: 1 << k, (2 if t % 2 else 3): 3 << k}


def cyclic_between(order):
    a = order.index(0)
    b = order.index(1)
    return (b - a - 1) % len(order)


def sweep(x, order, neighbor_masks):
    for vertex in order:
        if (x & neighbor_masks[vertex]).bit_count() % 2:
            x ^= 1 << vertex
    return x


def check_graph(k):
    n = k + 2
    mask_leaves = ((1 << k) - 1) << 2
    neighbor_masks = [mask_leaves | 2, mask_leaves | 1] + [3] * k
    phase_schedules = Counter()
    state_order_pairs = 0
    for order in permutations(range(n)):
        t = cyclic_between(order)
        phase_schedules[t % 2] += 1
        pred = expected(k, t)
        counts = Counter()
        for x in range(1 << n):
            y = x
            for p in range(1, 5):
                y = sweep(y, order, neighbor_masks)
                if y == x:
                    counts[p] += 1
                    break
            else:
                raise AssertionError(('nonperiodic', k, order, x))
        if dict(counts) != pred:
            raise AssertionError(('census', k, order, dict(counts), pred))
        state_order_pairs += 1 << n
    perms = factorial(n)
    assert sum(phase_schedules.values()) == perms
    if k % 2 == 0:
        unit = perms // (k + 1)
        assert phase_schedules[0] == (k // 2 + 1) * unit
        assert phase_schedules[1] == (k // 2) * unit
    else:
        assert phase_schedules[0] == phase_schedules[1] == perms // 2
    return state_order_pairs, dict(phase_schedules)


def main():
    total_pairs = 0
    total_orders = 0
    for k in range(1, 6):
        pairs, splits = check_graph(k)
        total_pairs += pairs
        total_orders += factorial(k + 2)
        print(f'k={k}: schedules={factorial(k+2)}, state-schedule pairs={pairs}, between-parity={splits} PASS')
    print(f'TOTAL: schedules={total_orders}, state-schedule pairs={total_pairs}; all exact periods and schedule frequencies PASS')


if __name__ == '__main__':
    main()

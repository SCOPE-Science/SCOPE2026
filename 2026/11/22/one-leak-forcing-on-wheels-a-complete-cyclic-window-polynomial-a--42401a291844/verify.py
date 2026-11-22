#!/usr/bin/env python3
"""Independent finite checks for one-leak zero forcing in wheel graphs.

The main theorem has a symbolic proof; these checks are finite regression tests.
Run with Python 3, no external dependencies.
"""
from collections import Counter, defaultdict
from math import comb


def adjacency(n):
    ans = []
    for i in range(n):
        ans.append((1 << ((i - 1) % n)) | (1 << ((i + 1) % n)) | (1 << n))
    ans.append((1 << n) - 1)
    return ans


def propagates(n, initial, leak):
    adj = adjacency(n)
    full = (1 << (n + 1)) - 1
    blue = initial
    while blue != full:
        new = 0
        for vertex in range(n + 1):
            if vertex == leak or not (blue >> vertex & 1):
                continue
            unseen = adj[vertex] & (full ^ blue)
            if unseen and not (unseen & (unseen - 1)):
                new |= unseen
        if not new:
            return False
        blue |= new
    return True


def robust_direct(n, mask):
    return all(propagates(n, mask, leak) for leak in range(n + 1))


def triple_count(n, rim):
    return sum(all((rim >> ((i + j) % n)) & 1 for j in (-1, 0, 1))
               for i in range(n))


def classified(n, mask):
    rim = mask & ((1 << n) - 1)
    if mask >> n & 1:
        return any((rim >> i & 1) and (rim >> ((i + 1) % n) & 1)
                   for i in range(n))
    return triple_count(n, rim) >= 2


def cyclic_transfer_bad(n):
    # Four states are the last two rim bits (a,b). Transitions (a,b)->(b,c).
    # The count of 111 occurrences is truncated at 2, which is enough for
    # the coefficients of u^0 and u^1.
    out = Counter()
    for start in range(4):
        dp = {(start, 0, 0): 1}
        for _ in range(n):
            new = defaultdict(int)
            for (state, selected, triples), ways in dp.items():
                for c in (0, 1):
                    nxt = ((state & 1) << 1) | c
                    r = min(2, triples + (state == 3 and c == 1))
                    new[(nxt, selected + c, r)] += ways
            dp = new
        for (state, selected, triples), ways in dp.items():
            if state == start and triples <= 1:
                out[selected] += ways
    return out


def cyclic_independent(n):
    # Counting by independent subset (separate from the forcing simulation).
    out = Counter()
    for rim in range(1 << n):
        if not any((rim >> i & 1) and (rim >> ((i + 1) % n) & 1)
                   for i in range(n)):
            out[rim.bit_count()] += 1
    return out


def predicted_polynomial(n):
    bad = cyclic_transfer_bad(n)
    independent = cyclic_independent(n)
    out = Counter()
    for k in range(n + 1):
        out[k] += comb(n, k) - bad[k]  # hub unselected
        out[k + 1] += comb(n, k) - independent[k]  # hub selected
    return +out


def predicted_minimal(n):
    out = Counter({3: n})
    out[4] = (1 if n == 4 else n)
    if n >= 8:
        out[6] = n * (n - 7) // 2
    return out


def main():
    for n in range(4, 12):
        robust = set()
        poly = Counter()
        for mask in range(1 << (n + 1)):
            calc = robust_direct(n, mask)
            criterion = classified(n, mask)
            assert calc == criterion, ('classification', n, mask, calc, criterion)
            if calc:
                robust.add(mask)
                poly[mask.bit_count()] += 1
        assert poly == predicted_polynomial(n), ('polynomial', n)
        minimal = Counter()
        for mask in robust:
            if all((mask ^ (1 << i)) not in robust
                   for i in range(n + 1) if mask >> i & 1):
                minimal[mask.bit_count()] += 1
        assert minimal == predicted_minimal(n), ('minimal', n, minimal)
        print(f'W_{n}: brute forcing / transfer / minimal OK; '
              f'robust={len(robust)} minimal={sum(minimal.values())}')
    for n in range(12, 17):
        counts = Counter()
        for mask in range(1 << (n + 1)):
            if classified(n, mask):
                counts[mask.bit_count()] += 1
        assert counts == predicted_polynomial(n), ('extended transfer', n)
    print('TRANSFER_EXTENDED_OK')
    print('WHEEL_ONE_LEAK_VERIFY_OK')


if __name__ == '__main__':
    main()

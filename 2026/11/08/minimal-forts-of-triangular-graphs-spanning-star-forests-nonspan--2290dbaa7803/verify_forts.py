#!/usr/bin/env python3
"""Independent finite checks of a minimal-fort classification for triangular graphs.

Uses direct line-graph neighborhoods to find forts, a full-subset dynamic
program for inclusion-minimality, and a separate rooted-component recurrence
for the claimed counting formula. No external packages are required.
"""
from collections import Counter
from math import comb, factorial


def predicted(n):
    # Minimal edge covers: spanning star forests via the distinguished vertex.
    vals = [Counter() for _ in range(n + 1)]
    vals[0][0] = 1
    for s in range(1, n + 1):
        for k in range(2, s + 1):
            mult = 1 if k == 2 else k
            for q, count in vals[s - k].items():
                vals[s][q + k - 1] += comb(s - 1, k - 1) * mult * count
    p = vals[n].copy()
    # Nonspanning cycles, with undirected cyclic order up to reversal.
    for k in range(3, n):
        p[k] += comb(n, k) * factorial(k - 1) // 2
    return p


def structural(n, selected_edges):
    ds = [0] * n
    adj = [set() for _ in range(n)]
    for u, v in selected_edges:
        ds[u] += 1
        ds[v] += 1
        adj[u].add(v)
        adj[v].add(u)
    # Nonspanning single simple cycle.
    support = [u for u in range(n) if ds[u]]
    if len(support) < n and len(support) >= 3 and all(ds[u] == 2 for u in support):
        reached = {support[0]}
        stack = [support[0]]
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v not in reached:
                    reached.add(v)
                    stack.append(v)
        if len(reached) == len(support):
            return True
    # Spanning star forest (including isolated edges), tested by components.
    if len(support) != n:
        return False
    seen = set()
    for start in range(n):
        if start in seen:
            continue
        stack = [start]
        component = set([start])
        seen.add(start)
        while stack:
            u = stack.pop()
            for v in adj[u]:
                if v not in seen:
                    seen.add(v)
                    component.add(v)
                    stack.append(v)
        if len(component) < 2:
            return False
        if sum(ds[u] >= 2 for u in component) > 1:
            return False
    return True


def exhaustive(n):
    edges = [(u, v) for u in range(n) for v in range(u+1, n)]
    e = len(edges)
    neighbor_masks = []
    for i, (u, v) in enumerate(edges):
        neighbor_masks.append(sum(1 << j for j, (a, b) in enumerate(edges)
                                  if i != j and (u == a or u == b or v == a or v == b)))
    all_masks = (1 << e) - 1
    has_fort_subset = bytearray(1 << e)
    observed = Counter()
    forts = 0
    checked = 0
    for mask in range(1, 1 << e):
        checked += 1
        # This checks every proper subset, not merely single-edge deletions.
        proper_fort = False
        b = mask
        while b:
            bit = b & -b
            if has_fort_subset[mask ^ bit]:
                proper_fort = True
                break
            b ^= bit
        # Direct graph test: each unselected triangular-graph vertex
        # has either 0 or at least 2 selected neighbors.
        is_fort = True
        b = all_masks ^ mask
        while b:
            bit = b & -b
            i = bit.bit_length() - 1
            if (neighbor_masks[i] & mask).bit_count() == 1:
                is_fort = False
                break
            b ^= bit
        if is_fort:
            forts += 1
        has_fort_subset[mask] = 1 if is_fort or proper_fort else 0
        if is_fort and not proper_fort:
            observed[mask.bit_count()] += 1
            selected = [edges[i] for i in range(e) if mask & (1 << i)]
            if not structural(n, selected):
                raise AssertionError(('unexpected minimal fort', n, selected))
    expect = predicted(n)
    if observed != expect:
        raise AssertionError(('coefficient discrepancy', n, dict(observed), dict(expect)))
    print(f'n={n} vertices={e} checked_nonempty={checked} forts={forts} minimal={sum(observed.values())} coefficients={dict(sorted(observed.items()))}', flush=True)
    return checked, forts, sum(observed.values())


def main():
    total_subsets = total_forts = total_min = 0
    for n in range(3, 8):
        a, b, c = exhaustive(n)
        total_subsets += a
        total_forts += b
        total_min += c
    print(f'VERIFY_OK n=3..7 nonempty_subsets={total_subsets} forts={total_forts} minimal_forts={total_min} all_subsets_and_coefficients=PASS', flush=True)


if __name__ == '__main__':
    main()

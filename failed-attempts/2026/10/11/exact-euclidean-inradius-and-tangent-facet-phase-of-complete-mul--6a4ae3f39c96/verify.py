#!/usr/bin/env python3
from fractions import Fraction
from itertools import product


def partitions(n, lo=1):
    if n == 0:
        yield ()
        return
    for a in range(lo, n + 1):
        for tail in partitions(n - a, a):
            yield (a,) + tail


def graph_data(parts):
    part_of = []
    for j, a in enumerate(parts):
        part_of.extend([j] * a)
    n = len(part_of)
    edges = [(u, v) for u in range(n) for v in range(u + 1, n)
             if part_of[u] != part_of[v]]
    return edges


def connected_tight(n, tight):
    adj = [[] for _ in range(n)]
    for u, v in tight:
        adj[u].append(v)
        adj[v].append(u)
    seen = {0}
    stack = [0]
    while stack:
        u = stack.pop()
        for v in adj[u]:
            if v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == n


def projected_norm_sq(f):
    n = len(f)
    s = sum(f)
    return Fraction(n * sum(x * x for x in f) - s * s, n)


def predicted(parts):
    n = sum(parts)
    central = Fraction((n * n) // 4, n)
    local = Fraction(0, 1)
    for a in parts:
        if a >= 2:
            local = max(local, Fraction(a * n - (a & 1), n))
    return max(central, local)


def brute_max(parts):
    n = sum(parts)
    edges = graph_data(parts)
    best = Fraction(-1, 1)
    count = 0
    # With f(0)=0, the edge Lipschitz condition and graph diameter at most 2
    # force every facet labeling into [-2,2].
    for tail in product(range(-2, 3), repeat=n - 1):
        f = (0,) + tail
        if any(abs(f[u] - f[v]) > 1 for u, v in edges):
            continue
        tight = [(u, v) for u, v in edges if abs(f[u] - f[v]) == 1]
        if not connected_tight(n, tight):
            continue
        count += 1
        best = max(best, projected_norm_sq(f))
    return best, count


def main():
    tested = 0
    facet_labelings = 0
    for n in range(3, 9):
        for parts in partitions(n):
            if len(parts) < 3:
                continue
            observed, count = brute_max(parts)
            expected = predicted(parts)
            if observed != expected:
                raise SystemExit(f"FAIL parts={parts} observed={observed} expected={expected}")
            tested += 1
            facet_labelings += count
    print(f"VERIFY_OK complete-multipartite symmetric-edge inradius partitions={tested} facet_labelings={facet_labelings} n=3..8")


if __name__ == '__main__':
    main()

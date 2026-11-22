"""Independent finite checks of connected zero forcing on one-leaf unicyclic graphs.

Usage: python VERIFY.py
Requires only Python 3.9+ standard library. The general theorem is proved in RESULT.md;
these finite tests are independent corroboration, not a proof for all sizes.
"""
from collections import Counter


def graph(c, t):
    """Cycle on 0,...,c-1 plus tail c,...,c+t-1 attached to vertex 0."""
    n = c + t
    nbr = [set() for _ in range(n)]
    edges = [(i, (i + 1) % c) for i in range(c)]
    edges.extend([(0, c)] + [(c + i, c + i + 1) for i in range(t - 1)])
    for u, v in edges:
        nbr[u].add(v)
        nbr[v].add(u)
    return nbr


def connected(nbr, mask):
    n = len(nbr)
    if mask == 0:
        return False
    root = next(i for i in range(n) if (mask >> i) & 1)
    seen = {root}
    stack = [root]
    while stack:
        for v in nbr[stack.pop()]:
            if ((mask >> v) & 1) and v not in seen:
                seen.add(v)
                stack.append(v)
    return len(seen) == mask.bit_count()


def forces(nbr, mask):
    n = len(nbr)
    full = (1 << n) - 1
    while mask != full:
        progress = False
        for u in range(n):
            if not ((mask >> u) & 1):
                continue
            white = [v for v in nbr[u] if not ((mask >> v) & 1)]
            if len(white) == 1:
                mask |= 1 << white[0]
                progress = True
                break
        if not progress:
            return False
    return True


def direct_distribution(c, t):
    nbr = graph(c, t)
    counts = Counter()
    checked = 0
    for mask in range(1 << (c + t)):
        checked += 1
        if connected(nbr, mask) and forces(nbr, mask):
            counts[mask.bit_count()] += 1
    return counts, checked


def proposed_distribution(c, t):
    counts = Counter()
    for q in range(2, c):
        counts[q] += c - q
        for j in range(t + 1):
            counts[q + j] += q
    for j in range(t + 1):
        counts[c + j] += 1
    return counts


def unimodal(values):
    decreasing = False
    for left, right in zip(values, values[1:]):
        if right < left:
            decreasing = True
        elif right > left and decreasing:
            return False
    return True


def logconcave(values):
    return all(values[k] ** 2 >= values[k - 1] * values[k + 1]
               for k in range(1, len(values) - 1))


def main():
    instances = subsets = 0
    for c in range(3, 10):
        for t in range(1, 6):
            if c + t > 13:
                continue
            observed, checked = direct_distribution(c, t)
            expected = proposed_distribution(c, t)
            assert observed == expected, (c, t, observed, expected)
            instances += 1
            subsets += checked
    print("DIRECT_ALL_SUBSETS_OK", "instances", instances, "subsets", subsets)

    shapes = 0
    for c in range(3, 51):
        for t in range(1, 36):
            poly = proposed_distribution(c, t)
            values = [poly[k] for k in range(2, c + t + 1)]
            assert poly[2] == c
            assert poly[c + t] == 1
            assert sum(values) == (c - 1) * (c - 2) // 2 + (t + 1) * c * (c - 1) // 2
            assert unimodal(values)
            assert logconcave(values) == (c <= 4 or t == 1), (c, t, values)
            shapes += 1
    print("COEFFICIENT_AND_SHAPE_FORMULAS_OK", "cases", shapes)
    print("VERIFY_OK")


if __name__ == "__main__":
    main()

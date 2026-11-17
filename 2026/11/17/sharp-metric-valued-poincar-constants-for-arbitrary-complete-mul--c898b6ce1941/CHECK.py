"""Exact finite checks for the multipartite metric Poincare theorem.

This script is supplementary evidence; the proof for arbitrary sizes and targets
is analytical. Requires only Python's standard library.
"""
from fractions import Fraction
from itertools import combinations, product
from random import Random


def edge_count(parts):
    return sum(a * b for a, b in combinations(parts, 2))


def formula(parts):
    parts = tuple(sorted(parts, reverse=True))
    n = sum(parts)
    e = edge_count(parts)
    m = n * (n - 1) // 2
    scores = []
    for r in range(1, len(parts) + 1):
        a = sum(v * (v - 1) for v in parts[:r])
        b = e - edge_count(parts[r:])
        scores.append(Fraction(a, b))
    return Fraction(e, m) * (1 + max(scores)), scores


def brute_subset(parts):
    k = len(parts)
    e = edge_count(parts)
    best = Fraction(0)
    for bits in product((0, 1), repeat=k):
        if not any(bits):
            continue
        s = [j for j in range(k) if bits[j]]
        c = [parts[j] for j in range(k) if not bits[j]]
        a = sum(parts[j] * (parts[j] - 1) for j in s)
        b = e - edge_count(c)
        best = max(best, Fraction(a, b))
    return best


def all_pairs_metric(parts, f):
    membership = [i for i, n in enumerate(parts) for _ in range(n)]
    pairs = list(combinations(range(len(membership)), 2))
    E = sum(f(u, v, membership) for u, v in pairs
            if membership[u] != membership[v])
    P = sum(f(u, v, membership) for u, v in pairs)
    return P, E


def extremal(parts, selected):
    selected = set(selected)
    def d(u, v, group):
        if u == v:
            return 0
        i, j = group[u], group[v]
        if i not in selected and j not in selected:
            return 0
        if i == j and i in selected:
            return 2
        return 1
    return d


def run():
    rng = Random(46201)
    count = 0
    for k in range(2, 6):
        for parts in product(range(1, 5), repeat=k):
            parts = tuple(sorted(parts, reverse=True))
            gamma, scores = formula(parts)
            assert gamma == Fraction(edge_count(parts), sum(parts) * (sum(parts)-1)//2) * (1 + brute_subset(parts))
            for r in range(1, k + 1):
                if r == k - 1 and k > 2:
                    continue
                d = extremal(parts, range(r))
                P, E = all_pairs_metric(parts, d)
                if E:
                    assert Fraction(P, E) == 1 + scores[r-1]
                count += 1
            count += 1
    for k in range(2, 8):
        for _ in range(125):
            parts = tuple(rng.randint(1, 6) for _ in range(k))
            coordinates = [[rng.randint(-10, 10) for j in range(5)] for i in range(sum(parts))]
            def d(u, v, group):
                return sum(abs(a-b) for a, b in zip(coordinates[u], coordinates[v]))
            P, E = all_pairs_metric(parts, d)
            if E:
                target, _ = formula(parts)
                # gamma = (mean over vertex pairs)/(mean over edges).
                n = sum(parts)
                ratio = Fraction(P * edge_count(parts), E * (n*(n-1)//2))
                assert ratio <= target
            count += 1
    # Two intermediate phases, neither graph metric nor one-part collapse.
    for parts, r, expected in [((4,3,1,1), 2, Fraction(33,26)),
                                ((4,3,2,1,1),3,Fraction(144,121))]:
        gamma, scores = formula(parts)
        assert gamma == expected
        assert scores[r-1] > max(s for j,s in enumerate(scores) if j not in (r-1, len(parts)-2))
        count += 1
    print('PASS:', count, 'exact subset, witness, and sampled-metric assertions')


if __name__ == '__main__':
    run()

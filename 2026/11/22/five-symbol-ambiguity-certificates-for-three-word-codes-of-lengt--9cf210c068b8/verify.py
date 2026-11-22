"""Exact symbolic equality-pattern certificate for three codeword lengths 2,2,3.

No third-party modules, data files, or external services are required.
Run: python verify.py
"""
from itertools import combinations, product
from collections import Counter


def canonical_partitions(n):
    # Restricted growth strings give each set partition of n positions exactly once.
    def extend(p, top):
        if len(p) == n:
            yield tuple(p)
            return
        for v in range(top + 2):
            yield from extend(p + [v], max(top, v))
    yield from extend([0], 0)


def strip_prefix(u, v):
    """The residual after removing u from the start of v, or None."""
    return v[len(u):] if v[:len(u)] == u else None


def non_ud_sardinas_patterson(words):
    """Classical finite residual-reachability decision procedure."""
    initial = set()
    for u in words:
        for v in words:
            if u != v:
                tail = strip_prefix(u, v)
                if tail is not None:
                    initial.add(tail)
    pending = list(initial)
    seen = set(initial)
    while pending:
        s = pending.pop()
        if not s or s in words:
            return True
        for w in words:
            for x, y in ((s, w), (w, s)):
                t = strip_prefix(x, y)
                if t is not None and t not in seen:
                    seen.add(t)
                    pending.append(t)
    return False


def predicted_exception(x, y, z):
    a, b, c = z
    short = {x, y}
    return ((a == b == c and (a, a) in short)
            or (a == c and a != b and short == {(a, b), (b, a)}))


def short_witness(x, y, z):
    if z[0] == z[1] == z[2]:
        t = (z[0], z[0]); return (z + t, t + z)
    a, b, _ = z
    return (z + (b, a), (a, b) + z)


def check_symbolic():
    all_patterns = 0
    eligible = 0
    failures = Counter()
    positive = Counter()
    for p in canonical_partitions(7):
        all_patterns += 1
        x, y, z = p[:2], p[2:4], p[4:7]
        if x == y:
            continue
        eligible += 1
        actual = non_ud_sardinas_patterson((x, y, z))
        predicted = predicted_exception(x, y, z)
        assert actual == predicted, (p, actual, predicted)
        if actual:
            positive[max(p) + 1] += 1
            left, right = short_witness(x, y, z)
            assert left == right
            assert (z, (z[1], z[0])) != ((z[0], z[1]), z)
        else:
            failures[max(p) + 1] += 1
    assert all_patterns == 877
    assert eligible == 825
    assert positive == {2: 8, 3: 2}
    assert sum(failures.values()) == 815
    return all_patterns, eligible, positive


def check_literal_alphabets():
    counts = []
    for q in (2, 3, 4, 5):
        alph = tuple(range(q))
        short = list(product(alph, repeat=2))
        triple = list(product(alph, repeat=3))
        found = 0
        for x, y in combinations(short, 2):
            for z in triple:
                if non_ud_sardinas_patterson((x, y, z)):
                    assert predicted_exception(x, y, z)
                    found += 1
        assert found == q * (q - 1) * (q + 2), (q, found)
        counts.append((q, found))
    return counts


if __name__ == '__main__':
    p, eligible, pos = check_symbolic()
    counts = check_literal_alphabets()
    print('VERIFY_OK partition_patterns={} eligible={} nonUD={} k2={} k3={} literal={}'.format(
        p, eligible, sum(pos.values()), pos[2], pos[3], counts))

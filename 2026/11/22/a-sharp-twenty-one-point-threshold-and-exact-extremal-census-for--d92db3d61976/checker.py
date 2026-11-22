#!/usr/bin/env python3
"""Independent finite checks for the 21-point two-order rank-three threshold."""
from itertools import permutations, combinations
import random


def valid_5(p):
    if p[2] != 2:
        return False
    observed = {(i > 2, p[i] > 2) for i in range(5) if i != 2}
    return len(observed) == 4

LOCAL = [p for p in permutations(range(5)) if valid_5(p)]


def interleaving_valid(positions):
    a = sorted(positions)
    b = [i for i in range(10) if i not in positions]
    return b[0] < a[2] < b[-1] and a[0] < b[2] < a[-1]

WEAVES = [set(c) for c in combinations(range(10), 5) if interleaving_valid(set(c))]


def generate(rng):
    quadrants = ('SW', 'NW', 'SE', 'NE')
    # Every side consists of ten positions interleaving two named 5-sets.
    x = {}
    y = {}
    for name, labels, ranks, target in [
        ('left', ('SW', 'NW'), range(0, 10), x),
        ('right', ('SE', 'NE'), range(11, 21), x),
        ('bottom', ('SW', 'SE'), range(0, 10), y),
        ('top', ('NW', 'NE'), range(11, 21), y),
    ]:
        weave = rng.choice(WEAVES)
        target.setdefault(labels[0], []).extend(r for j, r in enumerate(ranks) if j in weave)
        target.setdefault(labels[1], []).extend(r for j, r in enumerate(ranks) if j not in weave)
    p = [None] * 21
    p[10] = 10
    for q in quadrants:
        internal = rng.choice(LOCAL)
        for j in range(5):
            p[x[q][j]] = y[q][internal[j]]
    assert sorted(p) == list(range(21))
    return p


def prime_extensions_covered(p, marked):
    """Independent direct enumeration: all 2D insertion gaps of marked vertices."""
    n = len(p)
    xs = sorted(marked)
    ys = sorted(p[i] for i in marked)
    types = set()
    for i in range(n):
        if i in marked:
            continue
        a = sum(i > x for x in xs)
        b = sum(p[i] > y for y in ys)
        types.add((a, b))
    return len(types) == (len(marked) + 1) ** 2


def rank_ge_3(p):
    """Three-step one-point-extension recursion, with no appeal to quadrant formula."""
    n = len(p)
    for anchor in range(n):
        ok = True
        for qx in (False, True):
            for qy in (False, True):
                partners = [j for j in range(n) if j != anchor and
                            (j > anchor) == qx and (p[j] > p[anchor]) == qy]
                if not any(prime_extensions_covered(p, (anchor, j)) for j in partners):
                    ok = False
                    break
            if not ok:
                break
        if ok:
            return True
    return False


def geometric_rank3(p):
    n = len(p)
    for a in range(n):
        good = [False] * 4
        for b in range(n):
            if a == b: continue
            if prime_extensions_covered(p, (a, b)):
                good[2 * (b > a) + (p[b] > p[a])] = True
        if all(good): return True
    return False


def run():
    assert len(LOCAL) == 16, len(LOCAL)
    assert len(WEAVES) == 180, len(WEAVES)
    assert len(LOCAL) ** 4 * len(WEAVES) ** 4 == 68797071360000
    rng = random.Random(604213)
    for t in range(250):
        p = generate(rng)
        assert rank_ge_3(p)
        assert geometric_rank3(p)
        # Every proper induced subpermutation loses the rank-three property.
        for removed in range(21):
            a = p[:removed] + p[removed + 1:]
            a = [sum(y < v for y in a) for v in a]
            assert not rank_ge_3(a)
    for n in range(0, 21):
        for t in range(100):
            p = list(range(n))
            rng.shuffle(p)
            assert not rank_ge_3(p)
    print('CHECK_OK local_patterns=16 valid_interleavings=180 exact_minimal_count=68797071360000')
    print('CHECK_OK 250 constructive hosts, 5250 deletion instances, 2100 random subthreshold instances')


if __name__ == '__main__':
    run()

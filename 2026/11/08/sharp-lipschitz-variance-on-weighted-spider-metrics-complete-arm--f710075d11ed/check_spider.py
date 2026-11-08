"""Exact rational-arithmetic tests for variance extrema of weighted path-arm metrics.

Run: python3 check_spider.py
All arithmetic in the enumeration is integer; dividing by total_mass**2 gives variance.
"""
from itertools import product
from random import Random


def raw_spread(arms, weights, signs):
    """Return W*sum(w f^2) - (sum w f)^2; center is at zero."""
    idx = 0
    values = [0]
    for arm in arms:
        t = 0
        for length in arm:
            t += signs[idx] * length
            idx += 1
            values.append(t)
    W = sum(weights)
    return W * sum(w * x * x for w, x in zip(weights, values)) - sum(w * x for w, x in zip(weights, values)) ** 2


def raw_formula(arms, weights):
    idx = 1
    qs = []
    C = 0
    for arm in arms:
        t = 0
        q = 0
        for length in arm:
            t += length
            w = weights[idx]
            q += w * t
            C += w * t * t
            idx += 1
        qs.append(q)
    D = min(abs(sum(s * q for s, q in zip(ss, qs))) for ss in product((-1, 1), repeat=len(qs)))
    return sum(weights) * C - D * D


def check_one(arms, weights):
    e = sum(map(len, arms))
    best = -1
    winners = []
    for ss in product((-1, 1), repeat=e):
        v = raw_spread(arms, weights, ss)
        if v > best:
            best, winners = v, [ss]
        elif v == best:
            winners.append(ss)
    expected = raw_formula(arms, weights)
    assert best == expected, (arms, weights, best, expected)
    # Every maximizing edge-sign array is constant along each rooted arm.
    for ss in winners:
        offset = 0
        for arm in arms:
            assert len(set(ss[offset:offset + len(arm)])) == 1, (arms, weights, ss)
            offset += len(arm)
    return len(winners)


def main():
    rng = Random(20261102)
    count = 0
    winner_count = 0
    for r in (2, 3, 4, 5):
        for iteration in range(45):
            lengths = [rng.randrange(1, 5) for _ in range(r)]
            while sum(lengths) > 11:
                j = rng.randrange(r)
                lengths[j] = max(1, lengths[j] - 1)
            arms = [[rng.randrange(1, 6) for _ in range(L)] for L in lengths]
            weights = [rng.randrange(1, 10) for _ in range(1 + sum(lengths))]
            winner_count += check_one(arms, weights)
            count += 1
    print('ARBITRARY_POSITIVE_INTEGER_EDGE_LENGTHS_AND_VERTEX_MASSES_OK', count, winner_count)
    eq = 0
    for r in range(2, 8):
        for L in range(1, 5):
            if r*L > 12:
                continue
            arms = [[1] * L for _ in range(r)]
            n = 1 + r * L
            weights = [1] * n
            target = n * r * L * (L + 1) * (2 * L + 1) // 6 - ((r & 1) * (L * (L + 1) // 2) ** 2)
            assert target == raw_formula(arms, weights)
            winner_count += check_one(arms, weights)
            eq += 1
    print('EQUAL_ARM_PARITY_FORMULA_AND_ALL_MAXIMIZERS_OK', eq)
    for aa, feasible in [([1, 1, 2], True), ([1, 2, 4], False), ([2, 3, 5], True), ([2, 3, 6], False)]:
        A=sum(aa)
        arms=[[1] for _ in aa]
        weights=[A] + aa  # root mass = 1/2 after normalization
        expected=sum(weights) * sum(aa)
        optimum=raw_formula(arms, weights)
        assert (optimum == expected) == feasible
        check_one(arms, weights)
    print('STAR_PARTITION_THRESHOLD_EXACT_OK', 4)
    print('ALL_WEIGHTED_SPIDER_VARIANCE_CHECKS_OK')

if __name__ == '__main__':
    main()

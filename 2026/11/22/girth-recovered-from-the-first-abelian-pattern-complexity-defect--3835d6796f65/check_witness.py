#!/usr/bin/env python3
"""Check explicit triangular-length pattern witnesses using sparse integer sets.

The checker evaluates designated translates, not all translates of the
infinite word. Infinite quantifiers are proved symbolically in RESULT.md.
"""
from math import comb


def construct(r):
    count = comb(r, 2)
    scale = 2*r + 1
    spikes = [scale * 3**j for j in range(1, count+4)]
    support = {0, r-1, r} | set(spikes)
    pattern = set(range(r))
    nextspike = 0
    for row in range(1, r):
        for _ in range(row):
            pattern.add(spikes[nextspike] - row)
            nextspike += 1
    assert len(pattern) == comb(r+1, 2)
    return pattern, support, spikes


def main():
    checks = 0
    for r in range(2, 13):
        pattern, support, spikes = construct(r)
        counts = []
        for t in range(r):
            hits = sum(1 for s in pattern if t+s in support)
            counts.append(hits)
            assert hits == t+2, (r, t, hits)
            checks += 1
        # Pick a remote spike past the entire diameter of the pattern.
        future = spikes[-1]
        assert future > max(pattern)
        before = future - max(pattern)
        # Every element of before + pattern is within the long empty gap
        # immediately preceding this future spike except its last element.
        assert sum(1 for s in pattern if before+s in support) == 1
        # Another translation lies strictly inside that gap.
        zero_translation = before - 1
        assert zero_translation >= 0
        assert sum(1 for s in pattern if zero_translation+s in support) == 0
        print(f'r={r}, arity={len(pattern)}, isolated row counts={counts}, plus 0 and 1')
    print(f'WITNESS_CHECKS_OK tagged_rows={checks} parameters=11')


if __name__ == '__main__':
    main()

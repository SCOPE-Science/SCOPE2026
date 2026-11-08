#!/usr/bin/env python3
"""Recheck finite certificates for the period-doubling tortoise thresholds."""
import csv
from collections import defaultdict
from functools import lru_cache
from pathlib import Path

@lru_cache(None)
def block(letter, depth):
    if depth == 0:
        return letter
    previous = block(letter, depth - 1)
    return ''.join('10' if c == '1' else '11' for c in previous)

@lru_cache(None)
def factors(n):
    assert n >= 1
    depth = 0
    while (1 << depth) < n:
        depth += 1
    width = 1 << depth
    pairs = ('01', '10', '11')
    return frozenset((block(a, depth) + block(b, depth))[j:j+n]
                     for a, b in pairs for j in range(2*width - n + 1))

def first_one_step(s):
    j = s.find('1')
    return s if j == -1 else s[:j] + s[j+1:] + '1'

def iteration(s, k):
    for _ in range(k):
        s = first_one_step(s)
    return s

def delete_first_k(s, k):
    count = 0
    kept = []
    for c in s:
        if c == '1' and count < k:
            count += 1
        else:
            kept.append(c)
    return ''.join(kept) + '1' * count

def word_by_valuations(n):
    def bit(i):
        m = i + 1
        v = 0
        while m % 2 == 0:
            v += 1
            m //= 2
        return '1' if v % 2 == 0 else '0'
    return ''.join(bit(i) for i in range(n))

def load_table(p):
    with open(p, encoding='utf-8', newline='') as f:
        return list(csv.DictReader(f))

def main():
    data_file = Path(__file__).parent / 'thresholds.csv'
    rows = load_table(data_file)
    assert len(rows) == 32
    prefix = word_by_valuations(16384)
    for r in rows:
        k, N = int(r['k']), int(r['threshold'])
        assert k in range(1, 33)
        assert N >= 2*k
        assert int(r['k']) == rows.index(r)+1
        previous, current = factors(N-1), factors(N)
        assert len(current) == int(r['factor_count_at_threshold'])
        # Independent sequence construction, rather than two-superblock factor extraction.
        for n, expected in ((N-1, previous), (N, current)):
            direct = {prefix[i:i+n] for i in range(len(prefix)-n+1)}
            assert direct == expected, (k, n, len(direct), len(expected))
        def fibers(words):
            classes = defaultdict(list)
            for w in words:
                a, b = iteration(w,k), delete_first_k(w,k)
                assert a == b, (k,w)
                classes[a].append(w)
            return classes
        before, after = fibers(previous),fibers(current)
        assert len(after) == len(current), ('not injective',k,N)
        assert len(previous)-len(before) == int(r['deficit_before']), (k,N)
        collisions = [tuple(sorted(v)) for v in before.values() if len(v)>1]
        assert len(collisions) == 1 and len(collisions[0]) == 2, (k,collisions)
        assert collisions[0] == (r['witness_a'],r['witness_b']), (k,collisions[0])
        assert not any('00' in w for w in current)
    print('PERIOD_DOUBLING_REVERSED_TORTOISE_VERIFY_OK 32')

if __name__ == '__main__':
    main()

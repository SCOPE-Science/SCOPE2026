#!/usr/bin/env python3
"""Finite independent checks of uniform-triple-partition membership concepts."""
import itertools
from collections import Counter
from functools import lru_cache


def triple_partitions(n):
    assert n % 3 == 0
    def generate(rest):
        if not rest:
            yield ()
            return
        x = rest[0]
        for y, z in itertools.combinations(rest[1:], 2):
            for tail in generate(tuple(a for a in rest if a not in (x,y,z))):
                yield ((x,y,z),) + tail
    return list(generate(tuple(range(n))))


def incidence(n):
    ps = triple_partitions(n)
    edges = list(itertools.combinations(range(n), 2))
    patterns = []
    for partition in ps:
        block_of = {x: b for b, block in enumerate(partition) for x in block}
        patterns.append(sum(1 << i for i, (a,b) in enumerate(edges)
                            if block_of[a] == block_of[b]))
    return edges, patterns


def support_stats(n):
    edges, patterns = incidence(n)
    counter = Counter({0: 1})
    # Any shattered support is present in an all-positive concept. Thus the
    # following union exhausts all candidates for every support cardinality.
    candidates = {}
    for mask in patterns:
        ones = [i for i in range(len(edges)) if mask >> i & 1]
        for k in range(1, len(ones)+1):
            target = candidates.setdefault(k, set())
            for subset in itertools.combinations(ones, k):
                target.add(sum(1 << i for i in subset))
    for k, masks in candidates.items():
        for s in masks:
            if len({p & s for p in patterns}) == 1 << k:
                counter[k] += 1
    return dict(sorted(counter.items()))


def ldim(n, max_depth):
    edges, patterns = incidence(n)
    m = len(patterns)
    col = [sum(1 << i for i, pattern in enumerate(patterns) if pattern >> e & 1)
           for e in range(len(edges))]
    @lru_cache(None)
    def feasible(concept_subset, depth):
        if depth == 0:
            return True
        if concept_subset.bit_count() < 1 << depth:
            return False
        for column in col:
            positive = concept_subset & column
            negative = concept_subset ^ positive
            if positive and negative and feasible(positive, depth-1) and feasible(negative, depth-1):
                return True
        return False
    full = (1 << m) - 1
    return [feasible(full, d) for d in range(max_depth+1)]


def strong_witness(n):
    m = n // 3
    if m < 2:
        return None
    support = []
    for j in range(m-2):
        a = 3*j
        support.extend([(a,a+1), (a+1,a+2)])
    a = 3*(m-2)
    support.extend([(a,a+1), (a+3,a+4)])
    edges, patterns = incidence(n)
    inds = [edges.index(e) for e in support]
    counts = Counter(tuple((p>>i)&1 for i in inds) for p in patterns)
    return min(counts.values()), len(counts), len(support)


def main():
    for n in (3,6,9):
        edges, patterns = incidence(n)
        assert len(patterns) == {3:1, 6:10, 9:280}[n]
        stats = support_stats(n)
        expected = {3:{0:1},6:{0:1,1:15,2:105},
                    9:{0:1,1:36,2:630,3:5040,4:18900}}[n]
        assert stats == expected, (n,stats)
        print('SHATTER',n,stats)
        if n in (6,9):
            ls = ldim(n, n//3 * 2)
            assert ls == [True] * (2*(n//3)) + [False],(n,ls)
            print('LDIM',n,2*(n//3)-1)
            min_trace,num_traces,support_size = strong_witness(n)
            assert num_traces == 1<<support_size and min_trace >= 2
            print('STRONG',n,support_size,num_traces,min_trace)
    # A larger boundary check of the strong-trace witness; not an exhaustive
    # support search at twelve vertices.
    min_trace,num_traces,support_size = strong_witness(12)
    assert (min_trace,num_traces,support_size) == (2,64,6)
    print('STRONG',12,support_size,num_traces,min_trace)
    print('TRIPLE_BLOCK_SHATTERING_AND_ONLINE_PASS')

if __name__ == '__main__':
    main()

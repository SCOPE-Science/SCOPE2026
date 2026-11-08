#!/usr/bin/env python3
"""Exact exhaustive finite-graph verification for two binary16 beta maps.

Only Python's standard library is needed. Every floating-point number is
represented by an integer multiple of 2^-24, and every rounding decision is
made by integer comparison with ties to even.
"""
from bisect import bisect_left
from collections import Counter
import hashlib
import struct

N = 0x3C00                      # All nonnegative binary16 values below 1
ONE = 1 << 24
SCALE = 1 << 25


def numerator24(bits):
    """Exact binary16 value multiplied by 2^24 (bits in [0,0x4000])."""
    exponent = (bits >> 10) & 31
    fraction = bits & 1023
    if exponent == 0:
        return fraction
    return (1024 + fraction) << (exponent - 1)


def nearest_even(target, options):
    """Index of closest sorted binary16 number, using ties to even."""
    j = bisect_left(options, target)
    if j == 0:
        return 0
    if j == len(options):
        return j - 1
    a, b = target - options[j-1], options[j] - target
    if a < b:
        return j - 1
    if b < a:
        return j
    return j - 1 if (j - 1) % 2 == 0 else j


def successors():
    # Sorted encodings of nonnegative binary16 numbers [0,1] and [0,2]
    unit = [2*numerator24(bits) for bits in range(N + 1)]
    double = [2*numerator24(bits) for bits in range(0x4001)]
    assert len(unit) == 15361 and unit[0] == 0 and unit[-1] == SCALE
    assert double[-1] == 2*SCALE
    assert all(a < b for a, b in zip(unit, unit[1:]))
    assert all(a < b for a, b in zip(double, double[1:]))
    post_remainder, rounded_product = [], []
    for bits in range(N):
        exact_product = 3*numerator24(bits)   # scale is 2^-25
        remainder = exact_product % SCALE
        a = nearest_even(remainder, unit) % N
        rounded = double[nearest_even(exact_product, double)]
        b = nearest_even(rounded % SCALE, unit) % N
        post_remainder.append(a)
        rounded_product.append(b)
    return post_remainder, rounded_product


def analyze(graph):
    assert len(graph) == N and all(0 <= u < N for u in graph)
    known = bytearray(N)
    labels = [-1]*N
    distance = [-1]*N
    cycles = []
    for start in range(N):
        if known[start]:
            continue
        trail = []
        locations = {}
        u = start
        while not known[u] and u not in locations:
            locations[u] = len(trail)
            trail.append(u)
            u = graph[u]
        if u in locations:
            first = locations[u]
            cyc = trail[first:]
            label = len(cycles)
            cycles.append(cyc)
            for v in cyc:
                labels[v] = label
                distance[v] = 0
            transient = trail[:first]
        else:
            transient = trail
        for v in reversed(transient):
            nxt = graph[v]
            labels[v] = labels[nxt]
            distance[v] = distance[nxt] + 1
        for v in trail:
            known[v] = 1
    assert all(known) and all(label >= 0 for label in labels)
    assert all(x >= 0 for x in distance)
    for idx, cycle in enumerate(cycles):
        assert len(set(cycle)) == len(cycle)
        for j, v in enumerate(cycle):
            assert graph[v] == cycle[(j+1) % len(cycle)]
            assert labels[v] == idx and distance[v] == 0
    for v in range(N):
        if distance[v]:
            assert distance[graph[v]] == distance[v] - 1
            assert labels[graph[v]] == labels[v]
    stats = {len(c):Counter(labels)[i] for i, c in enumerate(cycles)}
    assert len(stats) == len(cycles), "Multiple cycles with a shared period: adapt manifest"
    return stats, max(distance), {len(c):min(c) for c in cycles}


def main():
    a, b = successors()
    a_basin, a_max, a_reps = analyze(a)
    b_basin, b_max, b_reps = analyze(b)
    assert a_basin == {1:468, 3:28, 8:2480, 18:187, 164:12197}, a_basin
    assert b_basin == {1:5705, 3:26, 4:3138, 24:2013, 41:4478}, b_basin
    assert a_max == 144 and b_max == 155
    assert sum(u != v for u, v in zip(a,b)) == 512
    assert sum(a_basin.values()) == N and sum(b_basin.values()) == N
    for name, graph, basin, maximum, reps in [
        ('post-remainder',a,a_basin,a_max,a_reps),
        ('rounded-product',b,b_basin,b_max,b_reps),
    ]:
        graph_digest = hashlib.sha256(b''.join(struct.pack('<H',n) for n in graph)).hexdigest()
        print(f'{name}: basins={dict(sorted(basin.items()))}; max_transient={maximum}; '\
              f'representative_bit_patterns={dict(sorted(reps.items()))}; graph_sha256={graph_digest}')
    print('BETA_HALF_EXACT_CENSUS_OK; states=15360; differing_successors=512')


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Exact finite checks for triangle-free endpoint-pairing interval graphs.

No finite enumeration is used to infer the infinite-n laws.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb

ASSERTIONS = 0


def check(condition, message=''):
    global ASSERTIONS
    ASSERTIONS += 1
    if not condition:
        raise AssertionError(message)


def pairings(positions):
    if not positions:
        yield ()
        return
    a = positions[0]
    for j in range(1, len(positions)):
        b = positions[j]
        for tail in pairings(positions[1:j] + positions[j + 1:]):
            yield ((a, b),) + tail


def open_height(pairs):
    events = [0] * (2 * len(pairs))
    for a, b in pairs:
        events[a] = 1
        events[b] = -1
    height = maximum = 0
    for e in events:
        height += e
        maximum = max(maximum, height)
    check(height == 0, 'incomplete endpoint pairing')
    return maximum


def code_from_pairs(pairs):
    intervals = sorted(pairs)
    letters = []
    for i, (a, b) in enumerate(intervals):
        if not i:
            continue
        live = [(u, v) for u, v in intervals[:i] if v > a]
        if len(live) > 1:
            return None
        if len(live) == 0:
            letters.append('B')
        elif live[0][1] > b:
            letters.append('O')
        else:
            letters.append('N')
    return ''.join(letters)


def pairs_from_code(word):
    start = 0
    next_pos = 1
    pairs = []
    for letter in word:
        if letter == 'B':
            pairs.append((start, next_pos))
            next_pos += 1
            start = next_pos
            next_pos += 1
        elif letter == 'O':
            new_start = next_pos
            next_pos += 1
            pairs.append((new_start, next_pos))
            next_pos += 1
        elif letter == 'N':
            new_start = next_pos
            next_pos += 1
            pairs.append((start, next_pos))
            next_pos += 1
            start = new_start
        else:
            raise ValueError(letter)
    pairs.append((start, next_pos))
    return tuple(sorted(pairs))


def graph_data(pairs):
    intervals = sorted(pairs)
    n = len(intervals)
    graph = [set() for _ in range(n)]
    for i, (a, b) in enumerate(intervals):
        for j, (c, d) in enumerate(intervals[:i]):
            if c < b and a < d:
                graph[i].add(j)
                graph[j].add(i)
    component_sizes = []
    seen = set()
    for i in range(n):
        if i in seen:
            continue
        seen.add(i)
        stack = [i]
        component = {i}
        while stack:
            u = stack.pop()
            for v in graph[u]:
                if v not in seen:
                    seen.add(v)
                    component.add(v)
                    stack.append(v)
        component_sizes.append(len(component))
        # Remove all degree-one and degree-zero vertices and test the remaining path.
        core = {v for v in component if len(graph[v]) >= 2}
        check(all(len(graph[v] & core) <= 2 for v in core), 'non-caterpillar core degree')
        if core:
            cc = {next(iter(core))}
            stack = list(cc)
            while stack:
                u = stack.pop()
                for v in graph[u] & core:
                    if v not in cc:
                        cc.add(v)
                        stack.append(v)
            check(cc == core, 'disconnected caterpillar core')
    edges = sum(map(len, graph)) // 2
    return len(component_sizes), edges, max(map(len, graph)), max(component_sizes), Counter(component_sizes)


def run_lengths(word):
    m = max(map(len, word.split('B')), default=0) + 1
    o = max(map(len, word.replace('B', 'N').split('N')), default=0)
    return m, o


for n in range(1, 8):
    component_hist = Counter()
    accepted = 0
    total = 0
    for pairs in pairings(tuple(range(2*n))):
        total += 1
        h = open_height(pairs)
        encoded = code_from_pairs(pairs)
        check((h <= 2) == (encoded is not None), f'eligibility mismatch n={n}')
        if h > 2:
            continue
        accepted += 1
        word = encoded
        check(pairs_from_code(word) == tuple(sorted(pairs)), f'inverse failure n={n}')
        c, e, delta, biggest, sizes = graph_data(pairs)
        longest, o_run = run_lengths(word)
        check(c == word.count('B') + 1, 'component count')
        check(e == n-c, 'forest edge count')
        check(biggest == longest, 'maximum component run')
        check(o_run <= delta <= o_run+2, 'maximum degree run inequality')
        component_hist[c] += 1
    check(accepted == 3**(n-1), f'height-two pairing count at n={n}')
    check(sum(component_hist.values()) == accepted, 'component histogram size')
    for c in range(1,n+1):
        check(component_hist[c] == comb(n-1,c-1)*2**(n-c), f'binomial component law n={n}, c={c}')
    print(f'pairings n={n}: total={total}, triangle_free={accepted}')

# Independently enumerate all ternary codes and recover exact component-size means.
for n in range(1, 11):
    total = 0
    size_sum = Counter()
    for letters in product('BON', repeat=n-1):
        word = ''.join(letters)
        pairs = pairs_from_code(word)
        check(code_from_pairs(pairs) == word, 'word reconstruction')
        check(open_height(pairs) <= 2, 'height violated')
        c, edges, delta, largest, size_counts = graph_data(pairs)
        check(c == 1 + word.count('B'), 'component count by letter')
        check(edges == n-c, 'edge count by letter')
        m, o = run_lengths(word)
        check(largest == m, 'largest component by word')
        check(o <= delta <= o+2, 'degree bounds by word')
        for k, v in size_counts.items():
            size_sum[k] += v
        total += 1
    check(total == 3**(n-1), 'code enumeration count')
    for k in range(1, n+1):
        observed = Fraction(size_sum[k], total)
        if k == n:
            exact = Fraction(2,3)**(n-1)
        else:
            exact = (Fraction(2,3) + Fraction(n-k-1,9)) * Fraction(2,3)**(k-1)
        check(observed == exact, f'component-size mean n={n},k={k}: {observed} != {exact}')
    print(f'codes n={n}: verified {total} words')

print(f'PASS: {ASSERTIONS} exact finite assertions')

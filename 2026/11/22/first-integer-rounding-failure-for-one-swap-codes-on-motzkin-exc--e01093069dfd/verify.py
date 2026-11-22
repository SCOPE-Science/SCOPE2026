#!/usr/bin/env python3
"""Reconstruct the finite Motzkin one-swap channel and verify exact certificates.

Requires Python 3.9+ standard library only. Run: python verify.py
All outputs, including paths that descend below zero, are retained.
"""
import itertools
import json
from collections import defaultdict
from fractions import Fraction
from pathlib import Path


def sources(n):
    groups = defaultdict(list)
    for letters in itertools.product('UDH', repeat=n):
        height = 0
        for letter in letters:
            height += (letter == 'U') - (letter == 'D')
            if height < 0:
                break
        else:
            if height == 0:
                word = ''.join(letters)
                groups[word.count('U')].append(word)
    return groups


def ball(w):
    result = {w}
    for i in range(len(w) - 1):
        if w[i] != w[i + 1]:
            result.add(w[:i] + w[i + 1] + w[i] + w[i + 2:])
    return result


def maximum_clique(adj):
    """Exact clique search; greedy coloring is a proved upper bound.

    A proper r-coloring of the candidate graph bounds every clique by r.
    For a fixed coloring order, prefix candidates appearing up to index i
    use at most color_bound[i] colors. Iterating indices backward allows
    pruning whenever current_size + color_bound[i] <= incumbent_size.
    Every non-pruned choice branches on v with future candidates restricted
    to neighbors of v; removing v makes branches disjoint and exhaustive.
    """
    n = len(adj)
    incumbent = []
    visited = 0

    def color_order(P):
        ordering, caps = [], []
        color = 0
        while P:
            color += 1
            possible = P
            while possible:
                bit = possible & -possible
                v = bit.bit_length() - 1
                ordering.append(v)
                caps.append(color)
                P &= ~bit
                possible &= ~bit
                possible &= ~adj[v]
        return ordering, caps

    def visit(chosen, P):
        nonlocal visited, incumbent
        visited += 1
        if not P:
            if len(chosen) > len(incumbent):
                incumbent = chosen[:]
            return
        order, caps = color_order(P)
        for i in range(len(order) - 1, -1, -1):
            if len(chosen) + caps[i] <= len(incumbent):
                return
            v = order[i]
            visit(chosen + [v], P & adj[v])
            P &= ~(1 << v)

    visit([], (1 << n) - 1)
    return len(incumbent), visited


def verify_record(rec):
    n, k = rec['n'], rec['k']
    words = sources(n)[k]
    assert len(words) == rec['source_count']
    balls = {w: ball(w) for w in words}
    received = set().union(*balls.values())
    assert len(received) == rec['output_count']
    assert len(rec['codebook']) == rec['maximum']
    assert len(set(rec['codebook'])) == len(rec['codebook'])
    assert set(rec['codebook']) <= set(words)
    occupancy = set()
    for w in rec['codebook']:
        assert not (occupancy & balls[w]), ('collision', n, k, w)
        occupancy.update(balls[w])

    # Every fractional variable is nonnegative and lives on a legal source
    # or on an actual received word. All primal/dual checks use exact rationals.
    primal = {w: Fraction(t) for w, t in rec['primal'].items()}
    dual = {y: Fraction(t) for y, t in rec['dual'].items()}
    assert set(primal) <= set(words) and set(dual) <= received
    assert all(x >= 0 for x in primal.values())
    assert all(y >= 0 for y in dual.values())
    for y in received:
        assert sum((primal.get(w, 0) for w in words if y in balls[w]), Fraction()) <= 1, (n, k, 'primal', y)
    for w in words:
        assert sum((dual.get(y, 0) for y in balls[w]), Fraction()) >= 1, (n, k, 'dual', w)
    optimum = Fraction(rec['fractional_optimum'])
    assert sum(primal.values(), Fraction()) == optimum
    assert sum(dual.values(), Fraction()) == optimum

    # Compatibility edges are recomputed directly, without importing an
    # optimization library or trusting the original search output.
    adj = [0] * len(words)
    for i in range(len(words)):
        for j in range(i):
            if balls[words[i]].isdisjoint(balls[words[j]]):
                adj[i] |= 1 << j
                adj[j] |= 1 << i
    max_size, visited = maximum_clique(adj)
    assert max_size == rec['maximum'], (n, k, max_size, rec['maximum'])
    assert visited == rec['clique_nodes'], (n, k, visited, rec['clique_nodes'])
    assert rec['maximum'] <= optimum
    return max_size, optimum, visited


def main():
    data = json.loads(Path(__file__).with_name('certificates.json').read_text('utf-8'))
    assert data['ranges'] == [1, 7]
    sums = defaultdict(lambda: [0, Fraction()])
    nodes = 0
    total_groups = 0
    for n in range(1, 8):
        group_data = sources(n)
        for k, words in sorted(group_data.items()):
            key = f'{n}:{k}'
            assert key in data['groups']
            record = data['groups'][key]
            assert record['n'] == n and record['k'] == k
            capacity, optimum, visited = verify_record(record)
            sums[n][0] += capacity
            sums[n][1] += optimum
            nodes += visited
            total_groups += 1
    assert total_groups == len(data['groups']) == 19
    capacities = [sums[n][0] for n in range(1, 8)]
    fractionals = [sums[n][1] for n in range(1, 8)]
    assert capacities == [1, 2, 2, 4, 7, 14, 28]
    assert fractionals == [Fraction(a) for a in ['1','2','2','4','7','71/5','5515/182']]
    assert all(capacities[i] == fractionals[i] for i in range(5))
    assert int(fractionals[5]) == capacities[5]
    assert int(fractionals[6]) > capacities[6]
    print(f'VERIFY_OK groups={total_groups} nodes={nodes}')
    print('Integer capacities:', ','.join(map(str, capacities)))
    print('Fractional optima:', ','.join(map(str, fractionals)))


if __name__ == '__main__':
    main()

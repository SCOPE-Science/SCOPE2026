#!/usr/bin/env python3
"""Finite corroboration for the two-variable classification of tournaments.

Run with Python 3; no third-party packages required.
This program implements color refinement of one-free-variable FO^2 types.
It does not replace the mathematical proof of the unbounded-depth result.
"""
from itertools import combinations
from collections import defaultdict
import random


def tournament(n, mask):
    E = [[False] * n for _ in range(n)]
    pairs = list(combinations(range(n), 2))
    for k, (i, j) in enumerate(pairs):
        E[i][j] = not bool((mask >> k) & 1)
        E[j][i] = not E[i][j]
    return E


def invariant(E):
    alive = list(range(len(E)))
    a = 0
    while True:
        sources = [x for x in alive if all(x == y or E[x][y] for y in alive)]
        if not sources:
            break
        assert len(sources) == 1
        alive.remove(sources[0]); a += 1
    if not alive:
        return ('transitive', a)
    b = 0
    while True:
        sinks = [x for x in alive if all(x == y or E[y][x] for y in alive)]
        if not sinks:
            break
        assert len(sinks) == 1
        alive.remove(sinks[0]); b += 1
    assert len(alive) >= 3
    assert all(any(E[x][y] for y in alive if x != y) and any(E[y][x] for y in alive if x != y) for x in alive)
    return ('nontransitive', a, b)


def global_refinement(models):
    ids = [tuple(0 for _ in E) for E in models]
    for r in range(16):
        signatures = []
        for E, old in zip(models, ids):
            n = len(E)
            signatures.append([ (old[x], tuple(sorted({old[y] for y in range(n) if E[x][y]})),
                                   tuple(sorted({old[y] for y in range(n) if E[y][x]}))) for x in range(n) ])
        palette = {}
        new = []
        for arr in signatures:
            colors = []
            for key in arr:
                if key not in palette:
                    palette[key] = len(palette)
                colors.append(palette[key])
            new.append(tuple(colors))
        # Check partition stability, not numerical IDs.
        if r > 0 and all((a[i] == a[j]) == (b[i] == b[j])
                         for a, b in zip(ids, new)
                         for i in range(len(a)) for j in range(i + 1, len(a))):
            # Still need global equality across different models; check via palette cardinalities.
            if len(set(x for arr in ids for x in arr)) == len(palette):
                ids = new
                break
        ids = new
    classes = defaultdict(set)
    witnessed = defaultdict(set)
    for E, color in zip(models, ids):
        spectrum = frozenset(color)
        classes[spectrum].add(invariant(E))
        witnessed[invariant(E)].add(spectrum)
    assert all(len(v) == 1 for v in classes.values()), [v for v in classes.values() if len(v) > 1][:3]
    assert all(len(v) == 1 for v in witnessed.values()), [v for v in witnessed.values() if len(v) > 1][:3]
    return r + 1, len(classes)


def run():
    rng = random.Random(7349)
    models = []
    counts = []
    for n in range(1, 7):
        masks = range(1 << (n * (n-1)//2)) if n <= 5 else rng.sample(range(1 << 15), 600)
        each = [tournament(n, s) for s in masks]
        models.extend(each)
        cnt = len(set(map(invariant, each)))
        expected = 1 if n < 3 else 1 + (n - 1)*(n - 2)//2
        assert cnt == expected, (n, cnt, expected)
        counts.append((n, len(each), cnt))
    stages, nclasses = global_refinement(models)
    assert nclasses == len(set(map(invariant, models)))
    print('finite models:', len(models))
    print('per-order models and observed theory classes:', counts)
    print('simultaneous FO2 unary-type refinement rounds:', stages)
    print('global FO2 equivalence classes:', nclasses)
    print('all invariant-vs-refinement comparisons: PASS')

if __name__ == '__main__': run()

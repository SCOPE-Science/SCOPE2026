#!/usr/bin/env python3
"""Exhaustive small-case check for separate refinement on two equivalences.

Usage: python verify_two_equivalence_forests.py 8
No third-party dependencies. The check is finite corroboration, not the
all-size proof.
"""
import collections
import itertools
import sys


def partitions(n):
    labels = [0] * n
    def walk(i, maximum):
        if i == n:
            yield tuple(labels)
            return
        for k in range(maximum + 2):
            labels[i] = k
            yield from walk(i + 1, max(maximum, k))
    yield from walk(1, 0)


def classes(labels):
    groups = collections.defaultdict(list)
    for i, a in enumerate(labels):
        groups[a].append(i)
    return tuple(tuple(v) for v in groups.values())


def incidence(e, f):
    left, right = max(e) + 1, max(f) + 1
    adj = [set() for _ in range(left + right)]
    for x, y in zip(e, f):
        adj[x].add(left + y)
        adj[left + y].add(x)
    # Parallel incidence edges cannot occur in a forest.
    return adj, left


def forest(e, f):
    left, right = max(e) + 1, max(f) + 1
    parent = list(range(left + right))
    def root(x):
        while parent[x] != x:
            parent[x] = parent[parent[x]]
            x = parent[x]
        return x
    for x, y in zip(e, f):
        a, b = root(x), root(left + y)
        if a == b:
            return False
        parent[a] = b
    return True


def forest_canonical_form(e, f):
    adj, left = incidence(e, f)
    seen = set()
    component_codes = []
    def rooted(v, parent):
        children = sorted(rooted(w, v) for w in adj[v] if w != parent)
        return ('L' if v < left else 'R') + '(' + ''.join(children) + ')'
    for start in range(len(adj)):
        if start in seen:
            continue
        component = {start}
        seen.add(start)
        todo = [start]
        while todo:
            v = todo.pop()
            for w in adj[v]:
                if w not in seen:
                    seen.add(w)
                    component.add(w)
                    todo.append(w)
        component_codes.append(min(rooted(v, -1) for v in component))
    return tuple(sorted(component_codes))


def separate_refinement_signature(e, f, n, registries):
    group_e, group_f = classes(e), classes(f)
    c = (0,) * n
    for t in range(n + 2):
        eprofile = [None] * n
        fprofile = [None] * n
        for group in group_e:
            profile = tuple(sorted(c[i] for i in group))
            for i in group:
                eprofile[i] = profile
        for group in group_f:
            profile = tuple(sorted(c[i] for i in group))
            for i in group:
                fprofile[i] = profile
        registry = registries[t]
        nxt = []
        for i in range(n):
            key = (c[i], eprofile[i], fprofile[i])
            if key not in registry:
                registry[key] = len(registry) + 1
            nxt.append(registry[key])
        c = tuple(nxt)
    return tuple(sorted(c))


def test(max_n):
    for n in range(1, max_n + 1):
        size_profiles = {tuple(sorted(collections.Counter(p).values()))
                         for p in partitions(n)}
        e_reps = [tuple(itertools.chain.from_iterable(
            [j] * width for j, width in enumerate(profile)))
            for profile in sorted(size_profiles)]
        f_partitions = list(partitions(n))
        registries = [{} for _ in range(n + 2)]
        observed = {}
        cyc = set()
        configurations = nforest = 0
        for e in e_reps:
            for f in f_partitions:
                configurations += 1
                signature = separate_refinement_signature(e, f, n, registries)
                if forest(e, f):
                    nforest += 1
                    code = forest_canonical_form(e, f)
                    if signature in cyc:
                        raise AssertionError(('cyclic competitor', n, e, f))
                    if signature in observed and observed[signature] != code:
                        raise AssertionError(('nonisomorphic forests', n, e, f))
                    observed[signature] = code
                else:
                    if signature in observed:
                        raise AssertionError(('cyclic competitor', n, e, f))
                    cyc.add(signature)
        print('n={} tested={} forest_cases={} forest_types={} failures=0'.format(
            n, configurations, nforest, len(observed)), flush=True)


if __name__ == '__main__':
    test(int(sys.argv[1]) if len(sys.argv) > 1 else 8)

#!/usr/bin/env python3
"""Independent exhaustive distance-signature verification on the labelled five-cube."""
import hashlib
import json
from collections import Counter, deque
from itertools import combinations

DIM = 5
VERTICES = tuple(range(1 << DIM))
PAIRS = tuple(combinations(VERTICES, 2))
FULL = (1 << len(PAIRS)) - 1


def separate_mask(s):
    return sum(1 << p for p, (u, v) in enumerate(PAIRS)
               if ((u ^ s).bit_count() != (v ^ s).bit_count()))


def distances(adjacency, start):
    out = {start: 0}
    q = deque([start])
    while q:
        u = q.popleft()
        for v in adjacency[u]:
            if v not in out:
                out[v] = out[u] + 1
                q.append(v)
    return out


def main():
    cover = [separate_mask(v) for v in VERTICES]
    small = {k: sum(1 for t in combinations(VERTICES, k)
                    if _union(cover[v] for v in t) == FULL)
             for k in range(1, 4)}
    assert small == {1: 0, 2: 0, 3: 0}
    bases = [t for t in combinations(VERTICES, 4)
             if _union(cover[v] for v in t) == FULL]
    assert len(bases) == 1280
    lookup = {s: i for i, s in enumerate(bases)}
    jumps = [set() for _ in bases]
    slides = [set() for _ in bases]
    for i, s in enumerate(bases):
        old = set(s)
        for outgoing in s:
            for incoming in VERTICES:
                if incoming in old:
                    continue
                successor = tuple(sorted((old - {outgoing}) | {incoming}))
                j = lookup.get(successor)
                if j is not None:
                    jumps[i].add(j)
                    if (outgoing ^ incoming).bit_count() == 1:
                        slides[i].add(j)
    assert all(len(z) == 12 for z in jumps)
    assert not any(slides)
    assert all(i in jumps[j] for i, js in enumerate(jumps) for j in js)

    untouched = set(range(len(bases)))
    components = []
    total_dist = Counter()
    while untouched:
        root = min(untouched)
        reached = distances(jumps, root)
        component = frozenset(reached)
        assert component <= untouched
        untouched -= component
        components.append(component)
        assert len(component) == 80
        support = set().union(*(set(bases[i]) for i in component))
        assert len(support) == 10
        assert {v ^ 31 for v in support} == support
        for i in component:
            length = distances(jumps, i)
            assert len(length) == 80
            total_dist.update(length.values())
    assert len(components) == 16
    assert sorted(total_dist.items()) == [(0, 1280), (1, 15360), (2, 38400), (3, 35840), (4, 11520)]
    assert sum(map(len, jumps)) // 2 == 7680
    data = {
        'dimension': DIM,
        'tested_triples': 4960,
        'tested_quadruples': len(list(combinations(VERTICES, 4))),
        'smaller_resolving_set_counts': small,
        'minimum_size': 4,
        'minimum_bases': len(bases),
        'jump_edges': sum(map(len, jumps)) // 2,
        'jump_degree': 12,
        'jump_components': len(components),
        'component_size': 80,
        'component_ordered_distance_histogram': dict(sorted(total_dist.items())),
        'component_diameter': 4,
        'slide_edges': sum(map(len, slides)) // 2,
        'bases_sha256': hashlib.sha256(''.join(','.join(map(str, b)) + ';' for b in bases).encode()).hexdigest(),
    }
    assert data['tested_triples'] == 4960
    print(json.dumps(data, sort_keys=True, indent=2))


def _union(iterable):
    out = 0
    for x in iterable:
        out |= x
    return out


if __name__ == '__main__':
    main()

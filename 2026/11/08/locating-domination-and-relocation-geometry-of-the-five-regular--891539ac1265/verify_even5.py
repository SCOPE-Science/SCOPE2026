#!/usr/bin/env python3
"""Exact census and token-relocation checks for the 5-regular Clebsch graph.

Vertices are even-weight 5-bit words; adjacency is Hamming distance four.
Only Python's standard library is needed.
"""
import collections
import itertools
import json

words = [x for x in range(32) if x.bit_count() % 2 == 0]
assert len(words) == 16
adj = [sum(1 << j for j, b in enumerate(words) if (a ^ b).bit_count() == 4)
       for a in words]
assert all(a.bit_count() == 5 for a in adj)
assert all(((adj[i] >> j) & 1) == ((adj[j] >> i) & 1)
           for i in range(16) for j in range(16))

def signature_condition(mask):
    signatures = []
    for v in range(16):
        if mask & (1 << v):
            continue
        s = adj[v] & mask
        if not s or s in signatures:
            return False
        signatures.append(s)
    return True

def graph_type(mask):
    selected = [i for i in range(16) if (mask >> i) & 1]
    degrees = sorted((adj[v] & mask).bit_count() for v in selected)
    if degrees == [0, 0, 0, 0, 0]:
        return 'independent'
    if degrees == [0, 0, 0, 1, 1]:
        return 'single_edge'
    if degrees == [1, 1, 1, 1, 4]:
        return 'four_star'
    return 'other'

count_by_cardinality = {}
for size in range(5):
    count_by_cardinality[str(size)] = sum(
        signature_condition(sum(1 << i for i in indices))
        for indices in itertools.combinations(range(16), size))
assert not any(count_by_cardinality.values())
valid = []
all_shape_count = collections.Counter()
for indices in itertools.combinations(range(16), 5):
    mask = sum(1 << i for i in indices)
    shape = graph_type(mask)
    all_shape_count[shape] += 1
    yes = signature_condition(mask)
    assert yes == (shape != 'other'), (indices, shape, yes)
    if yes:
        valid.append(mask)
assert len(valid) == 416
shape = [graph_type(s) for s in valid]
assert collections.Counter(shape) == {'independent': 16, 'single_edge': 320, 'four_star': 80}

def reconfigure(slide):
    g = [set() for _ in valid]
    for i, x in enumerate(valid):
        for j in range(i):
            y = valid[j]
            d = x ^ y
            if d.bit_count() != 2:
                continue
            removed = (x & ~y).bit_length() - 1
            added = (y & ~x).bit_length() - 1
            if slide and not ((adj[removed] >> added) & 1):
                continue
            g[i].add(j)
            g[j].add(i)
    visited = set()
    sizes = []
    all_ecc = []
    for initial in range(len(g)):
        if initial in visited:
            continue
        stack = [initial]
        visited.add(initial)
        vertices = []
        while stack:
            v = stack.pop()
            vertices.append(v)
            for t in g[v]:
                if t not in visited:
                    visited.add(t)
                    stack.append(t)
        sizes.append(len(vertices))
        for start in vertices:
            depth = {start: 0}
            queue = collections.deque([start])
            while queue:
                v = queue.popleft()
                for t in g[v]:
                    if t not in depth:
                        depth[t] = depth[v] + 1
                        queue.append(t)
            assert len(depth) == len(vertices)
            all_ecc.append(max(depth.values()))
    class_degree = collections.defaultdict(set)
    connections = collections.Counter()
    for i, ns in enumerate(g):
        class_degree[shape[i]].add(len(ns))
        for j in ns:
            if i < j:
                connections['/'.join(sorted([shape[i], shape[j]]))] += 1
    return {
        'edges': sum(map(len, g)) // 2,
        'components': len(sizes),
        'component_sizes': sorted(sizes),
        'radius': min(all_ecc),
        'diameter': max(all_ecc),
        'eccentricity_histogram': dict(sorted(collections.Counter(all_ecc).items())),
        'degree_by_shape': {k: sorted(v) for k, v in sorted(class_degree.items())},
        'edges_by_shape': dict(sorted(connections.items())),
    }

report = {
    'graph': '5-regular Clebsch, 16 vertices, 40 edges',
    'minimum': 5,
    'smaller_counts': count_by_cardinality,
    'five_sets_total': sum(all_shape_count.values()),
    'five_set_shape_counts': dict(sorted(all_shape_count.items())),
    'minimum_set_count': len(valid),
    'minimum_shapes': dict(sorted(collections.Counter(shape).items())),
    'jump': reconfigure(False),
    'slide': reconfigure(True),
}
assert report['jump']['edges'] == 2960 and report['slide']['edges'] == 1360
assert (report['jump']['radius'], report['jump']['diameter']) == (5, 6)
assert (report['slide']['radius'], report['slide']['diameter']) == (6, 7)
print(json.dumps(report, sort_keys=True, separators=(',', ':')))

#!/usr/bin/env python3
"""Exhaustive synchronous out-neighbor voting on small Paley tournaments.

Python 3 standard library only. Each bit i is the state of vertex i.
"""
import json
from collections import Counter, deque

ORDERS = (3, 7, 11, 19)


def residues(p):
    return sorted({(j * j) % p for j in range(1, p)})


def successors(p):
    q = residues(p)
    assert len(q) == (p - 1) // 2
    assert all(((p - j) % p) not in q for j in q)
    neighbors = [sum(1 << ((i + j) % p) for j in q) for i in range(p)]
    threshold = ((p - 1) // 2) // 2 + 1
    def step(x):
        return sum(1 << i for i in range(p)
                   if (x & neighbors[i]).bit_count() >= threshold)
    return [step(x) for x in range(1 << p)]


def cycle_data(f):
    size = len(f)
    visited = bytearray(size)
    depth = [-1] * size
    period = [0] * size
    cycles = []
    for x in range(size):
        if visited[x]:
            continue
        path = []
        index = {}
        u = x
        while not visited[u] and u not in index:
            index[u] = len(path)
            path.append(u)
            u = f[u]
        if u in index:
            cut = index[u]
            cyc = path[cut:]
            cycles.append(cyc)
            for v in cyc:
                visited[v] = 1
                depth[v] = 0
                period[v] = len(cyc)
            path = path[:cut]
        for v in reversed(path):
            depth[v] = depth[f[v]] + 1
            period[v] = period[f[v]]
            visited[v] = 1
    assert all(visited) and min(depth) == 0
    return depth, period, cycles


def natural_geometry(p, f, depth, period):
    mask = (1 << p) - 1
    q = residues(p)
    recurrent = {i for i, d in enumerate(depth) if d == 0}
    def rotate(x):
        return ((x << 1) & mask) | (x >> (p - 1))
    def multiply(x, a):
        y = 0
        while x:
            bit = x & -x
            y |= 1 << ((a * (bit.bit_length() - 1)) % p)
            x -= bit
        return y
    classes = []
    while recurrent:
        start = min(recurrent)
        orbit = {start}
        todo = deque([start])
        while todo:
            x = todo.popleft()
            for y in (f[x], rotate(x), x ^ mask):
                if y not in orbit:
                    orbit.add(y)
                    todo.append(y)
            for a in q:
                y = multiply(x, a)
                if y not in orbit:
                    orbit.add(y)
                    todo.append(y)
        assert orbit <= recurrent, 'the group action must preserve recurrence'
        assert len({period[v] for v in orbit}) == 1
        recurrent.difference_update(orbit)
        classes.append({'representative': start,
                        'period': period[start],
                        'configurations': len(orbit),
                        'weight': start.bit_count()})
    return sorted(classes, key=lambda c:(c['period'],c['representative']))


def compute(p):
    f = successors(p)
    depth, period, cycles = cycle_data(f)
    c = Counter(len(cycle) for cycle in cycles)
    hist = Counter((depth[x], period[x]) for x in range(1 << p))
    classes = natural_geometry(p, f, depth, period)
    assert sum(len(cyc) for cyc in cycles) == sum(1 for d in depth if d == 0)
    assert sum(hist.values()) == (1 << p)
    return {'p': p,
            'quadratic_residues': residues(p),
            'cycles_by_length': {str(k): c[k] for k in sorted(c)},
            'periodic_states_by_length': {str(k): k*c[k] for k in sorted(c)},
            'entry_depth_by_period': [{'entry': t, 'period': L, 'count': v}
                                      for (t,L),v in sorted(hist.items())],
            'maximum_transient': max(depth),
            'geometric_classes': classes}

if __name__ == '__main__':
    data = {'description': 'Complete labelled-state functional graph and natural affine-complement-time classes',
            'cases': [compute(p) for p in ORDERS]}
    print(json.dumps(data, sort_keys=True, separators=(',', ':')))

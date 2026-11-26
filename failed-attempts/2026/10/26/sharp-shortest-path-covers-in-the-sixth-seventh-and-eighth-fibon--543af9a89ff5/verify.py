#!/usr/bin/env python3
"""Independently replay the explicit finite geodesic-edge covers."""
from collections import deque
import json
from pathlib import Path


def cube(n):
    vertices = {format(i, f'0{n}b') for i in range(2**n)
                if not (i & (i << 1))}
    edges = set()
    neighbors = {v: set() for v in vertices}
    for v in vertices:
        for j in range(n):
            w = v[:j] + ('0' if v[j] == '1' else '1') + v[j+1:]
            if w in vertices:
                edges.add(tuple(sorted((v, w))))
                neighbors[v].add(w)
    return vertices, edges, neighbors


def distance(neighbors, u, v):
    q = deque([(u, 0)])
    seen = {u}
    while q:
        w, d = q.popleft()
        if w == v:
            return d
        for x in neighbors[w]:
            if x not in seen:
                seen.add(x)
                q.append((x, d + 1))
    raise AssertionError('Disconnected graph')


def fibonacci(n):
    a, b = 0, 1
    for _ in range(n):
        a, b = b, a + b
    return a


def main():
    path = Path(__file__).with_name('geodesics.json')
    data = json.loads(path.read_text(encoding='utf-8'))
    assert set(data) == {'6', '7', '8'}
    expected_edges = {6: 38, 7: 71, 8: 130}
    for n in (6, 7, 8):
        vertices, edges, nbr = cube(n)
        covered = set()
        paths = data[str(n)]
        assert len(paths) == fibonacci(n), (n, len(paths))
        assert len(edges) == expected_edges[n], (n, len(edges))
        for p in paths:
            assert len(p) == len(set(p)) and len(p) >= 4, (n, p)
            assert all(v in vertices for v in p), (n, p)
            walked = {tuple(sorted((x, y))) for x, y in zip(p, p[1:])}
            assert len(walked) == len(p)-1 and walked <= edges, (n, p)
            # This computes the shortest-path distance from first principles,
            # rather than assuming the Fibonacci cube is isometric.
            assert len(p)-1 == distance(nbr, p[0], p[-1]), (n, p)
            covered.update(walked)
        assert covered == edges, (n, len(covered), len(edges))
        # The two extreme bit coordinates each induce exactly F_n edges.
        first = sum(u[0] != v[0] for u, v in edges)
        last = sum(u[-1] != v[-1] for u, v in edges)
        assert first == last == fibonacci(n), (n, first, last)
        print(f'n={n} vertices={len(vertices)} edges={len(edges)} '
              f'geodesics={len(paths)} union_edges={len(covered)} '
              f'extreme_coordinate_edges={first}')
    print('VERIFICATION_OK')


if __name__ == '__main__':
    main()

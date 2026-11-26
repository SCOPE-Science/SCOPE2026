#!/usr/bin/env python3
"""Check two-landmark refinement/orbit partitions of finite Hamming graphs.
Uses only the Python standard library; finite checks do not prove the theorem.
"""
from collections import Counter, defaultdict
from itertools import product
from math import comb, factorial


def color_partition(q, d, b):
    vertices = list(product(range(q), repeat=d))
    ids = {v: i for i, v in enumerate(vertices)}
    first = (0,) * d
    second = (1,) * b + (0,) * (d - b)
    marks = [first, second]
    nbr = []
    for v in vertices:
        nbr.append([ids[v[:j] + (z,) + v[j+1:]]
                    for j in range(d) for z in range(q) if z != v[j]])
    colors = [0] * len(vertices)
    colors[ids[first]], colors[ids[second]] = 1, 2
    rounds = 0
    while True:
        signatures = [(colors[i], tuple(sorted(Counter(colors[j] for j in ns).items())))
                      for i, ns in enumerate(nbr)]
        tab = {s: k for k, s in enumerate(sorted(set(signatures)))}
        nxt = [tab[s] for s in signatures]
        if len(set(nxt)) == len(set(colors)):
            assert all((colors[i] == colors[j]) == (nxt[i] == nxt[j])
                       for i in range(len(vertices)) for j in range(i+1, len(vertices))) if len(vertices) <= 125 else True
            break
        colors = nxt
        rounds += 1
        assert rounds <= d+1
    by_color = defaultdict(list)
    by_orbit = defaultdict(list)
    a = d - b
    for i, v in enumerate(vertices):
        s = sum(v[j] != 0 for j in range(b, d))
        v_first = sum(v[j] == 0 for j in range(b))
        v_second = sum(v[j] == 1 for j in range(b))
        orbit = (s, v_first, v_second)
        by_color[colors[i]].append(i)
        by_orbit[orbit].append(i)
    classes_cr = {frozenset(group) for group in by_color.values()}
    classes_orbit = {frozenset(group) for group in by_orbit.values()}
    assert classes_cr == classes_orbit, (q, d, b, len(classes_cr), len(classes_orbit))
    expected_count = (a+1) * comb(b+2, 2)
    assert len(classes_cr) == expected_count, (q, d, b, len(classes_cr), expected_count)
    assert rounds <= d+1, (q, d, b, rounds)
    for (s, firsts, seconds), group in by_orbit.items():
        thirds = b - firsts - seconds
        expected_size = comb(a, s) * (q-1)**s * factorial(b)//(factorial(firsts)*factorial(seconds)*factorial(thirds)) * (q-2)**thirds
        assert len(group) == expected_size, (q, d, b, s, firsts, seconds)
    return len(vertices), expected_count, rounds


def main():
    cases = 0
    vertices_total = 0
    max_rounds = 0
    for q, dmax in [(3, 6), (4, 5), (5, 4), (6, 3)]:
        for d in range(1, dmax+1):
            for b in range(1, d+1):
                n, cells, rounds = color_partition(q, d, b)
                print(f'q={q} d={d} landmark_distance={b} vertices={n} stable_cells={cells} rounds={rounds}')
                cases += 1
                vertices_total += n
                max_rounds = max(max_rounds, rounds)
    print(f'PASS cases={cases} aggregate_vertices={vertices_total} max_refinement_rounds={max_rounds}')

if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Exact cubical-boundary and mod-two rank cross-checks for star complexes.

Finite checks corroborate, but do not replace, the homotopy proof.
"""
from collections import defaultdict
from itertools import product


def cubical_cells(arms, colors):
    vertices = [(i,) for i in range(arms + 1)]
    edges = [(0, j) for j in range(1, arms + 1)]
    cells = defaultdict(list)
    for cube in product(vertices + edges, repeat=colors):
        if not set.intersection(*(set(factor) for factor in cube)):
            cells[sum(len(factor) == 2 for factor in cube)].append(cube)
    return cells


def boundary(cube):
    answer = defaultdict(int)
    orientation = 0
    for pos, factor in enumerate(cube):
        if len(factor) == 2:
            before, after = factor
            base = cube[:pos]
            tail = cube[pos+1:]
            answer[base + ((before,),) + tail] -= (-1) ** orientation
            answer[base + ((after,),) + tail] += (-1) ** orientation
            orientation += 1
    return {cell: c for cell, c in answer.items() if c}


def mod2_rank(columns, rows, boundary_function):
    indexes = {cell: index for index, cell in enumerate(rows)}
    pivots = {}
    for col in columns:
        vec = 0
        for face in boundary_function(col):
            vec ^= 1 << indexes[face]
        while vec:
            pivot = vec.bit_length() - 1
            if pivot not in pivots:
                pivots[pivot] = vec
                break
            vec ^= pivots[pivot]
    return len(pivots)


def assert_integral_chain_complex(cells, boundary_function):
    for degree in range(1, max(cells) + 1):
        lower_set = set(cells[degree-1])
        for cell in cells[degree]:
            assert set(boundary_function(cell)) <= lower_set
            if degree >= 2:
                combined = defaultdict(int)
                for face, c in boundary_function(cell).items():
                    for subface, d in boundary_function(face).items():
                        combined[subface] += c * d
                assert all(c == 0 for c in combined.values())


def bettis(cells, boundary_function):
    top = max(cells)
    ranks = {degree: mod2_rank(cells[degree], cells[degree-1], boundary_function)
             for degree in range(1, top + 1)}
    return [len(cells[degree])-ranks.get(degree,0)-ranks.get(degree+1,0)
            for degree in range(top + 1)]


def join_minus_diagonal(arms, colors):
    # A face selects at most one arm label in each of the labelled color parts.
    # The m same-label facets are the only missing top-dimensional simplices.
    cells = defaultdict(list)
    for pattern in product(range(arms + 1), repeat=colors):
        if all(x == 0 for x in pattern):
            continue  # zero denotes an absent color part
        face = tuple((i,x) for i,x in enumerate(pattern) if x)
        if len(face) == colors and len({x for _,x in face}) == 1:
            continue
        cells[len(face)-1].append(face)
    return cells


def simplicial_boundary(face):
    return {face[:j]+face[j+1:]:(-1)**j for j in range(len(face))}


def main():
    cases = 0
    for arms in range(3, 8):
        for colors in range(2, 5):
            expected = (arms - 1)**colors - arms
            cubical = cubical_cells(arms, colors)
            assert_integral_chain_complex(cubical, boundary)
            cb = bettis(cubical, boundary)
            assert cb[0] == 1 and cb[colors-1] == expected
            assert all(x == 0 for j,x in enumerate(cb) if j not in (0,colors-1))
            link = join_minus_diagonal(arms, colors)
            assert_integral_chain_complex(link, simplicial_boundary)
            lb = bettis(link, simplicial_boundary)
            assert lb[0] == 1 and lb[colors-1] == expected
            assert all(x == 0 for j,x in enumerate(lb) if j not in (0,colors-1))
            print('PASS arms=%d colors=%d top_rank=%d cubical=%d join=%d' %
                  (arms, colors, expected, sum(map(len, cubical.values())),
                   sum(map(len, link.values()))))
            cases += 1
    print('PASS: %d matched cubical and independent join cases' % cases)


if __name__ == '__main__':
    main()

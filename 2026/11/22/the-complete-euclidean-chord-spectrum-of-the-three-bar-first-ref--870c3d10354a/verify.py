#!/usr/bin/env python3
"""Recompute an exact finite Euclidean chord census using two constructions.

Run with Python 3 from any directory; reads the adjacent CHORD_SPECTRUM.csv.
All arithmetic, including distance arithmetic, is integer or rational.
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations
from pathlib import Path
import csv

RELATIONS = ((1,2),(2,3),(4,5),(5,6),(7,8),(8,9),(1,4),(4,7))


def topological_extensions():
    predecessors = [0] * 10
    for a,b in RELATIONS:
        predecessors[b] |= (1 << (a-1))
    output = []
    def walk(prefix, seen):
        if len(prefix) == 9:
            output.append(tuple(prefix))
            return
        for label in range(1,10):
            bit = 1 << (label-1)
            if not (seen & bit) and (seen & predecessors[label]) == predecessors[label]:
                walk(prefix + [label], seen | bit)
    walk([], 0)
    return output


def permutation_filter():
    # Deliberately independent of the topological-sort recursion.
    return [p for p in permutations(range(1,10))
            if all(p.index(a) < p.index(b) for a,b in RELATIONS)]


def chord_census(vertices):
    spectrum = Counter()
    degree = Counter()
    for i, p in enumerate(vertices):
        for q in vertices[i+1:]:
            squared_distance = sum((x-y)*(x-y) for x,y in zip(p,q))
            spectrum[squared_distance] += 1
            if squared_distance == 152:
                degree[p] += 1
                degree[q] += 1
    return spectrum, degree


def main():
    x = topological_extensions()
    y = permutation_filter()
    assert len(x) == len(y) == 280
    assert len(set(x)) == 280 and set(x) == set(y)
    sx, dx = chord_census(x)
    sy, dy = chord_census(y)
    assert sx == sy and dx == dy
    with (Path(__file__).resolve().parent / "CHORD_SPECTRUM.csv").open(newline="",encoding="utf-8") as f:
        rows = list(csv.DictReader(f))
    expected = {int(t["squared_distance"]): int(t["unordered_pairs"]) for t in rows}
    assert len(rows) == len(expected) == 75 and dict(sx) == expected
    assert set(sx) == set(range(2,148,2)) | {150,152}
    assert sum(sx.values()) == 39060
    assert sum(s*c for s,c in sx.items()) == 2737080
    assert Fraction(sum(s*c for s,c in sx.items()),39060) == Fraction(15206,217)
    assert max(sx) == 152 and sx[152] == 45 and sx[150] == 15
    assert len(dx) == 90 and set(dx.values()) == {1}
    assert len(x)-len(dx) == 190
    print("BARCODE_CHORD_PASS vertices=280 pairs=39060 shells=75 diameter_sq=152 diameter_pairs=45")

if __name__ == "__main__":
    main()

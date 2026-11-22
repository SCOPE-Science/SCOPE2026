#!/usr/bin/env python3
"""Exact finite-distance certificate for the canonical Constr(3,4) realization.
Run in the same directory as CHORD_SPECTRUM.csv. Standard library only.
The all-orders vertex construction follows the braid-fan refinement of the
Bottman--Poliakova generalized-permutahedron realization.
"""
import csv
from collections import Counter
from itertools import permutations
from pathlib import Path

def blocks(length, selected):
    out = []
    pos = 0
    for edge in range(length - 1):
        if edge not in selected:
            out.append((pos, edge))
            pos = edge + 1
    out.append((pos, length - 1))
    return out

def point(order):
    merged = {"m": set(), "l": set()}
    coordinates = {}
    for axis, edge in order:
        size = {"m": 3, "l": 4}[axis]
        opposite = "l" if axis == "m" else "m"
        opposite_size = {"m": 4, "l": 3}[axis]
        left = right = None
        for lo, hi in blocks(size, merged[axis]):
            if lo <= edge <= hi: left = hi - lo + 1
            if lo <= edge + 1 <= hi: right = hi - lo + 1
        assert left is not None and right is not None
        thickness = 1 + sum((hi-lo+1)*(hi-lo)//2 for lo,hi in blocks(opposite_size,merged[opposite]))
        coordinates[(axis, edge)] = left * right * thickness
        merged[axis].add(edge)
    return tuple(coordinates[('m',k)] for k in range(2)) + tuple(coordinates[('l',k)] for k in range(3))

def main():
    events = [('m',0),('m',1),('l',0),('l',1),('l',2)]
    seq = list(permutations(events))
    assert len(seq) == 120
    vertices = sorted(set(point(o) for o in seq))
    assert len(vertices) == 108
    assert all(len(v)==5 and sum(v)==27 for v in vertices)
    dist = Counter()
    maximizing = []
    for i, a in enumerate(vertices):
        for b in vertices[i+1:]:
            squared = sum((u-v)**2 for u,v in zip(a,b))
            dist[squared] += 1
            if squared == 430:
                maximizing.append((a,b))
    with open(Path(__file__).with_name('CHORD_SPECTRUM.csv'),newline='',encoding='utf-8') as fh:
        rows = list(csv.DictReader(fh))
    expected = {int(row['squared_distance']):int(row['unordered_pairs']) for row in rows}
    assert len(rows)==174 and len(expected)==174 and expected==dist
    assert sum(dist.values())==108*107//2==5778
    assert min(dist)==2 and dist[2]==67
    assert max(dist)==430 and dist[430]==4
    assert dist[424]==4 and all(d<=424 for d in dist if d!=430)
    degree = Counter()
    for a,b in maximizing:
        degree[a] += 1; degree[b] += 1
    assert sorted(degree.values())==[1,1,1,1,2,2]
    assert len(degree)==6 and len(maximizing)==4
    # A 2-P_3 diameter graph, with 102 isolated vertices.
    assert len([v for v in degree if degree[v]==2])==2
    assert not any(a in degree and degree[a]==2 and b in degree and degree[b]==2 for a,b in maximizing)
    print('CONSTRAINAHEDRON_CHORD_PASS orders=120 vertices=108 pairs=5778 shells=174 diameter_squared=430 diametral_pairs=4')

if __name__=='__main__':main()

#!/usr/bin/env python3
"""Finite independent homology checks for two edge-faulted wheel families.

These are corroborative computations. The all-n homotopy proof uses
simplicial pushouts and the independence-complex recursion for paths.
"""
from collections import defaultdict
import json


def forest_faces(n, fault):
    """Return nonempty induced-forest faces as vertex bitmasks.

    Rim vertices are 0,...,n-1; hub is n. Fault is 'spoke' (hub--0)
    or 'rim' (0--(n-1)).
    """
    assert n >= 5 and fault in ('spoke', 'rim')
    edges = [(i, (i + 1) % n) for i in range(n)
             if not (fault == 'rim' and i == n - 1)]
    edges += [(n, i) for i in range(n)
              if not (fault == 'spoke' and i == 0)]
    faces = []
    for mask in range(1, 1 << (n + 1)):
        parent = list(range(n + 1))
        def root(a):
            while a != parent[a]:
                a = parent[a]
            return a
        acyclic = True
        for a, b in edges:
            if not ((mask >> a) & 1 and (mask >> b) & 1):
                continue
            aa, bb = root(a), root(b)
            if aa == bb:
                acyclic = False
                break
            parent[aa] = bb
        if acyclic:
            faces.append(mask)
    return faces


def rank_binary(columns):
    pivots = {}
    for value in columns:
        while value:
            lead = value.bit_length() - 1
            if lead in pivots:
                value ^= pivots[lead]
            else:
                pivots[lead] = value
                break
    return len(pivots)


def betti_binary(faces):
    levels = defaultdict(list)
    for face in faces:
        levels[face.bit_count() - 1].append(face)
    ranks = defaultdict(int)
    for dim in range(1, max(levels) + 1):
        locations = {mask: index for index, mask in enumerate(levels[dim-1])}
        columns = []
        for face in levels[dim]:
            col = 0
            remaining = face
            while remaining:
                bit = remaining & -remaining
                remaining ^= bit
                col ^= 1 << locations[face ^ bit]
            columns.append(col)
        ranks[dim] = rank_binary(columns)
    homology = [len(levels[d]) - ranks[d] - ranks[d+1]
                for d in range(max(levels)+1)]
    return {str(i): value for i, value in enumerate(homology) if value}


def predicted(n, fault):
    expected = {0:1}
    if fault == 'spoke':
        expected[n-2] = 1
        if n % 3 != 0:
            dimension = (n+2) // 3
            expected[dimension] = expected.get(dimension, 0) + 1
    else:
        if n % 3 == 0:
            expected[n // 3] = 1
        elif n % 3 == 2:
            expected[(n+1) // 3] = 1
    return {str(k):v for k,v in sorted(expected.items())}


def main():
    reports=[]
    for n in range(5, 13):
        for fault in ('spoke', 'rim'):
            f=forest_faces(n,fault)
            actual=betti_binary(f)
            wanted=predicted(n,fault)
            assert actual == wanted, (n,fault,actual,wanted)
            reports.append({'rim_vertices':n,'fault':fault,
                            'nonempty_faces':len(f),'betti_mod2':actual,
                            'status':'PASS'})
    print(json.dumps({'checks':len(reports),'status':'PASS',
                      'results':reports},separators=(',',':')))

if __name__=='__main__':
    main()

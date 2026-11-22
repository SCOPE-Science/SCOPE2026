#!/usr/bin/env python3
"""Independent finite-field persistence test for dimension-delayed cone filtrations.

Run: python3 verify_cone.py
The exact theorem for arbitrary cones is proved separately by a filtered integral
basis change; computations here test implementations and boundary conventions.
"""
import itertools
import random
from collections import Counter


def base_faces(n, maximal):
    out = set()
    for face in maximal:
        for k in range(1, len(face) + 1):
            out.update(itertools.combinations(sorted(face), k))
    out.update((i,) for i in range(1, n))
    return sorted(out)


def filtered_complex(n, base, values, delays):
    cells = [(0,)] + list(base) + [tuple(sorted((0,) + s)) for s in base]
    assert len(cells) == len(set(cells))
    filtration = lambda s: max(values[i] for i in s) + delays[len(s)-1]
    return sorted(cells, key=lambda s: (filtration(s), len(s), s)), filtration


def field_barcode(cells, filtration, prime):
    loc = {s: i for i, s in enumerate(cells)}
    columns = {}
    births = []
    pairs = []
    for j, cell in enumerate(cells):
        col = {}
        if len(cell) > 1:
            for k in range(len(cell)):
                face = cell[:k] + cell[k+1:]
                i = loc[face]
                assert i < j
                col[i] = ((-1)**k) % prime
        while col:
            low = max(col)
            if low not in columns:
                break
            basis = columns[low]
            coefficient = col[low] * pow(basis[low], -1, prime) % prime
            for i, c in basis.items():
                value = (col.get(i, 0) - coefficient*c) % prime
                if value:
                    col[i] = value
                else:
                    col.pop(i, None)
        if col:
            low = max(col)
            columns[low] = col
            pairs.append((len(cells[low])-1, filtration(cells[low]), filtration(cell)))
        else:
            births.append(j)
    ended = set(columns)
    essentials = [(len(cells[i])-1, filtration(cells[i]), 'inf') for i in births if i not in ended]
    return Counter(pairs + essentials)


def predicted(base, values, delays):
    res = [(0, values[0] + delays[0], 'inf')]
    for s in base:
        k = len(s)-1
        a = max(values[i] for i in s)
        res.append((k, a + delays[k], a + delays[k+1]))
    return Counter(res)


def run():
    rng = random.Random(1729)
    tests = 0
    for n in range(2, 9):
        for t in range(45):
            vertices = list(range(1,n))
            maximal = []
            for sz in range(1, min(4,n-1)+1):
                for s in itertools.combinations(vertices, sz):
                    if rng.random() < (0.35 if sz == 1 else 0.19):
                        maximal.append(s)
            if t % 11 == 0:
                maximal.append(tuple(vertices))
            base = base_faces(n,maximal)
            values = [rng.randint(0,2)]
            values.extend(values[0]+rng.randint(0,9) for _ in vertices)
            delays = [0]
            delays.extend(delays[-1] + rng.randint(1,4) for _ in range(n))
            cells, filtration = filtered_complex(n,base,values,delays)
            target = predicted(base,values,delays)
            for prime in (2,3,5):
                got = field_barcode(cells,filtration,prime)
                assert got == target, (n,t,prime,base,values,delays,got-target,target-got)
                tests += 1
    assert tests == 945
    print('PASS: 945 complete finite-field barcodes, primes 2, 3, 5; random weighted cones 2..8 vertices')
    print('PASS: arbitrary tie patterns, nonuniform strictly increasing dimension delays, full simplices included')
    print('Finite testing is not a proof; integral proof is the filtered triangular chain basis.')

if __name__ == '__main__':
    run()

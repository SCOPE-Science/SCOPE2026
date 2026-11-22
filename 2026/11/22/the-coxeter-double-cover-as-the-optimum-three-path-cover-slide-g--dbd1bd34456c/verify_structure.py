#!/usr/bin/env python3
"""Exact Fano-plane proof certificate for 3-path-cover slide reconfiguration."""
from itertools import combinations
from collections import Counter, deque

POINTS = frozenset(range(7))
LINES = tuple(frozenset(((i + j) % 7 for j in (0, 1, 3))) for i in range(7))
assert len(set(LINES)) == 7
assert all(sum({p, q} <= line for line in LINES) == 1 for p, q in combinations(POINTS, 2))
EDGES = tuple((p, 7 + i) for i, line in enumerate(LINES) for p in line)
assert len(EDGES) == 21

def independent_of_three_path(mask):
    for center in range(14):
        if not (mask >> center & 1):
            continue
        if sum(mask >> (other if center >= 7 else other + 7) & 1
               for other in (LINES[center - 7] if center >= 7 else
                             [i for i, line in enumerate(LINES) if center in line])) > 1:
            return False
    return True

def mask_of(points, lines):
    return sum(1 << p for p in points) | sum(1 << (7 + i) for i in lines)

TRIANGLES = sorted(tuple(T) for T in combinations(range(7), 3) if frozenset(T) not in LINES)
assert len(TRIANGLES) == 28
A = {}  # selected three Fano points and the four non-side Fano lines
B = {}  # their seven-vertex complements
for T in TRIANGLES:
    pts = set(T)
    non_sides = [i for i, line in enumerate(LINES) if len(line & pts) <= 1]
    assert len(non_sides) == 4
    A[T] = mask_of(pts, non_sides)
    B[T] = ((1 << 14) - 1) ^ A[T]

VALID = set(A.values()) | set(B.values()) | {(1 << 7) - 1, ((1 << 14) - 1) ^ ((1 << 7) - 1)}
assert len(VALID) == 58
assert all(v.bit_count() == 7 and independent_of_three_path(v) for v in VALID)
assert all(not independent_of_three_path(sum(1 << i for i in X)) for X in combinations(range(14), 8))
assert {sum(1 << i for i in X) for X in combinations(range(14), 7)
        if independent_of_three_path(sum(1 << i for i in X))} == VALID

def exchange_graph(sliding):
    graph = {v: set() for v in VALID}
    for v in VALID:
        if sliding:
            replacements = ((1 << p, 1 << q) for p, q in EDGES)
        else:
            replacements = ((1 << p, 1 << q) for p in range(14) for q in range(p + 1, 14))
        for pa, qa in replacements:
            if bool(v & pa) == bool(v & qa):
                continue
            u = v ^ pa ^ qa
            if u in VALID:
                graph[v].add(u)
    return graph

TS = exchange_graph(True)
TJ = exchange_graph(False)
assert TS == TJ
assert sum(map(len, TS.values())) // 2 == 84
assert Counter(map(len, TS.values())) == {3: 56, 0: 2}
assert all((B[U] in TS[A[T]]) == (set(T).isdisjoint(U)) for T in TRIANGLES for U in TRIANGLES)

# The Coxeter graph is the disjointness graph on the 28 nonline triples.
COX = {T: {U for U in TRIANGLES if set(T).isdisjoint(U)} for T in TRIANGLES}
assert Counter(map(len, COX.values())) == {3: 28}
assert all(COX[T] == {U for U in TRIANGLES if B[U] in TS[A[T]]} for T in TRIANGLES)

def shells(graph, start):
    distance = {start: 0}
    pending = deque([start])
    while pending:
        v = pending.popleft()
        for u in graph[v]:
            if u not in distance:
                distance[u] = distance[v] + 1
                pending.append(u)
    return distance, tuple(Counter(distance.values())[i] for i in range(max(distance.values()) + 1))

THE_SHELLS = (1, 3, 6, 12, 18, 12, 3, 1)
for T in TRIANGLES:
    for v in (A[T], B[T]):
        distance, sh = shells(TS, v)
        assert len(distance) == 56 and sh == THE_SHELLS
assert all(len(TS[v]) == 0 for v in VALID - set(A.values()) - set(B.values()))
print('STRUCTURAL PASS: max dissociation=7; 58 optimal covers; 2 isolated + Coxeter x K2; 84 edges')
print('All 56 mobile states have distance shells:', THE_SHELLS)
print('TS and TJ adjacency agree exactly; mobile radius=diameter=7')

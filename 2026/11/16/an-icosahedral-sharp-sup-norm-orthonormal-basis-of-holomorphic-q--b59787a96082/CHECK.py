#!/usr/bin/env python3
"""Finite numerical cross-check for the explicit icosahedral quadratic basis.

This is a reproducibility check, not a proof of exact identities.
"""
import cmath
import math

phi = (1 + math.sqrt(5)) / 2
size = math.sqrt(1 + phi * phi)
raw = [(0,1,phi),(0,1,-phi),(1,phi,0),(1,-phi,0),(phi,0,1),(phi,0,-1)]
vec = [[x / size for x in row] for row in raw]
phase = (-7 + 1j * math.sqrt(15)) / 8
assert abs(abs(phase) - 1) < 1e-13

def inner(x, y):
    return sum(a*b.conjugate() for a,b in zip(x,y))

def mat(v):
    return [[(1 if a == b else 0) + (phase-1) * v[a] * v[b]
             for b in range(3)] for a in range(3)]

basis = [mat(v) for v in vec]
checks = 0
for j, v in enumerate(vec):
    assert abs(inner(v,v)-1)<1e-12
    checks += 1
    for k,w in enumerate(vec):
        assert abs(abs(inner(v,w))**2 - (1 if j==k else .2))<1e-12
        checks += 1
    u = basis[j]
    for a in range(3):
        for b in range(3):
            assert abs(sum(u[a][t]*u[b][t].conjugate() for t in range(3))-(1 if a==b else 0)) < 1e-12
            assert abs(u[a][b]-u[b][a]) < 1e-12
            checks += 2
for j,u in enumerate(basis):
    for k,w in enumerate(basis):
        gram = sum(u[a][b]*w[a][b].conjugate() for a in range(3) for b in range(3))
        assert abs(gram - (3 if j==k else 0)) < 1e-12
        assert abs(gram/3 - (1 if j==k else 0)) < 1e-12
        checks += 2
print('PASS: %d finite numerical comparisons; exact proof in RESULT.md' % checks)

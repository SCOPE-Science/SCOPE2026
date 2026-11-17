#!/usr/bin/env python3
"""Exact modular-rank checks for ridge faces of rectangular matching polytopes.

All geometric inputs are 0/1 vertices and integer facet normals; no external
packages are required. The proof for all dimensions is given in RESULT.md.
"""
from itertools import combinations
from fractions import Fraction
from math import comb

PRIME = 1000003


def vertices(p, q):
    def go(i, used, v):
        if i == p:
            yield tuple(v)
            return
        yield from go(i + 1, used, v)
        for j in range(q):
            if not (used >> j) & 1:
                v[i*q+j] = 1
                yield from go(i + 1, used | (1 << j), v)
                v[i*q+j] = 0
    return list(go(0, 0, [0]*(p*q)))


def facets(p, q):
    d = p*q
    fs = []
    for i in range(p):
        for j in range(q):
            v = [0]*d
            v[i*q+j] = -1
            fs.append((('Z', i, j), tuple(v), 0))
    for i in range(p):
        v = [0]*d
        for j in range(q):
            v[i*q+j] = 1
        fs.append((('R', i), tuple(v), 1))
    for j in range(q):
        v = [0]*d
        for i in range(p):
            v[i*q+j] = 1
        fs.append((('C', j), tuple(v), 1))
    return fs


def dot(x, y):
    return sum(a*b for a, b in zip(x, y))


def dimension_mod_prime(vertices_on_face):
    if not vertices_on_face:
        return -1
    base = vertices_on_face[0]
    pivots = {}
    for v in vertices_on_face[1:]:
        w = [(a-b) % PRIME for a, b in zip(v, base)]
        for pivot in sorted(pivots):
            coef = w[pivot]
            if coef:
                u = pivots[pivot]
                w = [(a-coef*b) % PRIME for a, b in zip(w, u)]
        first = next((k for k, a in enumerate(w) if a), None)
        if first is not None:
            inv = pow(w[first], -1, PRIME)
            pivots[first] = [(a*inv) % PRIME for a in w]
    return len(pivots)


def nonridge(f, g, p, q):
    a,b=f[0],g[0]
    if a == 'Z' and b == 'Z':
        return False
    if a == 'Z' and b == 'R':
        return f[1] == g[1] and q == 2
    if a == 'R' and b == 'Z':
        return g[1] == f[1] and q == 2
    if a == 'Z' and b == 'C':
        return f[2] == g[1] and p == 2
    if a == 'C' and b == 'Z':
        return g[2] == f[1] and p == 2
    if a == 'R' and b == 'R':
        return q == 2
    if a == 'C' and b == 'C':
        return p == 2
    return False


def category(f, g, p, q):
    a,b=f[0],g[0]
    if {a,b} == {'Z','R'}:
        z,r=(f,g) if a=='Z' else (g,f)
        if z[1] == r[1]:
            return 'acute_row'
    if {a,b} == {'Z','C'}:
        z,c=(f,g) if a=='Z' else (g,f)
        if z[2] == c[1]:
            return 'acute_column'
    if {a,b} == {'R','C'}:
        return 'obtuse'
    return 'right'


def verify(p, q):
    verts = vertices(p,q)
    expected_verts = sum(comb(p,k)*comb(q,k)*__import__('math').factorial(k) for k in range(min(p,q)+1))
    assert len(verts) == expected_verts
    ff=facets(p,q)
    F=len(ff)
    assert F == p*q+p+q
    counts = {'acute_row':0,'acute_column':0,'obtuse':0,'right':0}
    blocked=0
    for ((f,a,ba),(g,b,bb)) in combinations(ff,2):
        selected = [v for v in verts if dot(v,a) == ba and dot(v,b) == bb]
        dim = dimension_mod_prime(selected)
        excluded = nonridge(f,g,p,q)
        if excluded:
            assert dim < p*q-2, (p,q,f,g,dim)
            blocked+=1
            continue
        assert dim == p*q-2, (p,q,f,g,dim)
        kind = category(f,g,p,q)
        counts[kind] += 1
        raw = dot(a,b)
        if kind=='acute_row':
            assert raw == -1 and Fraction(raw*raw,dot(a,a)*dot(b,b)) == Fraction(1,q)
        elif kind=='acute_column':
            assert raw == -1 and Fraction(raw*raw,dot(a,a)*dot(b,b)) == Fraction(1,p)
        elif kind=='obtuse':
            assert raw == 1 and Fraction(raw*raw,dot(a,a)*dot(b,b)) == Fraction(1,p*q)
        else:
            assert raw == 0
    b_expected = (p*q if q==2 else 0) + (p*q if p==2 else 0) + (comb(p,2) if q==2 else 0) + (comb(q,2) if p==2 else 0)
    assert blocked == b_expected
    assert counts['acute_row'] == (p*q if q>=3 else 0)
    assert counts['acute_column'] == (p*q if p>=3 else 0)
    assert counts['obtuse'] == p*q
    assert sum(counts.values()) + blocked == comb(F,2)
    return f'{p}x{q}: vertices={len(verts)} facets={F} ridges={sum(counts.values())} blocked={blocked} classes={counts}'

if __name__ == '__main__':
    cases=[(2,2),(2,3),(2,4),(3,2),(3,3),(3,4),(4,3),(4,4)]
    for p,q in cases:
        print(verify(p,q))
    print('MATCHING_RIDGE_EXACT_PASS cases='+str(len(cases)))

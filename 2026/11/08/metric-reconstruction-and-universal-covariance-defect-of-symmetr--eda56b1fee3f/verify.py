#!/usr/bin/env python3
"""Exact finite checks for canonical boundary-column geometry.

No numerical tolerance or external packages are used. Example complexes include
simplex boundaries, cross-polytope boundaries, stacked spheres, and two
14-facet triangulated spheres cited in the motivating literature.
"""
from collections import defaultdict, deque
from fractions import Fraction
from itertools import combinations, product


def simplex_boundary(d):
    vertices = range(d + 2)
    return [tuple(v for v in vertices if v != i) for i in vertices]


def crosspolytope_boundary(d):
    return [tuple(2*i + s[i] for i in range(d+1))
            for s in product((0,1), repeat=d+1)]


def stacked_sphere(extra):
    fs = simplex_boundary(2)
    for j in range(extra):
        f = fs.pop(j % len(fs))
        vertex = 4+j
        for i in range(3):
            fs.append(tuple(sorted(tuple(x for x in f if x != f[i]) + (vertex,))))
    return fs


def paper_examples():
    words = [
        '123 125 136 159 168 189 234 245 347 367 459 478 489 678',
        '123 124 135 145 237 248 279 289 356 367 456 467 478 789'
    ]
    return [[tuple(int(c) for c in w) for w in line.split()] for line in words]


def check(facets):
    facets = [tuple(sorted(f)) for f in facets]
    assert len(set(facets)) == len(facets)
    F = len(facets)
    k = len(facets[0])
    assert k >= 2 and all(len(f) == k for f in facets)
    ridges = defaultdict(list)
    for fi, facet in enumerate(facets):
        for pos in range(k):
            ridge = facet[:pos] + facet[pos+1:]
            ridges[ridge].append((fi, (-1)**pos))
    assert all(len(v) == 2 for v in ridges.values())
    eps = {0: 1}
    near = defaultdict(list)
    for inc in ridges.values():
        (u, s), (v, t) = inc
        near[u].append((v, -s*t))
        near[v].append((u, -s*t))
    q = deque([0])
    while q:
        u = q.popleft()
        for v, ratio in near[u]:
            sign = eps[u]*ratio
            if v not in eps: eps[v] = sign; q.append(v)
            else: assert eps[v] == sign
    assert len(eps) == F
    rows = []
    A = [[0]*F for _ in range(F)]
    for inc in ridges.values():
        (u,s),(v,t)=inc
        assert u != v
        assert A[u][v]==0
        A[u][v]=A[v][u]=1
        row = [0]*F
        row[u] = s*eps[u]
        row[v] = t*eps[v]
        assert row[u] == -row[v]
        rows.append(row)
    assert all(sum(A[i])==k for i in range(F))
    # B^T B via explicitly summing the oriented rows.
    Gram = [[sum(row[i]*row[j] for row in rows) for j in range(F)]
            for i in range(F)]
    assert all(Gram[i][j] == (k if i==j else -A[i][j])
               for i in range(F) for j in range(F))
    assert all(sum(Gram[i]) == 0 for i in range(F))
    # Projector rank is F-1, since a connected incidence matrix has 1D kernel.
    # All columns are vertices: distinct vectors of the common norm sqrt(k).
    columns = [tuple(row[j] for row in rows) for j in range(F)]
    assert len(set(columns+ [tuple(-x for x in v) for v in columns])) == 2*F
    assert all(sum(x*x for x in v)==k for v in columns)
    # All pairwise squared distances between antipodal vertex classes recover A.
    for i,j in combinations(range(F),2):
        small = min(sum((x-y)**2 for x,y in zip(columns[i],columns[j])),
                    sum((x+y)**2 for x,y in zip(columns[i],columns[j])))
        assert small == 2*k-2*A[i][j]
    tr_C = Fraction(sum(Gram[i][i] for i in range(F)),F)
    tr_C2 = Fraction(sum(Gram[i][j]**2 for i in range(F) for j in range(F)),F*F)
    assert tr_C == k
    assert tr_C2 == Fraction(k*(k+1),F)
    defect = tr_C2 - tr_C**2/Fraction(F-1)
    assert defect == Fraction(k*(F-k-1),F*(F-1))
    coefficient = defect/Fraction(F-1)/Fraction(k,F-1)**2
    assert coefficient == Fraction(F-k-1,F*k)
    assert (defect == 0) == (F==k+1)
    tri = sum(A[i][j] and A[j][h] and A[h][i]
              for i,j,h in combinations(range(F),3))
    return (k-1,F,len(rows),defect,coefficient,tri)


def main():
    examples=[]
    for d in range(1,6): examples.append((f'simplex_{d}',simplex_boundary(d)))
    for d in range(1,5): examples.append((f'crosspolytope_{d}',crosspolytope_boundary(d)))
    for j in range(1,9): examples.append((f'stacked_{j}',stacked_sphere(j)))
    for j,facets in enumerate(paper_examples(),1): examples.append((f'paper_sphere_{j}',facets))
    output=[]
    for label,faces in examples:
        val = check(faces)
        output.append((label,val))
        print(label, 'd,F,R,defect,CV2,triangles=', val)
    a=output[-2][1]
    b=output[-1][1]
    assert a[:5] == b[:5] and a[-1] != b[-1]
    assert {a[-1],b[-1]} == {0,3} or {a[-1],b[-1]} == {0,2} or (a[-1] == 0 and b[-1] > 0)
    print('PASS',len(examples),'oriented complexes; distinct 14-facet dual-graph triangle spectra')

if __name__ == '__main__': main()

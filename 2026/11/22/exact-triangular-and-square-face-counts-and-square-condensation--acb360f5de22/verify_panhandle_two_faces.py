"""Exact combinatorial checks for two-face area counts of panhandle matroid polytopes.

Only standard-library rational/integer arithmetic is used. The face search
is independent of the closed formula: it enumerates supporting-coordinate
faces, then determines their affine ranks by rational Gaussian elimination.
"""
from itertools import combinations
from math import comb
from fractions import Fraction


def C(n,k):
    return comb(n,k) if 0 <= k <= n else 0


def rank(matrix):
    m = [list(map(Fraction, row)) for row in matrix]
    if not m:
        return 0
    nr, nc, col, rk = len(m), len(m[0]), 0, 0
    while col < nc and rk < nr:
        pivot = next((j for j in range(rk,nr) if m[j][col]),None)
        if pivot is None:
            col += 1
            continue
        m[rk],m[pivot] = m[pivot],m[rk]
        a=m[rk][col]
        m[rk]=[v/a for v in m[rk]]
        for j in range(nr):
            if j != rk:
                a=m[j][col]
                if a:
                    m[j]=[b-a*c for b,c in zip(m[j],m[rk])]
        rk += 1
        col += 1
    return rk


def predicted(p,t,r):
    triangles=(C(p,r-1)*C(p+t-r+1,3)
      + C(p,3)*C(p-3,r-2)
      + t*C(p,2)*C(p-2,r-2)
      + t*C(p,3)*C(p-2,r-2))
    squares=C(p,2)*C(t,2)*C(p-2,r-2)
    return triangles,squares


def enumerated(p,t,r):
    n=p+t
    vertices=[tuple(int(j in b) for j in range(n))
              for b in combinations(range(n),r)
              if sum(j >= p for j in b) <= 1]
    boundaries=[]
    for i in range(n):
        for val in (0,1):
            boundaries.append(frozenset(j for j,v in enumerate(vertices)
                                         if v[i] == val))
    boundaries.append(frozenset(j for j,v in enumerate(vertices)
                                 if sum(v[p:]) == 1))
    all_vertices=frozenset(range(len(vertices)))
    faces={all_vertices}
    queue=[all_vertices]
    while queue:
        current=queue.pop()
        for bdry in boundaries:
            child=current & bdry
            if len(child) >= 3 and child not in faces:
                faces.add(child)
                queue.append(child)
    triangles=squares=0
    for face in faces:
        if len(face)<3:
            continue
        subset=[vertices[j] for j in sorted(face)]
        if rank([[u-v for u,v in zip(row,subset[0])]
                 for row in subset[1:]]) != 2:
            continue
        if len(subset) == 3:
            triangles += 1
        elif len(subset) == 4:
            squares += 1
        else:
            raise AssertionError(('non-triangle-square',p,t,r,face))
    return triangles,squares


def validate():
    cases=[(2,2,2),(3,2,2),(3,3,2),(3,3,3),
           (4,2,2),(4,3,2),(4,3,3),(4,3,4)]
    for p,t,r in cases:
        observed=enumerated(p,t,r)
        expected=predicted(p,t,r)
        assert observed == expected,(p,t,r,observed,expected)
    # Also verify the Vandermonde and Pascal reductions exactly.
    for p in range(2,11):
        for t in range(2,9):
            for r in range(2,p+1):
                a=sum(C(p,i)*C(t,3-i)*C(p-i,r-1) for i in range(4))
                assert a==C(p,r-1)*C(p+t-r+1,3)
                b=C(p,3)*(C(p-3,r-2)+C(p-3,r-3))
                assert b==C(p,3)*C(p-2,r-2)
    print('PANHANDLE_TWO_FACE_EXACT_PASS cases=%d algebraic_parameter_checks=%d' %
          (len(cases),sum((p-1)*7 for p in range(2,11))))


if __name__ == '__main__':
    validate()

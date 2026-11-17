"""Independent finite checks of exact face enumeration for bipartite symmetric edge polytopes.

Requires NumPy, SciPy, and SymPy. Executable with python verify_bipartite_faces.py.
The all-parameter theorem is proved in the accompanying text; these are finite tests.
"""
from math import comb
from itertools import combinations
import numpy as np
from scipy.spatial import ConvexHull
from sympy import Poly, cancel, symbols

z = symbols('z')

def closed_formula(p, q):
    U = lambda r: (1 + z)**r - 1
    T = lambda r: (1 + 2*z)**r - 2*(1 + z)**r + 1
    F = 2*U(p)*U(q)/z**2 + T(p)*T(q)/z**3 + z**(p-2)*T(q) + z**(q-2)*T(p)
    coefficients = [int(c) for c in reversed(Poly(cancel(F), z).all_coeffs())]
    return coefficients

def independent_faces(p, q):
    n = p + q
    points = []
    for i in range(p):
        for j in range(p, n):
            root = np.zeros(n, dtype=float)
            root[i], root[j] = 1, -1
            points.extend([root[:-1], -root[:-1]])
    points = np.asarray(points)
    hull = ConvexHull(points)
    supporting_facets = set()
    for hyperplane in hull.equations:
        a, b = hyperplane[:-1], hyperplane[-1]
        vertices = frozenset(i for i, v in enumerate(points)
                             if abs(np.dot(a, v) + b) < 1e-7)
        supporting_facets.add(vertices)
    faces = {frozenset(range(len(points)))}
    for facet in supporting_facets:
        faces.update(face.intersection(facet) for face in tuple(faces))
    faces.discard(frozenset())
    by_dim = [0] * n
    triangles = squares = 0
    for f in faces:
        subset = points[list(f)]
        dimension = np.linalg.matrix_rank(subset[1:] - subset[0], tol=1e-7)
        by_dim[dimension] += 1
        if dimension == 2:
            assert len(f) in (3, 4), (p, q, f)
            triangles += len(f) == 3
            squares += len(f) == 4
    assert by_dim[-1] == 1
    return by_dim[:-1], triangles, squares

def two_face_spectrum(p, q):
    C = lambda a,b: comb(a,b) if 0 <= b <= a else 0
    triangles = (2*(p*C(q,3) + q*C(p,3)) +
                 12*(C(p,2)*C(q,3) + C(p,3)*C(q,2)))
    squares = (2*C(p,2)*C(q,2)
               + (q*(q-1) if p == 2 else 0)
               + (p*(p-1) if q == 2 else 0))
    return triangles, squares

if __name__ == '__main__':
    cases = [(2,2),(2,3),(2,4),(2,5),(3,3),(3,4),(3,5),(4,4)]
    checks = 0
    for p,q in cases:
        observed, tri, sq = independent_faces(p,q)
        predicted = closed_formula(p,q)
        assert observed == predicted, (p,q,observed,predicted)
        assert observed[0] == 2*p*q
        assert observed[-1] == 2**p + 2**q - 2
        assert (tri,sq) == two_face_spectrum(p,q)
        assert tri + sq == observed[2]
        checks += 4 + len(observed)
        print(f'K_{{{p},{q}}}: f={observed}; triangles={tri}; quadrilaterals={sq}',flush=True)
    print(f'PASS: {checks} independent whole-face and two-face checks across {len(cases)} instances')

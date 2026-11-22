#!/usr/bin/env python3
"""Exact checks supporting quadratic uniqueness for Archimedean vertex orbits.

Requires Python and SymPy. Mathematical proof is in RESULT.md.
The six sampled octahedral vectors are examples of orbit types, not a
replacement for the full orbit classification in the proof.
"""
from itertools import permutations, product
from sympy import Matrix, Rational, sqrt, simplify


def evaluation(vertices):
    return Matrix([[1, x, y, z, x*x, y*y, z*z, x*y, y*z, z*x]
                   for x, y, z in vertices])


def truncated_tetrahedron():
    return sorted({tuple(t*s for t, s in zip(p, signs))
                   for p in set(permutations((3, 1, 1)))
                   for signs in product((-1, 1), repeat=3)
                   if signs[0]*signs[1]*signs[2] == 1})


def parity(p):
    return (-1)**sum(p[i] > p[j] for i in range(3) for j in range(i+1, 3))


def octahedral_orbit(v):
    return sorted({tuple(v[p[i]]*s[i] for i in range(3))
                   for p in permutations(range(3))
                   for s in product((-1,1), repeat=3)
                   if parity(p)*s[0]*s[1]*s[2] == 1})


def icosahedron():
    phi = (1 + sqrt(5))/2
    raw = []
    for a,b in product((-1,1), repeat=2):
        raw.extend(((0,a,b*phi),(a,b*phi,0),(a*phi,0,b)))
    return raw


def main():
    v = truncated_tetrahedron()
    assert len(v) == 12
    m = evaluation(v)
    assert m.rank() == 9
    kernel = m.nullspace()
    assert len(kernel) == 1
    # Sphere: coordinates have radius squared 11.
    assert (m*Matrix([-11,0,0,0,1,1,1,0,0,0])).is_zero_matrix
    print('truncated tetrahedron: 12 vertices, rank nine, only spherical quadric')

    for v in ((1,1,0), (0,1,2), (1,1,2),
              (1,1,3), (1,2,3), (1,2,4)):
        orbit = octahedral_orbit(v)
        assert len(orbit) >= 12
        assert evaluation(orbit).rank() == 9
        print('octahedral representative', v, 'size',len(orbit), 'rank nine')
    for v, size, rank in [((1,1,1),8,7), ((1,0,0),6,6)]:
        orbit = octahedral_orbit(v)
        assert len(orbit) == size
        assert evaluation(orbit).rank() == rank
        print('octahedral boundary example',v,'size',size,'rank',rank)

    # Proper octahedral rotation classes: 1, order-4, face-axis half-turn,
    # order-3, edge-axis half-turn.  Character orthogonality is exact.
    octweights=(1,6,3,8,6)
    octchars=((3,1,-1,0,-1),(2,0,2,-1,0),(3,-1,-1,0,1))
    for i,a in enumerate(octchars):
        for j,b in enumerate(octchars):
            value=Rational(1,24)*sum(w*x*y for w,x,y in zip(octweights,a,b))
            assert value == (1 if i==j else 0)
    print('octahedral H1/E2/T2 representations: irreducible and pairwise distinct')

    phi = (1+sqrt(5))/2
    chi1 = (3,-1,0,phi,1-phi)
    chi2 = (5,1,-1,0,0)
    weights=(1,15,20,12,12)
    def inner(a,b):
        return simplify(Rational(1,60)*sum(w*x*y for w,x,y in zip(weights,a,b)))
    assert inner(chi1,chi1) == 1
    assert inner(chi2,chi2) == 1
    assert inner(chi1,chi2) == 0
    print('icosahedral degree-one and degree-two characters: irreducible and distinct')
    I=evaluation(icosahedron())
    assert I.rows==12 and I.rank()==9
    print('icosahedron: exact Q(sqrt(5)) rank nine')
    print('ARCHIMEDEAN_QUADRATIC_UNIQUENESS_CHECKS_PASS')

if __name__ == '__main__':
    main()

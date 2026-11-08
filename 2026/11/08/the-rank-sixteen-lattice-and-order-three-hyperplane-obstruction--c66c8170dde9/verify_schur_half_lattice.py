#!/usr/bin/env python3
"""Exact K3 half-line lattice check from the published 32 line triples.

Requires SymPy (requirements.txt). No network access or previous files.
All inputs are the numbered triples in Naskrecki--Pokora, arXiv:2607.07898v1,
Table 3, and the two integer vectors printed in RESULT.md.
"""
from sympy import Matrix, zeros, eye, ones, symbols, factor
from sympy.matrices.normalforms import smith_normal_form, hermite_normal_form
from sympy.polys.domains import ZZ

TRIPLES = (
    (1,5,6),(1,7,10),(1,8,12),(1,9,11),
    (2,3,4),(2,19,23),(2,20,22),(2,21,24),
    (3,7,14),(3,8,13),(3,9,15),
    (4,10,17),(4,11,16),(4,12,18),
    (5,13,19),(5,14,21),(5,15,20),
    (6,16,22),(6,17,24),(6,18,23),
    (7,16,19),(7,18,20),
    (8,16,21),(8,17,20),
    (9,17,19),(9,18,21),
    (10,13,22),(10,15,23),
    (11,13,24),(11,14,23),
    (12,14,22),(12,15,24),
)
T = (1,3,4,7,8,10,11,12,13,14,16,22)
MODULAR_WITNESS = (0,-1,2,4,-2,0,0,0,2,2,-4,2,
                   0,0,-1,0,-1,-1,0,-3,0,0,2,2)

def main():
    assert len(TRIPLES) == 32
    assert all(len(set(t)) == 3 and all(1 <= x <= 24 for x in t) for t in TRIPLES)
    A = zeros(24)
    seen = set()
    counts = [0]*24
    for tri in TRIPLES:
        for i in tri: counts[i-1] += 1
        for i in tri:
            for j in tri:
                if i >= j: continue
                assert (i,j) not in seen
                seen.add((i,j)); A[i-1,j-1] = 1; A[j-1,i-1] = 1
    assert len(seen) == 96 and counts == [4]*24
    assert all(sum(A[i,j] for j in range(24)) == 8 for i in range(24))
    G = A - 2*eye(24)
    lam = symbols('lam')
    f = factor(G.charpoly(lam).as_expr())
    assert (f == lam**8*(lam-6)*(lam+2)**9*(lam+6)**6), f
    assert G.rank() == 16
    diag = [abs(int(smith_normal_form(G,domain=ZZ)[i,i])) for i in range(24)]
    assert diag == [1]*10 + [2]*4 + [6,18] + [0]*8, diag
    c = Matrix([int(i+1 in T) for i in range(24)])
    unit = ones(24,1)
    assert sum(c) == 12 and G*c == 3*unit
    assert G*(unit-c) == 3*unit
    w = Matrix(MODULAR_WITNESS)
    assert sum(w) == 3 and all(int(x)%9 == 0 for x in G*w)
    # Independent integer-lattice membership cross-check, using column HNF.
    column_basis = hermite_normal_form(G)
    assert column_basis.shape == (24,16)
    assert hermite_normal_form(G.row_join(unit)) != column_basis
    assert hermite_normal_form(G.row_join(3*unit)) == column_basis
    print('SCHUR24_INCIDENCE_OK 32 triples 96 pairs 8-regular')
    print('SCHUR24_LATTICE_OK rank=16 signature=(1,15) discriminant=1728')
    print('SCHUR24_SMITH_OK', diag[:16])
    print('SCHUR24_HYPERPLANE_OK 12-line decomposition 3H; H not in generated lattice')
    print('SCHUR24_MOD9_NONMEMBERSHIP_CERTIFICATE_OK')
if __name__ == '__main__': main()

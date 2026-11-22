#!/usr/bin/env python3
"""Exact integral Chevalley--Eilenberg matrix reduction for a six-generator Lie ring.
Requires only the Python 3 standard library. Run: python3 verify.py.
Every elimination operation is an invertible integer row/column operation.
"""
from collections import Counter
from itertools import combinations

DIM = 6
BASIS = ('e', 'f', 'h', 't', 'x', 'y')
BR = {}

def put(i, j, k, coefficient):
    BR.setdefault((i, j), {})[k] = BR.get((i, j), {}).get(k, 0) + coefficient
    BR.setdefault((j, i), {})[k] = BR.get((j, i), {}).get(k, 0) - coefficient

# Standard integral sl2 triple, its 2-dimensional module, and a scalar torus.
put(2, 0, 0, 2)
put(2, 1, 1, -2)
put(0, 1, 2, 1)
put(2, 4, 4, 1)
put(2, 5, 5, -1)
put(0, 5, 4, 1)
put(1, 4, 5, 1)
put(3, 4, 4, 1)
put(3, 5, 5, 1)
SUBSETS = [list(combinations(range(DIM), d)) for d in range(DIM + 1)]

def bracket_vector(a, b, ring=0):
    v = [0] * DIM
    for i, ai in enumerate(a):
        for j, bj in enumerate(b):
            for k, c in BR.get((i, j), {}).items():
                v[k] += ai * bj * c
    return [t % ring for t in v] if ring else v

def basis(i):
    return [int(j == i) for j in range(DIM)]

def check_jacobi():
    for i, j, k in combinations(range(DIM), 3):
        a, b, c = basis(i), basis(j), basis(k)
        left = bracket_vector(a, bracket_vector(b, c))
        mid = bracket_vector(b, bracket_vector(c, a))
        right = bracket_vector(c, bracket_vector(a, b))
        assert all(left[z] + mid[z] + right[z] == 0 for z in range(DIM))
    for i in range(DIM):
        assert bracket_vector(basis(i), basis(i)) == [0]*DIM

def signs_for_tuple(args):
    if len(set(args)) != len(args):
        return 0
    return -1 if (sum(args[a] > args[b] for a in range(len(args))
                      for b in range(a+1, len(args))) % 2) else 1

def differential(degree):
    source, target = SUBSETS[degree], SUBSETS[degree + 1]
    rows, cols = len(target)*DIM, len(source)*DIM
    a = [[0] * cols for _ in range(rows)]
    for sidx, s in enumerate(source):
        for value in range(DIM):
            col = sidx*DIM + value
            for tidx, t in enumerate(target):
                # Module-action terms of the standard CE differential.
                for i, x in enumerate(t):
                    if t[:i] + t[i+1:] == s:
                        for z, c in BR.get((x, value), {}).items():
                            a[tidx*DIM+z][col] += (-1)**i*c
                # Argument-bracket terms, with alternating extension.
                for i in range(degree+1):
                    for j in range(i+1, degree+1):
                        rest = t[:i]+t[i+1:j]+t[j+1:]
                        for z, c in BR.get((t[i], t[j]), {}).items():
                            args = (z,) + rest
                            if tuple(sorted(args)) == s:
                                a[tidx*DIM+value][col] += (-1)**(i+j)*signs_for_tuple(args)*c
    return a

def matrix_multiply_zero(a, b):
    # Check AB=0 over the integers without approximate linear algebra.
    assert len(a[0]) == len(b)
    for i, row in enumerate(a):
        for j in range(len(b[0])):
            assert sum(row[k] * b[k][j] for k in range(len(b))) == 0, (i, j)

def diagonalize_with_unimodular_operations(matrix):
    """Diagonalize these matrices by exact integral row/column operations.

    Pivot 1 whenever available, then 2. Asserts divisibility before each
    elementary operation; if a matrix were not of this special type, it fails
    rather than inferring its Smith form from ranks or numerical experiments.
    """
    a = [r[:] for r in matrix]
    nr, nc = len(a), len(a[0])
    diagonal = []
    for k in range(min(nr, nc)):
        pivot = None
        for target in (1, 2):
            for i in range(k, nr):
                for j in range(k, nc):
                    if abs(a[i][j]) == target:
                        pivot = (i, j)
                        break
                if pivot is not None: break
            if pivot is not None: break
        if pivot is None:
            assert all(a[i][j] == 0 for i in range(k, nr) for j in range(k, nc)), \
                'Unreduced nonzero block: cannot claim Smith invariants'
            break
        i, j = pivot
        a[k], a[i] = a[i], a[k]   # unimodular row swap
        for row in a:
            row[k], row[j] = row[j], row[k]  # unimodular column swap
        if a[k][k] < 0:
            a[k] = [-v for v in a[k]]  # unimodular row sign change
        pivot_value = a[k][k]
        for i in range(k+1, nr):
            assert a[i][k] % pivot_value == 0
            quotient = a[i][k] // pivot_value
            if quotient:
                a[i] = [v-quotient*w for v, w in zip(a[i], a[k])]
        for j in range(k+1, nc):
            assert a[k][j] % pivot_value == 0
            quotient = a[k][j] // pivot_value
            if quotient:
                for i in range(nr):
                    a[i][j] -= quotient*a[i][k]
        diagonal.append(pivot_value)
    assert all(a[i][j] == (diagonal[i] if i == j and i < len(diagonal) else 0)
               for i in range(nr) for j in range(nc))
    assert diagonal == sorted(diagonal)  # 1's precede 2's, hence Smith normal form
    return diagonal

def cochain_vector(degree, function):
    out = [0]*(len(SUBSETS[degree])*DIM)
    for i, tup in enumerate(SUBSETS[degree]):
        v = function(tup)
        assert len(v) == DIM
        out[i*DIM:(i+1)*DIM] = v
    return out

def check_modular_deformation(d2, d1):
    # phi(x,y)=h+t, all other basis pairs zero, in characteristic two.
    target_pair = (4,5)
    central = [0,0,1,1,0,0]
    assert bracket_vector(central,basis(0),2) == [0]*DIM
    assert all(bracket_vector(central,basis(i),2) == [0]*DIM for i in range(DIM))
    phi = cochain_vector(2,lambda t: central if t==target_pair else [0]*DIM)
    assert all(sum(row[j]*phi[j] for j in range(len(phi)))%2==0 for row in d2)
    # Every coboundary evaluated on (x,y) has zero t-component.
    target = SUBSETS[2].index(target_pair)*DIM + 3
    assert all(x == 0 for x in d1[target])
    assert phi[target] == 1
    # phi(phi(u,v),w)=0 because its image is central and phi(h,-)=phi(t,-)=0.
    # Therefore [,-]+lambda*phi is an alternating Lie bracket for all lambda in char 2.
    def deformed_bracket(a, b, lam):
        z = bracket_vector(a, b, 2)
        # Polarization of the exterior pair x wedge y; in char 2 subtraction=addition.
        cross = (a[4]*b[5]+a[5]*b[4]) % 2
        return [(z[i] + lam * cross * central[i]) % 2 for i in range(DIM)]
    # Direct Jacobi check for the full deformed bracket, not just first-order closure.
    for lam in (0,1):
        for i,j,k in combinations(range(DIM),3):
            a,b,c = basis(i),basis(j),basis(k)
            xyz = [deformed_bracket(a,deformed_bracket(b,c,lam),lam),
                   deformed_bracket(b,deformed_bracket(c,a,lam),lam),
                   deformed_bracket(c,deformed_bracket(a,b,lam),lam)]
            assert all(sum(v[m] for v in xyz)%2==0 for m in range(DIM))
        outputs = [deformed_bracket(basis(i),basis(j),lam)
                   for i,j in combinations(range(DIM),2)]
        # The images are exactly h,x,y for lam=0 and h,t,x,y for lam=1.
        assert set(tuple(v) for v in outputs if any(v)) == (
            {(0,0,1,0,0,0),(0,0,0,0,1,0),(0,0,0,0,0,1)} if lam==0 else
            {(0,0,1,0,0,0),(0,0,1,1,0,0),(0,0,0,0,1,0),(0,0,0,0,0,1)})
    print('INTEGRABLE_NONBOUNDARY_COCYCLE_OK')

def main():
    check_jacobi()
    mats = [differential(k) for k in range(DIM)]
    for k in range(1, DIM):
        matrix_multiply_zero(mats[k], mats[k-1])
    expected = [(5,1),(27,3),(54,6),(51,9),(22,8),(3,3)]
    for k, mat in enumerate(mats):
        d = diagonalize_with_unimodular_operations(mat)
        c = Counter(d)
        assert (c[1], c[2]) == expected[k] and len(c) <= 2, (k,c)
        print('d%d: %d copies of 1; %d copies of 2' % (k,c[1],c[2]))
    # Exact UCT for a finite free cochain complex, with zero free cohomology.
    torsion = [0]+[t for ones,t in expected]
    char2 = [torsion[k] + (torsion[k+1] if k<DIM else 0) for k in range(DIM+1)]
    assert torsion == [0,1,3,6,9,8,3]
    assert char2 == [1,4,9,15,17,11,3]
    print('Integral H^k 2-torsion ranks:',torsion)
    print('Characteristic 2 Betti dimensions:',char2)
    check_modular_deformation(mats[2],mats[1])
    print('TORAL_SL2_INTEGRAL_ADJOINT_COHOMOLOGY_OK')

if __name__=='__main__': main()

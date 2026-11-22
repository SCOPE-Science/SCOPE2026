"""Exact finite checks for dihedral quotients of one-tolerance cycle edge complexes.

Usage: python verify_cycle_tolerance_quotient.py [maximum_n]
Requires SymPy. Mathematical proof for all n is in RESULT.md.
"""
import sys
from itertools import combinations
from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form


def faces(n):
    vertex = [(a,) for a in range(n)]
    edge = list(combinations(range(n), 2))
    triangle = [q for q in combinations(range(n), 3)
                if any((b-a == 1 or b-a == n-1)
                       for a, b in combinations(q, 2))]
    return [vertex, edge, triangle]


def transformed(simplex, n, a, reflect):
    return tuple(sorted(((a-v) if reflect else (a+v)) % n for v in simplex))


def orbit_representative(flag, n):
    return min(tuple(transformed(q, n, a, reflect) for q in flag)
               for reflect in (False, True) for a in range(n))


def orbits_of_triangles_with_trivial_stabilizer(n):
    triangles = faces(n)[2]
    reps = {}
    for q in triangles:
        rep = orbit_representative((q,), n)[0]
        reps[rep] = None
    nonreflected = 0
    for rep in reps:
        fixed = sum(transformed(rep, n, a, reflect) == rep
                    for reflect in (False, True) for a in range(n))
        assert fixed in (1, 2), (n, rep, fixed)
        nonreflected += fixed == 1
    return nonreflected


def quotient_homology(n):
    levels = faces(n)
    all_faces = [q for level in levels for q in level]
    flags = [[(q,) for q in all_faces], [], []]
    for a, b in combinations(all_faces, 2):
        if set(a) < set(b):
            flags[1].append((a, b))
    for v in levels[0]:
        for e in levels[1]:
            if set(v) < set(e):
                for t in levels[2]:
                    if set(e) < set(t):
                        flags[2].append((v, e, t))
    representatives = []
    indices = []
    for collection in flags:
        reps = sorted(set(orbit_representative(flag, n) for flag in collection))
        representatives.append(reps)
        indices.append({rep: i for i, rep in enumerate(reps)})
    boundaries = []
    for dim in (1, 2):
        b = Matrix.zeros(len(representatives[dim-1]), len(representatives[dim]))
        for col, flag in enumerate(representatives[dim]):
            for j in range(len(flag)):
                subflag = flag[:j] + flag[j+1:]
                row = indices[dim-1][orbit_representative(subflag, n)]
                b[row, col] += (-1)**j
        boundaries.append(b)
    d1, d2 = boundaries
    assert d1*d2 == Matrix.zeros(d1.rows, d2.cols)
    # Quotient barycentric edge graph: eliminate a spanning tree using a
    # unimodular change of 1-chain basis. The complementary rows of d2
    # then give the integral H_1 presentation and the free H_2 rank.
    roots = list(range(d1.rows))
    def root(i):
        while roots[i] != i:
            i = roots[i]
        return i
    tree = set()
    for j in range(d1.cols):
        endpoints = [i for i in range(d1.rows) if d1[i, j]]
        if len(endpoints) == 2:
            a, b = map(root, endpoints)
            if a != b:
                roots[a] = b
                tree.add(j)
    assert len(tree) == d1.rows-1
    other_edges = [j for j in range(d1.cols) if j not in tree]
    a = d2.extract(other_edges, list(range(d2.cols)))
    smith = smith_normal_form(a, domain=ZZ)
    diagonal = [abs(int(smith[i,i])) for i in range(min(smith.rows,smith.cols))
                if smith[i,i]]
    rank = len(diagonal)
    return (a.rows-rank, a.cols-rank, [d for d in diagonal if d>1],
            tuple(map(len, representatives)))


def run(maximum_n=20):
    for n in range(4, maximum_n+1):
        f = faces(n)
        assert len(f[2]) == n*(n-3)
        expected = (n-4)//2
        direct = orbits_of_triangles_with_trivial_stabilizer(n)
        b1,b2,torsion,cell_numbers = quotient_homology(n)
        assert direct == expected
        assert (b1,b2,torsion) == (0,expected,[])
        print('n={} triangles={} quotient_cells={} H1=0 H2=Z^{} torsion=none asym_orbits={}'.format(
            n,len(f[2]),cell_numbers,b2,direct))

if __name__ == '__main__':
    run(int(sys.argv[1]) if len(sys.argv)>1 else 20)

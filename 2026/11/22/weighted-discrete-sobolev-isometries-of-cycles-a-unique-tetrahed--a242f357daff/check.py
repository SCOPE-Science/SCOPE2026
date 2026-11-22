"""Finite checks for the real graph-variation isometry classification.

Run: python3 check.py. These checks support but do not prove the infinite family theorem.
"""
from fractions import Fraction as F
from itertools import permutations, product


def generators(n, gamma):
    unit = [tuple(F(int(i == j)) for i in range(n)) for j in range(n)]
    rim = [tuple(gamma * (unit[i][j]-unit[(i+1)%n][j]) for j in range(n)) for i in range(n)]
    return unit, unit + rim


def find_all(n, gamma):
    basis, gens = generators(n,gamma)
    allowed = set(gens) | {tuple(-z for z in g) for g in gens}
    images = list(allowed)
    found = set()
    for cols in permutations(images, n):
        # all spoke-generator images must have distinct unsigned directions
        if len(set(tuple(abs(z) for z in c) for c in cols)) != n:
            continue
        edge_images = [tuple(gamma*(cols[i][j]-cols[(i+1)%n][j]) for j in range(n)) for i in range(n)]
        if not all(q in allowed for q in edge_images):
            continue
        # A is bijective: if all the source generator images are distinct modulo sign,
        # the source and target direction multisets agree and span the whole space.
        dirs = {min(q,tuple(-z for z in q)) for q in (list(cols)+edge_images)}
        if len(dirs) != 2*n:
            continue
        found.add(cols)
    return found


def norm(v,gamma):
    n=len(v)
    return sum(abs(t) for t in v)+gamma*sum(abs(v[(i+1)%n]-v[i]) for i in range(n))


def main():
    total=0
    for n,gamma,expected in ((3,F(1),48),(3,F(1,2),12),(3,F(2),12),
                             (4,F(1),16),(4,F(1,2),16),(4,F(2),16)):
        group=find_all(n,gamma)
        assert len(group)==expected, (n,gamma,len(group),expected)
        total+=1
        for cols in group:
            for v in product(range(-1,2),repeat=n):
                Av = [sum(cols[i][j]*v[j] for j in range(n)) for i in range(n)]
                assert norm(Av,gamma)==norm(v,gamma), (n,gamma,cols,v)
                total+=1
    # Hidden symmetry at exactly gamma=1, but not otherwise.
    v=(F(1),F(0),F(0))
    moved=(-v[0],v[1]-v[0],v[2]-v[0])
    assert norm(v,F(1))==norm(moved,F(1)); total+=1
    assert norm(v,F(2))!=norm(moved,F(2)); total+=1
    print('DISCRETE_W11_WHEEL_ISOMETRY_CHECK_OK',total)


if __name__=='__main__':
    main()

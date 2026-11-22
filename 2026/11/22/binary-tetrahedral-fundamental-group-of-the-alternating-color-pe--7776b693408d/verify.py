#!/usr/bin/env python3
"""Integral cellular verification of the A4 color quotient of Hom(C5,K4).

Requires Python 3.10+ and SymPy. Run: python3 verify.py
The graph is the loopless pentagon and the four colors are 0,1,2,3.
"""
from collections import defaultdict
from functools import lru_cache
from itertools import permutations

from sympy import Matrix, ZZ
from sympy.matrices.normalforms import smith_normal_form

COLORS = range(4)
SUBSETS = tuple(
    tuple(c for c in COLORS if mask & (1 << c))
    for mask in range(1, 1 << 4)
)
EVEN_PERMS = tuple(
    p for p in permutations(COLORS)
    if sum(p[i] > p[j] for i in COLORS for j in range(i + 1, 4)) % 2 == 0
)
assert len(EVEN_PERMS) == 12


def disjoint(a, b):
    return not set(a).intersection(b)


def all_cells():
    out = []
    def add(t):
        if len(t) == 5:
            if disjoint(t[4], t[0]):
                out.append(t)
            return
        for a in SUBSETS:
            if not t or disjoint(t[-1], a):
                add(t + (a,))
    add(())
    return tuple(out)


def action(cell, perm):
    return tuple(tuple(sorted(perm[i] for i in a)) for a in cell)


def orientation(cell, perm):
    result = 1
    for a in cell:
        transformed = [perm[i] for i in a]
        inversions = sum(
            transformed[i] > transformed[j]
            for i in range(len(a)) for j in range(i + 1, len(a))
        )
        if inversions % 2:
            result = -result
    return result


@lru_cache(maxsize=None)
def representative(cell):
    options = [(action(cell, p), orientation(cell, p)) for p in EVEN_PERMS]
    root = min(t for t, _ in options)
    signs = {sgn for t, sgn in options if t == root}
    assert len(signs) == 1
    return root, signs.pop()


def dimension(cell):
    return sum(len(a) - 1 for a in cell)


def boundaries(groups):
    indices = {d: {c: j for j, c in enumerate(cells)} for d, cells in groups.items()}
    matrices = {}
    for d in range(1, 4):
        entries = [[0] * len(groups[d]) for _ in groups[d - 1]]
        for j, cell in enumerate(groups[d]):
            prefix = 0
            for i, a in enumerate(cell):
                if len(a) > 1:
                    for h in range(len(a)):
                        face = cell[:i] + (a[:h] + a[h + 1:],) + cell[i + 1:]
                        rep, orientation_to_rep = representative(face)
                        entries[indices[d - 1][rep]][j] += (
                            (-1) ** (prefix + h) * orientation_to_rep
                        )
                prefix += len(a) - 1
        matrices[d] = Matrix(entries)
    return matrices


def invariants(M):
    S = smith_normal_form(M, domain=ZZ)
    return [abs(int(S[i, i])) for i in range(min(S.rows, S.cols)) if S[i, i] != 0]


def main():
    cells = all_cells()
    assert len(cells) == 2160
    groups = defaultdict(list)
    seen = set()
    for cell in cells:
        if cell in seen:
            continue
        orbit = {action(cell, p) for p in EVEN_PERMS}
        # No nonidentity palette symmetry can preserve a nonempty product cell.
        assert len(orbit) == 12
        seen.update(orbit)
        groups[dimension(cell)].append(min(orbit))
    assert len(seen) == len(cells)
    groups = {d: sorted(groups[d]) for d in range(4)}
    counts = [len(groups[d]) for d in range(4)]
    assert counts == [20, 65, 70, 25], counts
    print('original cells: (240, 780, 840, 300)')
    print('A4 quotient cells:', counts)

    D = boundaries(groups)
    assert D[1] * D[2] == Matrix.zeros(len(groups[0]), len(groups[2]))
    assert D[2] * D[3] == Matrix.zeros(len(groups[1]), len(groups[3]))
    invariants_by_dim = {d: invariants(D[d]) for d in (1, 2, 3)}
    assert invariants_by_dim[1] == [1] * 19, invariants_by_dim[1]
    assert invariants_by_dim[2] == [1] * 45 + [3], invariants_by_dim[2]
    assert invariants_by_dim[3] == [1] * 24, invariants_by_dim[3]
    print('boundary ranks: (19, 46, 24)')
    print('Smith invariant factors: (1^19; 1^45, 3; 1^24)')
    print('d1*d2 = d2*d3 = 0')
    print('homology: H0=Z, H1=Z/3, H2=0, H3=Z')
    print('PASS_A4_PENTAGON_COLOR_QUOTIENT_BINARY_TETRAHEDRAL')


if __name__ == '__main__':
    main()

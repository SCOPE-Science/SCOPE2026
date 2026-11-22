#!/usr/bin/env python3
"""Exact rational Chevalley--Eilenberg and pentagon-symmetry calculation.

Standard library only. Lists and dictionaries enumerate every exterior monomial.
No numerical rank tolerances, probabilistic computations, or external packages.
"""
from fractions import Fraction
from itertools import combinations
from collections import defaultdict
from math import comb

NV = 5
EDGES = sorted(tuple(sorted((i, (i + 1) % NV))) for i in range(NV))
NE = len(EDGES)
N = NV + NE
BASES = [[sum(1 << i for i in sub) for sub in combinations(range(N), k)] for k in range(N + 1)]
EXPECTED_B = (1, 5, 20, 41, 70, 90, 70, 41, 20, 5, 1)
EXPECTED_ROT = (1, 1, 4, 9, 14, 18, 14, 9, 4, 1, 1)
EXPECTED_REF = (1, 3, 10, 21, 37, 45, 33, 20, 10, 2, 0)
EXPECTED_A = (1, 1, 2, 5, 9, 9, 5, 4, 2, 0, 0)
EXPECTED_BSIGN = (0, 0, 2, 4, 5, 9, 9, 5, 2, 1, 1)
EXPECTED_W = (0, 1, 4, 8, 14, 18, 14, 8, 4, 1, 0)


def differential(mask):
    """CE derivation with d(z_ij)=x_i wedge x_j, ordered wedge masks."""
    gen = [i for i in range(N) if mask & (1 << i)]
    out = defaultdict(int)
    for pos, idx in enumerate(gen):
        if idx < NV:
            continue
        a, b = EDGES[idx - NV]
        if mask & (1 << a) or mask & (1 << b):
            continue
        seq = gen[:pos] + [a, b] + gen[pos + 1:]
        swaps = sum(seq[p] > seq[q] for p in range(len(seq)) for q in range(p + 1, len(seq)))
        output = (mask ^ (1 << idx)) | (1 << a) | (1 << b)
        out[output] += -1 if (pos + swaps) % 2 else 1
    return {k: v for k, v in out.items() if v}


def matrix_rank(columns):
    """Sparse exact column elimination; every nonzero pivot normalized to 1."""
    pivots = {}
    for col in columns:
        c = {i: Fraction(x) for i, x in col.items() if x}
        while c:
            i = min(c)
            if i not in pivots:
                factor = c[i]
                pivots[i] = {j: a / factor for j, a in c.items()}
                break
            mul = c[i]
            for j, a in pivots[i].items():
                c[j] = c.get(j, 0) - mul * a
                if not c[j]:
                    del c[j]
    return len(pivots)


def generator_action(mapping):
    """Induced signed permutation on dual vertex and oriented edge cochains."""
    edge_id = {e: j for j, e in enumerate(EDGES)}
    perm = [(mapping[i], 1) for i in range(NV)]
    for a, b in EDGES:
        a1, b1 = mapping[a], mapping[b]
        edge = tuple(sorted((a1, b1)))
        assert edge in edge_id
        perm.append((NV + edge_id[edge], 1 if a1 < b1 else -1))
    return perm


def action(mask, perm):
    target = []
    coeff = 1
    for i in range(N):
        if mask & (1 << i):
            j, s = perm[i]
            target.append(j)
            coeff *= s
    coeff *= -1 if sum(target[i] > target[j] for i in range(len(target))
                       for j in range(i + 1, len(target))) % 2 else 1
    return sum(1 << i for i in target), coeff


def compose(mask, perms):
    sign = 1
    for perm in perms:
        mask, c = action(mask, perm)
        sign *= c
    return mask, sign


def invariant_orbits(basis, perm, group_order):
    rest = set(basis)
    vectors = []
    while rest:
        m0 = min(rest)
        m, sign = m0, 1
        orbit = {}
        for step in range(group_order):
            if m in orbit:
                assert m == m0
                break
            orbit[m] = sign
            rest.remove(m)
            m, factor = action(m, perm)
            sign *= factor
        assert m == m0
        if sign == 1:
            vectors.append(orbit)
    return vectors


def invariant_complex(perm, order):
    inv = [invariant_orbits(BASES[k], perm, order) for k in range(N + 1)]
    ranks = []
    for k in range(N):
        row_to_basis = {m: (j, v) for j, vec in enumerate(inv[k + 1]) for m, v in vec.items()}
        cols = []
        for vec in inv[k]:
            d = defaultdict(int)
            for m, a in vec.items():
                for dest, b in differential(m).items():
                    d[dest] += a * b
            coords = {}
            for m, a in d.items():
                if not a:
                    continue
                j, v = row_to_basis[m]
                c = a * v
                assert j not in coords or coords[j] == c
                coords[j] = c
            # Ensure no missing image monomials after zero cancellation.
            for m, a in d.items():
                if not a: continue
                j, v = row_to_basis[m]
                assert coords[j] * v == a
            cols.append(coords)
        ranks.append(matrix_rank(cols))
    betti = [len(inv[k]) - (ranks[k - 1] if k else 0) - (ranks[k] if k < N else 0)
             for k in range(N + 1)]
    return [len(x) for x in inv], ranks, betti


def full_dihedral_complex(rot, ref):
    """Independent full ten-element group-invariants: signed orbit BFS."""
    inv = []
    for basis in BASES:
        todo = set(basis)
        out = []
        while todo:
            m0 = min(todo)
            orbit = {m0: 1}
            queue = [m0]
            inconsistent = False
            for current in queue:
                for p in (rot, ref):
                    dest, sign = action(current, p)
                    required = orbit[current] * sign
                    if dest in orbit:
                        if orbit[dest] != required:
                            inconsistent = True
                    else:
                        orbit[dest] = required
                        queue.append(dest)
            todo.difference_update(orbit)
            if not inconsistent:
                out.append(orbit)
        inv.append(out)
    ranks = []
    for k in range(N):
        coords_by_mask = {m: (j, v) for j, orbit in enumerate(inv[k+1]) for m, v in orbit.items()}
        cols = []
        for vec in inv[k]:
            d = defaultdict(int)
            for m, a in vec.items():
                for target, b in differential(m).items():
                    d[target] += a*b
            col = {}
            for m, a in d.items():
                if not a:
                    continue
                assert m in coords_by_mask
                j, v = coords_by_mask[m]
                val = a*v
                assert j not in col or col[j] == val
                col[j] = val
            cols.append(col)
        ranks.append(matrix_rank(cols))
    beta = tuple(len(inv[k])-(ranks[k-1] if k else 0)-(ranks[k] if k<N else 0)
                 for k in range(N+1))
    return [len(x) for x in inv],ranks,beta

def main():
    print('Graph: C5, vertices 0..4, oriented edges:', EDGES)
    print('CE generators:', N, 'CE monomials:', sum(len(b) for b in BASES))
    print('Basis dimensions:', [len(b) for b in BASES])
    # Direct derivation check at every wedge basis element.
    for basis in BASES:
        for m in basis:
            twice = defaultdict(int)
            for m1, a in differential(m).items():
                for m2, b in differential(m1).items():
                    twice[m2] += a * b
            assert not any(twice.values())
    print('d^2=0: checked all 1024 basis monomials')
    rot = generator_action([(i + 1) % NV for i in range(NV)])
    ref = generator_action([(-i) % NV for i in range(NV)])
    for basis in BASES:
        for m in basis:
            assert compose(m, [rot] * 5) == (m, 1)
            assert compose(m, [ref, ref]) == (m, 1)
            assert compose(m, [ref, rot, ref, rot]) == (m, 1)
            for p in (rot, ref):
                out, sg = action(m, p)
                lhs = defaultdict(int)
                rhs = defaultdict(int)
                for m1, a in differential(out).items():lhs[m1] += sg * a
                for m1, a in differential(m).items():
                    m2, s2 = action(m1, p)
                    rhs[m2] += a * s2
                assert dict(lhs) == dict(rhs)
    print('D5 relations and both chain maps commute with d: checked 1024 monomials')
    ranks = [matrix_rank([differential(m) for m in BASES[k]]) for k in range(N)]
    betti = tuple(len(BASES[k]) - (ranks[k-1] if k else 0) - (ranks[k] if k < N else 0)
                  for k in range(N+1))
    assert betti == EXPECTED_B
    print('Full CE differential ranks:', ranks)
    print('Full Betti numbers:', betti, 'total=', sum(betti))
    dims_r, ranks_r, cyclic_betti = invariant_complex(rot, 5)
    dims_s, ranks_s, ref_betti = invariant_complex(ref, 2)
    assert tuple(cyclic_betti) == EXPECTED_ROT
    assert tuple(ref_betti) == EXPECTED_REF
    print('Rotation-invariant cochain dimensions:', dims_r)
    print('Rotation-invariant differential ranks:', ranks_r)
    print('C5-invariant Betti:', cyclic_betti)
    print('Reflection-invariant cochain dimensions:', dims_s)
    print('Reflection-invariant differential ranks:', ranks_s)
    print('Reflection-invariant Betti:', ref_betti)
    tr = [2 * f - b for f, b in zip(ref_betti, betti)]
    assert all((a + t) % 2 == 0 for a, t in zip(cyclic_betti, tr))
    assert all((b - a) % 4 == 0 for b, a in zip(betti, cyclic_betti))
    aa = tuple((a + t)//2 for a, t in zip(cyclic_betti, tr))
    bb = tuple((a - t)//2 for a, t in zip(cyclic_betti, tr))
    cc = tuple((b - a)//4 for b, a in zip(betti, cyclic_betti))
    assert (aa, bb, cc) == (EXPECTED_A, EXPECTED_BSIGN, EXPECTED_W)
    assert all(x + y + 4*z == b for x, y, z, b in zip(aa, bb, cc, betti))
    print('D5 reflection traces:', tr)
    print('Multiplicity trivial:', aa)
    print('Multiplicity sign:', bb)
    print('Multiplicity 4-dimensional cyclotomic:', cc)
    dihedral_dims, dihedral_ranks, dihedral_betti = full_dihedral_complex(rot, ref)
    assert dihedral_betti == EXPECTED_A
    print('Full D5-invariant cochain dimensions:', dihedral_dims)
    print('Full D5-invariant differential ranks:', dihedral_ranks)
    print('Full D5-invariant Betti:', dihedral_betti)
    # Poincare duality with orientation character epsilon: H^{10-k} = H^k dual tensor epsilon.
    assert all(betti[k] == betti[N-k] for k in range(N+1))
    assert all(aa[k] == bb[N-k] for k in range(N+1))
    assert all(cc[k] == cc[N-k] for k in range(N+1))
    # Euler + Lefschetz: each nontrivial rotation and each reflection has vanishing alternating trace.
    assert sum((-1)**k * betti[k] for k in range(N+1)) == 0
    assert sum((-1)**k * (aa[k] + bb[k] - cc[k]) for k in range(N+1)) == 0
    assert sum((-1)**k * tr[k] for k in range(N+1)) == 0
    print('Poincare duality (orientation twist), Euler and Lefschetz tests: PASS')
    print('ALL EXACT CERTIFICATE CHECKS PASSED')

if __name__ == '__main__':
    main()

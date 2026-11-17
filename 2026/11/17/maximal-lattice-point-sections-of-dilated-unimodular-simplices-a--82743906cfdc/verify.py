"""Exact finite corroboration of the maximal-lattice-slice classification.

All arithmetic is rational and uses Python's standard library. The unbounded
result is established by the projection argument in RESULT.md, not this script.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def points(d, k):
    def build(prefix, remaining):
        if len(prefix) == d:
            yield tuple(prefix)
            return
        for j in range(remaining + 1):
            yield from build(prefix + [j], remaining - j)
    return list(build([], k))


def rref_signature(rows, dim):
    M = [[Fraction(v) for v in row] for row in rows]
    lead_row = 0
    for col in range(dim + 1):
        pivot = next((r for r in range(lead_row, len(M)) if M[r][col]), None)
        if pivot is None:
            continue
        M[lead_row], M[pivot] = M[pivot], M[lead_row]
        q = M[lead_row][col]
        M[lead_row] = [a / q for a in M[lead_row]]
        for r in range(len(M)):
            if r != lead_row:
                q = M[r][col]
                if q:
                    M[r] = [a - q*b for a,b in zip(M[r],M[lead_row])]
        lead_row += 1
        if lead_row == len(M):
            break
    return tuple(tuple(r) for r in M[:lead_row]), lead_row


def all_flat_count(d, k, ell):
    P = points(d, k)
    groups = {}
    for ix in combinations(range(len(P)), ell+1):
        row = [(1, *P[i]) for i in ix]
        sig, rank = rref_signature(row, d)
        if rank < ell+1:
            continue
        if sig not in groups:
            groups[sig] = set()
        groups[sig].update(ix)
    M = max(map(len, groups.values()))
    winners = {sig for sig, s in groups.items() if len(s) == M}
    face_sigs = set()
    for vertex_indices in combinations(range(d+1), ell+1):
        vertices = [(0,)*d] + [tuple(int(i==j) * k for i in range(d)) for j in range(d)]
        sig, rank = rref_signature([(1, *vertices[i]) for i in vertex_indices], d)
        assert rank == ell+1
        face_sigs.add(sig)
    assert M == comb(k+ell, ell), (d,k,ell,M,comb(k+ell,ell))
    assert len(winners) == comb(d+1, ell+1), (d,k,ell,len(winners))
    assert winners == face_sigs, (d,k,ell,'non-face maximizing flat')
    return len(P), len(groups), M, len(winners)


def main():
    cases = [(3,k,ell) for k in range(1,5) for ell in (1,2)]
    cases += [(4,k,ell) for k in (1,2) for ell in (1,2,3)]
    cases += [(5,1,ell) for ell in (1,2,3,4)]
    total = 0
    for d,k,ell in cases:
        n, flats, maxpts, maxflats = all_flat_count(d,k,ell)
        total += flats
        print(f'd={d},k={k},ell={ell}: points={n}, candidate_flats={flats}, max_lattice_points={maxpts}, maximizers={maxflats}')
    print(f'PASS: {len(cases)} exact finite configurations; {total} affine-flat classes examined.')


if __name__ == '__main__':
    main()

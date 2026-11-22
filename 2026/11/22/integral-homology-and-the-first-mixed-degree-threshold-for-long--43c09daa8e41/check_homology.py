#!/usr/bin/env python3
"""Exact integral cellular chain contraction for full-cycle permutation complexes.

Requires only Python 3.10+. Run: python check_homology.py
All arithmetic is exact integer arithmetic. Unit-pivot cancellation is an
integral chain homotopy equivalence, not a floating-point rank estimate.
"""
from itertools import combinations, permutations

EXPECTED = {
    2: {-1: 0, 0: 0, 1: 0},
    3: {-1: 0, 0: 0, 1: 1, 2: 0},
    4: {-1: 0, 0: 0, 1: 0, 2: 3, 3: 0},
    5: {-1: 0, 0: 0, 1: 0, 2: 0, 3: 15, 4: 0},
    6: {-1: 0, 0: 0, 1: 0, 2: 0, 3: 1, 4: 88, 5: 0},
}


def full_cycle(p):
    n = len(p)
    v = 0
    seen = set()
    for _ in range(n):
        if v in seen:
            return False
        seen.add(v)
        v = p[v]
    return v == 0 and len(seen) == n


def construct(n):
    cycles = [p for p in permutations(range(n)) if full_cycle(p)]
    assert len(cycles) == __import__('math').factorial(n-1)
    bases = {-1: [()]}
    for k in range(n):
        bases[k] = sorted({f for p in cycles for f in combinations(p, k+1)})
    boundaries = {k: {} for k in range(n)}
    for k in range(n):
        for f in bases[k]:
            boundaries[k][f] = {f[:i] + f[i+1:]: (-1 if i % 2 else 1)
                                for i in range(k+1)}
    return cycles, bases, boundaries


def assert_chain(boundaries, n):
    # Exact integer proof obligation d_{k-1} d_k = 0.
    for k in range(1, n):
        lower = boundaries[k-1]
        for c, vec in boundaries[k].items():
            squares = {}
            for mid, coeff in vec.items():
                for r, z in lower[mid].items():
                    squares[r] = squares.get(r, 0) + coeff*z
            assert all(z == 0 for z in squares.values()), (k,c)


def integral_cancel(bases, boundaries, n):
    live = {k: set(b) for k,b in bases.items()}
    moves = 0
    while True:
        pivot = None
        # Pick unit entry with minimum Schur-complement fill estimate.
        for k in range(n-1, -1, -1):
            by_row = {}
            for col, column in boundaries[k].items():
                for row, coeff in column.items():
                    by_row.setdefault(row, {})[col] = coeff
            for row, cols in by_row.items():
                for col, v in cols.items():
                    if abs(v) == 1:
                        score = (len(cols)-1)*(len(boundaries[k][col])-1)
                        cand = (score, k, row, col, v, cols)
                        if pivot is None or cand[:2] < pivot[:2]:
                            pivot = cand
        if pivot is None:
            break
        _, k, row, col, unit, cols = pivot
        old = boundaries[k][col]
        # Integral Schur complement: new d[rr,other] =
        # old d[rr,other] - d[row,other]*d[rr,col]/d[row,col].
        for other, a in cols.items():
            if other == col:
                continue
            dst = boundaries[k][other]
            for rr,b in old.items():
                nv = dst.get(rr, 0) - a*b*unit
                if nv:
                    dst[rr] = nv
                else:
                    dst.pop(rr, None)
        del boundaries[k][col]
        for other in boundaries[k].values():
            other.pop(row, None)
        if k > 0:
            del boundaries[k-1][row]
        if k < n-1:
            for other in boundaries[k+1].values():
                other.pop(col, None)
        live[k].remove(col)
        live[k-1].remove(row)
        moves += 1
    assert_chain(boundaries, n)
    assert all(not any(vector.values())
               for matrix in boundaries.values() for vector in matrix.values()), \
        'Residual integer differential nonzero: homology not determined by cell count'
    return {k:len(c) for k,c in live.items()}, moves


def mod_rank(left, right, prime):
    """Independent sparse Gaussian rank from ORIGINAL cellular boundary."""
    index = {w:j for j,w in enumerate(left)}
    pivots = {}
    for word in right:
        col = {index[word[:i]+word[i+1:]]: (1 if i%2==0 else prime-1)
               for i in range(len(word))}
        while col:
            j = max(col)
            v = col[j]
            if j not in pivots:
                inv = pow(v, -1, prime)
                pivots[j] = {i:(x*inv)%prime for i,x in col.items()}
                break
            for i,x in pivots[j].items():
                z = (col.get(i,0) - v*x)%prime
                if z: col[i] = z
                else: col.pop(i, None)
    return len(pivots)


def main():
    for n in range(2,7):
        cycles, basis, diffs = construct(n)
        assert_chain(diffs, n)
        count = {k:len(v) for k,v in basis.items()}
        for p in (2,3,101):
            ranks = {-1:0, 0:1}
            for k in range(1,n):
                ranks[k] = mod_rank(basis[k-1],basis[k],p)
            ranks[n] = 0
            betti = {k:count[k]-ranks[k]-ranks[k+1]
                     for k in range(0,n)}
            betti[-1] = 0
            assert betti == EXPECTED[n], (n,p,betti)
        reduced, pairs = integral_cancel(basis, diffs, n)
        assert reduced == EXPECTED[n], (n,reduced)
        assert pairs*2 + sum(reduced.values()) == sum(count.values()), n
        print('n=%d full_cycles=%d cell_counts=%s unit_pairs=%d '
              'integral_homology_ranks=%s primes=2,3,101 PASS' %
              (n,len(cycles),[count[k] for k in range(-1,n)],pairs,
               [reduced[k] for k in range(-1,n)]),flush=True)
    print('All exact augmented-boundary, integer-cancellation, and modular tests PASS.')

if __name__ == '__main__':
    main()

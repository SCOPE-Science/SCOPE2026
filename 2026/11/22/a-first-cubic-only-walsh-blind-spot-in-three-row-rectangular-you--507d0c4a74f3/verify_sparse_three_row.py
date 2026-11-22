"""Independent exact checks for sparse Walsh cancellation of three-row Young diagrams.

Only the Python standard library is required. Cell coordinates are one-based.
"""
from itertools import combinations
from math import comb


def ideal_lengths(n):
    return [(a, b, c) for a in range(n+1)
            for b in range(a+1) for c in range(b+1)]


def cell_indices(n):
    return tuple((r, j) for r in range(1, 4) for j in range(1, n+1))


def incidence_masks(n):
    cells = cell_indices(n)
    ideals = ideal_lengths(n)
    masks = []
    for r, j in cells:
        masks.append(sum(1 << idx for idx, triple in enumerate(ideals)
                         if triple[r-1] >= j))
    assert len(ideals) == comb(n+3, 3)
    return masks, len(ideals)


def required_containing(n, subset):
    """Exact number of diagrams containing all selected cells, no enumeration."""
    lower = [0, 0, 0]
    for r, j in subset:
        lower[r-1] = max(lower[r-1], j)
    A, B, C = lower
    return sum((b-C+1) * (n-max(b, A)+1)
               for b in range(max(B, C), n+1))


def multiplier_formula(n, cells):
    """Polynomial exact inclusion-exclusion on at most three cells."""
    ans = 0
    for k in range(len(cells)+1):
        for J in combinations(cells, k):
            ans += (-2)**k * required_containing(n, J)
    return ans


def sparse_census(n, max_weight):
    masks, M = incidence_masks(n)
    zero_groups = {}
    for w in range(1, max_weight+1):
        groups = []
        for ind in combinations(range(3*n), w):
            parity = 0
            for i in ind:
                parity ^= masks[i]
            via_bits = M - 2*parity.bit_count()
            cells = tuple(cell_indices(n)[i] for i in ind)
            via_formula = multiplier_formula(n, cells)
            assert via_bits == via_formula, (n, cells, via_bits, via_formula)
            if via_bits == 0:
                groups.append(cells)
        zero_groups[w] = tuple(groups)
    return zero_groups


def rotate(n, cells):
    return tuple(sorted((4-r, n+1-j) for r, j in cells))


EXPECTED_N10_REPRESENTATIVES = (
 ((1,2),(1,5),(3,3)),
 ((1,2),(1,8),(3,6)),
 ((1,2),(1,9),(3,1)),
 ((1,3),(1,9),(3,1)),
 ((1,4),(1,9),(2,3)),
 ((1,4),(2,8),(3,2)),
 ((1,5),(1,8),(2,8)),
 ((1,5),(1,8),(3,3)),
 ((1,6),(2,9),(3,3)),
 ((1,7),(2,7),(2,9)),
 ((1,8),(2,5),(2,8)),
 ((1,8),(2,5),(3,3)),
 ((1,8),(2,6),(2,8)),
 ((1,9),(2,2),(3,2)),
 ((1,9),(2,3),(3,1)),
)


def check():
    target = {2:(0,2), 6:(0,3), 10:(0,0,30), 14:(0,2)}
    for n, expected in target.items():
        groups = sparse_census(n, len(expected))
        got = tuple(len(groups[w]) for w in range(1, len(expected)+1))
        assert got == expected, (n, got, expected)
        if n == 10:
            z = set(groups[3]); reps = sorted(min(c, rotate(n,c)) for c in z)
            reps = tuple(sorted(set(reps)))
            assert reps == tuple(sorted(EXPECTED_N10_REPRESENTATIVES))
            assert len(z) == 30 and len(reps) == 15
            assert all(rotate(n,c) in z for c in z)
        if n == 14:
            assert set(groups[2]) == {
                ((1,10),(1,14)), ((3,1),(3,5))
            }
        print('n=%d  ideals=%d  zero counts by weight %s' %
              (n, comb(n+3, 3), got))
    # Every odd width has a central-cell zero by dual complement.
    for n in range(1, 14, 2):
        cell=(2,(n+1)//2)
        assert multiplier_formula(n, (cell,)) == 0
    # Widths divisible by four have odd counts and hence no zero character.
    for n in (4,8,12):
        assert comb(n+3, 3)%2 == 1
    print('PASS: independent exhaustive bitset and inclusion-exclusion methods')


if __name__=='__main__':
    check()

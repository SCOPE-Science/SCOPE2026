"""Finite, direct checker for maximal induced bipartite sets in rook graphs.

Run: python3 verify_rook_bipartite.py
Uses only the Python standard library; finite checks do not replace the proof.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from math import factorial


@lru_cache(None)
def coeff(m, n):
    """Coefficient of x**m*y**n in the path/cycle exponential generating series."""
    if m < 0 or n < 0:
        return Fraction(0)
    if m == 0:
        return Fraction(1, factorial(n))
    ans = Fraction(0)
    for k in range(1, m + 1):
        ans += Fraction(k, 2) * coeff(m - k, n - k - 1)
        if k >= 2:
            ans += Fraction(1, 2) * coeff(m - k, n - k)
    return ans / m


def saturated_count(m, n):
    val = factorial(m) * factorial(n) * coeff(m, n)
    assert val.denominator == 1
    return int(val)


def predicted(m, n):
    assert 2 <= m <= n
    if m < n:
        return Counter({2 * m: saturated_count(m, n)})
    total = Counter({2 * m: saturated_count(m, m)})
    if m >= 3:
        total[2*m-1] = m*m*saturated_count(m-1, m-1)
    return total


def bipartite_direct(mask, m, n, neighbors):
    """Two-color each connected component in the induced rook graph."""
    seen = 0
    while mask & ~seen:
        root_bit = (mask & ~seen) & -(mask & ~seen)
        root = root_bit.bit_length() - 1
        color = {root: 0}
        seen |= root_bit
        todo = [root]
        while todo:
            u = todo.pop()
            adjacency = neighbors[u] & mask
            while adjacency:
                vbit = adjacency & -adjacency
                adjacency -= vbit
                v = vbit.bit_length() - 1
                if v in color:
                    if color[v] == color[u]:
                        return False
                else:
                    color[v] = 1 - color[u]
                    seen |= vbit
                    todo.append(v)
    return True


def capacity_ok(mask, m, n):
    for i in range(m):
        if ((mask >> (i*n)) & ((1 << n) - 1)).bit_count() > 2:
            return False
    for j in range(n):
        if sum((mask >> (i*n+j)) & 1 for i in range(m)) > 2:
            return False
    return True


def census(m, n, direct=True):
    size = m*n
    neighbors = [sum(1 << (a*n+b) for a in range(m) for b in range(n)
                     if ((a == i or b == j) and (a, b) != (i, j)))
                 for i in range(m) for j in range(n)]
    hist = Counter()
    bipartite_count = 0
    for mask in range(1 << size):
        cap = capacity_ok(mask, m, n)
        if direct:
            valid = bipartite_direct(mask, m, n, neighbors)
            assert cap == valid, (m, n, mask, 'capacity/bipartite mismatch')
        else:
            valid = cap
        if not valid:
            continue
        bipartite_count += 1
        maximal = True
        missing = (~mask) & ((1 << size) - 1)
        while missing:
            bit = missing & -missing
            missing -= bit
            extension = mask | bit
            if direct:
                ok = bipartite_direct(extension, m, n, neighbors)
                assert ok == capacity_ok(extension, m, n)
            else:
                ok = capacity_ok(extension, m, n)
            if ok:
                maximal = False
                break
        if maximal:
            hist[mask.bit_count()] += 1
    assert hist == predicted(m, n), (m, n, hist, predicted(m, n))
    return bipartite_count, hist


def main():
    cases = [(2,2), (2,3), (2,4), (2,5), (2,6),
             (3,3), (3,4), (3,5), (3,6), (4,4), (4,5)]
    total_masks = total_valid = total_max = 0
    for m,n in cases:
        # Direct rook-graph BFS for all subsets through 4x4; the 4x5 case
        # uses separately cross-checked capacity characterization.
        direct = (m*n <= 16)
        valid, hist = census(m,n,direct=direct)
        total_masks += 1 << (m*n)
        total_valid += valid
        total_max += sum(hist.values())
        print(f'{m}x{n} direct={direct} bipartite_sets={valid} maximal={dict(sorted(hist.items()))}')
    assert saturated_count(3,4) == 114
    assert saturated_count(4,4) == 90
    assert saturated_count(3,5) == 690
    assert saturated_count(4,5) == 2490
    print('VERIFY_OK cases=%d examined_subsets=%d bipartite_sets=%d maximal_sets=%d GF=PASS classification=PASS' %
          (len(cases), total_masks, total_valid, total_max))


if __name__ == '__main__':
    main()

#!/usr/bin/env python3
"""Exact finite-state certificate for pair extensions over disjoint two-chains.

Pure Python standard library. Prints certificate checks and a few values.
The row-vector annihilations establish all-index recurrences, not mere samples.
"""
from itertools import product
from collections import Counter
from fractions import Fraction

STATES = list(product(range(4), repeat=2))
EXPECTED_LESS = (1, 0, 2, 0, 2, 3, 4, 2, 0, 0, 3, 0, 0, 0, 2, 1)
EXPECTED_INCOMP = (1, 2, 2, 1, 2, 4, 1, 1, 2, 1, 4, 1, 1, 1, 1, 1)


def local_patterns(relation):
    """Each relation is -1 (x<y), 0 (x||y), +1 (y<x).
    Return all local signatures (a-x,a-y,b-x,b-y), a<b.
    A signature entry -1 means old<new, +1 new<old, 0 incomparable.
    """
    out = []
    for sig in product((-1, 0, 1), repeat=4):
        # Nodes a,b,x,y = 0,1,2,3.
        adjacency = [[False] * 4 for _ in range(4)]
        adjacency[0][1] = True
        if relation == -1:
            adjacency[2][3] = True
        elif relation == 1:
            adjacency[3][2] = True
        pairs = [(0, 2), (0, 3), (1, 2), (1, 3)]
        for (i, j), state in zip(pairs, sig):
            if state == -1:
                adjacency[i][j] = True
            if state == 1:
                adjacency[j][i] = True
        for k in range(4):
            for i in range(4):
                for j in range(4):
                    adjacency[i][j] |= adjacency[i][k] and adjacency[k][j]
        if any(adjacency[i][i] for i in range(4)):
            continue
        if relation == 0 and (adjacency[2][3] or adjacency[3][2]):
            continue
        if any((adjacency[i][j], adjacency[j][i]) !=
               ((s == -1), (s == 1))
               for (i, j), s in zip(pairs, sig)):
            continue
        mask = 0
        for offset, v in enumerate((2, 3)):
            if any(adjacency[i][v] for i in (0, 1)):
                mask |= 1 << (2 * offset)
            if any(adjacency[v][i] for i in (0, 1)):
                mask |= 2 << (2 * offset)
        out.append((sig, mask))
    return out


def update_one(old, new):
    """0=none, 1=old points below, 2=old points above,
    3=mixed entirely within one earlier two-chain.
    """
    if old == 0:
        return new
    if old == 1:
        return None if new & 2 else 1
    if old == 2:
        return None if new & 1 else 2
    return 3 if new == 0 else None


def update_state(old, mask):
    left = update_one(old[0], mask & 3)
    right = update_one(old[1], mask >> 2)
    return None if (left is None or right is None) else (left, right)


def transfer(patterns):
    m = [[0] * 16 for _ in range(16)]
    for i, old in enumerate(STATES):
        for _, mask in patterns:
            new = update_state(old, mask)
            if new is not None:
                m[i][STATES.index(new)] += 1
    return m


def multiply_row(row, mat):
    return [sum(row[i] * mat[i][j] for i in range(16)) for j in range(16)]


def characteristic_factor_coefficients(factors):
    # The polynomial p(t) = product (t-root)^multiplicity, low degree first.
    p = [1]
    for root, power in factors:
        for _ in range(power):
            q = [0] * (len(p) + 1)
            for j, a in enumerate(p):
                q[j] -= root * a
                q[j + 1] += a
            p = q
    return p


def comparable(m):
    return 9**m + 2 * 6**m + int((Fraction(4*m, 3) - 2) * 3**m) + m


def incomparable(m):
    return 2 * 9**m + 2 * 6**m + int((Fraction(8*m, 3) - 4) * 3**m) + (m-1)**2


def direct_check(blocks, relation):
    """Rebuild all edges on the full finite poset; bitset closure.
    In particular, test that no old cross-block comparison is induced.
    """
    m = len(blocks)
    n = 2*m + 2
    x, y = 2*m, 2*m+1
    adjacency = [0] * n
    for i in range(m):
        adjacency[2*i] |= 1 << (2*i+1)
    if relation == -1:
        adjacency[x] |= 1 << y
    elif relation == 1:
        adjacency[y] |= 1 << x
    for i, sig in enumerate(blocks):
        for old, added, sign in zip((2*i, 2*i, 2*i+1, 2*i+1),
                                    (x, y, x, y), sig):
            if sign == -1:
                adjacency[old] |= 1 << added
            elif sign == 1:
                adjacency[added] |= 1 << old
    for k in range(n):
        for i in range(n):
            if adjacency[i] & (1 << k):
                adjacency[i] |= adjacency[k]
    if any(adjacency[i] & (1 << i) for i in range(n)):
        return False
    for i in range(2*m):
        for j in range(2*m):
            expected = (i // 2 == j // 2 and i % 2 == 0 and j == i+1)
            if bool(adjacency[i] & (1 << j)) != expected:
                return False
    if relation == 0 and (adjacency[x] & (1 << y) or adjacency[y] & (1 << x)):
        return False
    for i, sig in enumerate(blocks):
        for old, added, sign in zip((2*i, 2*i, 2*i+1, 2*i+1),
                                    (x, y, x, y), sig):
            if bool(adjacency[old] & (1 << added)) != (sign == -1):
                return False
            if bool(adjacency[added] & (1 << old)) != (sign == 1):
                return False
    return True


def verify(relation, expected, formula, factors):
    patterns = local_patterns(relation)
    weight = Counter(mask for _, mask in patterns)
    assert tuple(weight.get(i, 0) for i in range(16)) == expected
    matrix = transfer(patterns)
    p = characteristic_factor_coefficients(factors)
    rows = []
    row = [int(i == 0) for i in range(16)]
    for m in range(max(10, len(p))):
        rows.append(row)
        row = multiply_row(row, matrix)
    # Exact polynomial annihilation of the *initial row*: proves the same
    # constant-coefficient recurrence for all indices, not just a finite fit.
    assert all(sum(p[k] * rows[k][j] for k in range(len(p))) == 0
               for j in range(16))
    for m in range(len(p) - 1):
        assert sum(rows[m]) == formula(m)
    for m in range(10):
        assert sum(rows[m]) == formula(m)
    direct_cases = 0
    for m in range(4):
        count = 0
        for tuple_patterns in product(patterns, repeat=m):
            signatures = [sig for sig, _ in tuple_patterns]
            state = (0, 0)
            for _, mask in tuple_patterns:
                state = update_state(state, mask) if state is not None else None
            valid_full = direct_check(signatures, relation)
            assert valid_full == (state is not None)
            count += valid_full
            direct_cases += 1
        assert count == formula(m)
    print('relation', relation, 'local', len(patterns), 'recurrence_order', len(p)-1,
          'full_diagrams_checked', direct_cases)
    print('counts_m0_to_m7', [formula(m) for m in range(8)])


def main():
    verify(-1, EXPECTED_LESS, comparable, [(9,1),(6,1),(3,2),(1,2)])
    verify(0, EXPECTED_INCOMP, incomparable, [(9,1),(6,1),(3,2),(1,3)])
    for m in range(25):
        c, i = comparable(m), incomparable(m)
        t = 2*c + i
        assert t == (4*9**m + 6*6**m +
                     int((Fraction(16*m,3)-8)*3**m) + m*m + 1)
        assert 2*c > i
    print('strict_half_comparability_checked_for_m0_through_m24')
    print('EXACT_RECURRENCE_AND_TRANSITIVITY_OK')

if __name__ == '__main__':
    main()

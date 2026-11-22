#!/usr/bin/env python3
"""Independent finite checks for an exact Fibonacci--Lucas local-square law.

This program is diagnostic rather than a proof of the infinite statements.
"""
from math import isqrt


def square_set(k):
    m = 3 ** k
    return {x*x % m for x in range(m)}


def theoretical_square_count(m):
    return 1 + sum(3 ** (m - 2*j - 1) for j in range((m - 1)//2 + 1)) if m >= 1 else 1


def observed_pairs(k):
    modulus = 3 ** k
    period = 8 * 3 ** (k - 1)
    squares = square_set(k)
    f, f_next = 0, 1
    l, l_next = 2, 1
    cells = {(a,b): 0 for a in (0,1) for b in (0,1)}
    for _ in range(period):
        cells[(int(f in squares), int(l in squares))] += 1
        f, f_next = f_next, (f+f_next) % modulus
        l, l_next = l_next, (l+l_next) % modulus
    assert (f, f_next, l, l_next) == (0, 1, 2, 1), 'joint period mismatch'
    return cells


def expected_pairs(k):
    T = 3 ** (k - 1)
    B = 1 if k == 1 else theoretical_square_count(k - 2)
    return {(1,1): T + 2*B, (1,0): 2*T,
            (0,1): 2*T, (0,0): 3*T - 2*B}


def v3(x):
    if not x:
        return None
    x = abs(x)
    v = 0
    while x % 3 == 0:
        x //= 3
        v += 1
    return v


def test_isometries():
    # Compute exact values for just the selected finite range, then compare
    # normalized singular branches, including non-adjacent indices.
    limit = 8*130+7
    fib, fib_next = 0, 1
    luc, luc_next = 2, 1
    F, L = [], []
    for n in range(limit+1):
        F.append(fib)
        L.append(luc)
        fib, fib_next = fib_next, fib + fib_next
        luc, luc_next = luc_next, luc + luc_next
    checks = 0
    for seq, branches in ((F, (0,4)), (L, (2,6))):
        for j in branches:
            vals = [seq[j+8*t]//3 for t in range(130)]
            assert all(seq[j+8*t] % 3 == 0 for t in range(130))
            for t in range(130):
                for u in (0,1,2,3,9,27,45,81,128):
                    if t == u:
                        continue
                    assert v3(vals[t]-vals[u]) == v3(t-u), (j,t,u)
                    checks += 1
    return checks


def main():
    for m in range(9):
        assert theoretical_square_count(m) == len(square_set(m)), m
    for k in range(1,10):
        observed = observed_pairs(k)
        expected = expected_pairs(k)
        assert observed == expected, (k, observed, expected)
        print(f'k={k}, period={8*3**(k-1)}, both={observed[(1,1)]}, '
              f'F_only={observed[(1,0)]}, L_only={observed[(0,1)]}, '
              f'neither={observed[(0,0)]}: PASS')
    isometry_checks = test_isometries()
    print(f'Finite normalized-branch isometry comparisons: {isometry_checks} PASS')
    print('All direct finite checks PASS. Infinite density and error follow from written proof.')


if __name__ == '__main__':
    main()

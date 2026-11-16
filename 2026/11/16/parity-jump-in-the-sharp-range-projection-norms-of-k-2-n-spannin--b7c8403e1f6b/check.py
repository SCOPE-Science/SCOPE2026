"""Exact integer checks for Fourier support of spanning trees of K_{2,n}.

Run: python3 check.py
Only the Python standard library is required.
"""
from fractions import Fraction
from itertools import combinations
from math import comb, prod


def fwht(values):
    """Unnormalized Walsh-Hadamard transform in place, integer arithmetic."""
    values = list(values)
    stride = 1
    while stride < len(values):
        for base in range(0, len(values), 2 * stride):
            for j in range(base, base + stride):
                x, y = values[j], values[j + stride]
                values[j] = x + y
                values[j + stride] = x - y
        stride *= 2
    return values


def is_tree(edge_subset, n):
    """Independent connectivity/acyclicity check on 2+n vertices."""
    parents = list(range(n + 2))

    def find(i):
        while parents[i] != i:
            i = parents[i]
        return i

    for e in edge_subset:
        vertex = 2 + e % n
        side = e // n
        a, b = find(side), find(vertex)
        if a == b:
            return False
        parents[a] = b
    return len({find(i) for i in range(n + 2)}) == 1


def direct_coeff(mask, n):
    s = [(-1 if mask & (1 << i) else 1) for i in range(n)]
    t = [(-1 if mask & (1 << (n + i)) else 1) for i in range(n)]
    return sum(s[j] * t[j] * prod(s[i] + t[i] for i in range(n) if i != j)
               for j in range(n))


def expected_coeff(mask, n):
    s = [(-1 if mask & (1 << i) else 1) for i in range(n)]
    mismatch = [i for i in range(n) if bool(mask & (1 << i)) != bool(mask & (1 << (n + i)))]
    if len(mismatch) >= 2:
        return 0
    if len(mismatch) == 1:
        return -(1 << (n - 1)) * prod(s[i] for i in range(n) if i != mismatch[0])
    return (1 << (n - 1)) * prod(s) * sum(s)


def target_norm(n):
    central = comb(n, n // 2)
    if n % 2:
        return Fraction((n + 1) * central, 1 << n)
    alpha = Fraction(central, 1 << n)
    return alpha * (n + (1 << (n // 2))) - alpha**2


def verify(n):
    dimension = 2 * n
    size = 1 << dimension
    # Fully independent spanning-tree enumeration, not the one-double-leaf formula.
    support = [0] * size
    for es in combinations(range(dimension), n + 1):
        if is_tree(es, n):
            mask = sum(1 << i for i in es)
            support[mask] = 1
    assert sum(support) == n * (1 << (n - 1))
    coeff = fwht(support)
    for mask, w in enumerate(coeff):
        assert w == direct_coeff(mask, n), (n, mask, w, direct_coeff(mask, n))
        assert w == expected_coeff(mask, n), (n, mask, w, expected_coeff(mask, n))
    frequency_support = [int(w != 0) for w in coeff]
    rank = sum(frequency_support)
    assert rank == (n + 1) * (1 << n) - (comb(n, n // 2) if n % 2 == 0 else 0)
    abs_nonzero = [abs(w) for w in coeff if w]
    assert min(abs_nonzero) == (1 << (n - 1))
    assert max(abs_nonzero) == n * (1 << (n - 1))
    projection_kernel = fwht(frequency_support)
    norm = Fraction(sum(abs(v) for v in projection_kernel), size)
    assert norm == target_norm(n), (n, norm, target_norm(n))
    return rank, norm


def verify_balanced(n):
    assert n % 2 == 0
    m = n // 2
    for z in range(n + 1):
        b = sum((-1)**j * comb(z, j) * comb(n-z, m-j)
                for j in range(max(0, m-(n-z)), min(z, m)+1))
        expected = (0 if z % 2 else
                    (-1)**(z//2) * comb(n, m) * comb(m, z//2)//comb(n, z))
        assert b == expected, (n, z, b, expected)


if __name__ == '__main__':
    for n in range(2, 9):
        rank, norm = verify(n)
        if n % 2 == 0:
            verify_balanced(n)
        print(f'n={n}; frequencies={1<<(2*n)}; nonzero={rank}; projection_norm={norm}')
    for n in range(2, 51, 2):
        verify_balanced(n)
    print('K2N_TREE_SUPPORT_EXACT_CHECKS_PASS')

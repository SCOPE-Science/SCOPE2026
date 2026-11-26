"""Exact small-dimensional check of automorphisms of binary perfect evolution algebras.

Run with Python 3; no third-party dependencies are required.
"""
from itertools import product, permutations
from math import comb, prod


def rank_binary(rows, n):
    a = list(rows)
    r = 0
    for c in range(n):
        piv = next((j for j in range(r, n) if a[j] & (1 << c)), None)
        if piv is None:
            continue
        a[r], a[piv] = a[piv], a[r]
        for j in range(n):
            if j != r and a[j] & (1 << c):
                a[j] ^= a[r]
        r += 1
    return r


def centralizer_count(n):
    assert n >= 2
    m = n - 2
    gl = lambda k: prod((2**k - 2**j) for j in range(k))
    return 2**(2*n - 3) * gl(m)


def check(n):
    ps = list(permutations(range(n)))
    trans = [j for j, p in enumerate(ps) if sum(i != p[i] for i in range(n)) == 2]
    maps = []
    for p in ps:
        maps.append([sum(((row >> j) & 1) << p[j] for j in range(n)) for row in range(1 << n)])
    inv = 0
    fixed = [0 for _ in ps]
    nontriv = 0
    single_trans = 0
    for rows in product(range(1 << n), repeat=n):
        if rank_binary(rows, n) != n:
            continue
        inv += 1
        stabilizers = []
        for idx, p in enumerate(ps):
            if all(rows[p[i]] == maps[idx][rows[i]] for i in range(n)):
                fixed[idx] += 1
                if any(i != p[i] for i in range(n)):
                    stabilizers.append(idx)
        nontriv += bool(stabilizers)
        single_trans += len(stabilizers) == 1 and stabilizers[0] in trans
    expected = centralizer_count(n)
    assert all(fixed[i] == expected for i in trans), (n, expected, [fixed[i] for i in trans])
    assert fixed[ps.index(tuple(range(n)))] == inv, (n, inv)
    print(f'n={n}: GL={inv}; transposition fixed={expected} each; nontrivial={nontriv}; exactly-C2-transposition={single_trans}; asymptotic main count={comb(n, 2)*expected}')
    return inv, nontriv, single_trans


if __name__ == '__main__':
    for n in (2, 3, 4):
        check(n)
    print('VERIFY_OK')

#!/usr/bin/env python3
"""Independent finite checks for even-cardinality circular-arc shattering."""
from itertools import combinations
from math import comb


def hypotheses(n):
    result = {0, (1 << n) - 1}
    for length in range(2, n, 2):
        for start in range(n):
            result.add(sum(1 << ((start + j) % n) for j in range(length)))
    return result


def shattered(support, hypotheses_):
    mask = sum(1 << x for x in support)
    return len({h & mask for h in hypotheses_}) == 1 << len(support)


def consecutive(s, n):
    return any({j % n, (j + 1) % n, (j + 2) % n} == set(s) for j in range(n))


def boundary_rank_mod2(n, triangles):
    edges = list(combinations(range(n), 2))
    index = {e: i for i, e in enumerate(edges)}
    basis = {}
    for tri in triangles:
        v = 0
        for edge in combinations(tri, 2):
            v ^= 1 << index[edge]
        while v:
            pivot = v.bit_length() - 1
            if pivot not in basis:
                basis[pivot] = v
                break
            v ^= basis[pivot]
    return len(basis)


def main():
    for n in range(4, 20, 2):
        H = hypotheses(n)
        f = [1]
        for k in range(1, 5):
            count = 0
            for S in combinations(range(n), k):
                sh = shattered(S, H)
                expected = k <= 2 or (k == 3 and not consecutive(S, n))
                assert sh == expected, (n, k, S, sh, expected)
                count += sh
            f.append(count)
        target = [1, n, comb(n, 2), comb(n, 3) - n, 0]
        assert f == target, (n, f, target)
        assert len(H) == 2 + n * (n // 2 - 1)
        if n <= 14:
            triangles = [S for S in combinations(range(n), 3) if not consecutive(S, n)]
            r = boundary_rank_mod2(n, triangles)
            beta1 = comb(n, 2) - n + 1 - r
            beta2 = len(triangles) - r
            expect1 = 3 if n == 4 else 0
            expect2 = 0 if n == 4 else comb(n - 1, 3) - n
            assert (beta1, beta2) == (expect1, expect2)
            print(f'n={n} concepts={len(H)} faces={f} rank_F2_d2={r} beta1_F2={beta1} beta2_F2={beta2}')
        else:
            print(f'n={n} concepts={len(H)} faces={f}')
    print('PYTHON_FINITE_CHECKS_PASS')

if __name__ == '__main__':
    main()

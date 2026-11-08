#!/usr/bin/env python3
"""Exact finite checks for a binary transposition pointed magma theorem.

The operation is x * y = tau(y+x) + tau(x) on F_2^r, with tau
interchanging the two nonzero vectors (c,0) and (c,1).
No external packages are needed.
"""
from itertools import permutations, product
from math import factorial


def operation(rank):
    N = 1 << rank
    a, b = 2, 3
    def tau(x):
        return b if x == a else a if x == b else x
    return tuple(tuple(tau(x ^ y) ^ tau(x) for y in range(N))
                 for x in range(N))


def automorphism(f, op, pointed=True):
    N = len(op)
    if len(set(f)) != N or (pointed and f[0] != 0):
        return False
    return all(f[op[x][y]] == op[f[x]][f[y]]
               for x in range(N) for y in range(N))


def socle_size(rank):
    N = 1 << rank
    def tau(x):
        return 3 if x == 2 else 2 if x == 3 else x
    return sum(all(tau(x ^ h) == (tau(x) ^ tau(h)) for x in range(N))
               for h in range(N))


def linear(f):
    N = len(f)
    return all(f[x ^ y] == (f[x] ^ f[y]) for x in range(N) for y in range(N))


def quotient_perms(q):
    """Independently enumerate all phi with phi(0)=0, phi(u^1)=phi(u)^1."""
    c = 1
    pairs = [(u, u ^ c) for u in range(2, q) if u < (u ^ c)]
    # For q=2 there are no non-distinguished pairs.
    for order in permutations(pairs):
        for flips in product((0, 1), repeat=len(pairs)):
            phi = list(range(q))
            phi[0], phi[1] = 0, 1
            for (src0, src1), (dst0, dst1), flip in zip(pairs, order, flips):
                phi[src0], phi[src1] = ((dst0, dst1) if not flip else (dst1, dst0))
            assert len(set(phi)) == q
            yield tuple(phi)


def candidates(rank, pointed=True):
    q = 1 << (rank - 1)
    for phi in quotient_perms(q):
        for mask in range(1 << (q - 1)):
            for eta0 in ((0,) if pointed else (0, 1)):
                eta = [eta0] + [(mask >> (u - 1)) & 1 for u in range(1, q)]
                yield tuple(2 * phi[u] + (t ^ eta[u])
                            for u in range(q) for t in range(2))


def gl_size(k):
    a = 1
    for j in range(k):
        a *= (1 << k) - (1 << j)
    return a


def verify():
    for rank in range(2, 5):
        op = operation(rank)
        N = len(op)
        assert all(op[op[x][y]][op[x][z]] == op[op[y][x]][op[y][z]]
                   for x in range(N) for y in range(N) for z in range(N))
        print(f'CYCLE_IDENTITY rank={rank} verified')
    for rank in range(2, 6):
        size = socle_size(rank)
        expected = 4 if rank == 2 else 2
        assert size == expected, (rank, size, expected)
        print(f'SOCLE rank={rank} size={size}')
    for rank in (2, 3):
        op = operation(rank)
        N = 1 << rank
        actual = {tuple((0,) + p) for p in permutations(range(1, N))
                  if automorphism((0,) + p, op)}
        predicted = set(candidates(rank))
        assert actual == predicted
        print(f'EXHAUSTIVE_POINTED rank={rank} aut={len(actual)} linear={sum(map(linear,actual))}')
        unpointed = {p for p in permutations(range(N)) if automorphism(p, op, pointed=False)}
        assert unpointed == set(candidates(rank, pointed=False))
        assert len(unpointed) == 2 * len(actual)
        print(f'EXHAUSTIVE_UNPOINTED rank={rank} aut={len(unpointed)}')
    rank = 4
    op = operation(rank)
    seen = set()
    linear_count = 0
    for f in candidates(rank):
        assert f not in seen
        seen.add(f)
        assert automorphism(f, op)
        if linear(f):
            linear_count += 1
    q = 1 << (rank - 1)
    predicted = 2 ** (3 * q // 2 - 2) * factorial(q // 2 - 1)
    predicted_linear = (2 ** (2 * rank - 3)) * gl_size(rank - 2)
    assert (len(seen), linear_count) == (predicted, predicted_linear)
    print(f'CONSTRUCTIVE_POINTED rank={rank} aut={len(seen)} linear={linear_count}')
    seen_all = set()
    for f in candidates(rank, pointed=False):
        assert f not in seen_all
        seen_all.add(f)
        assert automorphism(f, op, pointed=False)
    assert len(seen_all) == 2 * predicted
    print(f'CONSTRUCTIVE_UNPOINTED rank={rank} aut={len(seen_all)}')
    for rank in (2, 3, 4, 5):
        q = 1 << (rank - 1)
        order = 2 ** (3 * q // 2 - 2) * factorial(q // 2 - 1)
        order_lin = 2 ** (2 * rank - 3) * gl_size(rank - 2)
        assert order % order_lin == 0
        print(f'FORMULA rank={rank} pointed={order} unpointed={2*order} linear_order={order_lin} index={order//order_lin}')
    print('VERIFY_OK')


if __name__ == '__main__':
    verify()

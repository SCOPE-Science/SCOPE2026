#!/usr/bin/env python3
"""Exact finite checks for Hamming-weight-two universal-cycle enumeration.

Uses only Python 3's standard library; finite tests are not the all-length proof.
"""
from itertools import permutations, product
from math import comb, factorial


def formula(q, n):
    m = n - 1
    return factorial(q - 1) ** (1 + m * (q - 1)) * q ** (m * (q - 2) + m // 2)


def words(q, m):
    return [w for w in product(range(q), repeat=m) if sum(a != 0 for a in w) <= 2]


def direct_tours(q, n):
    m = n - 1
    vertices = words(q, m)
    edges = words(q, n)
    root = (0,) * m
    exits = {v: [w for w in edges if w[:-1] == v] for v in vertices}
    special = [v for v in vertices if sum(a != 0 for a in v) == 1]
    assert len(edges) == 1 + n * (q - 1) + comb(n, 2) * (q - 1)**2
    assert set(exits[root][0]) == {0}
    # Root's first edge is fixed at 0^n, making a unique cyclic representative.
    root_orders = [(exits[root][0],) + r for r in permutations(exits[root][1:])]
    other_orders = [list(permutations(exits[v])) for v in special]
    answer = 0
    tours = set()
    for root_order in root_orders:
        for ordering in product(*other_orders):
            order = {v: tuple(exits[v]) for v in vertices}
            order[root] = root_order
            order.update(zip(special, ordering))
            nextindex = {v: 0 for v in vertices}
            seen = set()
            bits = []
            v = root
            for _ in range(len(edges)):
                idx = nextindex[v]
                if idx == len(order[v]):
                    break
                e = order[v][idx]
                nextindex[v] = idx + 1
                assert e not in seen
                seen.add(e)
                bits.append(e[-1])
                v = e[1:]
            if len(seen) == len(edges) and v == root:
                assert seen == set(edges)
                L = len(bits)
                windows = {tuple(bits[(i+j) % L] for j in range(n)) for i in range(L)}
                assert windows == set(edges)
                # Uniqueness under rotation: root->root self-loop is visited first.
                s = tuple(bits)
                assert s not in tours
                tours.add(s)
                answer += 1
    return answer


def bareiss(A):
    A = [r[:] for r in A]
    n = len(A)
    sign = 1
    prev = 1
    for k in range(n - 1):
        if A[k][k] == 0:
            i = next(i for i in range(k+1, n) if A[i][k] != 0)
            A[k], A[i] = A[i], A[k]
            sign *= -1
        t = A[k][k]
        for i in range(k+1, n):
            for j in range(k+1, n):
                num = A[i][j] * t - A[i][k] * A[k][j]
                assert num % prev == 0
                A[i][j] = num // prev
        for i in range(k+1, n):
            A[i][k] = 0
        prev = t
    return sign * A[-1][-1]


def exact_tree_check(q, n):
    m = n - 1
    colors = range(1, q)
    nodes = [(a, j) for a in colors for j in range(m)]
    ix = {v: i for i, v in enumerate(nodes)}
    M = [[0] * len(nodes) for _ in nodes]
    for (a,j),i in ix.items():
        M[i][i] += q
        if j < m - 1:
            M[i][ix[(a,j+1)]] -= 1
        for b in colors:
            M[i][ix[(b, m-1-j)]] -= 1
    return bareiss(M)


def main():
    for q in range(2, 6):
        for n in range(2, 10):
            tree = exact_tree_check(q,n)
            target = q**((n-1)*(q-2) + (n-1)//2)
            assert tree == target, (q,n,tree,target)
    for q,n in [(2,k) for k in range(2,12)] + [(3,2),(3,3),(3,4),(4,2)]:
        direct = direct_tours(q,n)
        target = formula(q,n)
        assert direct == target, (q,n,direct,target)
        print('q=%d n=%d exact_cycles=%d' % (q,n,direct))
    print('VERIFY_OK: full distinct-window Euler-tour enumeration and independent integer-tree determinants')

if __name__ == '__main__':
    main()

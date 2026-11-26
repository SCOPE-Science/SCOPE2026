#!/usr/bin/env python3
"""Independent exact checks for minimum one-limited domination in GP(n,3).

Standard-library only. The mathematical argument for all n is in RESULT.md.
"""
from math import comb


def rot(mask, amount, length):
    amount %= length
    full = (1 << length) - 1
    return ((mask << amount) | (mask >> (length - amount))) & full if amount else mask


def spin_solution(mask, n):
    """Direct bitwise neighbor test for a size-n perfect matching cut."""
    full = (1 << n) - 1
    left = rot(mask, 1, n)
    right = rot(mask, n - 1, n)
    if (mask ^ left) & (mask ^ right):
        return False
    both_same = (~((mask ^ left) | (mask ^ right))) & full
    v = mask ^ both_same
    x = v ^ rot(v, 3, n)
    y = v ^ rot(v, n - 3, n)
    z = v ^ mask
    return (x | y | z) == full and ((x & y) | (x & z) | (y & z)) == 0


def direct_graph_check(n, D):
    """Build the original graph, independently of the cyclic-spin equations."""
    N = 2 * n
    adj = [set() for _ in range(N)]
    for i in range(n):
        for x, y in ((i, (i + 1) % n),
                     (n + i, n + ((i + 3) % n)), (i, n + i)):
            adj[x].add(y)
            adj[y].add(x)
    assert all(len(a) == 3 for a in adj)
    return all((sum(1 for j in adj[i] if j in D) >= 1 if i not in D
                else sum(1 for j in adj[i] if j not in D) <= 1)
               for i in range(N))


def count_independent(n):
    """Exhaustive original graph-set test, without using derived spin equations."""
    answer = 0
    for mask in range(1 << (2 * n)):
        if mask.bit_count() != n:
            continue
        D = {i for i in range(2 * n) if (mask >> i) & 1}
        if direct_graph_check(n, D):
            answer += 1
    return answer


def all_spin_solutions(period):
    return [mask for mask in range(1 << period) if spin_solution(mask, period)]


def expected(n):
    return 2 + 4 * (n % 4 == 0) + 10 * (n % 5 == 0)


def check_laurent_factorization():
    """Exact integer-coefficient check of the recurrence's key factorization."""
    def multiply(a, b):
        out = {}
        for i, c in a.items():
            for j, d in b.items():
                out[i + j] = out.get(i+j, 0) + c*d
        return {i: c for i, c in out.items() if c}
    def add(a, b, scale=1):
        out = dict(a)
        for i, c in b.items():
            out[i] = out.get(i,0) + scale*c
        return {i: c for i,c in out.items() if c}
    first = {0: 1, 3: -1, -3: -1}
    second = {0: 1, 1: -1, -1: -1}
    lhs = {i+4: c for i,c in add(multiply(first,second), {0:1}, -1).items()}
    rhs = multiply(multiply(multiply({1:1,0:-1},{1:1,0:-1}),{2:1,0:1}),
                   {0:1,1:1,2:1,3:1,4:1})
    assert lhs == rhs, (lhs, rhs)
    print('LAURENT_FACTORIZATION_EXACT_INTEGER_OK')


def run():
    check_laurent_factorization()
    for n in (7, 8, 9):
        got = count_independent(n)
        assert got == expected(n), (n, got)
        print('DIRECT_GRAPH_EXHAUSTIVE', n, got, 'candidate sets', comb(2*n,n))

    sol20 = all_spin_solutions(20)
    assert len(sol20) == 16
    assert all(rot(u, 4, 20) == u or rot(u, 5, 20) == u for u in sol20)
    assert sum(rot(u, 4, 20) == u and rot(u, 5, 20) != u for u in sol20) == 4
    assert sum(rot(u, 5, 20) == u and rot(u, 4, 20) != u for u in sol20) == 10
    print('TWENTY_WORD_COMPLETE_EXHAUSTIVE',len(sol20))

    for n in range(7, 101):
        d = __import__('math').gcd(n,20)
        admissible = all_spin_solutions(d)
        assert len(admissible) == expected(n), (n,d,len(admissible))
        for mask in admissible:
            u = sum(((mask >> (i % d)) & 1) << i for i in range(n))
            assert spin_solution(u,n)
            prev = rot(u,1,n)
            nxt = rot(u,n-1,n)
            v = u ^ (~((u ^ prev)|(u ^ nxt)) & ((1<<n)-1))
            D = {i for i in range(n) if (u >> i)&1} | {n+i for i in range(n) if (v >> i)&1}
            assert len(D) == n and direct_graph_check(n,D)
    print('ALL_RESIDUE_CLASSES_AND_CONSTRUCTIONS_OK 7..100')
    print('VERIFY_OK')

if __name__=='__main__':
    run()

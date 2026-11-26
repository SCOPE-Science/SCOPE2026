"""Reproduce the finite checks for the alternating-word 010 complement theorem.

No third-party modules are required. All index tuples are one-based block indices.
"""
from collections import defaultdict, Counter
from itertools import combinations
from math import comb


def direct(n, pattern="010"):
    host = "01" * n
    fibers = defaultdict(list)
    for ix in combinations(range(2*n), 3):
        if "".join(host[p] for p in ix) == pattern:
            removed = set(ix)
            residual = "".join(ch for p, ch in enumerate(host) if p not in removed)
            fibers[residual].append(tuple(ix))
    return fibers


def by_block_indices(n):
    host = "01" * n
    fibers = defaultdict(list)
    for i in range(1, n+1):
        for j in range(i, n+1):
            for k in range(j+1, n+1):
                forbidden = {2*i-2, 2*j-1, 2*k-2}
                residual = "".join(ch for p, ch in enumerate(host) if p not in forbidden)
                fibers[residual].append((i, j, k))
    return fibers


def predicted(n):
    host = "01" * n
    fibers = defaultdict(list)
    for t in range(1, n):
        exceptional = ("01"*(n-1))[:2*t-2] + ("01"*(n-1))[2*t-1:]
        # The labels here identify each of the n-1 embeddings rather than their positions.
        fibers[exceptional] = [('E', t, x) for x in range(n-1)]
    for i in range(1, n+1):
        for j in range(i+1, n+1):
            for k in range(j+2, n+1):
                forbidden = {2*i-2, 2*j-1, 2*k-2}
                residual = "".join(ch for p, ch in enumerate(host) if p not in forbidden)
                assert residual not in fibers, (n, i, j, k, residual)
                fibers[residual] = [(i, j, k)]
    return fibers


def run():
    small, larger, reverse = 0, 0, 0
    for n in range(3, 18):
        literal = direct(n)
        block = by_block_indices(n)
        assert set(literal)==set(block)
        assert {s:len(t) for s,t in literal.items()} == {s:len(t) for s,t in block.items()}
        predicted_fibers = predicted(n)
        assert {s:len(t) for s,t in literal.items()} == {s:len(t) for s,t in predicted_fibers.items()}
        assert len(literal) == comb(n-1,3) + n-1
        assert Counter(map(len,literal.values())) == (Counter({1:comb(n-1,3), n-1:n-1}) if n>=4 else Counter({2:2}))
        assert sum(map(len,literal.values())) == comb(n+1,3)
        # Reverse-complement is an automorphism of the alternating source.
        rc = lambda w: ''.join('1' if c=='0' else '0' for c in w[::-1])
        mirror = direct(n,'101')
        assert {rc(k):len(v) for k,v in literal.items()} == {k:len(v) for k,v in mirror.items()}
        small += 1; reverse += 1
    for n in (18,23,30,40,50,70):
        actual=by_block_indices(n)
        expected=predicted(n)
        assert {k:len(v) for k,v in actual.items()} == {k:len(v) for k,v in expected.items()}
        assert len(actual)==comb(n-1,3)+n-1
        larger+=1
    print(f'COMPLEMENT_010_VERIFY_OK n=3..17 direct 3-position extraction, block-index extraction, expected full fibers: {small} cases')
    print(f'COMPLEMENT_010_MIRROR_OK reverse-complement, {reverse} cases')
    print(f'COMPLEMENT_010_LARGE_OK explicit full block enumeration, {larger} cases through n=70')
    print('Finite tests are independent checks, not a proof for all n.')

if __name__=='__main__':
    run()

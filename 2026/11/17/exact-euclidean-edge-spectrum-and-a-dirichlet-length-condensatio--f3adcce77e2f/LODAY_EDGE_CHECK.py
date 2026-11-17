"""Exact finite checks of the Euclidean edge spectrum of Loday associahedra.

Use: python3 LODAY_EDGE_CHECK.py
Requires only the Python 3 standard library. Asymptotic claims are proved in RESULT.md,
not inferred from these finite checks.
"""
from collections import Counter
from functools import lru_cache
from math import comb

LEAF = '*'

@lru_cache(None)
def trees(leaves):
    if leaves == 1:
        return (LEAF,)
    return tuple((left, right) for k in range(1, leaves)
                 for left in trees(k) for right in trees(leaves - k))

@lru_cache(None)
def size(tree):
    return 1 if tree == LEAF else size(tree[0]) + size(tree[1])

def coordinates(tree):
    if tree == LEAF:
        return ()
    left, right = tree
    return coordinates(left) + (size(left)*size(right),) + coordinates(right)

def right_rotations(tree):
    """List of (new_tree, size_A, size_C) from each ((A B) C) -> (A (B C))."""
    if tree == LEAF:
        return []
    left, right = tree
    result = []
    if left != LEAF:
        a, b = left
        result.append(((a, (b, right)), size(a), size(right)))
    result.extend(((s, right), a, c) for s, a, c in right_rotations(left))
    result.extend(((left, s), a, c) for s, a, c in right_rotations(right))
    return result

def catalan(k):
    return comb(2*k, k)//(k+1)

def predicted(a, c, N):
    r = N-a-c
    if min(a,c,r) < 1:
        return 0
    return catalan(a-1)*catalan(c-1)*comb(2*r, r)//2

def check(N):
    observed = Counter()
    seen = set()
    for t in trees(N):
        v = coordinates(t)
        for s, a, c in right_rotations(t):
            assert size(s) == N
            key = (t, s)
            assert key not in seen
            seen.add(key)
            diff = [x-y for x,y in zip(coordinates(s),v)]
            assert sum(diff) == 0
            assert Counter(d for d in diff if d) == Counter((a*c, -a*c))
            observed[a,c] += 1
    expected = {(a,c): predicted(a,c,N) for a in range(1,N-1)
                for c in range(1,N-a)}
    assert all(observed[a,c] == count for (a,c), count in expected.items())
    assert len(seen) == sum(expected.values()) == (N-2)*catalan(N-1)//2
    weighted = sum(a*c*observed[a,c] for a,c in observed)
    asserted = ((2*N-3)*comb(2*N-4,N-2)-4**(N-2))//2
    assert weighted == asserted
    mult = Counter()
    for (a,c),count in observed.items():
        mult[a*c] += count
    assert max(mult) == ((N-1)//2)*((N-1+1)//2)
    print(f'N={N} vertices={len(trees(N))} edges={len(seen)} '
          f'edge_length_over_sqrt2_total={weighted} distinct_lengths={len(mult)}')

if __name__ == '__main__':
    for N in range(3,9):
        check(N)
    print('LODAY_EDGE_SPECTRUM_PASS')

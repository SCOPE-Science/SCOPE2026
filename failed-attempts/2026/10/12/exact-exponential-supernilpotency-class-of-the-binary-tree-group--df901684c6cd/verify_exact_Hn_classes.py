#!/usr/bin/env python3
from functools import lru_cache


def level(i: int) -> int:
    return i.bit_length() - 1


def verify(n: int):
    N = (1 << n) - 1
    cutoff = (1 << (n-1)) - 1

    def mul(i, j):
        if i == 0 or j == 0:
            return 0
        if i % 2 == 0 and j == i + 1 and i // 2 <= cutoff:
            return i // 2
        return 0

    @lru_cache(None)
    def max_leaves(i):
        if i == 0:
            return 0
        best = 1  # the one-leaf variable/constant term evaluating directly to a_i
        if i <= cutoff:
            best = max(best, max_leaves(2*i) + max_leaves(2*i+1))
        return best

    @lru_cache(None)
    def max_depth(i):
        if i == 0:
            return -1
        best = 0
        if i <= cutoff:
            best = max(best, 1 + max(max_depth(2*i), max_depth(2*i+1)))
        return best

    # Capacity invariant used in the proof.
    for i in range(1, N+1):
        cap = 1 << (n - 1 - level(i))
        assert max_leaves(i) == cap, (n, i, max_leaves(i), cap)
        assert max_depth(i) == n - 1 - level(i), (n, i, max_depth(i))

    # Every nonzero multiplication has additive capacity.
    for i in range(1, cutoff+1):
        left, right = 2*i, 2*i+1
        assert mul(left, right) == i
        cap_i = 1 << (n - 1 - level(i))
        cap_l = 1 << (n - 1 - level(left))
        cap_r = 1 << (n - 1 - level(right))
        assert cap_l + cap_r == cap_i

    # The complete balanced bottom product realizes the maxima at a_1.
    frontier = list(range(1 << (n-1), 1 << n))
    depth = 0
    while len(frontier) > 1:
        nxt = []
        for k in range(0, len(frontier), 2):
            z = mul(frontier[k], frontier[k+1])
            assert z != 0
            nxt.append(z)
        frontier = nxt
        depth += 1
    assert frontier == [1]
    assert depth == n-1
    assert max_leaves(1) == (1 << (n-1))

    return {
        "n": n,
        "size": N + 1,
        "max_nonzero_term_leaves": max_leaves(1),
        "max_nonzero_term_depth": max_depth(1),
        "nilpotency_parameter": n,
        "supernilpotency_parameter": 1 << (n-1),
    }


if __name__ == "__main__":
    for n in range(3, 11):
        r = verify(n)
        print("n={n} size={size} max_leaves={max_nonzero_term_leaves} max_depth={max_nonzero_term_depth} nil={nilpotency_parameter} super={supernilpotency_parameter}".format(**r))
    print("VERIFY_OK")

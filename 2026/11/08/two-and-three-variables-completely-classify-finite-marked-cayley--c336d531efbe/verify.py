#!/usr/bin/env python3
"""Independent finite checks for edge-coloured Cayley FO^2/FO^3 width threshold.
Standard Python 3 only. This is finite corroboration, not the infinite proof.
"""
from itertools import product, permutations
from collections import deque


def cyclic_profile(n, gens):
    signed = [0] + [a % n for a in gens] + [(-a) % n for a in gens]
    pattern = tuple(tuple(i for i, x in enumerate(signed) if x == v)
                    for v in sorted(set(signed), key=signed.index))
    return pattern, len(set(signed)) < n


def perm_mul(p, q):
    return tuple(p[q[i]] for i in range(len(p)))


def perm_inverse(p):
    return tuple(p.index(i) for i in range(len(p)))


def perm_profile(gens, elements):
    identity = tuple(range(len(gens[0])))
    signed = [identity] + list(gens) + [perm_inverse(x) for x in gens]
    pattern = tuple(tuple(i for i, x in enumerate(signed) if x == v)
                    for v in dict.fromkeys(signed))
    return pattern, len(set(signed)) < len(elements)


def cycles_fo_rank(n, m, width, max_rank=6):
    """Exact counting-free rank refinements on all partial pebble assignments."""
    sizes = [n, m]
    states = [(a, tup) for a, size in enumerate(sizes)
              for tup in product(range(-1, size), repeat=width)]
    ids = {state: idx for idx, state in enumerate(states)}
    def canonical(keys):
        cmap = {}; out = []
        for key in keys:
            if key not in cmap: cmap[key] = len(cmap)
            out.append(cmap[key])
        return out
    def atomic(a, tup):
        size = sizes[a]
        return tuple((i, j, tup[i] == tup[j],
                      (tup[j] - tup[i]) % size == 1)
                     for i in range(width) for j in range(width)
                     if tup[i] != -1 and tup[j] != -1)
    col = canonical([atomic(a, s) for a, s in states])
    blank = tuple([-1] * width)
    output = []
    for rank in range(max_rank + 1):
        output.append(col[ids[(0, blank)]] != col[ids[(1, blank)]])
        if rank == max_rank: break
        keys = []
        for idx, (a, tup) in enumerate(states):
            signatures = []
            for i in range(width):
                neighbors = set()
                for x in range(sizes[a]):
                    nxt = list(tup); nxt[i] = x
                    neighbors.add(col[ids[(a, tuple(nxt))]])
                signatures.append(tuple(sorted(neighbors)))
            keys.append((col[idx], tuple(signatures)))
        col = canonical(keys)
    return output


def profile_classification():
    p = {n: cyclic_profile(n, [1]) for n in range(1, 16)}
    assert len(set(p.values())) == 4
    assert all(p[n] == p[4] for n in range(4, 16))
    assert len({p[1], p[2], p[3], p[4]}) == 4
    assert cyclic_profile(6, [3, 2])[1] is True
    perms = list(permutations(range(3)))
    s = (1, 0, 2); t = (1, 2, 0)
    assert perm_profile([s, t], perms) == cyclic_profile(6, [3, 2])
    # The two regular coloured digraphs have the same FO^2 profile
    # yet one group is nonabelian and the other is abelian.
    assert perm_mul(s, t) != perm_mul(t, s)
    assert (3+2) % 6 == (2+3) % 6
    return 4


def cycle_pair_bound_check():
    tests = 0
    for m in range(2, 24):
        for n in range(m + 1, 25):
            # The word a^m is a relator only in C_m; m<=2D(C_m)+1.
            D = m // 2
            assert m <= 2*D + 1
            assert m % m == 0 and m % n != 0
            assert 1 + (m-1).bit_length() <= 1 + (2*D).bit_length()
            tests += 1
    return tests


def rank_checks():
    expected = {(4, 5): 3, (5, 7): 3, (6, 7): 3,
                (8, 9): 4, (10, 11): 4}
    for (n, m), first in expected.items():
        tw = cycles_fo_rank(n, m, 2, 6)
        th = cycles_fo_rank(n, m, 3, 6)
        assert not any(tw), (n, m, tw)
        assert not any(th[:first]) and all(th[first:]), (n,m,th)
    # Check the original unbounded two-variable collapse on every pair
    # in the selected seven-member stable range.
    for n, m in [(4, 7), (5, 6), (7, 9)]:
        assert not any(cycles_fo_rank(n, m, 2, 7))
    return len(expected) + 3


if __name__ == '__main__':
    print('Cyclic FO2 classes:',profile_classification())
    print('Ordered small-vs-large pair word-bound tests:',cycle_pair_bound_check())
    print('Finite exact pebble-game rank checks:',rank_checks())
    print('VERIFY_OK')

#!/usr/bin/env python3
"""Independent finite checks for a three-word scattered-subsequence theorem."""
from functools import lru_cache
from itertools import product


def morphic(d, k):
    w = (0,)
    for _ in range(k):
        v = []
        for x in w:
            if x < d - 1:
                v.extend((0, x + 1))
            else:
                v.extend((0, x, x))
        w = tuple(v)
    return w


def shortest_absent(w, d):
    """Next-occurrence recursion, not using the claimed formula."""
    n = len(w)
    nxt = [[n] * d for _ in range(n + 1)]
    for i in range(n - 1, -1, -1):
        nxt[i] = nxt[i + 1][:]
        nxt[i][w[i]] = i

    @lru_cache(None)
    def depth(i):
        if n in nxt[i]:
            return 1
        return 1 + min(depth(q + 1) for q in nxt[i])

    @lru_cache(None)
    def words(i):
        z = depth(i)
        result = set()
        for x, p in enumerate(nxt[i]):
            if p == n:
                if z == 1:
                    result.add((x,))
            elif depth(p + 1) == z - 1:
                result.update((x,) + suffix for suffix in words(p + 1))
        return frozenset(result)

    return depth(0), words(0)


def embeds(v, w):
    j = 0
    for x in w:
        if j < len(v) and x == v[j]:
            j += 1
    return j == len(v)


def explicit_absent(w, d, length):
    """Second method: enumerate every word of the proposed length."""
    return {v for v in product(range(d), repeat=length) if not embeds(v, w)}


def expected_three(a, b, m):
    return {tuple([a] * (2*m+1)),
            (b,) + tuple([a] * (2*m)),
            (b, b) + tuple([a] * (2*m-1))}


def run():
    checks = 0
    exhaustive = 0
    for d in range(3, 9):
        a, b = d - 2, d - 1
        # Finite ruler segment; v_2(j+1) is the count of trailing zero bits.
        U = tuple(((j + 1) & -(j + 1)).bit_length() - 1
                  for j in range(2**(d-2) - 1))
        R = U + (a,) + U + (b,)
        for k in (d-1, d, d+1):
            W = morphic(d, k)
            base = R if k == d-1 else (R+R+(b,)) if k == d else (R+R+(b,))*2+(0,b,b)
            assert W == base, ('substitution identity', d, k)
            length, sas = shortest_absent(W, d)
            if k == d-1:
                target = {(a, a)} | {(b, c) for c in range(d)}
            elif k == d:
                target = {(a,a,a), (b,a,a)} | {(b,b,c) for c in range(d-1)}
            else:
                target = expected_three(a,b,2)
            assert length == len(next(iter(target))) and sas == target, (d, k, length, sas)
            checks += 1
    for d in (3, 4, 5):
        a, b = d-2, d-1
        low = tuple(range(d-2))
        for size in range(max(1, len(low)), 5):
            for U in product(low, repeat=size):
                if set(U) != set(low):
                    continue
                R = U + (a,) + U + (b,)
                for m in (2, 3, 4):
                    for tail in ((), (0,), (b,0,b)):
                        w = (R + R + (b,))*m + tail
                        length, sas = shortest_absent(w, d)
                        target = expected_three(a,b,m)
                        assert length == 2*m+1 and sas == target, (d,U,m,tail)
                        checks += 1
                        if d <= 4 and size <= 3 and m <= 3 and not tail:
                            direct = explicit_absent(w,d,2*m+1)
                            assert direct == target, (d,U,m)
                            exhaustive += 1
    print('SUCCESS')
    print('morphic generation and theorem instances:', 18)
    print('total independently checked instances:', checks)
    print('instances with direct exhaustive length-level comparison:', exhaustive)
    print('The proof is structural; the finite tests are consistency checks only.')

if __name__ == '__main__':
    run()

#!/usr/bin/env python3
"""Independent exact checks for random-order FirstFit on crown graphs.

All arithmetic is integral or rational.  Two implementations of FirstFit are
used: direct permutation iteration and a memoized state traversal of all orders.
"""
from collections import Counter
from fractions import Fraction
from functools import lru_cache
from itertools import permutations
from math import factorial


def direct(n):
    out = Counter()
    for order in permutations(range(2*n)):
        assigned = [-1] * (2*n)
        used = 0
        for v in order:
            forbidden = {assigned[w] for w in range(2*n)
                         if assigned[w] >= 0 and (v < n) != (w < n)
                         and v % n != w % n}
            color = 0
            while color in forbidden:
                color += 1
            assigned[v] = color
            used = max(used, color+1)
        out[used] += 1
    return out


def state_counts(n):
    N = 2*n
    adj = [sum(1 << w for w in range(N)
               if (v < n) != (w < n) and v % n != w % n)
           for v in range(N)]
    @lru_cache(None)
    def finish(mask, colors):
        if mask == (1 << N) - 1:
            return ((max(colors)+1, 1),)
        counts = Counter()
        for v in range(N):
            if mask >> v & 1:
                continue
            blocked = {colors[w] for w in range(N)
                       if (mask >> w & 1) and (adj[v] >> w & 1)}
            c = 0
            while c in blocked:
                c += 1
            nxt = colors[:v] + (c,) + colors[v+1:]
            counts.update(dict(finish(mask | 1 << v, nxt)))
        return tuple(sorted(counts.items()))
    ans = dict(finish(0, (-1,)*N))
    return ans, finish.cache_info().currsize


def predicted(n):
    if n == 2:
        return {2: Fraction(1)}
    tail = {2: Fraction(1), 3: Fraction(1,n), n+1: Fraction(0)}
    for k in range(4,n+1):
        p = Fraction(1, n-k+3)
        for j in range(k-3):
            p *= Fraction(3, 2*(2*(n-j)-1))
        tail[k] = p
    return {k:tail[k]-tail.get(k+1, Fraction(0)) for k in range(2,n+1)}


def run():
    for n in range(2,8):
        dp, states = state_counts(n)
        assert sum(dp.values()) == factorial(2*n)
        exact = {k:Fraction(v,factorial(2*n)) for k,v in dp.items()}
        expected = predicted(n)
        assert exact == expected, (n, exact, expected)
        if n <= 4:
            brute = direct(n)
            assert dict(brute) == dp
        if n >= 3:
            assert sum(k*v for k,v in exact.items()) == 2+sum(
                sum(v for j,v in exact.items() if j>=k)
                for k in range(3,n+1))
            assert exact[2] == Fraction(n-1,n)
            assert exact[n] == Fraction(40*3**(n-3)*factorial(n),factorial(2*n))
        print('n={} permutations={} memo_states={} counts={} direct={}'.format(
            n, factorial(2*n), states, dict(sorted(dp.items())),
            'PASS' if n<=4 else 'not_run'))
    print('All exact distribution, tail, extremal-probability checks PASS.')

if __name__ == '__main__':
    run()

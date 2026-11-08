#!/usr/bin/env python3
"""Exact finite checks for the n-Sun probabilistic zero-forcing formulas.

Uses only the Python standard library. The all-n proof is given in RESULT.md;
these exact finite checks are independent diagnostics, not an infinite certificate.
"""
from fractions import Fraction as Q
from functools import lru_cache

checks = 0

def agree(lhs, rhs, name):
    global checks
    assert lhs == rhs, f"{name}: {lhs} != {rhs}"
    checks += 1


def closed_core(n):
    assert n >= 5
    return (Q(11*n, 16) + Q(4437, 3344)
            + Q(1323, 6688) * (-Q(2, 9))**(n-2)
            - Q(147, 608) * (-Q(2, 5))**(n-2))


def closed_difference(n):
    assert n >= 6
    return (Q(11, 16)
            - Q(1617, 6688) * (-Q(2, 9))**(n-3)
            + Q(1029, 3040) * (-Q(2, 5))**(n-3))


def closed_leaf_minus_core(n):
    return (Q(41, 152)
            - Q(27, 608) * (-Q(2, 9))**(n-2)
            + Q(147, 608) * (-Q(2, 5))**(n-2))


def interval_values(max_m):
    a = [Q(0), Q(89, 80)]
    b = [Q(0), Q(1)]
    c = [Q(0), Q(1)]
    for m in range(2, max_m+1):
        bm = 1 + a[m-1]/9 + b[m-1]*Q(2, 9) + a[m-2]*Q(2, 3)
        cm = 1 + a[m-2]
        am = Q(81, 80) * (
            1 + Q(4, 81)*(bm+cm)
            + Q(4, 27)*a[m-1] + Q(8, 27)*b[m-1]
            + Q(4, 9)*a[m-2])
        a.append(am)
        b.append(bm)
        c.append(cm)
    return a, b, c


def brute_full_graph(n, first):
    """Independent 2n-vertex Markov calculation without frontier reduction."""
    adj = [[] for _ in range(2*n)]
    for v in range(n):
        adj[v] = [(v-1)%n, (v+1)%n, n+v]
        adj[n+v] = [v]
    done = (1 << (2*n)) - 1
    @lru_cache(None)
    def e(mask):
        if mask == done:
            return Q(0)
        white = []
        for v in range(2*n):
            if mask & (1 << v):
                continue
            survival = Q(1)
            for u in adj[v]:
                if mask & (1 << u):
                    blue_closed = 1 + sum(bool(mask & (1 << w)) for w in adj[u])
                    survival *= 1-Q(blue_closed, len(adj[u]))
            if survival < 1:
                white.append((v, 1-survival))
        assert white
        branches = {0: Q(1)}
        for v,p in white:
            nxt = {}
            for delta,weight in branches.items():
                nxt[delta] = nxt.get(delta, Q(0)) + weight*(1-p)
                add = delta | (1 << v)
                nxt[add] = nxt.get(add, Q(0)) + weight*p
            branches = nxt
        no_change = branches.pop(0)
        assert no_change < 1
        return (1 + sum(weight*e(mask|delta) for delta,weight in branches.items()))/(1-no_change)
    out = e(1 << first)
    return out, e.cache_info().currsize


def main():
    a,b,c = interval_values(110)
    agree(a[0], 0, 'a0')
    agree(a[1], Q(89,80), 'a1')
    for m in range(2, 111):
        agree(b[m], 1 + a[m-1]/9 + Q(2,9)*b[m-1] + Q(2,3)*a[m-2], f'b{m}')
        agree(c[m], 1+a[m-2], f'c{m}')
        agree(Q(80,81)*a[m], 1 + Q(4,81)*(b[m]+c[m]) + Q(4,27)*a[m-1] + Q(8,27)*b[m-1] + Q(4,9)*a[m-2], f'a{m}')
    for n in range(5, 110):
        h = Q(9,8)+(b[n-2]+a[n-3])/2
        u = Q(63,38)+(8*a[n-2]+6*b[n-2]+5*a[n-3])/19
        core = u+1
        leaf = h+2
        agree(core, closed_core(n), f'core{n}')
        agree(leaf-core, closed_leaf_minus_core(n), f'leaf-gap{n}')
        assert leaf > core
        if n >= 6:
            agree(core-closed_core(n-1), closed_difference(n), f'increment{n}')
    # The preceding sequence check does not prove an all-n identity.
    # These independent full-graph computations check the uncompressed rules.
    for n in (5, 6):
        u,nu = brute_full_graph(n, 0)
        h,nh = brute_full_graph(n, n)
        agree(u, closed_core(n), f'full-Markov core{n}')
        agree(h-u, closed_leaf_minus_core(n), f'full-Markov leafgap{n}')
        print(f'n={n}: core={u}, leaf={h}, visited states={nu}+{nh}')
    # These are the original paper's displayed decimals, used only for diagnostics.
    paper = {5:'4.77765692007797', 6:'5.44614700021659',
             7:'6.14172265492263', 8:'6.82588757375988',
             9:'7.51474489939839', 10:'8.20169679288223'}
    for n, shown in paper.items():
        assert abs(float(closed_core(n))-float(shown)) < 0.00000000000002
        globals()['checks'] += 1
    print(f'PASS: {checks} exact equalities plus {len(paper)} numerical display comparisons')


if __name__ == '__main__':
    main()

"""Independent coefficient and cochain-matrix checks of the Betti formulas.

Python standard library only.  The Lie bracket is [t,y_i]=x_i; the
Chevalley--Eilenberg differential of x_i^* is -t^* wedge y_i^*.
Direct rank computation does not use the proof's tensor decomposition.
"""
from itertools import combinations
from math import comb


def degree_masks(n, k):
    return [sum(1 << j for j in c) for c in combinations(range(n), k)]


def rank_mod_p(columns, p):
    pivots = {}
    for column in columns:
        v = dict(column)
        while v:
            j = max(v)
            a = v[j] % p
            if not a:
                del v[j]
                continue
            if j not in pivots:
                inverse = pow(a, -1, p)
                pivots[j] = {k: (value * inverse) % p
                             for k, value in v.items() if value % p}
                break
            pivot = pivots[j]
            for k, value in pivot.items():
                t = (v.get(k, 0) - a * value) % p
                if t:
                    v[k] = t
                else:
                    v.pop(k, None)
    return len(pivots)


def differential_ranks(r, s, p):
    n = 2 * r + s + 1
    ranks = []
    for k in range(n + 1):
        targets = degree_masks(n, k + 1) if k < n else []
        position = {mask: i for i, mask in enumerate(targets)}
        columns = []
        for mask in degree_masks(n, k):
            column = {}
            if not (mask & 1):
                for i in range(r):
                    x = 1 << (2 * i + 1)
                    y = 1 << (2 * i + 2)
                    if mask & x and not mask & y:
                        output = (mask ^ x) | y | 1
                        j = position[output]
                        column[j] = (column.get(j, 0) - 1) % p
            columns.append(column)
        ranks.append(rank_mod_p(columns, p))
    return ranks


def polynomial_product(a, b):
    output = [0] * (len(a) + len(b) - 1)
    for i, x in enumerate(a):
        for j, y in enumerate(b):
            output[i + j] += x * y
    return output


def polynomial_2(r, s):
    part = [(comb(2 * r, k) +
             (comb(r, k // 2) if k % 2 == 0 else 0)) // 2
            for k in range(2 * r + 1)]
    return polynomial_product(part, [comb(s + 1, k) for k in range(s + 2)])


def kernel_0(r):
    a = []
    for i in range(2 * r + 1):
        if i % 2 == 0:
            a.append(comb(r, i // 2) ** 2)
        else:
            a.append(comb(r, i // 2) * comb(r, i // 2 + 1))
    return a


def polynomial_0(r, s):
    return polynomial_product(kernel_0(r),
                              [comb(s + 1, k) for k in range(s + 2)])


def betti_from_ranks(n, ranks):
    return [comb(n, k) - (ranks[k-1] if k else 0) - ranks[k]
            for k in range(n + 1)]


def check(r, s, odd=False):
    n = 2 * r + s + 1
    two = betti_from_ranks(n, differential_ranks(r, s, 2))
    assert two == polynomial_2(r, s), (r, s, 'characteristic two', two)
    assert sum(two) == (4 ** r + 2 ** r) * 2 ** s
    if odd:
        # The odd-prime check corroborates, but is not used to establish,
        # the characteristic-zero rank formula.
        odd_betti = betti_from_ranks(n, differential_ranks(r, s, 1009))
        assert odd_betti == polynomial_0(r, s), (r, s, 'odd prime', odd_betti)
    tau = polynomial_product(
        [0] + [a-b for a, b in zip(
            [(comb(2*r,k)+(comb(r,k//2) if k%2==0 else 0))//2
             for k in range(2*r+1)], kernel_0(r))],
        [comb(s, k) for k in range(s+1)])
    assert all(c >= 0 for c in tau)
    print('r=%d s=%d P2=%s two_primary_ranks=%s' % (r, s, two, tau))
    return two, tau

if __name__ == '__main__':
    for r, s in [(0,0), (1,0), (1,2), (2,0), (2,2),
                 (3,0), (3,1), (4,0), (4,1), (5,0)]:
        check(r, s, odd=(r<=4))
    assert check(3, 0)[1][4] == 1
    assert check(4, 0)[1][4:7] == [4, 2, 4]
    print('MODULAR_ALMOST_ABELIAN_BETTI_VERIFIED')

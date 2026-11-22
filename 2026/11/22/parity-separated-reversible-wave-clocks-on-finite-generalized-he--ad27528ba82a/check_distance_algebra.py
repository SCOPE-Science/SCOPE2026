#!/usr/bin/env python3
"""Exact binary distance-algebra identities for incidence graphs of equal-order generalized hexagons.

The distance-i adjacency matrices D_i form a formal basis.  This test does
not generate any particular generalized hexagon.  Its inputs are the
intersection numbers guaranteed by the geometric axioms.
"""

def multiply_by_adjacency(vec, q_parity):
    q = q_parity
    b = [1 ^ q, q, q, q, q, q]
    c = [0, 1, 1, 1, 1, 1, 1 ^ q]
    ans = [0] * 7
    for i, coeff in enumerate(vec):
        if coeff:
            if i > 0:
                ans[i-1] ^= b[i-1]
            if i < 6:
                ans[i+1] ^= c[i+1]
    return tuple(ans)


def xor(*vs):
    return tuple(sum(v[i] for v in vs) % 2 for i in range(7))


def run(q):
    powers = []
    a = (1,0,0,0,0,0,0)
    for _ in range(9):
        powers.append(a)
        a = multiply_by_adjacency(a, q)
    if q == 0:
        # x^7+x^5 = x^5(x+1)^2
        assert xor(powers[7], powers[5]) == (0,) * 7
        for i in range(7):
            assert powers[i][i] == 1
        assert powers[6] == (1,0,1,0,1,0,1)
        expected = 'x^5 (x+1)^2'
    else:
        # x^6+x^2 = x^2(x+1)^4
        assert xor(powers[6], powers[2]) == (0,) * 7
        for i in range(6):
            assert powers[i][i] == 1
        assert powers[5] == (0,0,0,1,0,1,0)
        expected = 'x^2 (x+1)^4'
    print('order parameter parity',q,'minimal polynomial',expected)
    return powers

if __name__ == '__main__':
    run(0)
    run(1)
    print('distance algebra PASS')

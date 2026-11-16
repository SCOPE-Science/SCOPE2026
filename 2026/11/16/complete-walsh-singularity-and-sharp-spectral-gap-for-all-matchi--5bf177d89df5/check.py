#!/usr/bin/env python3
"""Exact integer checks for the Walsh spectrum of all K_(3,n) matchings.

The full binary Walsh transform is obtained from the matching-incidence indicator,
independently of the aggregate-moment identity checked against it.
"""
from itertools import product, combinations_with_replacement
from math import factorial

SIGNS = tuple(product((1, -1), repeat=3))
H4 = ((1, 1, -1), (1, -1, -1), (-1, 1, 1), (-1, -1, 1))
H8 = SIGNS
ODD_ZERO = {1: ((-1, -1, 1),),
            3: ((1, 1, -1), (-1, -1, -1), (-1, -1, -1))}
ODD_TWO = {1: ((-1, -1, -1),),
           3: ((1, 1, 1), (-1, -1, -1), (-1, -1, -1))}
EVEN_ONE = {
    2: ((1, 1, 1), (-1, -1, 1)),
    4: ((1, 1, 1), (-1, 1, 1), (1, -1, -1), (1, -1, -1)),
    6: ((1, 1, 1),) * 4 + ((-1, -1, 1), (-1, -1, -1)),
    8: SIGNS,
}


def moment_value(columns):
    a = sum(z[0] for z in columns)
    b = sum(z[1] for z in columns)
    c = sum(z[2] for z in columns)
    ab = sum(z[0] * z[1] for z in columns)
    ac = sum(z[0] * z[2] for z in columns)
    bc = sum(z[1] * z[2] for z in columns)
    abc = sum(z[0] * z[1] * z[2] for z in columns)
    return ((1+a)*(1+b)*(1+c)
            -(1+c)*ab-(1+b)*ac-(1+a)*bc+2*abc)


def columns_from_frequency(mask, n):
    return tuple(tuple(1-2*((mask >> (r*n+j)) & 1) for r in range(3))
                 for j in range(n))


def direct_matching_masks(n):
    result = []
    def recurse(row, used, val):
        if row == 3:
            result.append(val)
            return
        recurse(row+1, used, val)
        for j in range(n):
            if not (used >> j) & 1:
                recurse(row+1, used | (1 << j), val | (1 << (row*n+j)))
    recurse(0, 0, 0)
    return result


def full_walsh_from_matching_support(n):
    support = direct_matching_masks(n)
    assert len(support) == n*n*n+2*n+1, (n, len(support))
    N = 1 << (3*n)
    data = [0] * N
    for v in support:
        assert data[v] == 0
        data[v] = 1
    step = 1
    while step < N:
        gap = step*2
        for start in range(0, N, gap):
            for j in range(start, start+step):
                u, v = data[j], data[j+step]
                data[j], data[j+step] = u+v, u-v
        step = gap
    return data


def proof_witnesses():
    # The 8-column block has all seven nontrivial moments equal to zero.
    for mask in range(1, 8):
        assert sum(__import__('math').prod(z[r] for r in range(3) if (mask >> r)&1)
                   for z in H8) == 0
    # H4 changes only the a*c moment, by -4.
    def moments(zs):
        return tuple(sum(__import__('math').prod(z[r] for r in range(3)
                                                if (mask >> r)&1) for z in zs)
                     for mask in range(1,8))
    assert moments(H4) == (0,0,0,0,-4,0,0), moments(H4)
    # Exact witnesses at every length, including beyond exhaustive transforms.
    for n in range(1, 201):
        if n % 2:
            r = 1 if n % 4 == 1 else 3
            blocks = (n-r)//4
            assert moment_value(ODD_ZERO[r] + H4*blocks) == 0
            assert abs(moment_value(ODD_TWO[r] + H4*blocks)) == 2
        else:
            r = n % 8 or 8
            assert r in EVEN_ONE
            assert abs(moment_value(EVEN_ONE[r] + H8*((n-r)//8))) == 1


def direct_column_dp(columns):
    # Independent three-row matching DP over occupied-row subsets.
    dp = [0] * 8
    dp[0] = 1
    for col in columns:
        nxt = dp.copy()
        for mask in range(8):
            for row in range(3):
                if not (mask & (1 << row)):
                    nxt[mask | (1 << row)] += dp[mask] * col[row]
        dp = nxt
    return sum(dp)


def type_reduced_check():
    # All frequencies modulo column permutations: exhaustive type multisets.
    for n in range(7, 13):
        zeros = 0
        smallest = None
        count = 0
        for indices in combinations_with_replacement(range(8), n):
            cols = tuple(SIGNS[i] for i in indices)
            val = direct_column_dp(cols)
            assert val == moment_value(cols)
            assert val % 2 == (n+1) % 2
            if val == 0:
                zeros += 1
            else:
                smallest = abs(val) if smallest is None else min(smallest, abs(val))
            count += 1
        assert (zeros > 0) == (n % 2 == 1)
        assert smallest == (2 if n % 2 else 1)
        print('type-reduced n', n, 'patterns', count, 'zero patterns',zeros,'least',smallest)


def main():
    proof_witnesses()
    for n in range(1, 7):
        vals = full_walsh_from_matching_support(n)
        zeros = 0
        least = None
        for mask, val in enumerate(vals):
            assert val == moment_value(columns_from_frequency(mask,n)), (n,mask,val)
            assert val % 2 == (n+1) % 2
            if val == 0: zeros += 1
            else:
                least = abs(val) if least is None else min(abs(val), least)
        assert (zeros > 0) == (n % 2 == 1)
        assert least == (2 if n % 2 else 1)
        if n % 2:
            assert zeros >= factorial(4) ** ((n-1)//4)
        else:
            assert zeros == 0
        print('n', n, 'frequencies',len(vals), 'zeros',zeros,'least',least)
    type_reduced_check()
    print('THREE_ROW_MATCHING_WALSH_EXACT_PASS')

if __name__ == '__main__': main()

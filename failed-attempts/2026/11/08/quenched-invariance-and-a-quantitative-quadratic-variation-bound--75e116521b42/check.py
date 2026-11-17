"""Finite, exact-rational diagnostics for a parity-recoded walk.

Run with Python 3.10 or later: python check.py
This diagnostic supplements the analytic infinite-horizon argument.
"""
from itertools import product
from math import comb
from fractions import Fraction


def masks_for(N):
    offsets = {}
    used = 0
    for j in range(1, N):
        offsets[j] = used
        used += j + 1
    table = {}
    for j in range(1, N):
        for s in range(j + 1):
            mask = 0
            for k in range(s + 1):
                if comb(s, k) % 2:
                    mask |= 1 << (offsets[j] + k)
            table[j, s] = mask
    return table, offsets, used


def squared_numerator(N, env, masks):
    ans = 0
    for path in range(1 << (N-1)):
        running = 1  # zeta_0
        negatives = 0
        for j in range(1, N):
            negatives += (path >> (j-1)) & 1
            running += -1 if (env & masks[j, negatives]).bit_count() & 1 else 1
        ans += running * running
    return ans


def run():
    nchecks = 0
    for N in range(1, 6):
        masks, offsets, nbits = masks_for(N)
        all_num = [squared_numerator(N, env, masks) for env in range(1 << nbits)]
        # Fair environments: E_beta E_xi[(N^{-1} sum zeta_j)^2] = 1/N exactly.
        assert sum(all_num) == (1 << nbits) * (1 << (N-1)) * N
        nchecks += 1
        denom = (1 << (N-1)) * N * N
        for env, num in enumerate(all_num):
            assert 0 <= num <= denom
            nchecks += 1
            # Whole blocks are the environmental units. Replacing any block
            # changes only one zeta term of each input path.
            for j, offset in offsets.items():
                block_mask = ((1 << (j+1)) - 1) << offset
                new_env = env ^ block_mask
                assert abs(num-all_num[new_env]) <= Fraction(4, N) * denom
                nchecks += 1
        # Lucas' parity identity for all relevant values.
        for j in range(1, N):
            for s in range(j+1):
                for k in range(s+1):
                    assert comb(s, k) % 2 == int((k & s) == k)
                    nchecks += 1
    print(f"PASS: {nchecks} finite exact-integer assertions (N=1,...,5)")


if __name__ == '__main__':
    run()

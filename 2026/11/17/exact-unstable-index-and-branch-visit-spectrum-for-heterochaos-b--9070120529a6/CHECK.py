"""Exact-rational finite diagnostics for branch-visit histograms. Not an infinite proof."""
from fractions import Fraction
from itertools import product
from math import comb, gcd

def is_m_adic(value, M):
    den = value.denominator
    while True:
        common = gcd(den, M)
        if common == 1:
            return den == 1
        den //= common

def regular_center_count(M, base_word):
    Q = Fraction
    # Piecewise affine center returns: (left, right, slope, intercept).
    branches = [(Q(0), Q(1), Q(1), Q(0))]
    for digit in base_word:
        new = []
        for left, right, slope, shift in branches:
            if digit < M:
                new.append((left, right, slope/M, (shift+digit)/M))
            else:
                for j in range(M):
                    lo = max(left, (Q(j,M)-shift)/slope)
                    hi = min(right, (Q(j+1,M)-shift)/slope)
                    if lo < hi:
                        new.append((lo, hi, M*slope, M*shift-j))
        branches = new
    out = 0
    for left, right, slope, shift in branches:
        if slope == 1:  # all possible fixed points are neutral, so excluded
            continue
        y = shift / (1-slope)
        if left < y < right and not is_m_adic(y, M):
            out += 1
    return out

def prediction(M, n, m):
    c = n-m
    if m<c:
        return comb(n,m)*(M**c-2*M**m)
    if m>c:
        return comb(n,m)*(M**m-2*M**c)
    return 0

def run():
    for M, max_n in ((2,8),(3,5),(4,4)):
        for n in range(1, max_n+1):
            observed = [0]*(n+1)
            for base_word in product(range(M+1), repeat=n):
                observed[base_word.count(M)] += regular_center_count(M,base_word)
            assert all(observed[m] == prediction(M,n,m) for m in range(n+1)),(M,n,observed)
            one = sum(observed[m] for m in range(n+1) if 2*m<n)
            two = sum(observed[m] for m in range(n+1) if 2*m>n)-(M**n-2)
            assert one-two == M**n-2,(M,n,one,two)
            assert two >= 0
    print('HETEROCHAOS_INDEX_HISTOGRAM_OK')
if __name__ == '__main__': run()

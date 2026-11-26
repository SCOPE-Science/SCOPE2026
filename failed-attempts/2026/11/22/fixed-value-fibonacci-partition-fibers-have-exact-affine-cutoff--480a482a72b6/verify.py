#!/usr/bin/env python3
"""Exact finite-state and independent partition checks for Fibonacci level sets."""
from collections import defaultdict
from functools import lru_cache


def numerator(k):
    """Return P_k satisfying sum_{L>=0} b_k(L)z^L=P_k(z)/(1-z)."""
    assert isinstance(k, int) and k >= 1

    @lru_cache(None)
    def F(A, q):
        # Values of A above k are equivalent for all continuations with q<=k.
        if A > k:
            return {1: 1} if q == k else {}
        out = defaultdict(int)
        delta = k - q
        if delta % A == 0:
            t = delta // A
            if t >= 0:
                j = 2*t + 1
                out[j] += 1
                out[j+2] -= 1  # (1-z) z^j(1+z)
        # Even gaps d=2h; q'=(h-1)A+q.
        for h in range(1, delta//A + 2):
            newA = h*A + q
            newq = (h-1)*A + q
            assert newq <= k
            for e, coefficient in F(min(newA, k+1), newq).items():
                out[e + 2*h] += coefficient
        # Odd gaps d=2h+1; q'=A'=hA+q.
        for h in range(1, delta//A + 1):
            newA = h*A + q
            if newA > k:
                continue
            for e, coefficient in F(newA, newA).items():
                out[e + 2*h+1] += coefficient
        return {e: c for e, c in out.items() if c != 0}

    return F(1, 1)


def prefix_count(P, L, k):
    if L < 0:
        return 0
    return int(k == 1) + sum(c*(L-d+1) for d, c in P.items() if d <= L)


def partition_counts(max_f_index):
    # f_1=1,f_2=2; n<f_{max_f_index+1}.
    f = [0, 1, 2]
    for i in range(3, max_f_index+2):
        f.append(f[-1] + f[-2])
    limit = f[max_f_index+1]
    counts = [0]*limit
    counts[0] = 1
    for part in f[1:max_f_index+1]:
        for n in range(limit-1, part-1, -1):
            counts[n] += counts[n-part]
    return f, counts


def via_zeckendorf(n, f):
    if n == 0:
        return 1
    bits = []
    r = n
    for idx in range(len(f)-1, 0, -1):
        if f[idx] <= r:
            bits.append(idx)
            r -= f[idx]
    assert r == 0 and all(a-b >= 2 for a, b in zip(bits,bits[1:]))
    A = q = 1
    for i, j in zip(bits,bits[1:]):
        d = i-j
        h = d//2
        newA = h*A + q
        newq = (h-1)*A+q if d%2 == 0 else newA
        A, q = newA, newq
    last = bits[-1]
    return q + (((last+1)//2)-1)*A


def main():
    P12 = {11:8,12:16,13:8,14:4,15:4,23:2,24:2}
    assert numerator(12) == P12
    assert sum(P12.values()) == 44
    assert sum(j*c for j,c in P12.items()) == 594
    for L in range(24, 120):
        assert prefix_count(P12,L,12) == 44*L-550
    # Check recurrence-produced numerators have positive nonzero slopes
    # and degree bound claimed in the accompanying proof, for sample k.
    P = {k: numerator(k) for k in range(1, 26)}
    for k, p in P.items():
        assert sum(p.values()) > 0
        assert max(p) <= 2*k*k+2*k+2
    # Independent 0/1 knapsack, not a Zeckendorf recurrence.
    last_L = 24
    f, counts = partition_counts(last_L)
    for n, value in enumerate(counts):
        assert via_zeckendorf(n, f) == value, (n, value)
    for k, p in P.items():
        # Exhaustive counts at each Fibonacci cutoff; direct independent sum.
        for L in range(last_L+1):
            actual = sum(value == k for value in counts[:f[L+1]])
            claimed = prefix_count(p,L,k)
            assert actual == claimed, (k,L,actual,claimed)
    print('PASS: all direct Zeckendorf/knapsack values through', f[last_L+1]-1)
    print('PASS: 25 multiplicity level polynomials and all 25 cutoffs')
    print('PASS: P_12=', sorted(P12.items()))
    print('PASS: C_12(L)=44L-550 for L>=24 from exact rational identity')

if __name__ == '__main__':
    main()

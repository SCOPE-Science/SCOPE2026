#!/usr/bin/env python3
"""Exact verification of path-orientation sink Walsh rank and run criterion.
Python 3 standard library only. Outputs reproducible integer checks.
"""

def sink_profile(n, edges):
    """Rightward edge orientations are bits at indices 0,...,n-2."""
    x = (1 if not (edges & 1) else 0)
    for i in range(1, n - 1):
        if (edges >> (i-1)) & 1 and not ((edges >> i) & 1):
            x |= 1 << i
    if (edges >> (n-2)) & 1:
        x |= 1 << (n-1)
    return x


def transform(a):
    a = list(a)
    h = 1
    while h < len(a):
        for i in range(0, len(a), 2*h):
            for j in range(i, i+h):
                u, v = a[j], a[j+h]
                a[j], a[j+h] = u+v, u-v
        h *= 2
    return a


def matrix_multiplier(n, selected):
    a, b = (-1 if selected & 1 else 1), 1
    for i in range(1, n-1):
        if (selected >> i) & 1:  # B=[[1,1],[-1,1]]
            a, b = a-b, a+b
        else:                  # J=[[1,1],[1,1]]
            a, b = a+b, a+b
    return a + b * (-1 if (selected >> (n-1)) & 1 else 1)


def run_survives(n, selected):
    if selected == (1 << n) - 1:
        return n % 4 != 0
    i = 0
    while i < n:
        if not ((selected >> i) & 1):
            i += 1
            continue
        j = i
        while j < n and ((selected >> j) & 1):
            j += 1
        k = j-i
        if i == 0 or j == n:
            if k % 4 == 1:
                return False
        elif k % 4 == 2:
            return False
        i = j
    return True


def recurrence_rank(n):
    arr = [0,0,2,5,7,16]
    for m in range(6, n+1):
        arr.append(arr[m-1] + arr[m-2] + 2*arr[m-4])
    return arr[n]


def automaton_rank(n):
    # E, Z, G, X; q counts states after interior letters
    vec = [1,0,1,0]
    for _ in range(n-2):
        vec = [vec[0]+vec[1]+2*vec[3],vec[0],vec[1],vec[2]]
    return sum(v*t for v,t in zip(vec,[1,2,1,2]))


def independent_sum_scaled(n, selected):
    """Compute 2^(n-1) times the signed weighted independent polynomial
    using only integer arithmetic (degree endpoints 1, internal degree 2)."""
    # DP tracked numerator with common denominator 2^(n-1):
    # easier evaluate sum by scanning independent subsets of selected mask
    total = 0
    sub = selected
    while True:
        if not (sub & (sub << 1)):
            total += (-1 if sub.bit_count() & 1 else 1) * (1 << (n-1 - sum(1 if i in (0,n-1) else 2 for i in range(n) if sub>>i&1) + sub.bit_count()))
        if sub == 0:break
        sub = (sub - 1) & selected
    return total


def main():
    # Completely independent orientation enumeration (not based on transfer formulas).
    for n in range(2, 15):
        mass = [0] * (1 << n)
        for e in range(1 << (n-1)):
            mass[sink_profile(n,e)] += 1
        assert sum(mass) == (1 << (n-1))
        freq = transform(mass)
        for s, w in enumerate(freq):
            assert w == matrix_multiplier(n,s), (n,s,w)
            assert (w != 0) == run_survives(n,s), (n,s,w)
        exact_rank = sum(w != 0 for w in freq)
        assert exact_rank == automaton_rank(n) == recurrence_rank(n), (n,exact_rank)
        print('n=%d orientations=%d rank=%d nullity=%d' %
              (n,1 << (n-1),exact_rank,(1 << n)-exact_rank))
    # Independent inclusion-exclusion / weighted hard-core identity.
    for n in range(2, 9):
        for s in range(1 << n):
            assert independent_sum_scaled(n,s) == matrix_multiplier(n,s)
    # Long-run symbolic test of recurrence versus a four-state unweighted automaton.
    for n in range(2, 201):
        assert automaton_rank(n) == recurrence_rank(n)
        assert 0 < automaton_rank(n) < (1 << n)
    print('PASS: direct enumeration, integer Walsh transform, matrix products,')
    print('run criterion, weighted independence identity, and recurrence')


if __name__ == '__main__':
    main()

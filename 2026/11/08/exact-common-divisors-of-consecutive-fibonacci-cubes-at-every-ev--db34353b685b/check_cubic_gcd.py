#!/usr/bin/env python3
"""Independent exact-arithmetic tests of a Fibonacci cubic consecutive-sum gcd theorem."""
from math import gcd

def fibs(max_index):
    f = [0, 1]
    while len(f) <= max_index:
        f.append(f[-1] + f[-2])
    return f

def lucas(max_index):
    l = [2, 1]
    while len(l) <= max_index:
        l.append(l[-1] + l[-2])
    return l

def predicted(k, f, l):
    assert k >= 2 and k % 2 == 0
    m = k // 2
    G = f[m] if m % 2 == 0 else l[m]
    D = G * (3 if G % 3 == 0 else 1)
    return D // (2 if G % 2 == 0 else 1), G, D

def test():
    f = fibs(512)
    l = lucas(260)
    cases = 0
    brute_sums = 0
    for k in range(2, 241, 2):
        answer, G, D = predicted(k, f, l)
        A = f[k+1] ** 3 - 1
        B = f[k+2] ** 3 - 1
        assert gcd(A, B) == D, ('two-difference', k)
        assert gcd(f[k+1]-1, f[k+2]-1) == G, ('linear-period', k)
        ss = [sum(f[n+j]**3 for j in range(1,k+1)) for n in range(20)]
        assert gcd(*ss) == answer, ('brute-consecutive-cubes', k)
        assert (2*ss[0]) % D == 0, ('twice-first-sum', k)
        if G % 2:
            assert ss[0] % D == 0, ('odd-modulus', k)
        else:
            assert (2*ss[0] // D) % 2 == 1, ('half-modulus', k)
        for n in range(20):
            assert (f[n+k]**3-f[n]**3) % D == 0, ('periodic-cube', k,n)
        cases += 1
        brute_sums += len(ss)
    # Explicit discrepancies from the previously conjectured direction of the factor two.
    assert predicted(6, f, l)[0] == 2 and gcd(f[7]**3-1,f[8]**3-1) == 4
    assert predicted(8, f, l)[0] == 9 and gcd(f[9]**3-1,f[10]**3-1) == 9
    print(f'VERIFY_OK even_lengths={cases} exact_sum_windows={brute_sums} odd_and_even_periods=checked discrepancy_k6=2_vs_4 k8=9_vs_half_9')

if __name__ == '__main__':
    test()

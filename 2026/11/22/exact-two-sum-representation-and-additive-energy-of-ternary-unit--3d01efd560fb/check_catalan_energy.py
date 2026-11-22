"""Standalone finite checks of Catalan ternary-unit additive representation formulas.
Python 3, standard library only. The theorems for all depths are proved separately.
"""
from math import comb
from collections import Counter


def ternary_digits(n, length):
    out = []
    for _ in range(length):
        out.append(n % 3)
        n //= 3
    assert n == 0
    return out


def no_two(n):
    while n:
        if n % 3 == 2:
            return False
        n //= 3
    return True


def unit_indices(r):
    M = 3 ** r
    return [n for n in range(M) if no_two((n + 1) // 3)]


def digit_weights(m):
    return [2 ** ternary_digits(n, m).count(1) for n in range(3 ** m)]


def test_depth(r, direct_catalan=False):
    M = 3 ** r
    m = r - 1
    A = unit_indices(r)
    assert len(A) == 3 * 2 ** m
    if direct_catalan:
        assert A == [n for n in range(M) if comb(2 * n, n) // (n + 1) % 3 != 0]
    freq = [0] * M
    for a in A:
        for b in A:
            freq[(a+b)%M] += 1
    w = digit_weights(m)
    for v in range(3 ** m):
        w0, w1 = w[v], w[(v+1) % (3 ** m)]
        assert freq[3*v] == 3*w0
        assert freq[3*v+1] == 2*w0+w1
        assert freq[3*v+2] == w0+2*w1
    assert min(freq) == 3
    assert sum(x == 3 for x in freq) == 2**m + 2
    assert max(freq) == 3*2**m
    if m:
        assert [i for i,x in enumerate(freq) if x==max(freq)] == [3*((3**m-1)//2)]
    energy = sum(x*x for x in freq)
    assert energy == (127*6**m+8)//5
    assert sum(freq) == len(A)**2
    print(f'r={r}, |A|={len(A)}, min={min(freq)}, max={max(freq)}, E={energy}, full Catalan check={direct_catalan}')
    return M + len(A)**2 + 5*M


def main():
    assertions = 0
    for r in range(1, 9):
        assertions += test_depth(r, direct_catalan=(r<=6))
    for m in range(0, 9):
        w=digit_weights(m)
        assert sum(z*z for z in w)==6**m
        assert sum(w[i]*w[(i+1)%len(w)] for i in range(len(w)))==(4*6**m+1)//5
        assertions += 2
    print('PASS: all finite identities verified; approximate scalar comparisons:', assertions)

if __name__ == '__main__':
    main()

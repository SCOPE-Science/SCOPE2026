"""Exact phase-character verification of random unimodular Fourier moment skewness."""
from collections import defaultdict
from itertools import combinations
from math import comb


def exponent_coefficients(A):
    """Nonconstant Haar characters and positive multiplicities in the fourth norm."""
    A = tuple(sorted(A))
    n = len(A)
    by_sum = defaultdict(list)
    for i, a in enumerate(A):
        for j in range(i, n):
            b = A[j]
            by_sum[a + b].append((i, j, 1 if i == j else 2))
    out = defaultdict(int)
    for pairs in by_sum.values():
        for a, b, p in pairs:
            for c, d, q in pairs:
                e = [0] * n
                e[a] += 1
                e[b] += 1
                e[c] -= 1
                e[d] -= 1
                e = tuple(e)
                if any(e):
                    out[e] += p * q
    return dict(out)


def moments(A):
    c = exponent_coefficients(A)
    zero = (0,) * len(A)
    variance = sum(k * k for k in c.values())
    third = 0
    for u, cu in c.items():
        for v, cv in c.items():
            w = tuple(-a-b for a, b in zip(u, v))
            third += cu * cv * c.get(w, 0)
    return variance, third


def four_progressions(A):
    A = set(A)
    return sum(1 for x in A for d in range(1, max(A)-min(A)+1)
               if x+d in A and x+2*d in A and x+3*d in A)


def three_progressions(A):
    A = set(A)
    return sum(1 for x in A for d in range(1, max(A)-min(A)+1)
               if x+d in A and x+2*d in A)


def quadruples(A):
    return sum(a+d == b+c for a, b, c, d in combinations(sorted(A), 4))


def main():
    checked = 0
    # Independent combinatorial fourth-moment variance and skewness checks
    # on all four-element supports of diameter at most 20.
    for tail in combinations(range(1, 21), 3):
        A = (0,) + tail
        var, third = moments(A)
        assert var == 8*three_progressions(A)+32*quadruples(A), A
        assert third == 192 if four_progressions(A) else third == 0, (A, third)
        checked += 1
    # A broader test includes four-, five- and six-point supports.
    for k in (5, 6):
        for tail in combinations(range(1, 11), k-1):
            A = (0,) + tail
            var, third = moments(A)
            assert var == 8*three_progressions(A)+32*quadruples(A), A
            assert third >= 192 * four_progressions(A), (A, third)
            assert third >= 0
            checked += 1
    for n in range(1, 9):
        A = tuple(range(n))
        assert moments(A)[1] >= 192 * four_progressions(A)
    assert moments((0, 1, 2, 3)) == (48, 192)
    assert moments((0, 1, 2, 4))[1] == 0
    assert moments((0, 1, 3, 4))[1] == 0
    print(f'STEINHAUS_SKEWNESS_EXACT_PASS checked_supports={checked} sharp_mu3=192')


if __name__ == '__main__':
    main()

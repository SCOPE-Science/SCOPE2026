"""Exact finite checks for three-probe eventual-onto times of binary Rule 102.
Run with Python 3.9+; only standard-library integer/rational arithmetic is used.
"""
from fractions import Fraction
from itertools import combinations
from math import comb


def rank2(rows):
    basis = {}
    for row in rows:
        v = row
        while v:
            bit = v.bit_length() - 1
            if bit not in basis:
                basis[bit] = v
                break
            v ^= basis[bit]
    return len(basis)


def independent_pascal_time(S):
    """Rows are Hasse derivative coefficients, not the 2-adic distance law."""
    W = max(S) - min(S)
    S = tuple(s - min(S) for s in S)
    for t in range(1, W + 2):
        rows = [sum((comb(s, j) & 1) << i for i, s in enumerate(S)
                    if s >= j) for j in range(t)]
        if rank2(rows) == len(S):
            return t
    raise AssertionError('finite difference matrix failed to span')


def proposed_time(S):
    return 1 + max((b-a) & -(b-a) for a, b in combinations(S, 2))


rank_cases = 0
for S in combinations(range(16), 3):
    assert independent_pascal_time(S) == proposed_time(S), S
    rank_cases += 1
print('PASS independent Pascal-row rank vs three-probe dyadic formula:', rank_cases)

for R in range(2, 7):
    N = 1 << R
    samples = tuple(combinations(range(N), 3))
    times = [proposed_time(S) for S in samples]
    denominator = (1 - Fraction(1, N)) * (1 - Fraction(2, N))
    mean_target = 2 + (Fraction(3*R, 2) - 4 + Fraction(6,N)
                       - Fraction(2,N*N)) / denominator
    Z2_target = (1 + Fraction(3,4) * (2*N - 2*R - Fraction(10,3)
                     + Fraction(4,N) - Fraction(8,3*N*N)) / denominator)
    assert Fraction(sum(times), len(times)) == mean_target, R
    assert Fraction(sum((t-1)**2 for t in times), len(times)) == Z2_target, R
    for m in range(1, R+1):
        observed = Fraction(sum(t <= 1 + (1 << (m-1)) for t in times), len(times))
        expected = Fraction(comb(1 << m, 3)*(N//(1 << m))**3, comb(N,3))
        assert observed == expected, (R,m,observed,expected)
    print('PASS all unordered triples and exact CDF/mean/second moment:',N,len(samples))

# Every sparse mask (not only triples): dyadic exactness is residue injectivity.
# The Hasse-Pascal row matrix is independent of the occupancy prediction.
mask_cases = 0
for N in (8, 12, 16):
    for k in range(2, min(6, N+1)):
        for S in combinations(range(N),k):
            for m in range(0, 5):
                t = 1 << m
                rows = [sum((comb(s,j)&1) << i for i,s in enumerate(S)
                            if s >= j) for j in range(t)]
                observed = rank2(rows) == k
                predicted = len({s % t for s in S}) == k
                assert observed == predicted, (N,k,S,t)
                mask_cases += 1
print('PASS general sparse-mask dyadic coverage vs independent Pascal rank:',mask_cases)

for R in range(3,6):
    N=1<<R
    for k in range(2,min(N+1,6)):
        subsets=list(combinations(range(N),k))
        for m in range(R+1):
            b=1<<m
            actual=sum(len({s%b for s in S})==k for S in subsets)
            expected=comb(b,k)*(N//b)**k
            assert actual==expected, (N,k,m,actual,expected)
print('PASS multi-probe dyadic occupancy census for N=8,16,32, k up to 5')

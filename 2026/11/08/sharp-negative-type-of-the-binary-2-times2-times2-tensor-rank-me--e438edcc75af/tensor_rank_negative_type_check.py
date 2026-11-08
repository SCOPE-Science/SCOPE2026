"""Exact exhaustive certificate for tensor-rank shells in (F_2^2)^(tensor 3).
Run: python3 tensor_rank_negative_type_check.py. Standard-library only.
"""
from collections import Counter, defaultdict
from itertools import product

N = 256

def simple(u, v, w):
    result = 0
    for i, j, k in product(range(2), repeat=3):
        if ((u >> i) & 1) and ((v >> j) & 1) and ((w >> k) & 1):
            result |= 1 << (4*i + 2*j + k)
    return result

S = {simple(u, v, w) for u, v, w in product((1, 2, 3), repeat=3)}
assert len(S) == 27 and 0 not in S
R = [set(), S, set(), set()]
R[0] = {0}
R[2] = {x ^ y for x, y in product(S, repeat=2)} - S - {0}
R[3] = set(range(N)) - (R[0] | R[1] | R[2])
assert [len(r) for r in R] == [1, 27, 162, 66]
assert all(R[i].isdisjoint(R[j]) for i in range(4) for j in range(i))
# Validate rank 3 is attained, not merely a complement: all 256 tensors are sums of 3 simples.
assert {x ^ y for x, y in product(R[2], S)}.issuperset(R[3])

def character(a, x):
    return 1 if ((a & x).bit_count() & 1) == 0 else -1

# Method 1: direct Walsh sum on each rank shell.
signatures = {}
counts = Counter()
representatives = {}
for a in range(1, N):
    sig = tuple(sum(character(a, x) for x in R[r]) for r in (1, 2, 3))
    signatures[a] = sig
    counts[sig] += 1
    representatives.setdefault(sig, a)
    assert sum(sig) == -1
expected = {
    (-9, 18, -10): 12,
    (-5, 2, 2): 54,
    (-1, 2, -2): 108,
    (3, -14, 10): 54,
    (11, 2, -14): 27,
}
assert counts == expected, (counts, expected)
# Method 2: fast Walsh-Hadamard transform, independent of summation method.
def fwht(a):
    a = list(a)
    h = 1
    while h < N:
        for p in range(0, N, 2*h):
            for i in range(p, p+h):
                u, v = a[i], a[i+h]
                a[i], a[i+h] = u+v, u-v
        h *= 2
    return a
transforms = [fwht([int(i in R[r]) for i in range(N)]) for r in (1, 2, 3)]
for a in range(1, N):
    assert signatures[a] == tuple(t[a] for t in transforms)
# Explicit witness of the endpoint: exactly 54 frequencies of the critical signature.
assert len([a for a, t in signatures.items() if t == (-5, 2, 2)]) == 54
print('TENSOR_RANK_SHELL_SIZES:', [len(r) for r in R])
for sig, count in sorted(counts.items()):
    print('FREQUENCY_SIGNATURE:', sig, 'multiplicity=', count,
          'representative=', format(representatives[sig], '#04x'))
print('ENDPOINT_NULLITY:', expected[(-5, 2, 2)])
print('MINIMUM_ENDPOINT_EUCLIDEAN_DIMENSION:', N-1-expected[(-5, 2, 2)])
print('ALL_2X2X2_TENSOR_NEGATIVE_TYPE_CERTIFICATES_OK')

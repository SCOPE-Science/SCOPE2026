"""Exact order-five even-permutation Walsh census; standard library only.
Run: python3 check_even_permutation_walsh.py
"""
from collections import Counter
from fractions import Fraction
from itertools import permutations

N = 1 << 16
f = [0] * N
perms = []
for p in permutations(range(5)):
    inversion_parity = sum(p[i] > p[j] for i in range(5) for j in range(i+1,5)) & 1
    if not inversion_parity:
        perms.append(p)
        mask = sum(1 << (4 * i + p[i]) for i in range(4) if p[i] < 4)
        f[mask] += 1
assert len(perms) == 60 and sum(f) == 60 and max(f) == 1

def walsh(a):
    a = a[:]
    for b in range(16):
        step = 1 << b
        for lo in range(0, N, 2 * step):
            for j in range(lo, lo + step):
                x, y = a[j], a[j + step]
                a[j] = x + y
                a[j + step] = x - y
    return a

W = walsh(f)
hist = Counter(abs(v) for v in W)
expected = {0:11320,4:24600,8:17400,12:7850,16:3720,20:360,24:200,28:60,36:25,60:1}
assert hist == expected, (hist, expected)
assert sum(v * v for v in W) == N * 60
assert W[0] == 60
support = [int(v != 0) for v in W]
proj = walsh(support)
norm = Fraction(sum(abs(v) for v in proj), N)
assert norm == Fraction(266611,4096), norm
assert Counter(abs(v) for v in proj)[0] == 60
assert sum(support) == 54216
assert min(abs(v) for v in W if v) == 4
# A local cancellation can occur on precisely the three edges of a length-three path.
# Representatives in the upper-left 4x4 block: (0,0),(0,1),(1,1)
path = (1 << 0) | (1 << 1) | (1 << 5)
assert W[path] == 0
for s in range(N):
    if s.bit_count() < 3:
        assert W[s] != 0
assert sum(v == 0 and i.bit_count() == 3 for i, v in enumerate(W)) == 144
# Direct independent small-support scan in all 25 matrix coordinates (not gauge quotient).
from itertools import combinations
three_zeros = []
for degree in range(4):
    for edges in combinations(range(25),degree):
        total = sum((-1) ** sum(p[e//5]==e%5 for e in edges) for p in perms)
        if total==0:
            assert degree == 3
            three_zeros.append(edges)
assert len(three_zeros)==400
for a,b,c in three_zeros:
    endpoints = [((e//5),e%5) for e in (a,b,c)]
    assert len({r for r, _ in endpoints}) == 2
    assert len({c for _, c in endpoints}) == 2
print('PASS even permutations=60, reduced character count=65536')
print('PASS magnitude histogram', sorted(hist.items()))
print('PASS full rank', 54216 * 512, 'full nullity', 11320 * 512)
print('PASS minimum support 3; upper-left paths 144; all graph paths 400')
print('PASS min nonzero=4; positive condition 15; sharp projection norm', norm)

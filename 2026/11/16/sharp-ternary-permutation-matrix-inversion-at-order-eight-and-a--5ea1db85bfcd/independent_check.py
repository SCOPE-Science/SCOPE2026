"""Exact integer verification of cubic-root permanent claims; no numerical complex arithmetic."""
from collections import Counter
from itertools import permutations
N = 8
ROOTS = ((1, 0), (0, 1), (-1, -1))

def multiply(u, v):
    a, b = u
    c, d = v
    return a*c-b*d, a*d+b*c-b*d

def permanent(matrix):
    dp = [(0, 0)] * (1 << N)
    dp[0] = (1, 0)
    for mask in range(1, 1 << N):
        row = mask.bit_count()-1
        x, y = 0, 0
        bitset = mask
        while bitset:
            bit = bitset & -bitset
            bitset -= bit
            j = bit.bit_length()-1
            a, b = multiply(dp[mask ^ bit], ROOTS[matrix[row][j]])
            x += a
            y += b
        dp[mask] = (x, y)
    return dp[-1]

def norm_squared(v):
    a, b = v
    return a*a-a*b+b*b

count = Counter()
minwords = 0
for q in range(3**N):
    x = q
    word = []
    for _ in range(N):
        word.append(x%3)
        x //= 3
    matrix = [[word[(j-i)%N] for j in range(N)] for i in range(N)]
    p = permanent(matrix)
    count[norm_squared(p)] += 1
assert sum(count.values()) == 6561
assert min(count) == 1296
assert count[1296] == 48
assert len(count) == 59

rows = [
    '00000000', '01201100', '00212210', '01102002',
    '01210201', '02110222', '01010212', '00100120'
]
mat = [[int(z) for z in row] for row in rows]
assert permanent(mat) == (9, 0)
residue_counts = Counter(sum(mat[i][p[i]] for i in range(N)) % 3
                         for p in permutations(range(N)))
assert residue_counts == {0: 13446, 1: 13437, 2: 13437}
assert 13446-13437 == 9
print('INDEPENDENT_EISENSTEIN_PASS circulant_count=48 levels=59 witness_permanent=9')

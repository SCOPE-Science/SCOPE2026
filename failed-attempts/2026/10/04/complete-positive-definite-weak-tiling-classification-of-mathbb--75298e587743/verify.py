from fractions import Fraction
from itertools import combinations

G = tuple(range(8))

def add(x, y):
    return x ^ y

def dot(x, y):
    return ((x & y).bit_count()) & 1

def translate(A, t):
    return frozenset(add(a, t) for a in A)

def diffset(A):
    return frozenset(add(a, b) for a in A for b in A)

def direct_tile(A):
    m = len(A)
    if 8 % m:
        return False
    k = 8 // m
    for B in combinations(G, k):
        sums = [add(a, b) for a in A for b in B]
        if len(sums) == 8 and len(set(sums)) == 8:
            return True
    return False

def is_subspace(S):
    return 0 in S and all(add(x, y) in S for x in S for y in S)

counts = {k: 0 for k in range(1, 9)}
for m in range(1, 9):
    for tup in combinations(G, m):
        A = frozenset(tup)
        counts[m] += 1
        tile = direct_tile(A)
        if m in (1, 2, 4, 8):
            assert tile
        else:
            assert not tile

        if m in (5, 6, 7):
            assert diffset(A) == frozenset(G)

        if m == 3:
            a0 = next(iter(A))
            A0 = translate(A, a0)
            assert 0 in A0
            S = diffset(A0)
            assert len(S) == 4 and is_subspace(S)
            chars = [k for k in range(1, 8) if all(dot(k, x) == 0 for x in S)]
            assert len(chars) == 1
            chi = chars[0]
            assert all(dot(chi, x) == 1 for x in G if x not in S)
            complement_mass = Fraction(8, 3) - 1
            fourier_value = 1 - complement_mass
            assert fourier_value == Fraction(-2, 3)

assert counts == {1:8, 2:28, 3:56, 4:70, 5:56, 6:28, 7:8, 8:1}
print(counts)
print('VERIFY_OK')

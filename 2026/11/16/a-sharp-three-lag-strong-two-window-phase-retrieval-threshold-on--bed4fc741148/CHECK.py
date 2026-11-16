"""Exact finite certificate for the ten-site Fourier support theorem.

Only standard-library arithmetic is used. A rank that is full modulo a prime
certifies full rank over the complex cyclotomic field via specialization.
"""
from itertools import combinations

N = 10
P = 1021
RHO = 432
assert all(P % d for d in range(2, 32))  # prime: sqrt(1021)<32
assert pow(RHO, 10, P) == 1 and pow(RHO, 5, P) == P - 1
assert pow(RHO, 2, P) != 1
assert (pow(RHO, 4, P) - pow(RHO, 3, P) + pow(RHO, 2, P) - RHO + 1) % P == 0


def components(s, bandwidth):
    s = set(s)
    unseen = set(s)
    count = 0
    while unseen:
        count += 1
        seed = unseen.pop()
        todo = [seed]
        while todo:
            x = todo.pop()
            for k in range(1, bandwidth + 1):
                for y in ((x + k) % N, (x - k) % N):
                    if y in unseen:
                        unseen.remove(y)
                        todo.append(y)
    return count


def disconnected_sets(bandwidth):
    return [tuple(s) for a in range(2, N + 1)
            for s in combinations(range(N), a)
            if components(s, bandwidth) > 1]


def canonical(s):
    return min(tuple(sorted((x + a) % N for x in s)) for a in range(N))


def rank_mod(matrix, p=P):
    a = [row[:] for row in matrix]
    cols = len(a[0])
    r = 0
    for j in range(cols):
        pivot = next((i for i in range(r, len(a)) if a[i][j]), None)
        if pivot is None:
            continue
        a[r], a[pivot] = a[pivot], a[r]
        inv = pow(a[r][j], -1, p)
        for k in range(j, cols):
            a[r][k] = a[r][k] * inv % p
        for i in range(r + 1, len(a)):
            factor = a[i][j]
            for k in range(j, cols):
                a[i][k] = (a[i][k] - factor * a[r][k]) % p
        r += 1
        if r == cols:
            break
    return r

sets3 = disconnected_sets(3)
expected = [(0, 4), (0, 5), (0, 1, 5), (0, 1, 6),
            (0, 2, 6), (0, 1, 2, 6), (0, 1, 5, 6)]
assert len(sets3) == 60
assert sorted({canonical(s) for s in sets3}, key=lambda s: (len(s), s)) == expected

# The full 60 x 60 ordered support-pair test. Rows are Fourier frequencies
# outside the candidate frequency support; columns are time coordinates.
# Cyclic translation of either set only multiplies rows/columns by roots
# of unity, so the final 7 x 7 orbit-representative check is a redundancy.
F = [[pow(RHO, j * k, P) for j in range(N)] for k in range(N)]
tests = 0
for s in sets3:
    for t in sets3:
        matrix = [[F[k][j] for j in s] for k in range(N) if k not in t]
        assert rank_mod(matrix) == len(s), (s, t)
        tests += 1
assert tests == 3600
for s in expected:
    for t in expected:
        matrix = [[F[k][j] for j in s] for k in range(N) if k not in t]
        assert rank_mod(matrix) == len(s)

# Sharpness at bandwidth 2: f(z)=(1+z^5)(z-1)(z-zeta^{-4}).
# Its six nonzero coefficients are at {0,1,2,5,6,7}; values are checked
# modulo P, while the complex factorization proves Fourier zero locations.
w = pow(RHO, 4, P)
assert w != 0 and (1 + w) % P != 0
coeffs = {0: w, 1: (-1-w) % P, 2: 1,
          5: w, 6: (-1-w) % P, 7: 1}
assert set(coeffs) == {0, 1, 2, 5, 6, 7}
assert all(x % P for x in coeffs.values())
assert components(coeffs, 2) == 2
spectrum = {k for k in range(N)
            if sum(v * pow(RHO, k * j, P) for j, v in coeffs.items()) % P}
assert spectrum == {2, 6, 8} and components(spectrum, 2) == 2
# The same witness is automatically disconnected at bandwidth 0, 1.
assert components(coeffs, 1) > 1 and components(spectrum, 1) > 1
print('CHECK_OK disconnected_supports=60 rotation_orbits=7 exact_modular_ranks=3600 sharp_witness=verified')

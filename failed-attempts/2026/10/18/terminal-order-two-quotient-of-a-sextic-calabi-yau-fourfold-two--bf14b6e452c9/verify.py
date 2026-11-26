#!/usr/bin/env python3
"""Exact combinatorial checks for a sextic-fourfold involution quotient.

Proofs of smoothness, quotient local models, and the global cohomological
identifications appear in the accompanying mathematical exposition. This
script independently checks their finite Hilbert-series consequences.
"""
from collections import Counter
from fractions import Fraction
from itertools import product
from math import comb


def hilbert_counts(n, top=4):
    result = Counter({0: 1})
    for _ in range(n):
        nxt = Counter()
        for d, c in result.items():
            for j in range(top + 1):
                nxt[d + j] += c
        result = nxt
    return result


A = hilbert_counts(3)
R = hilbert_counts(6)
assert A == Counter(sum(v) for v in product(range(5), repeat=3))
assert R == Counter(sum(v) for v in product(range(5), repeat=6))
assert sum(A.values()) == 5**3 and sum(R.values()) == 5**6
assert R == Counter({i: sum(A[j] * A[i-j] for j in A) for i in range(25)})

# Residue action is negative of the three-plus-three block swap:
# the block permutation has determinant (-1)^9 = -1.
primitive_grades = (0, 6, 12, 18, 24)
expected_rows = [
    (0, 1, 1, 0),
    (6, 426, 10, 208),
    (12, 1751, 19, 866),
    (18, 426, 10, 208),
    (24, 1, 1, 0),
]
rows = []
for m in primitive_grades:
    n = R[m]
    fixed = A[m // 2]
    anti = (n - fixed) // 2
    assert n - fixed >= 0 and (n - fixed) % 2 == 0
    rows.append((m, n, fixed, anti))
assert rows == expected_rows, rows

# The quotient's only nonzero rational Hodge types are listed below.
H = Counter({(0, 0): 1, (1, 1): 1, (3, 3): 1, (4, 4): 1})
for m, _, _, anti in rows:
    q = m // 6
    p = 4 - q
    H[p, q] += anti
H[2, 2] += 1  # The ambient hyperplane square.
assert H[3, 1] == H[1, 3] == 208
assert H[2, 2] == 867
assert H[4, 0] == H[0, 4] == 0
assert H[1, 1] == H[3, 3] == 1
assert all(H[p, q] == H[q, p] for p, q in H)
assert all(H[p, q] == H[4-p, 4-q] for p, q in H)

def betti(h, k):
    return sum(v for (p, q), v in h.items() if p + q == k)

B = tuple(betti(H, k) for k in range(9))
assert B == (1, 0, 1, 0, 1283, 0, 1, 0, 1), B
chi_quotient = sum((-1)**k * b for k, b in enumerate(B))
assert chi_quotient == 1287

# The fixed set is two disjoint smooth plane sextics, genus 10.
g = (6-1)*(6-2)//2
assert g == 10
chi_fixed = 2 * (2-2*g)
assert chi_fixed == -36

# Chern class calculation of Euler(X): c4(TX) = [H^4](1+H)^6/(1+6H).
c4 = sum(comb(6, j) * (-6)**(4-j) for j in range(5))
chi_X_chern = 6 * c4
chi_X_hodge = 4 + 1 + sum(R[m] for m in primitive_grades)
assert chi_X_chern == chi_X_hodge == 2610
assert (chi_X_chern + chi_fixed)//2 == chi_quotient
assert (chi_X_chern + chi_fixed) % 2 == 0

# Blowup along two genus-10 curves of codimension three adds two
# Tate-twisted copies of H*(C) for each curve. All added classes are invariant.
HC = {(0, 0): 1, (1, 0): g, (0, 1): g, (1, 1): 1}
HZ = H.copy()
for _ in range(2):
    for twist in (1, 2):
        for (p, q), v in HC.items():
            HZ[p+twist, q+twist] += v
assert HZ[1,1] == HZ[3,3] == 3
assert HZ[2,1] == HZ[1,2] == HZ[3,2] == HZ[2,3] == 20
assert HZ[3,1] == HZ[1,3] == 208
assert HZ[2,2] == 871
assert all(HZ[p, q] == HZ[q, p] for p, q in HZ)
assert all(HZ[p, q] == HZ[4-p, 4-q] for p, q in HZ)
BZ = tuple(betti(HZ, k) for k in range(9))
assert BZ == (1, 0, 3, 40, 1287, 40, 3, 0, 1), BZ
chi_Z = sum((-1)**k * b for k, b in enumerate(BZ))
assert chi_Z == 1215
assert chi_Z == chi_quotient + 2 * (2-2*g) * (3-1)

# Canonical discrepancy from codimension-3 blowup and degree-2 reflection.
# K_{Bl X} = beta^*K_X + (3-1)D,
# K_{Bl X} = r^*K_Z + D and r^*E=2D.
a = Fraction(3 - 1 - 1, 2)
assert a == Fraction(1,2)

print('VERIFY_OK')
print('primitive_degree,total,swap_trace,involution_invariants')
for row in rows:
    print(','.join(map(str, row)))
print('quotient_betti', B, 'chi', chi_quotient)
print('resolution_betti', BZ, 'chi', chi_Z, 'discrepancy', a)

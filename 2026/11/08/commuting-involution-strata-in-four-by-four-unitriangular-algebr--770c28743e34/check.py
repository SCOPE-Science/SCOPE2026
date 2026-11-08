"""Exhaustive square-one and commutation check in UT4 over GF(2) and GF(4).

Uses literal 4x4 matrix products (no symbolic centralizer formulas)."""
from itertools import product


def add(a, b):
    return a ^ b


def mul(a, b, q):
    if q == 2:
        return a & b
    out = 0
    for i in range(2):
        if (b >> i) & 1:
            out ^= a << i
    if out & 4:
        out ^= 0b111  # GF(4) = GF(2)[t]/(t^2+t+1)
    return out


def mm(X, Y, q):
    return tuple(tuple(add(0, __import__('functools').reduce(add,
          (mul(X[i][k], Y[k][j], q) for k in range(4)), 0))
          for j in range(4)) for i in range(4))


def matrix(coords):
    a, b, c, d, e, f = coords
    return ((1, a, d, f), (0, 1, b, e),
            (0, 0, 1, c), (0, 0, 0, 1))


def count(q):
    # This first filtering step computes g^2 using literal multiplication.
    I = tuple(matrix(c) for c in product(range(q), repeat=6)
              if mm(matrix(c), matrix(c), q)
              == ((1, 0, 0, 0), (0, 1, 0, 0),
                  (0, 0, 1, 0), (0, 0, 0, 1)))
    commuting = sum(mm(X, Y, q) == mm(Y, X, q) for X in I for Y in I)
    predicted_involutions = 2*q**4-q**2
    predicted_commuting = q**8+2*q**7-2*q**5
    assert len(I) == predicted_involutions, (q, len(I), predicted_involutions)
    assert commuting == predicted_commuting, (q, commuting, predicted_commuting)
    print(f'q={q} involutions={len(I)} commuting_ordered={commuting} expected={predicted_commuting} ratio={commuting}/{len(I)**2}')


for field_order in (2, 4):
    count(field_order)
print('ALL_DIRECT_CHECKS_PASS')

"""Finite arithmetic checks supporting a characteristic-zero dimension proof.

No finite test certifies the all-degree geometric argument. Run with Python 3.
"""
from itertools import product
from math import comb


def D(n):
    return 0 if n < 0 else (n + 1) * (n + 2) // 2


def rising(k, r):
    z = 1
    for j in range(r):
        z *= k + j
    return z


def mul(p, q, h=1, mod=None):
    """Ore product in k<w,u>/(uw-wu-h*w^2); keys=(w_exp,u_exp)."""
    out = {}
    for (i, j), a in p.items():
        for (k, ell), b in q.items():
            for r in range(j + 1):
                co = a * b * comb(j, r) * rising(k, r) * h**r
                if co:
                    key = (i + k + r, j + ell - r)
                    out[key] = out.get(key, 0) + co
    if mod is not None:
        return {k: v % mod for k, v in out.items() if v % mod}
    return {k: v for k, v in out.items() if v}


def add(p, q, mod=None):
    out = p.copy()
    for k, v in q.items():
        out[k] = out.get(k, 0) + v
    if mod is not None:
        return {k: v % mod for k, v in out.items() if v % mod}
    return {k: v for k, v in out.items() if v}


def sq_zero(A, B, C, Dd, h, mod):
    return all(not add(mul(X, Y, h, mod), mul(Z, W, h, mod), mod)
               for X, Y, Z, W in ((A, A, B, C), (A, B, B, Dd),
                                    (C, A, Dd, C), (C, B, Dd, Dd)))


def check():
    W, U = {(1, 0): 1}, {(0, 1): 1}
    for h in (0, 1, 2, 3):
        lhs = add(mul(U, W, h), {k: -v for k, v in mul(W, U, h).items()})
        assert lhs == ({} if h == 0 else {(2, 0): h})
        # PBW multiplication is associative on a generating basis segment.
        basis = [{(i, j): 1} for i in range(3) for j in range(3 - i)]
        for A, B, C in product(basis, repeat=3):
            assert mul(mul(A, B, h), C, h) == mul(A, mul(B, C, h), h)
    for m in range(1, 61):
        assert D(m) == comb(m + 2, 2)
        for r in range(m):
            for s in range(m + 1):
                for t in range(m + 1):
                    if t + 2*r <= m-1 and t + 2*s <= m and t+r+s <= m-1:
                        lhs = D(r) + D(s) + D(t) - 1
                        rhs = D(r+s+t) + 1 - r*s - t*(r+s)
                        assert lhs == rhs and lhs <= D(m)
    # Verify one member of each square-zero linear family, for general coefficients.
    for h in (0, 1, 2):
        for A, B, C, Dd in [({}, {}, {(0, 0): 3, (1, 0): -2, (0, 2): 5}, {}),
                            ({}, {(2, 0): 2, (2, 1): -3}, {}, {})]:
            assert sq_zero(A, B, C, Dd, h, 101)
    # Exhaust degree <=3 over odd finite fields in the PBW/matrix realization.
    for q in (3, 5):
        count = 0
        for a, b, c0, c1, c2, d in product(range(q), repeat=6):
            A = {(1, 0): a} if a else {}
            B = {(2, 0): b} if b else {}
            C = {key: v for key, v in (((0, 0), c0), ((1, 0), c1), ((0, 1), c2)) if v}
            Dd = {(1, 0): d} if d else {}
            count += sq_zero(A, B, C, Dd, 1, q)
        assert count == q**3 + q**2 - q, (q, count)
    print('SUPER_JORDAN_DIMENSION_DEGENERATION_OK')


if __name__ == '__main__':
    check()

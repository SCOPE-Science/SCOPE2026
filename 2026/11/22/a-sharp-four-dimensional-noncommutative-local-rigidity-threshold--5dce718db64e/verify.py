"""Reproduce finite-field tests for local derivations of two Zinbiel algebras.

Run: python3 zinbiel_local_verify.py
No nonstandard Python packages are required.
"""
from itertools import product


def ops(q):
    if q not in (2, 4, 8):
        raise ValueError('Only q=2,4,8 are used')
    mod = {2: 0b11, 4: 0b111, 8: 0b1011}[q]

    def mult(a, b):
        out = 0
        while b:
            if b & 1:
                out ^= a
            b >>= 1
            a <<= 1
            if a & q:
                a ^= mod
        return out
    inv = [0] + [next(b for b in range(1, q) if mult(a, b) == 1)
                 for a in range(1, q)]
    return mult, inv


def kernel(rows, ncols, q, mul, inv):
    a = [list(x) for x in rows if any(x)]
    pivot_columns = []
    for col in range(ncols):
        pivot = next((r for r in range(len(pivot_columns), len(a))
                      if a[r][col]), None)
        if pivot is None:
            continue
        rank = len(pivot_columns)
        a[rank], a[pivot] = a[pivot], a[rank]
        t = inv[a[rank][col]]
        a[rank] = [mul(t, x) for x in a[rank]]
        for r in range(len(a)):
            if r != rank and a[r][col]:
                c = a[r][col]
                a[r] = [x ^ mul(c, y) for x, y in zip(a[r], a[rank])]
        pivot_columns.append(col)
    free = [i for i in range(ncols) if i not in pivot_columns]
    basis = []
    for f in free:
        v = [0] * ncols
        v[f] = 1
        for rank, p in enumerate(pivot_columns):
            v[p] = a[rank][f]
        basis.append(v)
    return basis


def verify(q, B):
    mul, inv = ops(q)
    n = len(B) + 1
    w = n - 1
    # Multiplication lies in the final coordinate.
    def times(a, b):
        return B[a][b] if a < w and b < w else 0

    assert any(x for row in B for x in row)
    # Derivations as n-by-n matrices in column-major order.
    derivation_equations = []
    for a in range(n):
        for b in range(n):
            for k in range(n):
                eq = [0] * (n * n)
                val = times(a, b)
                if val:
                    eq[w * n + k] ^= val
                for j in range(n):
                    if k == w:
                        eq[a * n + j] ^= times(j, b)
                        eq[b * n + j] ^= times(a, j)
                if any(eq):
                    derivation_equations.append(eq)
    der = kernel(derivation_equations, n * n, q, mul, inv)
    assert len(der) == (5 if n == 4 else 2), (q, n, len(der))

    # For any v, the permitted derivation images form the span of {D(v)}.
    # A linear operator L is local precisely when L(v) is in that span.
    constraints = []
    for coords in product(range(q), repeat=n):
        if not any(coords):
            continue
        images = []
        for d in der:
            images.append([sum_of_products([mul(d[j * n + i], coords[j])
                                            for j in range(n)]) for i in range(n)])
        annihilator = kernel(images, n, q, mul, inv)
        for linear_form in annihilator:
            constraint = [mul(linear_form[i], coords[j])
                          for j in range(n) for i in range(n)]
            constraints.append(constraint)
    loc = kernel(constraints, n * n, q, mul, inv)
    assert len(loc) == len(der), (q, n, len(der), len(loc))
    if n == 4:
        assert not kernel(B, 3, q, mul, inv), 'The bilinear form must be nonsingular'
    print(f'field={q}, dimension={n}, derivations={len(der)}, '
          f'linear-local-derivations={len(loc)}, field-vectors={q**n}')


def sum_of_products(items):
    t = 0
    for x in items:
        t ^= x
    return t


def verify_3d_obstruction(q):
    """All 3D noncommutative, two-step algebras admit a derivation fixing the square."""
    mul, inv = ops(q)
    checked = 0
    for a, b, c, d in product(range(q), repeat=4):
        if b == c:
            continue
        e = b ^ c
        P = [[0, mul(d, inv[e])], [mul(a, inv[e]), 1]]
        B = [[a, b], [c, d]]
        for i, j in product(range(2), repeat=2):
            lhs = 0
            for k in range(2):
                lhs ^= mul(P[k][i], B[k][j]) ^ mul(B[i][k], P[k][j])
            assert lhs == B[i][j], (q, B, i, j)
        checked += 1
    assert checked == q**3*(q-1)
    print(f'field={q}, all noncommutative 3D forms checked={checked}')


if __name__ == '__main__':
    SMALL = [[1]]
    FOUR = [[0, 1, 1], [0, 1, 0], [1, 0, 0]]
    for q in (2, 4, 8):
        for B in (SMALL, FOUR):
            verify(q, B)
        verify_3d_obstruction(q)
    print('VERIFY_OK')

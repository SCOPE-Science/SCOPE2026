"""Exact characteristic-two identities for a genus-two Artin--Schreier--Witt family.

Requires only Python 3. Monomials in a multivariate polynomial over F2 are
stored as exponent tuples, and addition is symmetric difference.
"""

def one(n):
    return {tuple([0] * n)}


def mon(*e):
    return {tuple(e)}


def add(*args):
    z = set()
    for a in args:
        z.symmetric_difference_update(a)
    return z


def mul(a, b):
    z = set()
    for i in a:
        for j in b:
            e = tuple(x + y for x, y in zip(i, j))
            if e in z:
                z.remove(e)
            else:
                z.add(e)
    return z


def powpoly(a, n):
    z = one(len(next(iter(a))))
    while n:
        if n & 1:
            z = mul(z, a)
        a = mul(a, a)
        n //= 2
    return z


def deriv(a, i):
    z = set()
    for e in a:
        if e[i] & 1:
            ee = tuple(x - (j == i) for j, x in enumerate(e))
            z.add(ee)
    return z


# Variables w,t, so that lambda=w^4. Compute the characteristic-two Witt
# subtraction (t^2+t, y1^2+y1+t^2+t^3) and its Artin--Schreier reduction.
w, t, c = mon(1, 0), mon(0, 1), one(2)
lam = powpoly(w, 4)
x = add(powpoly(t, 2), t)
R = add(mul(lam, powpoly(x, 3)), powpoly(t, 2), powpoly(t, 3))
A = lam
B = add(lam, powpoly(w, 2), c)
C = add(w, c)
reduced = add(mul(A, powpoly(t, 5)), mul(B, powpoly(t, 3)), mul(C, t))
h = add(mul(powpoly(w, 2), powpoly(t, 3)),
        mul(powpoly(w, 2), powpoly(t, 2)), mul(C, t))
assert add(R, reduced, powpoly(h, 2), h) == set()
print('EXACT_WITT_TO_QUINTIC_IDENTITY_OK')

# Variables L,T. The polynomial for fibers of the rational classifier is
# F_T(L)=(L^2+L+1)^5 + T*L^6 (subtraction = addition in characteristic 2).
L, T, c = mon(1, 0), mon(0, 1), one(2)
P = add(powpoly(L, 2), L, c)
F = add(powpoly(P, 5), mul(T, powpoly(L, 6)))
assert max(e[0] for e in F) == 10
assert deriv(F, 0) == powpoly(P, 4)
assert powpoly(P, 5) == add(F, mul(T, powpoly(L, 6)))
print('DEGREE_TEN_SEPARABLE_FIBER_IDENTITY_OK')

# Explicit samples over GF(256), using irreducible t^8+t^4+t^3+t+1.
def fm(a, b):
    s = 0
    for _ in range(8):
        if b & 1:
            s ^= a
        b >>= 1
        a <<= 1
        if a & 256:
            a ^= 0x11b
    return s & 255


def fpow(a, e):
    out = 1
    while e:
        if e & 1:
            out = fm(out, a)
        a = fm(a, a)
        e >>= 1
    return out


def inv(a):
    assert a
    return fpow(a, 254)


classes = {}
for lam in range(1, 256):
    sqrt_lam = fpow(lam, 128)
    B = lam ^ sqrt_lam ^ 1
    k = fm(fpow(B, 5), inv(fpow(lam, 3)))
    rational = fm(fpow((fm(lam, lam) ^ lam ^ 1), 5), inv(fpow(lam, 6)))
    assert fm(k, k) == rational
    classes.setdefault(rational, []).append(lam)
assert len(classes.get(0, [])) == 2
assert all((fm(lam, lam) ^ lam ^ 1) == 0 for lam in classes[0])
print('FINITE_FIELD_F256_CLASSIFIER_AND_SPECIAL_FIBER_OK')
print('CERTIFICATE_OK')

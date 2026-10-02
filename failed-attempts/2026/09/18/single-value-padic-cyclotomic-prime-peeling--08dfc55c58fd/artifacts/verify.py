from fractions import Fraction
import math
import sympy as sp

X = sp.Symbol("X")

def vp_int(z, p):
    z = abs(int(z))
    if z == 0:
        return math.inf
    v = 0
    while z % p == 0:
        z //= p
        v += 1
    return v

def vp_frac(z, p):
    return vp_int(z.numerator, p) - vp_int(z.denominator, p)

def recover(n, x, ell):
    C = int(sp.cyclotomic_poly(n, X).subs(X, x))
    w = vp_int(x, ell)
    a = vp_int(C - 1, ell) // w
    r = n // a
    U = (C - 1) // (x ** a)

    if ell != 2:
        t = U % ell
        if t == 1:
            mu = -1
        elif t == ell - 1:
            mu = 1
        else:
            raise AssertionError(("sign", n, x, ell, t))
    else:
        assert a * w >= 2
        t = U % 4
        if t == 1:
            mu = -1
        elif t == 3:
            mu = 1
        else:
            raise AssertionError(("sign", n, x, ell, t))

    found = []
    P = 1
    while P < r:
        R = Fraction(C, 1)
        for d in sp.divisors(P):
            exponent = mu * int(sp.mobius(d))
            f = 1 - x ** (a * d)
            if exponent == 1:
                R /= f
            else:
                R *= f
        q = vp_frac(R - 1, ell) // (a * w)
        assert q > 1 and r % q == 0 and sp.isprime(q)
        found.append(int(q))
        P *= int(q)

    assert P == r
    return found

checked = 0
for n in range(2, 121):
    expected = sorted(sp.factorint(n))
    for x, ell in ((3, 3), (4, 2), (5, 5)):
        assert recover(n, x, ell) == expected
        checked += 1
    if all(e == 1 for e in sp.factorint(n).values()):
        continue
    assert recover(n, 2, 2) == expected
    checked += 1

print("sympy", sp.__version__)
print("verified cases", checked)
print("failures 0")

"""Finite diagnostic for a quartic-norm Fourier convolution; not an infinite proof.

Run with Python 3 standard library: python quartic_check.py
"""
import math


def radius(j, l):
    return math.hypot(j*j, l*l) ** 0.5


def finite_quotient(n, a, p, j_pad=32, l_max=None):
    if l_max is None:
        l_max = math.ceil(14*n**0.75) + 20
    total = 0.0
    for j in range(-j_pad, n+j_pad+1):
        for l in range(-l_max, l_max+1):
            r = radius(j, l)
            s = radius(n-j, l)
            gap = r+s-n
            total += math.exp(-a*gap + p*(math.log1p(n)-math.log1p(r)-math.log1p(s)))
    return total


def check():
    for u in range(-5, 6):
        for h in range(-5, 6):
            v = u+h
            error = v**4-u**4-4*u**3*h-h**4/3
            assert error >= -1e-8, (u, h, error)
    a = 1.0
    p = 1.75
    pred = math.sqrt(2)*math.gamma(0.25)
    rows = []
    for n in (32, 64, 128, 256):
        q = finite_quotient(n, a, p)
        rows.append((n, q, q / math.log(n)))
        assert q > 0
    # Broad diagnostic: no fixed finite N proves the limiting constant.
    assert all(3 < row[2] < 8 for row in rows)
    print("quartic convexity integer grid: passed")
    print("critical predicted coefficient:", format(pred, ".10f"))
    for n, q, scaled in rows:
        print("N=%d quotient=%.8f quotient/logN=%.8f" % (n, q, scaled))
    print("finite checks complete; asymptotic established separately by proof")


if __name__ == "__main__":
    check()

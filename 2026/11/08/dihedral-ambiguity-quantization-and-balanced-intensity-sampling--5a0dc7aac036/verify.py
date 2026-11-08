"""Reproducible finite checks for the two-circle polynomial intensity theorem.

Requires Python 3, SymPy, NumPy. Universal statements are proved in RESULT.md.
"""
import math
import numpy as np
import sympy as sp


def hermitian_evaluations(points, degree):
    rows = []
    for z in points:
        zc = sp.conjugate(z)
        row = [sp.expand((z * zc)**j) for j in range(degree + 1)]
        for j in range(degree + 1):
            for k in range(j + 1, degree + 1):
                u = sp.expand(z**j * zc**k)
                row.extend([2 * sp.re(u).expand(complex=True),
                            -2 * sp.im(u).expand(complex=True)])
        rows.append(row)
    return sp.Matrix(rows)


def main():
    z, w = sp.symbols('z w')
    h1 = (z-1)*(w-1)-2
    h2 = (z+1)*(w+1)-2
    assert sp.expand((z*z-1)*(w*w-1)-4*z*w - h1*h2) == 0
    # This is |z^2-1|^2-|2z|^2=0 on either crossing circle.
    rt2 = sp.sqrt(2)
    bad = [2+sp.I, 2-sp.I, 1+rt2*sp.I, 1-rt2*sp.I,
           -2+sp.I, -2-sp.I, -1+rt2*sp.I, -1-rt2*sp.I]
    assert hermitian_evaluations(bad, 2).rank() == 7
    good = list(bad)
    good[0] = sp.Rational(6,5)-sp.Rational(7,5)*sp.I
    assert sp.simplify((sp.re(good[0])-1)**2+sp.im(good[0])**2-2) == 0
    assert hermitian_evaluations(good, 2).rank() == 8
    # Further noncertificate tests across degrees and rational crossing angles.
    rng = np.random.default_rng(11213)
    checks = 0
    for d in (1, 2, 3):
        for q in (2, 3, 5):
            c = math.tan(math.pi/(2*q))
            radius = math.sqrt(1+c*c)
            angles = [rng.uniform(.1, 2*math.pi-.1, 2*d) for _ in range(2)]
            points = [center + radius*np.exp(1j*t)
                      for center, ts in zip((c,-c), angles) for t in ts]
            rows = []
            for z0 in points:
                row = [abs(z0)**(2*j) for j in range(d+1)]
                for j in range(d+1):
                    for k in range(j+1,d+1):
                        a = z0**j * z0.conjugate()**k
                        row.extend((2*a.real,-2*a.imag))
                rows.append(row)
            sig = np.linalg.svd(np.array(rows), compute_uv=False)
            assert sig[-1]/sig[0] > 1e-10, (d, q, sig[-1]/sig[0])
            checks += 1
    print('TWO_CIRCLE_PROFILE_VERIFY_PASS exact_ambiguity=1 exact_ranks=2 generic_designs=' + str(checks))


if __name__ == '__main__':
    main()

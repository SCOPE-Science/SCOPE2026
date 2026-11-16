"""Self-contained supplementary numerical checks for a nine-site harmonic determinant.

The analytic proof (not these finite samples) establishes the all-height statement.
Requires only Python 3's standard library.
"""
import cmath
import math

PI = math.pi
C = 5189853515625 / (1073741824 * PI**9)


def harmonics(z, phi):
    s = math.sqrt(max(0.0, 1.0 - z*z))
    e = cmath.exp(1j*phi)
    c00 = math.sqrt(1/(4*PI))
    c10 = math.sqrt(3/(4*PI))
    c20 = math.sqrt(5/(16*PI))
    c11 = math.sqrt(3/(8*PI))
    c21 = math.sqrt(15/(8*PI))
    c22 = math.sqrt(15/(32*PI))
    # Condon-Shortley phases; real nonzero signs are determinant-irrelevant.
    return [c00,
            c11*s/e, c10*z, -c11*s*e,
            c22*s*s/(e*e), c21*z*s/e,
            c20*(3*z*z-1), -c21*z*s*e, c22*s*s*e*e]


def determinant(matrix):
    a = [list(map(complex, row)) for row in matrix]
    n = len(a)
    det = 1+0j
    for j in range(n):
        pivot = max(range(j, n), key=lambda k: abs(a[k][j]))
        if abs(a[pivot][j]) < 1.e-25:
            return 0j
        if pivot != j:
            a[j], a[pivot] = a[pivot], a[j]
            det *= -1
        v = a[j][j]
        det *= v
        for k in range(j+1, n):
            w = a[k][j]/v
            for t in range(j+1, n):
                a[k][t] -= w*a[j][t]
    return det


def matrix(x, y, alpha, beta):
    pts = [(-1., 0.)]
    pts += [(x, alpha+2*PI*j/3) for j in range(3)]
    pts += [(y, beta+2*PI*k/5) for k in range(5)]
    return [harmonics(z, phi) for z, phi in pts]


def f(x, y):
    return (1+x)**4*(1-x)**2*(1+y)**8*(1-y)**6*(y-x)**6


def check():
    root = math.sqrt(2305)
    xp, yp = (11+root)/78, 3/26-root/130
    xm, ym = (11-root)/78, 3/26+root/130
    tests = [(xp, yp), (xm, ym), (0.3, -0.4), (-0.45, 0.52),
             (0.9, -0.6), (-0.1, 0.4), (0.0, -0.7)]
    count = 0
    for x, y in tests:
        for alpha, beta in [(0., 0.), (0.19, -0.73), (1.1, 2.03), (2.7, -1.5)]:
            d = determinant(matrix(x, y, alpha, beta))
            target = C*f(x, y)
            assert abs(abs(d)**2/target-1) < 2.e-11, (x, y, alpha, beta)
            count += 1
    for x, y in ((xp, yp), (xm, ym)):
        assert abs(6*x*x-3*x*y-x+y-3) < 1.e-12
        assert abs(7*x*y-x-10*y*y+y+3) < 1.e-12
        count += 2
    baseline = f(math.cos(PI/5), math.cos(3*PI/5))
    gain = f(xp, yp)/baseline-1
    assert 0.12357 < gain < 0.12359
    count += 1
    # Independent random deterministic arithmetic over both chambers.
    for j in range(50):
        x = -0.89 + 1.71 * ((37*j+13) % 101)/100
        y = -0.85 + 1.65 * ((53*j+7) % 103)/102
        if abs(x-y) < .02:
            continue
        alpha = ((23*j+2)%29)/8
        beta = ((31*j+3)%37)/10
        target = C*f(x,y)
        d = determinant(matrix(x,y,alpha,beta))
        assert abs(abs(d)**2/target-1) < 3.e-11
        count += 1
    print(f"PASS: {count} supplementary determinant, stationary-point and reference tests")
    print(f"critical heights {xp:.15f}, {yp:.15f}; determinant-square gain {100*gain:.9f}%")


if __name__ == '__main__':
    check()

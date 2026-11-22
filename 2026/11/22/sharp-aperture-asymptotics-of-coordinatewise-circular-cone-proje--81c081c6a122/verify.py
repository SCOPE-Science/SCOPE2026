"""Numerical checks for a circular-cone metric projector and its Jacobian.

Uses only the Python standard library. Numerical sampling checks examples,
not the universal analytic assertions in RESULT.md.
"""
import math
import random


def project(z, k):
    t = z[0]
    x = z[1:]
    r = math.sqrt(sum(v * v for v in x))
    if t >= k * r:
        return list(z)
    if t <= -r / k:
        return [0.0] * len(z)
    q = (k * t + r) / (1.0 + k * k)
    return [k * q] + [q * v / r for v in x]


def jacobian(z, k):
    t = z[0]
    x = z[1:]
    r = math.sqrt(sum(v * v for v in x))
    u = [v / r for v in x]
    inv = 1.0 / (1.0 + k * k)
    a, b, c = k * k * inv, k * inv, inv
    rho = (1.0 + k * t / r) * inv
    d = len(x)
    j = [[0.0] * (d + 1) for _ in range(d + 1)]
    j[0][0] = a
    for i in range(d):
        j[0][i + 1] = b * u[i]
        j[i + 1][0] = b * u[i]
        for h in range(d):
            j[i + 1][h + 1] = (rho if i == h else 0.0) + (c - rho) * u[i] * u[h]
    return j


def max_1d(f):
    # Fine grid followed by local golden section refinement; evidence only.
    count = 300
    grid = [(f(j / count), j / count) for j in range(count + 1)]
    val, at = max(grid)
    lo, hi = max(0.0, at - 1.0 / count), min(1.0, at + 1.0 / count)
    phi = (math.sqrt(5.0) - 1.0) / 2.0
    p, q = hi - phi * (hi - lo), lo + phi * (hi - lo)
    for _ in range(90):
        if f(p) < f(q):
            lo, p, q = p, q, lo + phi * (hi - lo)
            q = lo + phi * (hi - lo)
        else:
            hi, q = q, p
            p = hi - phi * (hi - lo)
    return max(val, f((lo + hi) / 2.0))


def bounds(d, k):
    c = 1.0 / (1.0 + k * k)
    root = math.sqrt(d - 1)
    A = k * (k + math.sqrt(d)) * c
    B = max_1d(lambda s: s * (k + s + root * math.sqrt(max(0.0, 1.0-s*s))) * c)
    C = max_1d(lambda s: 1 + c * (k*s + k*k *
                (s*root*math.sqrt(max(0.0, 1-s*s)) - s*s)))
    return max(1.0, A, B, C)


def run():
    rng = random.Random(20261116)
    jac_tests = 0
    pair_tests = 0
    for d in (2, 3, 5, 9):
        for k in (0.1, 0.5, 1.0, 2.0, 5.0):
            L = bounds(d, k)
            for _ in range(20):
                x = [rng.uniform(-1.0, 1.0) for _ in range(d)]
                r = math.sqrt(sum(v*v for v in x))
                t = r * rng.uniform(-0.9 / k, 0.9 * k)
                z = [t] + x
                J = jacobian(z, k)
                assert max(sum(abs(e) for e in row) for row in J) <= L + 1e-8
                for i in range(d + 1):
                    eps = 1e-6
                    zp, zm = z[:], z[:]
                    zp[i] += eps
                    zm[i] -= eps
                    p, m = project(zp, k), project(zm, k)
                    for j in range(d + 1):
                        assert abs((p[j]-m[j])/(2*eps)-J[j][i]) < 2e-7
                jac_tests += 1
            for _ in range(20):
                a = [rng.uniform(-2, 2) for _ in range(d + 1)]
                b = [rng.uniform(-2, 2) for _ in range(d + 1)]
                pa, pb = project(a, k), project(b, k)
                assert max(abs(x-y) for x,y in zip(pa,pb)) <= \
                       L*max(abs(x-y) for x,y in zip(a,b)) + 1e-8
                pair_tests += 1
    for d in (20, 100, 1000):
        for k in (0.2, 0.5, 1., 2., 5.):
            g = max(k, 0.5, k*k/2)/(1+k*k)
            L = bounds(d, k)
            assert g - 1e-9 <= L/math.sqrt(d) <= g + 1.5/math.sqrt(d) + 1e-8
    print('PASS:', jac_tests, 'Jacobian finite-difference checks,',
          pair_tests, 'pairwise bounds, 15 uniform-asymptotic inequalities')

if __name__ == '__main__':
    run()

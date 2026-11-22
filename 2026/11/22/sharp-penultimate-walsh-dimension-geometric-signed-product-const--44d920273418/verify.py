"""Finite diagnostics for a real-cube geometric signed-product theorem.

Python 3 standard library only. These tests do not replace the analytic proof.
"""
from fractions import Fraction
from itertools import product
from math import isclose, log, exp, sqrt
from random import Random


def profile(n):
    N = 2 ** (n - 1)
    m = n - 1
    q = 4.0 / N
    z = (2 - q) * m / (m + sqrt(m * m + q * (2 - q) * m))
    sharp = (m ** q) * (m + z) ** (2 - q) / (m + z * z)
    return N, m, q, z, sharp


def sign_rows(n):
    return [(1,) + v for v in product((-1, 1), repeat=n - 1)]


def signed_norms(vectors):
    n = len(vectors)
    dimension = len(vectors[0])
    return {
        signs: max(abs(sum(signs[i] * vectors[i][j]
                           for i in range(n)))
                   for j in range(dimension))
        for signs in sign_rows(n)
    }


def geometric_ratio(vectors):
    n = len(vectors)
    squares = sum(max(abs(v) for v in vector) ** 2 for vector in vectors)
    values = signed_norms(vectors).values()
    if not squares or 0 in values:
        return 0.0
    return exp((2 / 2 ** (n - 1)) * sum(log(float(v)) for v in values)) / float(squares)


def construct(n, z):
    N, m, q, _, sharp = profile(n)
    signs = sign_rows(n)
    paired = {s for s in signs if all(v == 1 for v in s[1:-1])}
    rest = [s for s in signs if s not in paired]
    vectors = [[0.0] * (N - 1) for _ in range(n)]
    for i in range(n - 1):
        vectors[i][0] = 1.0
    for j, s in enumerate(rest, start=1):
        for i in range(n):
            vectors[i][j] = s[i] if i != n - 1 else z * s[i]
    return vectors, paired


def run():
    count = 0
    rng = Random(20261120)
    for n in range(4, 9):
        N, m, q, z, sharp = profile(n)
        assert 0 < z < 1
        assert isclose(q*z*z + 2*m*z - (2-q)*m, 0.0, abs_tol=2e-12)
        assert (2-q)*m > 0 and (-q*(m+1)) < 0
        vectors, paired = construct(n, z)
        assert len(vectors[0]) == N-1 and len(paired) == 2
        observed = signed_norms(vectors)
        assert len(observed) == N
        for s, val in observed.items():
            assert isclose(val, float(m if s in paired else m + z), rel_tol=1e-12)
            count += 1
        assert isclose(geometric_ratio(vectors), sharp, rel_tol=1e-12)
        count += 1
        # Exact rational signed collision inequality: sampled tuples with
        # entries as small rational fractions and independent coordinate widths.
        for _ in range(6 if n >= 7 else 18):
            v = [[Fraction(rng.randint(-12, 12), rng.randint(1, 7))
                  for j in range(N-1)] for i in range(n)]
            radii = [max(abs(a) for a in row) for row in v]
            R, t = sum(radii), min(radii)
            all_values = signed_norms(v)
            # Avoid floating products and overflow by checking logarithms.
            if all_values and 0 not in all_values and t > 0:
                upper = (2-q)*log(float(R)) + q*log(float(R-t))
                actual = (2/N)*sum(log(float(a)) for a in all_values.values())
                assert actual <= upper + 3e-11, (n,actual,upper)
                count += 1
            value = geometric_ratio(v)
            assert value <= sharp + 4e-11, (n,value,sharp)
            count += 1
        # Independent exact sign-collision check with arbitrary rational radii.
        for _ in range(15 if n >= 7 else 60):
            r = [Fraction(rng.randint(1,30),rng.randint(1,10)) for i in range(n)]
            t = min(r);R=sum(r)
            s=R-t
            assert sum(x*x for x in r) >= s*s/(n-1)+t*t
            count += 1
        print(f'n={n} dimension={N-1} exact-root={z:.14f} sharp={sharp:.14f}')
    print('PENULTIMATE_SIGN_PRODUCT_DIAGNOSTIC_OK', count)


if __name__ == '__main__':
    run()

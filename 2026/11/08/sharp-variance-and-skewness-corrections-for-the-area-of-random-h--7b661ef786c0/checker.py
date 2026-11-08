"""Independent finite computations for spherical-triangle area asymptotics.

Run: python checker.py
Only the Python standard library is required. All random seeds are fixed.
Finite sampling corroborates, and does not prove, the asymptotic theorem.
"""
import math
import random


def exact_contractions(d):
    e2 = 1 / d
    e4 = 3 / (d * (d + 2))
    exyz = 1 / (d*d)
    ex2y2 = 1 / (d*d)
    es2 = 3*e2
    esq = 3*exyz
    eq2 = 3*ex2y2
    es_sym = 6*ex2y2
    es_cube = 3*e4
    variance_through_degree_4 = es2 - 2*esq + eq2 + es_sym + es_cube/3
    third_through_degree_4 = -6*exyz + 6*eq2
    assert abs(variance_through_degree_4 - (3/d + 3/d**2 + 3/(d*(d+2)))) < 1e-13
    assert abs(third_through_degree_4 - 12/d**2) < 1e-13
    return variance_through_degree_4, third_through_degree_4


def spherical_point(d, rng):
    vec = [rng.gauss(0, 1) for _ in range(d)]
    scale = 1 / math.sqrt(sum(t*t for t in vec))
    return [t*scale for t in vec]


def dot(a, b):
    return sum(u*v for u, v in zip(a, b))


def geodesic_area(a, b, c):
    # Implements the exact tangent-angle identities, not a Taylor approximation.
    def at_vertex(p, q, r):
        cosine = (r-p*q) / math.sqrt((1-p*p)*(1-q*q))
        return math.acos(max(-1., min(1., cosine)))
    return at_vertex(a, b, c) + at_vertex(a, c, b) + at_vertex(b, c, a) - math.pi


def run():
    rng = random.Random(300731)
    n = 28000
    table = []
    for d in (12, 24, 48, 96):
        exact_contractions(d)
        sums = [0., 0., 0.]
        for _ in range(n):
            u = spherical_point(d, rng)
            v = spherical_point(d, rng)
            w = spherical_point(d, rng)
            a, b, c = dot(u, v), dot(u, w), dot(v, w)
            # Three values are the three cosines of the side lengths.
            value = geodesic_area(a, b, c)-math.pi/2
            sums[0] += value
            sums[1] += value*value
            sums[2] += value*value*value
        mean = sums[0]/n
        var = sums[1]/n
        m3 = sums[2]/n
        v_approx, m3_approx = exact_contractions(d)
        # Sampling tolerances reflect estimated standard errors of raw moments.
        assert abs(mean) < 0.055/math.sqrt(d), (d, mean)
        assert abs(var-v_approx) < 0.29/d, (d, var, v_approx)
        # The third-moment asymptotic converges slowly; only sign is checked.
        assert m3 > -0.5/d**2, (d, m3)
        table.append((d, round(mean, 5), round(d*var, 5), round(d**2*m3, 5)))
    print('RANDOM_SPHERICAL_TRIANGLE_AREA_MOMENTS_OK', n, table)


if __name__ == '__main__':
    run()

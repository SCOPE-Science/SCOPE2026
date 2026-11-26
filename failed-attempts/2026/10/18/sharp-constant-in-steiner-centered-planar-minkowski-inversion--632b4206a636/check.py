"""Numerical regression checks for the explicit balanced sharpness family.

The universal conclusion follows analytically from the identities in RESULT.md.
This finite checker is supporting reproducibility, not a proof by sampling.
"""
import math

PI = math.pi


def green(theta):
    a = (theta + PI) % (2.0 * PI) - PI
    return -math.cos(a) / (4.0 * PI) + (0.5 - abs(a) / (2.0 * PI)) * math.sin(abs(a))


def family(eps):
    c = math.cos(eps)
    s = 1.0 / (1.0 + c)
    mu = [(eps, s / 2.0), (-eps, s / 2.0), (PI, 1.0 - s)]
    nu = [(0.0, s * c), (PI / 2.0, s * (1.0 - c) / 2.0),
          (-PI / 2.0, s * (1.0 - c) / 2.0), (PI, 1.0 - s)]
    return c, s, mu, nu


def mean_and_mass(atoms):
    return (sum(w for _, w in atoms),
            sum(w * math.cos(a) for a, w in atoms),
            sum(w * math.sin(a) for a, w in atoms))


def check(eps):
    c, s, mu, nu = family(eps)
    for atoms in (mu, nu):
        mass, mx, my = mean_and_mass(atoms)
        assert abs(mass - 1) < 1e-12
        assert abs(mx) < 1e-12
        assert abs(my) < 1e-12
        assert all(w > 0 for _, w in atoms)
    # The following four shipments comprise a feasible coupling.
    shipments = [(eps, 0, s*c/2), (-eps, 0, s*c/2),
                 (eps, PI/2, s*(1-c)/2), (-eps, -PI/2, s*(1-c)/2),
                 (PI, PI, 1-s)]
    cost = sum(w * min(abs(a-b), 2*PI-abs(a-b))
               for a, b, w in shipments)
    t = c*eps + (1-c)*(PI/2-eps)
    assert abs(cost-s*t) < 1e-12
    e = (0.5-eps/(2*PI))*math.sin(eps) - (1-c)/4
    gap1 = 2*PI*(sum(w*green(-a) for a, w in mu)
                 -sum(w*green(-a) for a, w in nu))
    gap2 = 2*PI*s*e
    assert abs(gap1-gap2) < 1e-11
    assert e > 0 and t > 0
    ratio = gap2/cost
    assert abs(ratio-2*PI*e/t) < 1e-11
    assert ratio < PI
    return ratio, e/eps, t/eps


if __name__ == '__main__':
    angles = (0.5, 0.2, 0.1, 0.05, 0.01, 0.001, 0.0001)
    out = [check(x) for x in angles]
    ratios = [x[0] for x in out]
    assert all(a < b for a, b in zip(ratios, ratios[1:]))
    assert abs(ratios[-1]-PI) < 0.001
    assert abs(out[-1][1]-0.5) < 0.001
    assert abs(out[-1][2]-1.0) < 0.001
    print('SHARP_PLANAR_MINKOWSKI_INVERSION_CHECKS_OK')
    print('sample lower-bound ratios:', [round(x, 7) for x in ratios])

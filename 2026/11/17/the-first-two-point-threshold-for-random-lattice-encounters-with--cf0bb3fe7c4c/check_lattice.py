"""Numerical checks for first lattice-pair onset under uniform rigid motions.

Run: python check_lattice.py. Requires scipy and numpy.
The checks support rather than replace the analytic asymptotic proof.
"""
import math
from scipy.integrate import quad
from scipy.special import beta


def disk_lens(separation):
    if separation >= 2:
        return 0.0
    if separation <= 0:
        return math.pi
    return 2 * math.acos(separation / 2) - (separation / 2) * math.sqrt(4 - separation**2)


def exact_ellipse_p2(a, b, epsilon):
    assert a >= b > 0 and 0 < epsilon < (math.sqrt(2) - 1) / (2 * a)
    t = 1 / (2 * a) + epsilon

    def weighted_overlap(theta):
        sep = math.hypot(math.cos(theta) / a, math.sin(theta) / b) / t
        return t * t * a * b * disk_lens(sep)

    # The factor 2 accounts for both nearest-neighbor lattice directions.
    return (2 / math.pi) * quad(weighted_overlap, 0, math.pi,
                                 epsabs=2e-13, epsrel=1e-11, limit=300,
                                 points=[0, math.pi / 2, math.pi])[0]


def noncircular_coefficient(a, b):
    return 4 * a * b * b / math.sqrt(a * a - b * b)


def disk_coefficient(radius):
    return 16 * radius**1.5 / 3


def angular_sq_moment(a, b, eps):
    t = 1 / (2 * a) + eps
    c = (a * a / (b * b) - 1) / 2
    scale2 = (2 * a * eps) / c

    def weight(theta):
        sep = math.hypot(math.cos(theta) / a, math.sin(theta) / b) / t
        return t * t * a * b * disk_lens(sep)

    numerator = quad(lambda th: (th * th / scale2) * weight(th), 0, math.pi / 2,
                     epsabs=1e-13, limit=250)[0]
    denominator = quad(weight, 0, math.pi / 2, epsabs=1e-13, limit=250)[0]
    return numerator / denominator


def main():
    assert abs((8 / (3 * math.pi)) * beta(.5, 2.5) - 1) < 3e-15
    for a, b in ((2., 1.), (3., 2.), (1.3, 0.7)):
        C = noncircular_coefficient(a, b)
        ratios = [exact_ellipse_p2(a, b, eps) / (C * eps**2)
                  for eps in (0.02, 0.01, 0.005, 0.002)]
        print('ellipse', a, b, 'ratios', [round(v, 7) for v in ratios])
        assert all(r > 0 for r in ratios)
        assert abs(ratios[-1] - 1) < .02
        assert all(abs(ratios[k + 1] - 1) < abs(ratios[k] - 1) for k in range(3))
    for radius in (1., 2.):
        ratios = [exact_ellipse_p2(radius, radius, eps) /
                  (disk_coefficient(radius) * eps**1.5)
                  for eps in (0.02, .01, .005, .002)]
        print('disk', radius, 'ratios', [round(v, 7) for v in ratios])
        assert abs(ratios[-1] - 1) < .01
    moment = angular_sq_moment(2, 1, 0.002)
    print('conditional normalized angular square', moment)
    assert abs(moment - 1 / 6) < .025
    # Unit square grid cannot contain three distinct points with all separations < sqrt(2):
    candidates = [(i, j) for i in range(-2, 3) for j in range(-2, 3)]
    for a_index, x in enumerate(candidates):
        for b_index in range(a_index + 1, len(candidates)):
            y = candidates[b_index]
            if (x[0]-y[0])**2 + (x[1]-y[1])**2 != 1:
                continue
            common = [z for z in candidates if z != x and z != y and
                      (z[0]-x[0])**2 + (z[1]-x[1])**2 == 1 and
                      (z[0]-y[0])**2 + (z[1]-y[1])**2 == 1]
            assert not common
    print('RIGID_MOTION_LATTICE_TWO_POINT_ONSET_OK')


if __name__ == '__main__':
    main()

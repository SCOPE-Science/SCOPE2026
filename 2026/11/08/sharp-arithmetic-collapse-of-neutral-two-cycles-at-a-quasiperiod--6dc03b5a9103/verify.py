"""Finite numerical replay for the critical clipped-reflection theorem.
Run: python verify.py. Requires Python standard library only.
The infinite-orbit statements are established analytically, not by this test.
"""
import math

TAU = 2 * math.pi


def wrap(t):
    return t % TAU


def parameters(rotation, fraction):
    w = TAU * rotation
    c = math.cos(w / 2)
    b_star = 2 * abs(c) / (1 + abs(c))
    b = fraction * b_star
    A = b / (2 * abs(c))
    a_min = 1 - b / 2 - A
    theta_star = w / 2 if c > 0 else w / 2 + math.pi
    return w, b, A, a_min, theta_star


def mu(theta, w, b):
    c = math.cos(w / 2)
    return -b / 2 - b / (2 * c) * math.cos(theta - w / 2)


def orbit(rotation, fraction, phase, deviation, n):
    w, b, A, a_min, theta_star = parameters(rotation, fraction)
    x = mu(phase, w, b) + deviation
    for _ in range(n):
        x = min(1, -x) - b * (1 + math.cos(phase))
        phase = wrap(phase + w)
    return x - mu(phase, w, b)


def predicted(rotation, fraction, phase, deviation, n):
    w, b, A, a_min, theta_star = parameters(rotation, fraction)
    r = abs(deviation)
    if deviation == 0:
        return 0.0
    if deviation > 0:
        m = n // 2
        record = min([r] + [1 + mu(phase + (2*j+1)*w, w, b) for j in range(m)])
        return record if n % 2 == 0 else -record
    m = (n + 1) // 2
    record = min([r] + [1 + mu(phase + 2*j*w, w, b) for j in range(m)])
    return -record if n % 2 == 0 else record


def covering_radius(w, m):
    points = sorted(wrap(2*j*w) for j in range(m))
    gaps = [(points[(j+1) % m] - points[j]) % TAU for j in range(m)]
    # For m=1, wrap of a full revolution is zero: handle separately.
    if m == 1:
        return math.pi, points[0], wrap(points[0] + math.pi)
    j = max(range(m), key=lambda k: gaps[k])
    return gaps[j] / 2, points[j], wrap(points[j] + gaps[j] / 2)


def replay():
    alpha = (3 - math.sqrt(5)) / 2
    alpha_2 = (math.sqrt(5) - 1) / 2
    tests = 0
    for rotation in (alpha, alpha_2):
        for fraction in (0.45, 0.8, 1.0):
            for phase in (0, .137, 1.8, 4.95):
                for deviation in (-8, -1.2, -0.07, 0, 0.07, 1.2, 8):
                    for n in (0, 1, 2, 3, 4, 5, 19, 50, 101, 240):
                        actual = orbit(rotation, fraction, phase, deviation, n)
                        expect = predicted(rotation, fraction, phase, deviation, n)
                        assert abs(actual - expect) < 4e-12, (rotation, fraction, phase, deviation, n, actual, expect)
                        tests += 1
    worst_cases = 0
    for rotation in (alpha, alpha_2):
        w, b, A, a_min, theta_star = parameters(rotation, 1.0)
        assert abs(a_min) < 1e-13
        for m in (1, 2, 3, 8, 13, 34, 70, 160, 600):
            rho, p, midpoint = covering_radius(w, m)
            # Odd sampling points are theta0 + (2j+1)w.
            phase = wrap(theta_star - w - midpoint)
            actual = abs(orbit(rotation, 1.0, phase, 3.0, 2*m))
            expect = A * (1 - math.cos(rho))
            assert abs(actual - expect) < 1e-11, (rotation, m, actual, expect)
            worst_cases += 1
    print('VERIFY_OK exact_running_min_cases=%d covering_radius_cases=%d critical_rotations=2 source_slope=-1' % (tests, worst_cases))


if __name__ == '__main__':
    replay()

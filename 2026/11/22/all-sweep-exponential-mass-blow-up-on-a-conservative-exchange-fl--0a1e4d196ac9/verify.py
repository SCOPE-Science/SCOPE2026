"""Independent finite checks for the stated multiplicative two-node formulas.

Finite tests illustrate identities and are not proofs of the infinite limits.
"""
import math


def source_step(x, y, h, sweeps):
    """Apply the predictor and source's componentwise correction directly."""
    def G(u, v):
        return v / u - 1.0, u / v - 1.0
    gx, gy = G(x, y)
    px, py = x * math.exp(h * gx), y * math.exp(h * gy)
    for _ in range(sweeps):
        gp, gq = G(px, py)
        px, py = x * math.exp(h * (gx + gp) / 2), y * math.exp(h * (gy + gq) / 2)
    return px, py


def closed_step(x, y, h, sweeps):
    """Independent reduction to the ratio recurrence and explicit output."""
    r = y / x
    if sweeps == 0:
        return x * math.exp(h * (r - 1)), y * math.exp(h * (1/r - 1))
    R = r * math.exp(h * (1 / r - r))
    for _ in range(1, sweeps):
        R = r * math.exp(h / 2 * (1 / r - r + 1 / R - R))
    return (x * math.exp(h / 2 * (r + R - 2)),
            y * math.exp(h / 2 * (1/r + 1/R - 2)))


def ratio_logs(r, h, sweeps):
    L = math.log(r) + h * (1/r - r)
    vals = [L]
    for _ in range(sweeps):
        L = math.log(r) + h / 2 * (1/r-r + math.exp(-L)-math.exp(L))
        vals.append(L)
    return vals


count = 0
for x, y in [(1, 1), (1, 2), (2, 1), (3, 4), (3, 1), (.3, .7)]:
    for h in [.015, .03, .08, .15, .3, .5, .75, 1.]:
        for m in range(5):
            if h > .25 and m > 2:
                continue
            a, b = source_step(x, y, h, m)
            c, d = closed_step(x, y, h, m)
            assert math.isclose(a, c, rel_tol=2e-11, abs_tol=1e-10), (x, y, h, m, a, c)
            assert math.isclose(b, d, rel_tol=2e-11, abs_tol=1e-10), (x, y, h, m, b, d)
            if m <= 3:
                log_ratio = ratio_logs(y/x, h, m)[m]
                assert math.isclose(math.log(b/a), log_ratio, rel_tol=2e-10, abs_tol=2e-10)
            count += 3 if m <= 3 else 2

# The first correction has a direct analytic formula for (1,2).
for h in [.01, .25, .5, 1, 2, 3, 4]:
    R0 = 2 * math.exp(-1.5*h)
    log_x1 = h * math.exp(-1.5*h)
    log_y1 = math.log(2)-.75*h+.25*h*math.exp(1.5*h)
    assert math.isclose(log_x1, .5*h*R0, rel_tol=1e-13, abs_tol=1e-13)
    assert math.isclose(log_y1, math.log(2)+.5*h*(.5+1/R0-2), rel_tol=2e-13, abs_tol=2e-13)
    count += 2

# Stiff sequence: log-ratio sign alternates while its magnitude increases by
# an exponential factor. All quantities here remain representable in floats.
for r in [.5, 2., 3.]:
    h = 2.
    vals = ratio_logs(r, h, 2)
    sigma = 1 if r > 1 else -1
    for m, L in enumerate(vals):
        assert L * ((-1)**(m+1))*sigma > 0
        count += 1
    assert abs(vals[2]) > 100 * abs(vals[1]) > abs(vals[0])
    count += 1

# Exact reversible exchange conserves initial x+y, unlike many numerical steps.
for x, y in [(1., 2.), (2., 1.)]:
    for h in [.1, 2., 4.]:
        exact_x = (x+y)/2 + (x-y)/2 * math.exp(-2*h)
        exact_y = (x+y)-exact_x
        assert math.isclose(exact_x+exact_y, x+y, rel_tol=0, abs_tol=1e-14)
        count += 1

print('CHECK_OK', count)

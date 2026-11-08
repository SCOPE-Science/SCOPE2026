"""Independent numerical checks for a continuous-time hypercube walk with
Poisson resetting. Python 3 standard library only.

One evaluation solves the tridiagonal backward equations for the killed
Hamming-distance process. The other directly integrates the product of
independent-coordinate transition probabilities. No simulation is involved.
"""
import math


def hitting_laplace_tridiagonal(d, k, r):
    assert 2 <= k <= d and r > 0
    # (d+r)f_j = j*f_{j-1}+(d-j)*f_{j+1}, with f_0=1.
    c = [0.0] * d
    b = [0.0] * d
    denominator = d + r
    c[0] = -(d - 1) / denominator
    b[0] = 1.0 / denominator
    for index in range(1, d):
        j = index + 1
        below = -float(j)
        above = -float(d - j)
        denominator = d + r - below * c[index - 1]
        c[index] = above / denominator
        b[index] = -below * b[index - 1] / denominator
    f = b[-1]
    solution = [0.0] * d
    solution[-1] = f
    for index in range(d - 2, -1, -1):
        solution[index] = b[index] - c[index] * solution[index + 1]
    return solution[k - 1]


def hitting_laplace_integral(d, k, r, steps=6000):
    # Simpson integration in x=d*t, with tail x>=60 bounded by e^{-(r/d)x}.
    c = r / d
    endpoint = 60.0 / min(1.0, c)
    steps += steps % 2
    dx = endpoint / steps
    s0 = sk = 0.0
    for i in range(steps + 1):
        x = i * dx
        ex = math.exp(-2.0 * x / d)
        q = (1.0 + ex) / 2.0
        a = -math.expm1(-2.0 * x / d) / 2.0
        p0 = math.exp(-c * x) * q ** d
        pk = math.exp(-c * x) * q ** (d - k) * a ** k
        weight = 1 if i == 0 or i == steps else (4 if i % 2 else 2)
        s0 += weight * p0
        sk += weight * pk
    return sk / s0


def mean_reset_time(d, k, r):
    f = hitting_laplace_tridiagonal(d, k, r)
    return (1.0 - f) / (r * f)


def golden_minimum(fn, left, right):
    ratio = (math.sqrt(5.0) - 1.0) / 2.0
    x1 = right - ratio * (right - left)
    x2 = left + ratio * (right - left)
    y1, y2 = fn(x1), fn(x2)
    for _ in range(100):
        if y1 < y2:
            right, x2, y2 = x2, x1, y1
            x1 = right - ratio * (right - left)
            y1 = fn(x1)
        else:
            left, x1, y1 = x1, x2, y2
            x2 = left + ratio * (right - left)
            y2 = fn(x2)
    x = (left + right) / 2.0
    return x, fn(x)


def run():
    tests = 0
    for d in (4, 7, 12, 24, 48):
        for k in (2, 3, min(d, 4)):
            for c in (0.4, 1.0, 2.0):
                r = c * d
                a = hitting_laplace_tridiagonal(d, k, r)
                b = hitting_laplace_integral(d, k, r)
                assert abs(a - b) / a < 2e-6, (d, k, r, a, b)
                tests += 1
    print(f'{tests} independent backward-equation/Laplace-integral matches')
    for k in (2, 3, 4):
        target = 1.0 / (k - 1)
        coeff = k ** k / (math.factorial(k) * (k - 1) ** (k - 1))
        for d in (20, 40, 80, 160):
            c, val = golden_minimum(lambda z: mean_reset_time(d, k, d * z), 0.08, 3.0)
            print(f'k={k}, d={d}, r_opt/d={c:.8f}, min/d^(k-1)={val/d**(k-1):.8f}, limit={coeff:.8f}')
        assert abs(c - target) < 0.08
        assert abs(val / d ** (k - 1) - coeff) / coeff < 0.17
    print('PASS: independent numerical checks; numerical examples do not prove asymptotic theorem')


if __name__ == '__main__':
    run()

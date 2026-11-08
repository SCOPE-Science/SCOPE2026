"""Finite numerical corroboration of the tangential spectral-curve asymptotics.

Requires mpmath. These finite tests do not certify the infinite-dimensional theorem.
"""
import mpmath as mp

mp.mp.dps = 70


def local_defect(alpha, kappa, eta, n):
    alpha = mp.mpf(alpha)
    kappa = mp.mpf(kappa)
    eta = mp.mpf(eta)
    n = mp.mpf(n)
    eps = n ** (1 - alpha)

    def norm_at_phase(u):
        t = (mp.pi + u) / n
        f = kappa * t ** alpha + eta * t ** (2 * alpha - 1)
        radial = mp.exp(-n * f)
        return mp.sqrt(1 + radial ** 2 + 2 * radial * mp.cos(u))

    optimal_approx = -2 * kappa * alpha * mp.pi ** (alpha - 1) * eps
    u = mp.findroot(lambda x: mp.diff(norm_at_phase, x),
                    (optimal_approx * mp.mpf('0.95'), optimal_approx * mp.mpf('1.05')))
    defect = 2 - norm_at_phase(u)
    first = kappa * mp.pi ** alpha * eps
    second_coefficient = (eta * mp.pi ** (2 * alpha - 1)
                          - kappa ** 2 * (mp.pi ** (2 * alpha) / 2
                                         + alpha ** 2 * mp.pi ** (2 * alpha - 2)))
    return (defect - first) / eps ** 2, second_coefficient, u / eps, -2 * kappa * alpha * mp.pi ** (alpha - 1)


def scaled_power_difference(alpha, kappa, n):
    alpha = mp.mpf(alpha)
    kappa = mp.mpf(kappa)
    n = mp.mpf(n)

    def objective(x):
        t = x / n ** (1 / alpha)
        f = kappa * t ** alpha
        z = mp.exp(-f + 1j * t)
        return n ** (1 / alpha) * mp.exp(-(n - 1) * f) * abs(1 - z)

    start = (alpha * kappa) ** (-1 / alpha)
    maximum_x = mp.findroot(lambda x: mp.diff(objective, x), (start * mp.mpf('0.98'), start * mp.mpf('1.02')))
    predicted = start * mp.exp(-1 / alpha)
    return objective(maximum_x), predicted


def main():
    count = 0
    for a, k, eta in [('2', '0.7', '0'), ('2', '0.7', '0.5'), ('3', '0.7', '-0.1')]:
        err_small = local_defect(a, k, eta, 500)
        err_large = local_defect(a, k, eta, 5000)
        for j in (0, 2):
            assert abs(err_large[j] - err_large[j + 1]) < abs(err_small[j] - err_small[j + 1])
            count += 1
        print('cusp', a, k, eta, 'second-order computed', mp.nstr(err_large[0], 14),
              'predicted', mp.nstr(err_large[1], 14), 'phase-scale', mp.nstr(err_large[2], 14))
    for a in ['2', '3']:
        err_small = scaled_power_difference(a, '0.7', 100)
        err_large = scaled_power_difference(a, '0.7', 2000)
        assert abs(err_large[0] - err_large[1]) < abs(err_small[0] - err_small[1])
        count += 1
        print('power', a, 'computed', mp.nstr(err_large[0], 14), 'predicted', mp.nstr(err_large[1], 14))
    print('TANGENTIAL_CUSP_FINITE_CORROBORATION_OK', count)


if __name__ == '__main__':
    main()

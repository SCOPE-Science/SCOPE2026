"""Reproduce finite tests for the spherical cap-survival asymptotics.

Requires Python 3 and mpmath. These checks supplement the analytic proof.
"""
import mpmath as mp

mp.mp.dps = 75
PI = mp.pi


def inverse_polar(angle, t):
    return angle + mp.asin(t * mp.sin(angle))


def forward_polar(angle, t):
    return mp.atan2(mp.sin(angle), mp.cos(angle) + t)


def boundary_distance(epsilon, t, steps):
    r = PI - epsilon
    for _ in range(steps):
        r -= mp.asin(t * mp.sin(r))
    return r


def spherical_survival(epsilon, t, steps, dim):
    r = boundary_distance(epsilon, t, steps)
    den = mp.beta(mp.mpf('0.5'), mp.mpf(dim)/2)
    return mp.quad(lambda v: mp.sin(v)**(dim-1), [0, r]) / den


def prefactor(dim):
    return 1 / (dim * mp.beta(mp.mpf('0.5'), mp.mpf(dim)/2))


def close(a, b, relative):
    if abs(a / b - 1) > relative:
        raise AssertionError((mp.nstr(a, 20), mp.nstr(b, 20), mp.nstr(a / b, 15)))


for t in (mp.mpf('0.1'), mp.mpf('0.4'), mp.mpf('0.83')):
    for theta in (PI/9, PI/3, 2*PI/3, 8*PI/9):
        close(inverse_polar(forward_polar(theta, t), t), theta, mp.mpf('1e-50'))
        close(forward_polar(inverse_polar(theta, t), t), theta, mp.mpf('1e-50'))

# Special dimensions have elementary cap laws.
for t in (mp.mpf('.35'), mp.mpf('.9')):
    for steps in (0, 1, 3):
        r = boundary_distance(PI/5, t, steps)
        close(spherical_survival(PI/5, t, steps, 2), (1-mp.cos(r))/2, mp.mpf('1e-40'))
        close(spherical_survival(PI/5, t, steps, 3),
              (r/2-mp.sin(2*r)/4)/(PI/2), mp.mpf('1e-40'))

DELTA = mp.mpf('1e-9')
for dim in (2, 3, 4):
    for m, fraction in ((1, mp.mpf('0.75')), (2, mp.mpf('0.4')), (3, mp.mpf('0.15'))):
        epsilon = PI * fraction
        alpha = 2**(m-1) * epsilon
        coefficient = -mp.tan(alpha)
        for extra in (0, 1):
            observed = spherical_survival(epsilon, 1-DELTA, m+extra, dim)
            predicted = prefactor(dim)*coefficient**dim*DELTA**(dim*(extra+1))
            close(observed, predicted, mp.mpf('.001'))
    for m in (1, 2, 3):
        for z in (-2, 0, 2):
            epsilon = PI / 2**m + z*mp.sqrt(DELTA)/2**(m-1)
            coefficient = mp.sqrt(z*z+2)-z
            for extra in (0, 1):
                observed = spherical_survival(epsilon, 1-DELTA, m+extra, dim)
                predicted = prefactor(dim)*coefficient**dim*DELTA**(dim*(extra+mp.mpf('.5')))
                close(observed, predicted, mp.mpf('.001'))

print('SPHERICAL_CAP_SURVIVAL_EXACT_AND_CRITICAL_LIMITS_OK')

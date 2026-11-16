"""Independent numerical checks for the hemispherical SU(2) convolution law.

Only Python's standard library is required. Finite tests do not prove the
analytic all-time identities or the circle-arc monotonicity lemma.
"""
import math

PI = math.pi


def simpson(f, left, right, intervals=20000):
    assert intervals % 2 == 0
    h = (right - left) / intervals
    acc = f(left) + f(right)
    for j in range(1, intervals):
        acc += (4 if j % 2 else 2) * f(left + h * j)
    return acc * h / 3


def lam(k):
    return (-1 if k % 2 else 1) * 4 / (PI * (2 * k + 1) * (2 * k + 3))


def chi_odd(k, theta):
    if abs(theta) < 1e-12:
        return 2*k+2
    return math.sin((2*k+2)*theta)/math.sin(theta)


def tv_series(t, terms=1000):
    return math.fsum(0.5 * (2*k+2)**2 * lam(k)**(t+1)
                     for k in range(terms))


def f_fourier(t, theta, terms=80):
    return 1 + math.fsum((2*k+2)*lam(k)**t*chi_odd(k, theta)
                         for k in range(terms))


if __name__ == '__main__':
    for k in range(12):
        n = 2*k+1
        rhs = 4/(PI*(n+1))*simpson(
            lambda x: math.sin(x)*math.sin((n+1)*x), 0, PI/2)
        assert abs(rhs - lam(k)) < 1e-11
    # Independent geometric two-step overlap and direct total variation.
    for j in range(100):
        theta = PI*j/99
        assert abs(2*(1-theta/PI) - 4*(PI-theta)/(2*PI)) < 1e-14
    direct_two = simpson(
        lambda theta: (2*(1-theta/PI)-1)*(2/PI)*math.sin(theta)**2,
        0, PI/2)
    assert abs(direct_two - (0.25-1/PI**2)) < 2e-11
    assert abs(tv_series(2)-direct_two) < 2e-8
    for t in (3, 4, 5, 6):
        integrate = simpson(
            lambda th: (f_fourier(t,th)-1)*(2/PI)*math.sin(th)**2,
            0, PI/2, 2000)
        assert abs(integrate - tv_series(t)) < 1e-10, (t, integrate, tv_series(t))
        # Fourier truncation is monotone over a mesh, away from endpoints.
        samples = [f_fourier(t, PI*j/100) for j in range(99)]
        assert all(samples[j] >= samples[j+1]-1e-10
                   for j in range(98)), t
        assert abs(f_fourier(t,0.37)+f_fourier(t,PI-0.37)-2) < 1e-10
    assert abs(tv_series(1,10000)-0.5) < 3e-5
    for t in (20, 30, 40):
        asymp = 2*(4/(3*PI))**(t+1)
        assert abs(tv_series(t)/asymp-1) < 1e-12
    print('PASS: character integrals, two-step law, TV series, symmetry,')
    print('finite Fourier monotonicity and sharp asymptotic checks')
    for t in range(1, 7):
        print('t=%d: TV≈%.14g' % (t, tv_series(t,10000)))

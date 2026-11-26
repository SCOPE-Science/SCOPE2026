"""Finite quadrature diagnostics for the Gaussian-mixture null-effect construction."""

from math import erf, exp, inf, pi, sqrt

from scipy.integrate import quad
from scipy.special import ndtr


def density(x, center, s):
    return exp(-0.5 * ((x - center) / s) ** 2) / (s * sqrt(2 * pi))


def cdf(x, center, s):
    return ndtr((x - center) / s)


def integrate(fun, breaks):
    return sum(quad(fun, a, b, epsabs=1e-12, epsrel=1e-12, limit=200)[0]
               for a, b in zip(breaks, breaks[1:]))


def main():
    pos = [0., .5, 1., 1.5, 2., 2.5, 3., 4., inf]
    whole = [-x for x in reversed(pos[1:])] + pos
    for s in [.1, .2, .4, 1., 2., 5.]:
        q = .5 * erf(1 / (2 * s))
        r = .5 * erf(3 / (2 * s))
        w = q / (q + r)
        assert .25 < w < .5
        assert abs((1 - w) * (.5 - 2*q*q) + w * (.5 + 2*q*r) - .5) < 1e-13

        def f(x):
            return .5 * (density(x, -1, s) + density(x, 1, s))

        def g(x):
            return ((1 - w) * density(x, 0, s)
                    + .5 * w * (density(x, -2, s) + density(x, 2, s)))

        def F(x):
            return .5 * (cdf(x, -1, s) + cdf(x, 1, s))

        def G(x):
            return ((1 - w) * cdf(x, 0, s)
                    + .5 * w * (cdf(x, -2, s) + cdf(x, 2, s)))

        assert abs(integrate(f, whole) - 1) < 2e-10
        assert abs(integrate(g, whole) - 1) < 2e-10
        theta = integrate(lambda x: F(x) * g(x), whole)
        j_fg = 4 * integrate(lambda x: F(x) * g(x), pos) - 1
        j_gf = 4 * integrate(lambda x: G(x) * f(x), pos) - 1
        assert max(abs(theta - .5), abs(j_fg - .5), abs(j_gf - .5)) < 5e-10
        tv = .5 * integrate(lambda x: abs(f(x) - g(x)), whole)
        bound = 1 - 4 * ndtr(-.5 / s)
        assert bound - 3e-10 <= tv <= 1 + 3e-10
        print(f"s={s:g} w={w:.12f} theta={theta:.12f} "
              f"J(F,G)={j_fg:.12f} J(G,F)={j_gf:.12f} TV={tv:.9f} bound={bound:.9f}")
    print("PASS six finite quadrature diagnostics")


if __name__ == "__main__":
    main()

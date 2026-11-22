"""Standalone finite checks for exact minimal random-box count; standard library only.

Run with: python3 check.py
These checks do not prove the asserted all-size and asymptotic results.
"""
from fractions import Fraction
from math import comb, exp, log, sqrt, pi, e, gamma


def exact_expectation(n, d):
    assert n >= 1 and d >= 1
    return n * sum(
        (-1)**k * comb(n - 1, k) * Fraction(2, (2*k + 1)*(2*k + 2))**d
        for k in range(n)
    )


def density_product_two(z):
    return 4 * ((1 + z)*log(1/z) - 2*(1-z))


def quadrature_integral(n, steps=16000):
    # z = exp(-s), s in [0,42], removes logarithmic endpoint singularity.
    end = 42.0
    h = end / steps
    def integrand(s):
        z = exp(-s)
        # f_Z(z)*z is the density of minus-log product.
        return n*(1-z*z)**(n-1)*z*4*((1+z)*s - 2*(1-z))
    accum = integrand(0.0) + integrand(end)
    for j in range(1, steps):
        accum += (4 if j % 2 else 2) * integrand(j*h)
    return accum*h/3


def main():
    checks=0
    for n in range(1, 50):
        for d in range(1, 6):
            value=exact_expectation(n,d)
            assert Fraction(1) <= value <= n, (n,d)
            checks+=1
    for n in (1,2,3,4,6,10,20,40):
        q = quadrature_integral(n)
        x = float(exact_expectation(n, 2))
        assert abs(q-x)<1e-8,(n,q,x)
        checks+=1
    assert exact_expectation(1,2)==1
    assert exact_expectation(2,2)==Fraction(35,18)
    checks+=2
    print(f'PASS: {checks} independent rational-bound and density-integral checks')
    for n in (200,1000,10000,100000):
        approximate=quadrature_integral(n)
        leading=sqrt(pi*n)*(log(n)+0.5772156649015328606+2*log(2)-4)
        print(f'n={n} planar integral={approximate:.8f}, two-term={leading:.8f}, residual={approximate-leading:.8f}')


if __name__ == '__main__':
    main()

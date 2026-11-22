"""Finite numerical checks for the exact logarithmic-Bergman boundary-chirp law.

Run: python checker.py. Finite checks corroborate, and do not replace, the proof.
"""
import math
import cmath


def simpson_integral(f, left, right, cells=12000):
    assert cells % 2 == 0
    h = (right - left) / cells
    s = f(left) + f(right)
    for j in range(1, cells):
        s += (4 if j % 2 else 2) * f(left + h * j)
    return h * s / 3


def main():
    checks = 0
    # Independent quadrature in logarithmic coordinates for the damped
    # Gaussian integral, before continuation to the oscillatory boundary.
    for N in (1.0, 2.0, 5.0):
        for beta in (0.2+0.3j, 0.6-0.7j, 1.2+0.1j):
            f = lambda t: cmath.exp(t/2 - N*math.exp(t) - beta*math.exp(-t))
            actual = simpson_integral(f, -12.0, 5.0)
            expected = math.sqrt(math.pi/N)*cmath.exp(-2*cmath.sqrt(N*beta))
            assert abs(actual-expected) <= 2e-10, (N,beta,actual,expected)
            checks += 1
    a = 0.75
    g = a-0.5
    A = math.sqrt(math.pi)/math.gamma(a)
    # The log-weighted monomial moment normalization and positive-symbol
    # eigenvalue are also independently integrated numerically.
    for N in (1, 2, 4, 10):
        moment = simpson_integral(lambda t: math.exp(a*t-N*math.exp(t)), -68, 4)/math.gamma(a)
        assert abs(moment - N**(-a)) < 3e-12
        checks += 1
        mag_moment = simpson_integral(lambda t: math.exp((a-g)*t-N*math.exp(t)), -68, 4)*N**a/math.gamma(a)
        assert abs(mag_moment - A*N**g) < 2e-10
        checks += 1
    # Exact phase-radius spiral and strict positive/every-Schatten contrast.
    for c in (0.03, 0.2, 1.4):
        for N in (1, 2, 7, 19, 57):
            lam = A*N**g*cmath.exp(-2*cmath.sqrt(-1j*c*N))
            target = A*N**g*math.exp(-math.sqrt(2*c*N))*cmath.exp(1j*math.sqrt(2*c*N))
            assert abs(lam-target) < 2e-12
            checks += 1
    # Finite Riemann sums approach the exact sharp quasi-Schatten constants.
    c = 0.002
    terms = 160000
    for p in (0.5, 1.0, 2.0, 3.0):
        empirical = sum((A*(n+1)**g*math.exp(-math.sqrt(2*c*(n+1))))**p for n in range(terms))**(1/p)
        coefficient = A*(2**(-p*g)*math.gamma(2*p*g+2)/p**(2*p*g+2))**(1/p)
        asymptotic = coefficient*c**(-g-1/p)
        assert abs(empirical/asymptotic - 1) < 0.005, (p,empirical/asymptotic)
        checks += 1
    c = 0.0008
    norm_empirical = max(A*N**g*math.exp(-math.sqrt(2*c*N)) for N in range(1,4000))
    norm_asymptotic = A*c**(-g)*(2*g*g)**g*math.exp(-2*g)
    assert abs(norm_empirical/norm_asymptotic - 1) < 0.0005
    checks += 1
    print(f"PASS {checks} finite numerical checks; these are not a proof")

if __name__ == '__main__':
    main()

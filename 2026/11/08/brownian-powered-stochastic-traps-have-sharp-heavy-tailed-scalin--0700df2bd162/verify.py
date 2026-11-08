"""Independent deterministic checks for Brownian-powered trap scaling constants.

Run with Python 3, SciPy and NumPy: python verify.py
The general weak-limit theorem is established analytically, not by these tests.
"""
import math
from scipy.integrate import quad
from scipy.special import erf, gamma

D = 1.3
lam = 0.8
stiffness_base = 0.3
c = math.sqrt(D / lam)


def scaled_variance_linear_path(t, p):
    # Test the deterministic continuous path b(v)=v, for which b(1)=1.
    # This checks the Brownian-scaling identity's singular-endpoint integral.
    T = t ** (1.0 + p / 2.0)
    def integrand(y):
        phase = -math.expm1((p + 1.0) * math.log1p(-y / T))
        return math.exp(-2 * stiffness_base * y / t ** (p / 2)
                        - 2 * lam * T * phase / (p + 1.0))
    hi = min(60., T * 0.9)
    val, err = quad(integrand, 0., hi, epsabs=1e-12, epsrel=1e-12)
    assert err < 1e-9
    # The omitted piece is exponentially tiny for these parameters.
    return 2 * D * val


checks = 0
for p in (1., 2., 4.):
    target = D / lam
    values = [scaled_variance_linear_path(t, p) for t in (100., 500., 2000.)]
    assert values[0] < values[1] < values[2] < target
    assert abs(values[-1] / target - 1.) < 0.025
    print('path integral p=',p,'values=',values,'limit=',target)
    checks += 3

# Integrate the Gaussian scale mixture's characteristic function for p=2.
for q in (0.2, 1.0, 3.0):
    a = q*q*c*c/2
    got, err = quad(lambda g: math.sqrt(2/math.pi) * math.exp(-g*g/2 - a/(g*g)),
                    0., 20., epsabs=1e-12, epsrel=1e-12)
    want = math.exp(-c*q)
    assert abs(got-want) < 1e-10
    print('Cauchy CF:',q,got,want)
    checks += 1

# Check the asymptotic two-sided survival prefactor for three powers.
for p in (1., 2., 4.):
    x = 1000.
    power = 2./p
    def integrand(z):
        return math.sqrt(2/math.pi)*math.exp(-z*z/2)*erf((c*z/x)**power/math.sqrt(2))
    tail, err = quad(integrand, 0., 16., epsabs=1e-13, epsrel=1e-12)
    K = 2**(0.5+1/p)*gamma(0.5+1/p)*(D/lam)**(1/p)/math.pi
    observed = tail*x**power
    assert abs(observed/K - 1.) < 0.01
    print('tail p=',p,'x^power * P=',observed,'K=',K)
    checks += 1

# The p=2 Cauchy prefactor is a special case of the general formula.
assert math.isclose(2**(0.5+0.5)*gamma(1.)*(D/lam)**.5/math.pi, 2*c/math.pi, rel_tol=1e-14)
checks += 1
print('PASS',checks,'deterministic independent checks')

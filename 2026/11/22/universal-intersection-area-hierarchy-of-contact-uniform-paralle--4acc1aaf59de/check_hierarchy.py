"""Independent numerical checks of an exact beta-square intersection-area identity.
The proof is analytic; numerical quadrature is diagnostic only.
Requires Python 3 and scipy.
"""
import math
from scipy.integrate import quad
from scipy.special import beta

for m in (1, 2, 3, 4, 5, 10, 20, 100):
    integral = quad(lambda x: (1 - x*x)**(m/2), -1, 1,
                    epsabs=1e-11, epsrel=1e-11)[0]
    from_integral = integral*integral/4
    from_beta = beta(0.5, 1 + m/2)**2/4
    error = abs(from_integral - from_beta)
    assert error < 1e-10, (m, error)
    if m == 1:
        assert abs(from_beta - math.pi**2/16) < 1e-12
    if m == 2:
        assert abs(from_beta - 4/9) < 1e-12
    print(m, f"numerical={from_integral:.15f}",
          f"beta={from_beta:.15f}", f"abs_error={error:.3g}")

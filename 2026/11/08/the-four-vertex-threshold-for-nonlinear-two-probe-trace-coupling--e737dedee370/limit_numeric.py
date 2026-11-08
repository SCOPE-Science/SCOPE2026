"""Optional numerical check of the asymptotic quantile integral.

Requires SciPy. This is a quadrature estimate, not a certified error bound.
The exact integral and its mathematical limit are established in RESULT.md.
"""
from scipy.integrate import quad
from scipy.special import ndtri

def q(u):
    return (ndtri((1.0+u)/2.0)**2-1.0)/2.0

# Reflection symmetry reduces the integral to (0, 1/2).
half, estimated_error=quad(lambda u: q(u)*q(1-u), 0.0, 0.5,
                           epsabs=2e-12, epsrel=2e-12, limit=400)
print(f"integral estimate={2*half:.15f}")
print(f"variance-ratio estimate={1+4*half:.15f}")
print(f"scipy estimated half-integral absolute error={estimated_error:.3g}")
print("Not a rigorously certified numerical enclosure")

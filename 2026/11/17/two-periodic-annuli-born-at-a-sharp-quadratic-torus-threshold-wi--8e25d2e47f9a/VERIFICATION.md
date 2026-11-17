---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification of the scientific claim

The derivation in `RESULT.md` is an analytic proof, and its only nonstandard geometric factors are reproducible by differentiating the explicit torus parametrization. The parameter threshold is the minimum of \((s+u)/(1-u^2)\) over \((-1,1)\); differentiating gives \(u_*=-s+\sqrt{s^2-1}\). The exact two-annulus normal form follows by completing the square in \(\eta^2(1-u^2)-s-u\). The physical period follows by one elementary trigonometric integral, without reparametrizing time. The area Jacobian is computed with the two tangent vectors and cross-product, then integrated over both signs of \(z\). The arcsine convergence follows from an exact density with a smoothly convergent positive prefactor and the integrable weight \((1-\xi^2)^{-1/2}\).

`CHECK.py` is a standalone standard-library script. Run `python3 CHECK.py`. It verifies the exact rational roots \((-1/4,0)\) and midpoint \(-1/8\) of an explicit periodic band, with period \(8\pi\). Numerical quadrature at \(a=2\) and two small positive critical offsets checks that the renormalized area and period-weighted area approach the explicit constants; it also checks the first two moments of the arcsine limit. It prints `QUADRATIC_TORUS_TWO_BANDS_AND_ARCSINE_CHECK_OK` on success. Finite quadrature is not a proof of the limiting statements and its tolerances are deliberately stated in the script.

The general result's principal limitations are its exact algebraic field, the stationary-circle convention, and the one-sided coefficient limit. External independent verification has not been performed.

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

# Mathematical verification and limits

The analytic proof uses the exact Gamma law for radial Fock Toeplitz eigenvalues, the Gamma Chernoff bounds, the central limit theorem for integer-shape Gamma variables, a smooth cutoff with repeated integration by parts in the supercritical phase, and weighted Weyl equidistribution. No finite experiment is interpreted as an all-degree proof.

For independent verification of the key normalization, with integer \(q=n+d\) the exponential-frequency moment at \(\beta=2\) is exactly \(\mathbb E e^{imU_q}=(1-im)^{-q}\). At criticality, the delta-method variance of \(\sqrt{U_q}-\sqrt q\) is \(1/4\), which yields the Fourier multiplier \(e^{-m^2/8}\), not \(e^{-m^2/2}\) except at Fourier frequency two. The complete degree multiplicity is \(\binom{n+d-1}{d-1}\).

Numerical cross-checks (standardized Gamma density quadrature, with a window of 10 standard deviations and 40,001 evaluation points): for \(d=1,n=1200\), the integral of \(\cos(U_q^{\beta/2})\) is approximately \(-0.51041\) at \(\beta=0.6\), while \(\cos(q^{0.3})\approx-0.51239\); at \(\beta=1\), the integral is approximately \(-0.87861\), while \(e^{-1/8}\cos(\sqrt q)\approx-0.87827\); at \(\beta=1.4\), the integral is approximately \(0.00047\). These checks support but do not validate the infinite-dimensional result. No independent audit, external theorem certification, or unseen computation is asserted.

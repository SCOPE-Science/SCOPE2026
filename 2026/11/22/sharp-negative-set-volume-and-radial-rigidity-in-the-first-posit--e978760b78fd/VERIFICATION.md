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

# Verification notes

The analytic proof is provided in `RESULT.md`. The independent-to-the-derivation computational sanity checks in `artifacts/verify_quartic.py` use Python 3 standard library only. Running `python3 artifacts/verify_quartic.py` completed 1,999 assertions covering exact Gaussian Fourier coefficient transformations, quartic spherical Laplacians, and numerical anisotropic examples. These checks do not verify all dimensions or continuous angular configurations; the symbolic identities and Jensen/integration-by-parts proof cover those.

The statement includes all integer dimensions \(d\ge2\) and all real even degree-at-most-four Fourier-self-dual polynomial Gaussians vanishing at the origin. The nonpositive zero set has zero Lebesgue measure for a nonzero polynomial Gaussian. In the quantitative bound, the spherical quartic is assumed strictly positive. The limiting proof using \(A+\varepsilon\) covers quartics with spherical zeros. Worldwide publication priority and any external mathematical certification have not been established.

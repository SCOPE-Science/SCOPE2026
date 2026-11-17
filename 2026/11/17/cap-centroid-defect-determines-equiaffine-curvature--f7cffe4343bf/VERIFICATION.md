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

# Verification and reproducibility

The analytic argument in `RESULT.md` derives the infinite-limit statement from a \(C^4\) Taylor expansion, a signed inverse-series computation and two exact slice integrals. The separate finite-conic assertion follows from the exact quadratic discriminant and a weighted-mean covariance comparison.

Run `python check_cap_curvature.py` with Python and `mpmath` installed. In this package, execution returned `CAP_CENTROID_AFFINE_CURVATURE_CHECKS_OK`. The tests evaluate exact ellipse, parabola and hyperbola chord-width integrals at four heights and repeat with an asymmetric quartic curve. They confirm signs and decreasing errors, not an exhaustive interval certificate or a proof of the limit.

The graph formula for equiaffine curvature is explicitly normalized as \(k_{\rm ea}=f''''/(3(f'')^{5/3})-5(f''')^2/(9(f'')^{8/3})\), with \(f''>0\). The coefficient is \(\frac{3}{175}(\frac{3}{4\sqrt2})^{2/3}\). The result is pointwise and makes no claim of numerical uniformity over arbitrary convex curves.

Independent mathematical validation: not performed. Historical priority is not certified.

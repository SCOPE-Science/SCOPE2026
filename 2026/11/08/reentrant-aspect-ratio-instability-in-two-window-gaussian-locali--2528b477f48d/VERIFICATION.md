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

The proof is analytic: direct Gaussian overlap, exact Hilbert–Schmidt trace factorization, differentiation in logarithmic aspect ratio, and three controlled asymptotic regimes. The coefficient of the intermediate-area Hessian is \(1/(2\sqrt s)\), strictly positive for all sufficiently large squeezing \(s\). The small- and large-area Hessians have strictly negative leading coefficients for every fixed \(s>1\).

`check_mixed_rectangles.py` is a standard-library Python check. It evaluates three independent overlap integrals by complex midpoint quadrature, three Gaussian convolution integrals by direct two-dimensional midpoint sums, five curvature values by independent centered finite differences, and the predicted sign pattern at squeezing \(s=100\). It also checks that a nonsquare rectangle has larger Hilbert–Schmidt energy at area one. Finite checks do not establish infinitely many parameter cases, exact transition counts, or priority over uninspected literature.

The underlying prior work addresses a fixed single-Gaussian kernel, sharp operator norms, or the general mixed-state convolution formalism. Independent external review has not been performed.

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

# Finite computation checks and analytic limits

Run `python3 verify.py` using Python 3 (standard library only). The checker calculates the weighted monomial coefficients via exact coefficient recurrences in floating point, independently reconstructs small complex Gram matrices from circular samples, verifies their expected diagonal and inverse-trace bound, checks strict improvement over angular perturbations, and bisects the unique radial stationary point across representative exponents and degrees. It also checks the exact unweighted two-point squared radius \(1/4\) and finite-degree consistency with all three asymptotic regimes.

The run passed **278 finite diagnostic assertions**. The infinite assertions in `RESULT.md` are supported by the Schur-complement, Fourier-rigidity, strict-convexity, Riemann-sum, Beta-integral, and endpoint-Laplace arguments, not by numerical extrapolation. The critical \(\log\log N\) law converges slowly, so the finite checks intentionally use loose diagnostics rather than purporting to prove the limiting constants.

No external mathematical audit or validation has been performed. The first-public paper date used is 10 November 2021, explicitly listed in its 2021 author-hosted article PDF. The nearest published condition-number result was available as an indexed statement, but its full repository text was inaccessible; this is a historical-priority limitation.

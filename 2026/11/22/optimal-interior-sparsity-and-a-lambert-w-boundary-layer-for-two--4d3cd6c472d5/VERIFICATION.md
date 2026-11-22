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

# Reproducibility and mathematical verification

Run `python3 check.py` in the folder containing this file. Python 3.9 or later is sufficient; no packages, network calls, or random seeds are required. The checker enumerates each of the nine possible signed/zero outcomes per row, checks exact rank by minors, and compares the resulting rational failure probability with the formula for \(m=2,3,4\), at five rational densities each. It also checks the derivative sign on either side of the computed stationary point for \(2\le m\le160\), the exact \(m=2\) optimum and four finite Lambert-\(W\) diagnostics; the verified output reported 497 checks passed.

For the infinite family, the verification is the all-parameter mathematical argument in RESULT.md: four-line event union, strict derivative-sign classification, and a logarithmic estimate with explicit upper control on the optimizing displacement. Numeric roots do not certify uniqueness or the asymptotic; those assertions are proved analytically.

The computation and theorem use exact rank of real matrices and exclude floating-point stability, spectral conditioning and uniform guarantees for arbitrary subspaces. This package does not contain external independent review.

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

# Reproducibility and verification

Run `python verify.py` from the directory containing this file, `RESULT.md`, and `verify.py`. Requires Python 3.10+ and the publicly available SymPy package version 1.10 or later. The verifier in this package completed successfully, reporting **PASS 1214 checks**, including four symbolic identities derived directly from the four categorical likelihood probabilities, 1,200 independent exact-fraction checks of the determinant and its positivity, four exact-fraction checks of the two competing schedules, two numeric checks of the constant \(a_*\), and four large-budget numerical diagnostics.

Analytical facts not established by finite computation are proven in `RESULT.md`: determinant factorization for all admissible parameters; strict equal-effort optimality at sufficiently small dimensionless effort via uniform strict concavity; the exact finite unequal-effort witness; and convergence of every global maximizer's shorter normalized duration to \(a_*\), including the determinant efficiency asymptotic. The code is an independent algebraic replay and a guard against transcription errors, not an infinite-domain certification. No external validation has been performed.

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

Run `python checker.py` with standard Python 3 (no external packages). The deterministic checker verifies 509 exact-rational or numerical assertions on the finite-generation smoothing-transform recurrence and on its moment/Laplace calculations; the printed pass count is an observed test outcome, not evidence of exhaustive state enumeration. The three symmetric split laws have mass fractions concentrated at \(1/2\), a half-and-quarter mixture, and quarter/three-quarter splitting, respectively.

The infinite-dimensional conclusions depend on the independent analytical argument in `RESULT.md`: mean preservation, strict quadratic-Wasserstein contraction, continuity of convex order under the limiting construction, and strict Jensen comparison. Arithmetic checks neither certify universal correctness nor establish global originality. The stationary-kinetic normalization and asymptotic domain are stated explicitly in `RESULT.md`; no independent audit has been performed.

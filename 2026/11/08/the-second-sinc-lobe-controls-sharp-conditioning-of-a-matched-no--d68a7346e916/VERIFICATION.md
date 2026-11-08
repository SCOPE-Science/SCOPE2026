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

Execute `python check.py` with mpmath installed. The checker implements outward interval arithmetic at 35 decimal digits for 20,001 nodes in each of two intervals. The grid-checking step uses the rigorous mean-value covering radius and globally justified derivative bounds, rather than treating sample points as exhaustive. The proof in RESULT.md gives global derivative sign, convexity, and tail exclusion arguments; the checker verifies critical strict numerical inequalities, root-sign brackets and the multiplier normalization.

This evidence is an analytic proof with computationally assisted rational/interval inequalities. It is not an independent audit. The full mathematical statement covers a continuous Fourier symbol in exact arithmetic; no physical finite-element experiment or discrete PCG run was performed.

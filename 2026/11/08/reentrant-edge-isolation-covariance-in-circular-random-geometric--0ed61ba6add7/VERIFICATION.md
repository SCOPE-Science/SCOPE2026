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

# Reproducible checks

Execute `python3 verify.py` using Python 3 (standard library only) from the extracted package folder. The script evaluates the claimed formula via two algebraic forms at 567 parameter pairs, establishes exact rational signs at selected crossings and interiors, exhaustively enumerates several independently defined small discrete circular-sampling models, and verifies convergence from discrete circle grids to the continuous formula. The recorded total is 588 passed assertions.

The central mathematical evidence is the exact conditional uniform-arc integration and piecewise sign proof in `RESULT.md`; the checker alone is not an all-parameter proof. Discrete-grid checks concern an auxiliary lattice approximation, not an exact identification with the continuous point model. The independently unverified status refers only to external review; no independent validation is claimed.

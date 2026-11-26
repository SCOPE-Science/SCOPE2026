---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproducibility and limits

The proof in `RESULT.md` is self-contained. `check.py` executes finite-step diagnostics of the exact map, including positivity and reciprocal-growth bounds, the two-step normalized mismatch identity, and the alternating endpoint sign bracket. The proof, not the diagnostics, establishes convergence and the existence of at least one critical initial trait. It distinguishes absolute convergence of the amplitude series on the exponential branch from conditional convergence on the algebraic branch. No uniqueness of the critical trait is asserted; finite-precision root numerics do not certify its uniqueness or geometry.

The published model's mathematical endpoint is studied exactly; no independent mathematical validation has been performed.

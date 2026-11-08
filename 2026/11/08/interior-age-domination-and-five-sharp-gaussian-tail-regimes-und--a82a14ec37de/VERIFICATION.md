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

# Mathematical verification

The proof in `RESULT.md` reconstructs the stationary density from Poisson regeneration, verifies matrix inverse derivatives, separates the five strict-convexity and boundary regimes, and derives the exact gamma/Gaussian prefactors by changing variables in the integral. The nonflat case has no other minimizer. The degenerate flat case is exact and handled separately. The conditional reset-age limit laws use the same localized conditional density.

The script `verify_tail.py` was executed using the pinned lower bounds in `requirements.txt` and passed 130 deterministic assertions. It independently computes matrix derivatives, exact two-dimensional geometry, five asymptotic ratios via scaled quadrature, and an exactly flat-rate example. It does not certify the limit at infinite distance or broad literature novelty. All numerical quantities are supplementary to the closed analytical argument.

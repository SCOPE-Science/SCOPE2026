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

# Reproducibility and limits

The proof is self-contained in `RESULT.md`. The independent computational companion is `checker.py`, invoked with `python3 checker.py`; the standard library is sufficient. It evaluates killed two-boundary Brownian cycle probabilities rather than merely substituting the theorem's final formula, checks random resetting laws and thresholds, verifies moment-envelope interpolation and inversion, and simulates independent exact cycle outcomes. The final replay passed 8,276 counted diagnostic assertions.

The experiment is a finite diagnostic and cannot establish the statement for all real parameters and laws. The universal assertions follow from solving linear boundary-value problems, a strictly positive derivative, and sharp convexity inequalities. The result assumes Poisson resetting, bounded positive reset locations, a fixed positive initial position, and observation thresholds larger than both the support and the initial point. No external validation has been performed.

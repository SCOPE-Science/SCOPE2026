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

# Verification notes

The standalone Python file `verify_circumscribed_tradeoff.py` was executed in the delivered package's source directory before packaging. It checks the normalization of the angular sampler, independently evaluates the normalized volume and mean-width risks, finds the exact scalar stationarity root to bisection accuracy, and tests the predicted quadratic multiplier shift and sixth-order minimax-versus-average gap for several nonzero shape parameters. The marker is `CIRCUMSCRIBED_TRADEOFF_NUMERICAL_CHECKS_OK`.

The planar support function and curvature-radius identities are explicit. Exact binomial-series identities, the moments of \(\cos(2\theta)\), and the two derivative formulas in `RESULT.md` allow symbolic reproduction without specialized software. The proof establishes the continuum theorem. The numerical sample does not establish uniqueness, all-dimensional claims, historical priority, or asymptotic remainder bounds.

The preprint first appeared 20 February 2026. Its 13 October 2026 revision is distinguished from first public availability.

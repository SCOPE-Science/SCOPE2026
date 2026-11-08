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
# Verification of the two-by-three martingale Sinkhorn boundary theorem

The included `verify_martingale.py` runs independently from the embedded package with Python 3 and SymPy. It symbolically checks the fixed-point equation and derivative identities, then carries out 350 seeded one-step row/column projection checks. It also evaluates nondegenerate geometric iterations and three boundary cases after 100,000 scalar updates and 60 independent full-matrix alternating KL projections, verifying the square-root growth, negative-endpoint mass, and KL constants. The proof in `RESULT.md`, not these finite calculations, is the justification for the arbitrary-parameter and infinite-time claims.

Reproduction command: `python verify_martingale.py`.

The tests do not claim to cover arbitrary couplings or finite-precision stability. Independent mathematical audit: not performed.

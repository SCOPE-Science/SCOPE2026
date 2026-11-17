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

# Verification

Run `python verify_reentrant.py` with Python 3 and NumPy. The checker was executed in the same packaged directory and printed `VERIFY_OK graphs 4 amplitudes_per_graph 8 checked 32`, followed by the four scaled thresholds. It checks the actual lifted two-step orbit against the theoretical colour flip, the full Jacobian against the weighted Laplacian formula, and attraction/repulsion in all four open regimes on four graph geometries; it also samples 5,000 scalar amplitudes to confirm the sign inequality numerically.

Universal correctness relies on the independent analytic calculations in RESULT.md: signless-Laplacian eigenvalue identification, global positivity of \(q-tq'\), monotonicity and range of \(K\), and the exact Jacobian spectrum. Numerical sampling has no bearing on the global quantifiers or historical priority. None of the neutral boundaries is claimed to be asymptotically attracting. Independent audit: not performed.

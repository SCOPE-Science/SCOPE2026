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

# Verification scope

Run `python3 check.py` after extracting the embedded files together. The exact verifier performs independent weighted enumeration of every ordered pair of code strings for sizes two through five at copying probability one half, computes six raw moment quantities and their centered equivalents, and compares them with the analytical formulas. It also checks endpoint identities and the covariance inequalities at several rational probabilities through size thirty.

On the reviewed artifact the result was: `PASS 749 exact rational checks, independent weighted enumeration n=2..5`.

The asymptotic covariance derivation and limiting Gaussian proof are in `RESULT.md`. Finite enumeration cannot prove a limit theorem. The variance optimizer is certified analytically by the strict positivity of the derivative of its monotonic threshold function and the signs at the two endpoints. No independent external mathematical validation has been performed.

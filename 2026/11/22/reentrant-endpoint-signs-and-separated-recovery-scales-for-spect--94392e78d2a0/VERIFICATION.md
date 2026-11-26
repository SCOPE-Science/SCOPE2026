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

# Verification notes

The analytical evidence is the exact four-eigenvalue projector computation, the monotone rescaled derivative for the distance-two entry, the endpoint sign classification cited in RESULT.md, exact sign bounds at scaled times log 2 and 2, and bracketing at simple limiting zeros on the two time scales. Together these prove the whole-matrix recovery statement and the limiting constants.

The unchanged companion `checker.py` requires Python, NumPy and SciPy. It compares the explicit entries with spectral matrix reconstructions and checks sign and root brackets at selected powers, as well as the scale limits on finite samples. These are finite diagnostics, not proofs of the all-exponent claim; insensitivity to arbitrarily small or faraway roots is not certified by the grid.

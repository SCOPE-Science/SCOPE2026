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

Run `python3 checker.py` using Python 3's standard library only. The checker enumerates actual two-card fair-swap dynamics, verifies the explicit one-sweep joint endpoint law and the reduced-state transitions for all initial difference vectors in dimensions 1 through 5, and checks all two-sweep Chapman–Kolmogorov entries in dimensions 1 through 3. A run returned `PASS: 39668 exact rational equalities`. This finite exercise is not a proof for arbitrary dimension or sweep count; the independent analytic derivation is in `RESULT.md`. The code does not claim independent certification.

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

The standalone exact-integer script `verify_progressions.py` enumerates all admissible and inadmissible candidate first-coordinate steps for each modulus from 2 to 160, including even moduli, and verifies the claim's formulas and full-cycle extension. Re-run with `python verify_progressions.py` in an ordinary Python environment. This is a regression computation; the general proof is independent of the finite check. No independent audit has been conducted.

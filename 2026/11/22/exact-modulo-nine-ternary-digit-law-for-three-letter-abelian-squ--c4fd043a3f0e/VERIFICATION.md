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

# Reproducibility

The finite Laurent identity is verified exactly by `checker.py`, including all Laurent monomials rather than selected coefficients. The checker validates the integer sequence recurrence and compares direct trinomial-square sums for small indices with independently constructed recurrence values. It tests the digit congruence through index 1600. Its tests are finite; the infinite proof is in RESULT.md, equations (1) and (2).

Run with `python3 checker.py` on Python 3 with no third-party dependencies. The algebra certificate is not an independent mathematical audit.

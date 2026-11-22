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

Run `python3 verify_transfer.py` to reproduce the exact transfer, determinant and numerator certificates using only Python's standard library. Run `python3 verify_direct.py` for an independent exhaustive literal enumeration for lengths one through twelve. Both programs executed successfully before the review and agreed with the reported values.

The all-length proof depends on the 72-state complement orbit quotient, the fact that a hole inside the five-character suffix leaves within five ordinary-letter transitions, the 16-state characteristic polynomial, and a rigorous bound of 41 on the numerator degree. Checking an arbitrary finite prefix *without* these structural facts would not prove the theorem.

Asymptotic constants are rounded in prose and defined exactly in the theorem. This is reproducible self-review, not independent validation.

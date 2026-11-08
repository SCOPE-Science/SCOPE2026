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

Run `python3 verify_design.py` with Python 3 and no third-party dependencies. The program compares the stated exact rational endpoint factorization identities; verifies the arithmetic reduction of the two-level obstruction; for each of nine representative admissible dimensions it uses 90-digit decimal arithmetic and interval bisection to construct the promised three positive distinct parameters and verify their first three moments. It also compares all three even partition types of degree six (the sixth single-coordinate moment, the fourth–second mixed moment, and the second–second–second mixed moment).

Successful execution ends with `ALL_CHECKS_PASS`. The checks do not enumerate infinitely many dimensions, are not an independent mathematical audit, and do not certify historical priority. The full all-dimension argument is in `RESULT.md`.

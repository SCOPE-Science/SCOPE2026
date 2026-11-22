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

Run `python3 verify.py` with Python 3. The program enumerates all coefficients and inputs for base primes 3, 5, 7, 11, 13, 17, 19 in exact quadratic-field arithmetic and verifies the permutation and fixed-point counts. It also evaluates exact torus identities for 154 nonsplit cases among primes through 1999. The expected success terminator is `FIELD_FIXED_POINT_DIAGNOSTICS_OK 7 complete prime fields, 154 nonsplit torus fields through 1999`. The exhaustive domain is only the specified small prime fields; those checks cannot certify the infinite classification. The mathematical proof invokes a published criterion for permutation coefficients.

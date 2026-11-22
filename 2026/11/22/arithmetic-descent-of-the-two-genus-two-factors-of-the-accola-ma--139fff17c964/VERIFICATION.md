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

The arithmetic test is the standalone `verify.py` in this package. It enumerates every element and square of the fields of cardinalities 11 and 121; asserts counts (16,118) and (8,118) for the two genus-two quotients, and (12,114) for the genus-four curve; recovers the Weil coefficients; checks group order 14080; and rules out all degree-one and degree-two factors modulo three. The geometric decomposition, twist, and isogeny are proved in `RESULT.md` and are not inferred from finite-field tests. Independent mathematical audit has not been performed.

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

# Reproduction of mathematical checks

Run `python3 checks/verify.py` with Python 3 and the standard library. The checker enumerates the ten parameters of a candidate multiplication table with a fixed flag over the prime fields of sizes 2 and 3, including the two potentially nonzero squares of the second basis vector. It checks the four identities for both the published and the altered fourth identities by evaluating basis triples; triples involving the annihilator are automatically zero. The final output is `FIXED_FLAG_CENSUS_PASS`. The fixed-flag equal and unequal leading-product counts are respectively 28 and 8 over the field of size 2, and 468 and 108 over the field of size 3. The labelled totals are obtained by summing the strata, not by enumerating all labelled tensors. The proof in `RESULT.md` establishes the component geometry and point counts over the stated general fields independently of these checks.

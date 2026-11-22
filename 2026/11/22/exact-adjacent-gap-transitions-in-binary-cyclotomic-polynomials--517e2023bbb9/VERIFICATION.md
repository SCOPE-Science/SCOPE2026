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

# Reproducible verification

The mathematical argument is in `RESULT.md`. Run the attached program with `python verification/verify.py` (Python 3 and SymPy). It computes the coefficient transitions in the semigroup polynomial directly, compares the complete ordered gap-pair counts for 396 integers \(q\), verifies the cyclic insertion increments, and constructs cyclotomic polynomials symbolically for 22 distinct primes to check the equivalence. Last execution output:

`PASS: 396 semigroup moduli; 4 base/insertion checks; 22 independently constructed prime cyclotomic polynomials.`

These tests do not enumerate all integers or replace the infinite periodic-insertion proof. No independent mathematical audit is represented or claimed.

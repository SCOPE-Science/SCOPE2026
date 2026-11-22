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

# Reproducibility and proof boundaries

Execute `python3 verify.py` from the directory containing this document and the script, with Python 3 and its standard library only. The script constructs all polynomials from the defining recurrence, directly evaluates a range of parameters, computes four independent exact signed Sylvester determinants using fraction-free elimination, and compares common factors modulo 25 small primes using finite-field Euclidean division. It also checks complete periods for the three smallest parameters.

The observed terminal output is `VERIFY_OK 1158 exact finite comparisons; 4 Sylvester determinants; 7 polynomial identities`.

The script is a finite consistency check. The proof in `RESULT.md` establishes the claimed identities for every integer parameter and every integer index parameter at least two. It does not prove unrelated statements about arbitrary pairs or factorization of the resultant integers. No independent external audit or certification is claimed.

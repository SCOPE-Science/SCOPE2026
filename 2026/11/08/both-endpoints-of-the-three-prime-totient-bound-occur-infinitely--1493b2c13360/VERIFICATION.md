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

# Reproducibility and limits

Run `python3 verify.py` with a standard Python 3 interpreter. It checks the two exact finite CRT parity certificates using separate inverse-based and CRT-digit constructions, then enumerates all odd integers under the two sample moduli with exact gcd arithmetic. It additionally verifies two extra primes in the lower-bound progression and one in the upper-bound progression.

Expected primary certificate tuples \((|G_P|,O_P,B_r,S,T,2T-S)\) are \((63,30,68,21861,10924,-13)\) and \((75,38,70,20025,10018,11)\). These finite checks are reproducible and do not constitute an infinite proof. The period assertion is proved algebraically in RESULT.md, and infinitude uses Dirichlet's theorem for arithmetic progressions. Independent mathematical audit has not been performed.

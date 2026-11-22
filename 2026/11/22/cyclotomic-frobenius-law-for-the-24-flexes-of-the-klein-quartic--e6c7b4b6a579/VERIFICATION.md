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

# Verification of the cyclotomic flex calculation

The included `VERIFY.py` is an executable exact certificate, requiring SymPy (see `requirements.txt`). It checks the integral Hessian identity, both affine equations at each of four cyclotomic representatives, the complete affine elimination polynomial, the four elimination/minimal-polynomial identities, all relevant discriminants and cross-resultants, and the four Frobenius cycle profiles (one for each distinct residue behavior). Success prints `KLEIN_FLEX_CYCLOTOMIC_CERTIFIED_OK`.

**Limits.** Computer algebra verifies finite identities; the mathematical proof supplies uniformity for infinitely many primes by the resultant/discriminant bounds and Bézout. A single fixed plane model is studied. Prior knowledge covers the geometric 24-point orbit and the characteristic-five row. No independent external scientific audit has been performed.

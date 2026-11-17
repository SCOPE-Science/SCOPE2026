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

# Verification

The analytical proof in `RESULT.md` is self-contained and covers all real and complex matrices of order three. The source comparison uses the accessible author manuscript of Foucart's 2016 article, especially §4, Theorem 1, Theorem 3 and Corollary 4. The exact radical is supported by the rank-one singular-value calculation; the full-rank bound is strict and does not rely on sampled unitary matrices.

Run `python3 check_constant.py` with Python 3 and NumPy. The checker evaluates the rational critical identities, the exact extremizing real matrix to numerical tolerance, 3,000 seeded real/complex partial-isometry tests and a finite unitary-eigenangle grid. Numeric tests are corroboration, not an exhaustive matrix search. The full proof does not rely on randomized evidence.

The independent audit channel is not performed; no independent verification or certification is asserted.

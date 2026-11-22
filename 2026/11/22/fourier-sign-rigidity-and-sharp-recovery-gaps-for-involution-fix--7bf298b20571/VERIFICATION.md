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

The included `verify.py` is a standalone Python 3 exact-integer reproduction script. It uses direct recursive involution enumeration to generate full fixed-point masks, a separate fast Walsh–Hadamard transform, and a closed-form binomial enumeration for the comparison. It checked all 4094 frequency values for orders 1 through 11. Exact recurrence and symmetry tests extend through order 60. The output was `PASS`.

The all-order theorem rests on the separate Gaussian moment/inclusion-exclusion argument and the adjacent-weight induction in `RESULT.md`; finite enumeration cannot establish the infinite result. No external independent audit has been performed.

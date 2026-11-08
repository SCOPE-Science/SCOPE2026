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

Run `python signed_perm_checker.py` with Python 3 (standard library only). The checker uses exact rational arithmetic and explicit complete enumeration at \(n=2,3,4\), together with exact formula/witness tests at larger finite ranks. Successful output ends with `ALL_SIGNED_PERMUTATION_MATRIX_COEFFICIENT_CHECKS_OK`. The proof of the universal statements is in `RESULT.md`; no sampling or finite enumeration certifies the theorem for all ranks. The self-review has passed; independent audit has not been performed.

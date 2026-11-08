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

The supplied `verify_hadamard.py` executes with standard Python 3 and no external packages. Its exact arithmetic checks the Walsh quadratic character expansion and its Parseval identity for various dyadic sizes, the closed variance for uniformly chosen row subsets, exhaustive row-subset cases, every possible common sign vector in small dimensions, exact independent-sign variance, and matching-permutation sharpness. The code independently enumerates the combined shared-sign and row-sampling probability space for one nontrivial asymmetric positive-semidefinite example.

The recorded execution result is `PASS 3151 exact variance and equality assertions`. A replay after extracting the actual embedded program and comparing the output byte-for-byte is required before using this file as delivered evidence. The universal proof is provided in RESULT.md and does not follow from a finite run. Uninspected specialist literature means originality cannot be independently certified.

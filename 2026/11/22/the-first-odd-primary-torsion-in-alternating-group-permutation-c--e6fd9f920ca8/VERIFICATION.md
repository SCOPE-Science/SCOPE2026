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

The executable `verify_a6.py` reconstructs the integer matrix directly from the 360 even full words and the 720 five-letter words. A deterministic 354-step integer unit-pivot reduction is followed by exact Smith normal form of a 366-by-6 remainder; the Smith diagonal is (1,1,1,1,1,3). Finite-field Gaussian elimination independently returns ranks 360,359,360,360,360 for primes 2,3,5,7,11. The standard full injective-word complex has exact cellular chains below top dimension, yielding the remaining ranks. The code does not perform a full all-size classification, a homotopy-type proof, or an independent mathematical audit.

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

# Reproducible checks and limits

Run `python3 verify_rule23.py` and `python3 verify_signed_shift.py` from the extracted package directory. The first script implements the in-place majority-complement update literally and checks the asserted image, invariance, and exact fixed counts at all temporal indices from one through twice the spatial circumference for each circumference three through fourteen. The second independently implements packed-bit truth-table updates, verifies their agreement with the stated affine shift throughout the core up to circumference seventeen, and computes temporal fixed counts independently up to circumference eleven.

The exact captured standard outputs are supplied as `direct_output.txt` and `signed_output.txt`. All indicated assertions passed. These computations are finite cross-checks, not a replacement for the symbolic all-length proof. No independent mathematical audit has been performed. The characterization is restricted to cyclic binary rings, the fixed left-to-right scan, and lengths at least three.

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

# Reproducibility checks

Run `python3 verify.py` with a Python 3 standard-library interpreter in the directory containing this document and the accompanying source. The checker independently enumerates the 1-, 2-, and 3-root forest weights, compares exact rational variance with the derivative of the partition function at 15,870 parameter tuples, verifies inversion symmetry and tests the hyperbolic identity for diverse edge ratios. Expected ending: `VERIFY_OK 31816 exact rational and independent numerical checks`.

The proof is symbolic and parameter-uniform; finite enumeration alone would not prove the infinite continuum statement. No independent external mathematical audit or certified theorem prover run has been performed. Historical-priority uncertainty remains.

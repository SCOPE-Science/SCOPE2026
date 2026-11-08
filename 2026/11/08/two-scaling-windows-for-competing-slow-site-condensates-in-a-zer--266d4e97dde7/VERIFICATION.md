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

Run `python3 verify.py` with the Python 3 standard library. The packaged checker independently enumerates 28 small labeled-state systems (four ordinary-site counts and masses from zero through six as coded), verifies stationary inflow/outflow and flux, and checks exact two-defect partition formulas. It compares increasingly large canonical sums with the critical and condensed limit predictions for several positive, zero, and negative asymmetries.

The finite checks are not proofs of limits. The infinite-size argument uses exact product-form balance, the geometric local central limit theorem and lower-tail control, and Riemann-sum evaluation; see `RESULT.md`. No external certification or independent audit has been performed.

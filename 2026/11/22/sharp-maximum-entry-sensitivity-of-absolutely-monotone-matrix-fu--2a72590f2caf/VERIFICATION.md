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

The analytical proof is contained in `RESULT.md`. Run `python check.py` with NumPy; this exercises the rank-one row extremizer, derivatives of matrix powers and resolvents, and sampled two-input inequalities. A finite test is not a proof for all dimensions, functions, or matrices. The hypotheses about positivity of coefficients and convergence radius are essential. Independent external audit has not been performed.

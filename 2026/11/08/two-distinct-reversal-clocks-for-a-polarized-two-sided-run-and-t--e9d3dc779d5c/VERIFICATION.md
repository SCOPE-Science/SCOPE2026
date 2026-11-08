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

Run `python check.py` from this directory with SciPy installed. It independently integrates Beta holding-time fractions conditional on Poisson flip counts, compares the first absolute displacement with the Bessel expression, solves the two crossing equations, verifies the predicted ordering, and samples the analytic strict-inequality proof. The checker passed. Finite numerical calculations cannot establish the universal result; the proof in `RESULT.md` establishes the full parameter range. Primary literature was not independently audited in full.

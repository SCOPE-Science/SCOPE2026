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

# Verification notes

The source `verify_trace.py` was run with Python, NumPy, SymPy and mpmath. The recorded output `verification_output.txt` reports 396 passing tests, a high-precision numerical threshold, quadrature comparisons and direct Gaussian estimator simulations. The analytic proof in `RESULT.md` independently justifies all universal and asymptotic claims; Monte Carlo tolerances are validation aids rather than probability-one certificates. The tests also verify the exact symbolic variance-difference polynomial and root sign pattern. No independent audit has been performed.

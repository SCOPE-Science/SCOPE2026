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

# Reproducible verification

Execute `python checker.py` with Python 3, SymPy and mpmath. The script uses fixed random seeds, evaluates 70 independent stationary covariance integrals, performs 150 separate exact-lobe comparisons, and symbolically verifies the coefficients of the exponential formula. It prints representative finite-root counts. All these tests passed before packaging and are replayed from the embedded file after extraction. A finite set of tests cannot certify the global classification; the main proof establishes the infinite cases and the exact parameter staircase by monotone lobe maxima. The sole independent scientific audit remains unperformed.

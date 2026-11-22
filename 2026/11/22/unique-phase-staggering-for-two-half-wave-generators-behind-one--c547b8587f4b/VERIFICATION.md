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

The proof uses exact integrations and global sign inequalities. Run `python CHECKER.py` using the Python 3 standard library. On the packaged source, 848 supplementary assertions pass. The script recomputes the objective from its original integral on a midpoint grid, independently compares the exact formula, and tests stationary roots, monotonic optima and asymptotic ratios. Numerical integration, sampled parameter grids and finite calculations do not certify the theorem for all parameters; the analytic proof in RESULT.md does.

The premise is only the mathematical capped half-wave model and not measured PV performance. Independent scientific review remains unperformed.

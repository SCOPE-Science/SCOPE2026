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

Run `python3 verify.py` in a Python 3 environment. This script was executed directly from the delivered package path and passed 480 high-precision finite assertions for masses, first two raw moments and centered influence variance, and the limiting-constant/root and convergence assertions. The analytic proof of the nonfinite CLT and Poisson local limit steps is in `RESULT.md`; no finite grid is presented as exhaustive, and no independent audit is asserted.

For all parameters the source statistic is explicitly defined in `RESULT.md`. The test's rejection statement is for fixed alternative parameters as sample size increases; the total-variation asymptotic is a separate parameter sequence.

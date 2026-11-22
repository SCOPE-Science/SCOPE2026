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

# Reproducibility

Run `python3 CHECK.py` from this package. Only Python 3 standard library is needed. The file implements an independent Gaussian-elimination solve of the stationary row vector for 2,590 positive Markov kernels, checks conserved edge current and its sign against the analytic product expression, tests canceling destination-only quality factors, and checks the equal-mean two-root witness.

The printed roots are numerical cross-checks of the exact Lambert-\(W\) formulas. No finite test proves the all-size root bound. The proof is self-contained in RESULT.md, including its strict positivity and all coefficient degeneracies. In this self-review the test completed without assertion failure; the numerical environment is not a separate independent audit.

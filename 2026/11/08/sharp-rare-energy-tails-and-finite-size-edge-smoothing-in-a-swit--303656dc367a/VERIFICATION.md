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

# Verification of empirical-energy edge and tail formulas

The exact stationary variance mixing density is obtained by solving the two-state stationary flux equations, with \(a=D/\mu_1\), \(b=D/\mu_2\), \(p=r_1/(2\mu_1)\), and \(q=r_2/(2\mu_2)\). Conditional chi-square integration gives the exact density at every finite particle number. The proof in `RESULT.md` derives the good large-deviation rate, both one-sided exponential-plus-power asymptotics, both Gaussian-convolution edge limits, and the threshold probability prefactors by explicit saddle analysis.

`CHECK.py` requires the package specified by `requirements.txt`; run it from the same directory. The checker evaluates the exact integral with arbitrary-precision arithmetic, verifies mixing normalization and moments, compares 12 pairs of outer-tail/edge asymptotics for each of two parameter families, and separately examines the four signed scaled-edge offsets in each family. It reports forty finite numerical diagnostics. These experiments are reproducibility checks only, not exhaustive verification for all real parameters or an independent audit.

Checks do not cover degenerate trap stiffnesses, zero switching rates, nonstationary initial conditions, simultaneous particle-number and physical-parameter limits, or shrinking energy thresholds approaching zero. The fitted algebraic powers are derived from the analytic proof and must not be inferred solely from the finite checks.

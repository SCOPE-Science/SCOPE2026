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

# Verification and scope

Run `python3 checker.py` in a Python 3 standard-library environment. The deterministic output is recorded in `CHECKER_OUTPUT.txt`: 1124 finite diagnostics passed, testing the exact adjacent difference, threshold roots, discrete monotonicity, direct trigonometric quadrature, asymptotic scaling and moment-match discrepancy. The analytic steps for every positive real time and all integer orders are in `RESULT.md`; no finite test is being offered as a proof for those infinite statements.

The error is normalized with the probability measure \(d\theta/(2\pi)\). The approximation family is translated, nonnegative, mean-one Fejér kernels indexed by positive integers, with a constant kernel at order one. The term \(O(N^{-4})\) is at fixed heat normalization, from the Euler–Maclaurin expansion with a nonzero derivative at the limiting root. The first-moment comparison uses rounding of \((1-e^{-t})^{-1}\) to a positive integer and is asymptotic only as \(t\downarrow0\).

No independent mathematical review has been performed.

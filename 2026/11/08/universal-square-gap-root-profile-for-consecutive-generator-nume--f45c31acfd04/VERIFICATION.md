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

# Reproducibility and verification

The analytic claim is proved in `RESULT.md`: an exact elementwise semigroup test, a complete quadratic Gauss-correlation bound for all moduli, a standard two-dimensional Erdős–Turán–Koksma estimate, and monotone-curve rectangle bracketing. It does not depend on extrapolating finite computations.

Run the Python standard-library-only checker with `python check.py` in the same directory. The expected unedited output is `check-output.txt`. The checker compares 5,247 semigroup membership instances with direct generator enumeration; separately verifies 1,260 numerical instances of the complete quadratic-sum bound and reports square-gap counts for nine sample moduli through 100,000. Checks use floating-point arithmetic only for the finite exponential-sum corroboration; the general exponential-sum bound is proved by exact orthogonality.

Scientific limits: the displayed absolute implicit error constant is not numerically optimized; the bound is for all integers \(m\ge2\) and fixed or moving macroscopic half-open windows, not for sub-power-length windows. Residual priority risk is an unidentified equivalent application in the wider literature. Independent audit has not been performed.

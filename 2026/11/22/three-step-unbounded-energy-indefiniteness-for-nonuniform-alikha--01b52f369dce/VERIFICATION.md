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

The coefficients are obtained from the quadratic interpolants on completed intervals and the affine interpolant on the final fractional interval. Exact symbolic integration gives \(A_{\alpha}=\alpha/[(1-\alpha)(2-\alpha)]\). An elementary reflected-integral comparison proves \(B_{\alpha}>0\) for \(0<\alpha<1\). The limiting energy follows by taking the three relevant matrix coefficients, with the positive factor \(\Gamma(1-\alpha)^{-1}\) kept explicit.

The reproducibility script `checker.py` uses only Python's `decimal` module for the \(\alpha=1/2\) case. It constructs the three-step operator from each interpolation segment, checks a fully rational mesh and integer-increment negative witness, then checks convergence to the stated asymptotic coefficient. Its recorded execution is in `checker-output.txt`. The separate `general_order_check.py` evaluates the analytically derived coefficients for fractional orders 0.2, 0.5 and 0.8; see `general-order-output.txt`.

The script's numerical cases do not establish the all-\(\alpha\) result, which follows from the written integral argument. No independent mathematical audit or historical-priority certification has been carried out.

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

# Verification of finite-time inverse-square expansion

Run `python verify.py` with SymPy installed. It simplifies the polynomial GAL reduction and the exact inverse-square recurrence, and checks ten finite signed parameter samples with \(x_0=0.4\) and \(n\varepsilon\) near \(1.2\). It also tests numerical convergence of \(y_n-2n-(3/2)\log n\) at the exact critical point. The successful terminal line is:

`VERIFY_OK exact_recurrence=1 GAL_reduction=1 signed_crossover_samples=10 critical_constant=1`

Finite tests do not certify the all-time or uniform parameter-window claims. The proof uses geometric comparison and summation bounds, not extrapolation from this script. The numerical coefficient ratios converge slowly because the correction itself is logarithmic; the code checks bounded residuals rather than falsely presenting modest parameter sizes as exact convergence.

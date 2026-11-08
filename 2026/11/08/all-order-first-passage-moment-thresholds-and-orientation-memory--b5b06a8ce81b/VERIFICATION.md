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

# Verification performed

The stated theorem follows analytically from five steps reproduced in `RESULT.md`: moment generator identities; monotone coupling and martingale time-scale lower bound; divergent integrating-factor integral for necessity; explicit polynomial Foster–Lyapunov functions and compact regeneration for sufficiency; and an all-order power-tail induction for coefficients. Every parameter range is included in the theorem and a fixed moment order is assumed.

The supplied `check_hierarchy.py` was executed with Python 3, SymPy, NumPy, and SciPy. It reported `symbolic_assertions 34`. With speed \(v=1/2\), flip rate \(\gamma=1\), and \(\beta=8\), the exact predicted coefficients for moment orders one, two, and three were `4/7`, `16/35`, and `64/105`. For starting positions \(20,40,80\), the computed order-three average normalized by its predicted asymptotic term was `1.50839, 1.31091, 1.21638`, and the normalized sign difference was `1.43348, 1.27794, 1.19966`. All symbolic assertions completed successfully, and all finite-domain solves returned positive moments. These finite-size diagnostics cannot establish exact asymptotics or an infinite-time theorem by themselves.

The boundary for the numerical scheme is artificially absorbing at a distant position and the upwind grid introduces truncation error; both can affect the ratios. The analytic theorem covers \(x>v^{-1}-1\) and fixed finite moment orders only, with no numerical error bound or uniformity in order.

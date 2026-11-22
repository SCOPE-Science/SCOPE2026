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

The standalone file `check_inverse.py` was run with Python 3 and the standard library, producing `PASS 1105 finite diagnostics`. It checks the exact rational negative-Jacobian witness using a lower Taylor bound on \(\cosh(3)\), the determinant formula against direct matrix arithmetic, positive Jacobian signs for diffeomorphic regimes, and three converged distinct numerical inverse solutions at \((T,\alpha)=(23/10,1/2)\). At \(T=20/3\), \(\alpha=1/2\), it verifies a decreasing positive determinant along the suggested path toward a singular limit at infinity.

The infinite all-target claims are **not inferred** from these finite tests. They follow from exact analytic arguments in RESULT.md: properness and mapping degree, positivity of the full-plane Jacobian in the injective regimes, the exact rectangular image at unit step, a strict negative-Jacobian region beyond the threshold, and the degree forcing two additional positive inverse branches. Numerical roots are not used to certify exhaustive inverse multiplicities at any particular output. Independent validation has not been performed.

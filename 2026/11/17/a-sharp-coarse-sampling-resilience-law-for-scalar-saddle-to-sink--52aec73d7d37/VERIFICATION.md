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

The theorem is an analytic statement for all stated \(C^2\) scalar vector fields, not a numerical extrapolation. To reproduce its finite tests using Python 3 and only the standard library, run `python CHECK.py` in the package directory. The program checks algebraic logistic and cubic intensity identities, a fixed-eigenvalue nonlinear-deformation prefactor using Simpson quadrature and flow-coordinate bisection, and sampled coarse times. Every assertion must complete for the script to print its pass message. The exact cubic formula is credited to Yu and Wang (2026), arXiv:2608.02933.

The generic proof's critical steps are the previously established finite-\(h\) barrier formula, a half-orbit forcing both endpoints into the maximizer limit, the stationary relation \(f(y_h)=f(x_h)\), and the convergent endpoint logarithmic asymptotics of the inverse-time coordinate. The code has no authority to verify these infinite statements; the numerical tests are supplementary. The historical originality review is limited to inspected scientific sources and mathematical-record search coverage.

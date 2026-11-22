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

# Verification and reproducibility

The mathematical proof is in `RESULT.md`. Run `python3 check_marks.py` in an environment providing Python 3, SciPy, and SymPy. The executed checker completed 109 assertions, computing the exact circular beta-integral coefficient, independently integrating the finite-radius marked densities, and comparing rectangular and elliptic meridian examples with the stated first-order and second-order behaviors. The code contains no numerical evidence for a universal quantifier; the analytic support-function and total-variation arguments cover the general theorem.

At unit circular meridian, the exact conditional density is \(x/(J_R\sqrt{1-x^2/R^2})\) on the triangle \(x>0,y>0,x+y<1\), where \(J_R\) is the one-dimensional normalization integral written in the proof. The target density is \(6x\); this defines the exact finite-\(R\) comparison. For a rectangular meridian of horizontal half-width \(a\), the numerical total-variation product \(R\,d_{\mathrm{TV}}\) tends to \(2a\). For elliptic meridians the first-order coefficient vanishes and the tested error is of order \(R^{-2}\).

Verification here is analytical proof plus same-model finite checks; no independent audit, external certification, or universal symbolic verification has occurred. Numerical quadrature depends on the stated package versions and cannot eliminate all implementation risks.

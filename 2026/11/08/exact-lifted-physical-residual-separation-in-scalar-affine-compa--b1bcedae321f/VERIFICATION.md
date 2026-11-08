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

# Verification

Run `python verify.py` with SymPy to reproduce 175 exact-rational, zero-start finite-dimensional companion-GMRES least-squares comparisons across five values of \(c\), five values of \(s\) and seven Krylov lengths, and one symbolic simplification of the nonzero asymptotic lifted-residual floor at \(c=s>1\).

The verifier constructs the matrix columns directly, solves normal equations over exact rationals, and calculates the recovered original scalar residual independently of the projection formula. A normal-equations solve is an exact diagnostic here, not a proposed floating-point implementation. The analytic proof supplies the all-iteration and asymptotic results. No claim of external verification, independent audit, general-matrix stability, or numerical robustness is made.

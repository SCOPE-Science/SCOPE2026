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

The exact proof is contained in `RESULT.md`. Reproducibility: run `python3 verify.py` with Python 3's standard library (the program requires no internet or nonstandard packages).

The verifier checks 435 deterministic test conditions: exactly rational generator balance identities, vanishing first three antisymmetry Taylor coefficients, nonzero cubic coefficient, numerical solution of six generator-moment equations compared with the independent closed form, signs and root brackets, independent long-lag coefficient extraction, and exact cancellation of independent Gaussian thermal contributions. The observed positive roots in dimensionless time are approximately \(3.845481152\) at dimension \(8\), \(3.224418129\) at dimension \(9\), and \(2.893527361\) at dimension \(10\).

Proof versus computation: finite tests do not establish uniqueness for all positive lags or dimensions. Those statements follow from the sign and derivative structure of \(F_d\) proved in `RESULT.md`. The large-lag coefficient for general redraw rates does not cover \(r\le1\), and where its leading factor vanishes it does not decide the next order. The claimed noise robustness is algebraic, not a simulation estimate.

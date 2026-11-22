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
# Reproducibility

Run `python verify.py` in the same directory after installing NumPy and SciPy. The program recomputes finite weighted-shift orbit norms by two independent methods, checks truncated basis constants against their sharp infinite bound, displays one explicit two-pulse gain, and checks beta-layer limiting coefficients at small positive separations.

The script's 50 assertions are finite numerical diagnostics. In particular, asymptotic quadrature and finite-horizon agreement do not prove the uniform parameter theorem or establish bibliographic novelty. Those rely on the analytical argument in `RESULT.md`. All quantities are dimensionless, with the normalized weighted sequence norm given in the proof.

Only self-review has been conducted. Independent audit: not yet performed.

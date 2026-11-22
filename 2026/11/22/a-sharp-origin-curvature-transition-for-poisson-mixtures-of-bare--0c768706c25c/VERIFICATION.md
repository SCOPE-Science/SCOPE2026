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

The normalized beta kernel and positive renewal-age integral are proved in `RESULT.md`. To reproduce numerical checks, run `python3 checker.py` using mpmath. The script checks exact \(\sigma=1/2\) beta constants, normalization for representative regimes, the critical exponential-integral identity, and convergence of finite-position ratios to the three asymptotic coefficients. Finite-position tests do not prove asymptotic statements: the proof uses dominated convergence and an exact logarithmic integral. Neither independent validation nor a complete higher-regularity classification was performed.

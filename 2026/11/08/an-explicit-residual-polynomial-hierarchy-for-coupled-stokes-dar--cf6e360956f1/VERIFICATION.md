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

# Analytic and executable verification

The full analytic proof is in RESULT.md: a block-inverse multiplication, a base matrix-polynomial identity, induction over every integer \(m\ge2\), an accretive-resolvent norm inequality, and GMRES polynomial minimization. Each step is independent of finite-precision tests.

`verify.py` is a standalone Python 3 program requiring NumPy and SymPy; execute `python verify.py` after extraction. The check was run successfully and reported `PASS: 3119 polynomial, norm, scalar and block-structure checks`. It tests exact symbolic scalar polynomials and the scalar two-step residual norm, randomized block forms, finite-degree polynomials, norm estimates, and direct finite GMRES least-squares residual comparisons.

Limitations: finite tests cannot prove the all-degree identity; it follows from analytic induction. The two-step scalar example certifies only the order in \(lpha\), not sharpness of all residual constants. The preconditioner must be exact and stationary, and mesh-independent or inexact-preconditioner guarantees require additional hypotheses. Independent audit was not performed.

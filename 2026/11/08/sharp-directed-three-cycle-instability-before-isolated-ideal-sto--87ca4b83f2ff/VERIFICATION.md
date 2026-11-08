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

The accompanying standalone `verify.py` was run with Python and SymPy. It verifies the modal Jacobian characteristic polynomial by direct algebra and independently matches the full real six-dimensional Jacobian determinant to the product of the homogeneous and conjugate nonhomogeneous mode factors. It also proves by exact symbolic expansion that the complex quadratic Schur–Cohn deficit equals negative one sixteenth of the quartic claimed in the result.

It computes exact rational signs at the endpoints of \((0.8141,0.8142)\), the exact value \(P(5/6)=49/48\), and the three complete real-Jury inequalities as identities; the unique positive root follows analytically by Descartes' rule, not from numerical root finding. At \(\delta=5/6\) it additionally evaluates the six multipliers to confirm the expected two exterior and four interior eigenvalues, with spectral radius approximately \(1.020441989493\).

Reproduction: `python verify.py` (requires SymPy). Expected diagnostic prefix: `VERIFY_OK`. The numerical root approximation is a check, not a proof of uniqueness or a certificate for other parameters. Exact symbolic polynomial identities together with the mathematical Schur–Cohn/Jury criteria establish the infinite-family assertion. No nonlinear invariant objects or independent scientific audit have been checked.

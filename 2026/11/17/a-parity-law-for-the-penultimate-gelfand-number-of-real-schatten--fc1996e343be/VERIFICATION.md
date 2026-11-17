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

# Verification record

The theorem was checked analytically against the definitions of the real Schatten quasi-norm and Gelfand number. The key finite-dimensional identities are \(J^\mathsf TJ=I\), \(J^\mathsf T=-J\), \((aI+bJ)^\mathsf T(aI+bJ)=(a^2+b^2)I\), and their odd-size block-embedded analogues. The elementary odd-determinant sign-reversal lemma is proved in RESULT.md.

Replay the accompanying exact integer checker with `python checker.py`. It checks dimensions \(2\) through \(15\) and a finite grid of integer pencil parameters, as a diagnostic rather than an exhaustive proof. The exact all-dimension and all-exponent result depends on the symbolic derivation, not the finite test sample. The formulas concern real square matrices only.

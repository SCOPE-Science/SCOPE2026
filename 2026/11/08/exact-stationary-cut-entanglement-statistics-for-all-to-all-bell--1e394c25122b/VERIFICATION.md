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

Run `python verify.py` using Python 3 and its standard library. This enumerates the exact finite matching-state transition kernels at dimensions 4 through 8, with three rational measurement probabilities, and compares the transition balance, probability-generating polynomial and every factorial moment on every nontrivial cut. It separately evaluates the total-pair Gibbs sums at dimensions 1000, 3000 and 6000 to test the derived thermodynamic coefficients. The script generated `PASS: 74636 deterministic detailed-balance, PGF, moment and asymptotic assertions` on the packaged source.

Proof of the stationary law and infinite-size coefficient is contained in `RESULT.md`; finite checks alone cannot establish those universal statements. The asymptotic estimate holds for fixed \(0<p<1\) and \(0<\theta<1\), not at endpoint probabilities or vanishing block fractions. Independent review and external proof validation have not been performed.

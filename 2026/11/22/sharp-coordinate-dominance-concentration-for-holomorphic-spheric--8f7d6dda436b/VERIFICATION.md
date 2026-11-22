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

# Reproducible checks

The accompanying `verify.py` requires Python 3 and `mpmath`. Run `python verify.py` in a directory containing this file. It computes the finite-sum rational concentration eigenvalues, exhaustively tests all compositions for \(2\le k\le5\) and \(0\le m\le7\), checks exact extremizer multiplicities, and evaluates nine independent 65-digit gamma-CDF integrals to better than \(10^{-50}\) absolute difference. This is a finite cross-check of the analytic theorem rather than a proof over all parameters.

The full proof in `RESULT.md` supplies exact monomial normalization, probability identification, strict Poisson-tail log-concavity and its implication for minimizers, gamma coupling for maximizers, and explicit endpoint and asymptotic evaluations. No independent review has been performed.

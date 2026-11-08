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

# Verification notes

The proof establishes exact monomial Jacobian factorization for every admissible symbolic word, the half-lazy cyclic-walk representation under normalized Lebesgue measure, and a martingale central limit theorem with explicit covariance. The argument uses the ergodic theorem for finite-state irreducible aperiodic chains and the bounded-increment martingale central limit theorem; it does not infer any infinite or asymptotic assertion from experiments.

Execute `python3 checker.py` in the same directory as this file. The standalone program uses Python's standard library only. The reproduced checks include exhaustive enumeration of binary branch words through length nine for dimensions two through six, exact binomial counting for dimension two through length eleven, and seeded finite-sample covariance comparisons for dimensions three and five.

Critical limitations: fixed dimension; Lebesgue-distributed initial state; almost-everywhere differentiability; singular rather than eigenvalue spectra; asymptotic distribution rather than finite-time Gaussian equality; no external independent audit. The full primary source was inspected as an HTML rendering of the published arXiv preprint. An earlier related calculation for dimension three and periodic-orbit counting was compared at claim level.

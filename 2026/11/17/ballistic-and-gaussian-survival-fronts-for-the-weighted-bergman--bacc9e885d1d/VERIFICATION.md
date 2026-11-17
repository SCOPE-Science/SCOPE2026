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

# Reproducibility and limits

The proof is self-contained after the explicit weighted-Bergman map and the standard moment monotonicity supplied in the cited source. Its key algebraic check is the identity for the action on \(E_{ij}\); scalar diagonalization then yields the Markov recurrence and geometric holding-time generating function. The compact-ideal conclusion uses norm-density of the finite corners plus complete-positive contractivity. The general ballistic speed uses the bounded martingale difference strong law; the beta-weight Gaussian statement uses an explicit binomial coupling and an \(O(\log m)\) expected discrepancy, with the classical binomial CLT.

The companion `CHECK.py` is standalone standard-library Python and performs 466 finite exact-rational assertions involving finite Markov recurrences, coefficients of the spectral expansion, and reciprocal binomial moments. It can be executed with `python CHECK.py` after extracting the embedded file bytes. It cannot establish the infinite-dimensional or limit statements; those require the analytical proof. All references are public scholarly sources; an independent mathematical audit has not been performed.

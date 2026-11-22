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

The result is a stationary finite-second-moment theorem for independent random fractional removals and additive input between events. The proof constructs the stationary stock in \(L^2\), computes its first two moments, obtains the event-export covariance by conditioning on the next storm, and extends it to every positive event lag. The correlation envelope follows from two explicit nonnegative factorizations. The threshold is strict whenever the indicated inequality is strict, and equality gives zero covariance, not necessarily stochastic independence.

Reproducibility: run `python3 check.py` with a Python 3 standard-library interpreter. Exact rational checks compare independently derived recurrence moments with the claimed algebra on admissible parameter grids. Three seeded Monte Carlo simulations are supplementary finite diagnostics, not proofs. Pearson correlations are defined only when at least one innovation is nondegenerate.

The analytical model does not cover rainfall-dependent wash-off efficiency, seasonal trends, within-event pollutant transport, or inference from observations. Independent scientific validation was not performed.

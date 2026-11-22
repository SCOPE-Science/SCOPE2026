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

Run `python3 verifier.py` in the same directory as `SPECTRUM.csv` and `MATCHING_WEIGHTS.csv`, using a standard Python 3 interpreter. No external packages are needed.

The checker reconstructs the explicit icosahedral adjacency, verifies degree and all pair distances, checks the exact independence number and 125 perfect matchings, and recomputes all terminal probabilities by independently structured forward and backward rational recurrences. It derives the completion-time exponential spectrum from the Kolmogorov equations, verifies all 17 tabulated coefficients, evaluates five first-step Laplace transforms independently, checks the exact mean, and enumerates all perfect-matching weights by a distinct restricted-edge-order sum. Numerical rounding and Monte Carlo are not involved.

The state-space proof has finite scope: 1,720 reachable occupied masks and 125 perfect matchings for this particular graph. The results concern precisely the stated independent single-arrival clocks and do not assert model robustness or a thermodynamic limit.

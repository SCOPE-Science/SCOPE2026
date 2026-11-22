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
# Reproducible checks and proven scope

`CHECKER.py` is standalone and requires Python 3's standard library only. It checks exact-rational agreement between a binomial-integral expansion and the finite no-edge expression, two independently assembled second-moment counts, and exhaustive sorted integer grids for the clique-birth order-statistic criterion. Executing it gave `PASS: 7387 exact assertions; finite integrals, moments, clique clocks`.

The mathematical proof additionally establishes convergence of the **whole** bounded marked graph path in total variation by a binomial-point-process coupling, with the sum-of-squared-Bernoulli-probabilities bound. Poisson arrival times give the clique-clock laws and one-dependent Gamma gaps; Poisson integration gives the unique active-component distribution. No numerical test is offered as an infinite-dimensional proof.

Known limits: fixed observation horizon, independent uniform weights, fixed clique indices in convergence of birth times, and an upper-bound rather than an optimality assertion for the total-variation error. Independent audit has not been performed.

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

# Reproduction and limits

The standalone source `verify_extremes.py` was executed from its actual package directory with `python verify_extremes.py` and NumPy/SciPy available. It passed 142,730 finite combinatorial assertions and 10 numerical-integral comparisons: a direct geometric graph reconstruction versus spacing identities over all permutations of three to seven gap ranks, exponential-rate numerical integrations, and bounded exact overlap implications. A separate seeded Monte Carlo diagnostic at 8,000 sample points and 2,400 repetitions gave marginal zero-threshold frequencies 0.3800, 0.3596, 0.3800 and joint frequency 0.0517, compared with the limiting 0.3679 and 0.0498. These tests are not exhaustive over real spacings or a proof of convergence.

The analytic argument supplies the infinite proof: event windows have independent exponential coordinates outside bounded neighborhoods; every distinct overlapping rare-event pair has probability at most order \(n^{-4/3}\); the factorial-moment expansion gives joint independent Poisson exceedances; boundaries and the common exponential denominator vanish after centering. No independent audit is reported.

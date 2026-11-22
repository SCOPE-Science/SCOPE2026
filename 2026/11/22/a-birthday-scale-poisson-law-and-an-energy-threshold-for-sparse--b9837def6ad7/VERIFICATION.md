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

# Reproducibility and verification

The accompanying `checker.py` uses Python's standard library. Running `python checker.py` returned `PASS 2011 assertions`, including exact rational checks of the finite Dirichlet-one formula, sequential predictive increments, unit expectation under the uniform null, nonuniform collision-variance identities, and exact analytic-copula cell masses. Seeded simulation at \(n=d=450\) was checked against Poisson intensity \(\tau J(f)\) for amplitudes \(0\), \(0.8\) and \(0.98\). The simulation is a diagnostic, not the proof of any infinite-dimensional limit.

The mathematical proof separately verifies the factorial-moment graph expansion, the three-occupancy error bound, and the concentration estimate for pair collisions. The results apply to terminal evidence with a grid chosen separately for each sample size. Power for empirically sequential ranks under dependence, optional-stopping properties of a grid-switching process, and the unscaled critical energy equality are outside scope.

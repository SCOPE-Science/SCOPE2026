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

# Verification and boundaries

The theorem is proved analytically in `RESULT.md`. It requires \(1<a<2\), \(1<c<a2^{1-a}\), and the endpoint-saturated individual choice rule. No infinite theorem is delegated to a finite computation.

`CHECK.py` is a Python 3 standard-library checker. Run `python CHECK.py` from the directory containing it. It tests the independent microscopic ideological-threshold decision construction against the two-dimensional map, uses a separate inverse-function implementation for the full-turnout amplitude, tests a radical expression for the nontrivial basin threshold, and checks exact finite turnout capture and both dynamical regimes over randomized initial conditions. It also checks strict relative-imbalance contraction during under-mobilization and two distinct long-run basins for the same 80:20 committed ratio. The source's mathematical definition and the proof, not the computed data, certify the all-state, all-parameter conclusions.

A successful local execution reported 160 quadrature comparisons using 10,001 midpoint ideological samples each, 400 independent finite-capture tests, positive repelling derivative at the unstable cycle, and finite hitting times of 238, 344, 451, and 558 rounds at distances \(10^{-3}\), \(10^{-4}\), \(10^{-5}\), \(10^{-6}\) above the \(\lambda=2/3,\gamma=41/20\) threshold. These values are numerical and are not treated as exact certificates. The exact threshold is given in radicals in `RESULT.md`.

Potential limits: discrete sampling approximates continuous ideological mass; finite tests do not establish global convergence; the source's implicit cut is not defined for all drives without endpoint saturation. The proof explicitly resolves these logically, within its defined model, independently of the checker.

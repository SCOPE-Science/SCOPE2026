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

# Reproducibility checks and scientific boundaries

Run `python verify.py` with Python 3 and SymPy. This performs exact-rational comparisons for the three payoff matrices, negative tangent-space quadratic forms, full and supported equilibria, excluded-phenotype payoffs, unique crossing cubics, and endpoint decay-rate constants. The main proof in RESULT.md establishes the all-time conclusions; the finite computations confirm the algebra only. A separate numerical integration from a strictly positive initial state to dynamical time \(10^4\) confirmed convergence toward the endpoint states to solver tolerance, with notably slow resistant decline in the buffered scenario.

The supported result is restricted to the deterministic four-strategy replicator with fixed payoff matrix on one of two explicit interpolation segments. No independent validation or certification has been performed.

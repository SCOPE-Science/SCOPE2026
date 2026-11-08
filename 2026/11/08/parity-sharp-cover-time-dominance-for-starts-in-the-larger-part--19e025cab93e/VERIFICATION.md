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

# Verification record
The analytic proof uses the independence of alternating uniform coupon streams on each part, a Rolle-interlacing proof of ordered-Bell polynomial real-rootedness, strict Newton inequalities, and a common coupling of cover-time laws. The exact infinity-wide strictness is mathematical, not based on finite exhaustive tests.

Run `python check_cover.py` with the Python standard library. The checker independently evolves the finite-state Markov walk on each complete bipartite graph with part sizes 1 to 5, tracking current vertex and visited-vertex mask; it verifies 850 full-cover CDF probabilities through 16 traversals against the claimed formulas, and separately checks 60 strict even-time stochastic comparisons. It checks the Stirling coefficient inequality for each k from 2 through 29, the first \(K_{3,2}\) CDF difference \(1/9\) at time \(4\), the rational expected-time advantage \(7/10\), and all mean-gap boundary types with part sizes through seven.

Limits: finite computation does not prove a theorem for arbitrary part sizes; the separate analytic proof does. The historical-priority assessment is not an independent novelty certification. No independent mathematical audit has been performed.

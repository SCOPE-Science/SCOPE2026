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

# Verification

Run `python3 cone_apex_cliques_check.py` with Python 3 standard library. An observed successful run ended with `CONE_APEX_CLIQUE_CHECKS_OK` after checks of the exact \(k=3,4,5\) subset probabilities, the properly labeled-anchor Dirichlet moments, the exact shared-pair triple-overlap integral, an exact-versus-sparse subset-count cross-check, the finite triple-count variance, and two critical-window simulations.

The simulations are finite corroboration only. The all-size correctness argument is analytic: cone distance criterion, simplex-volume identity, explicit dependency bounds for each overlap size, and Markov/Chebyshev bounds. Historical novelty has been assessed against the listed sources and remains subject to independent expert review. No independent mathematical audit has been performed.

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

# Reproducibility and mathematical limits

The proof is self-contained given the standard polar decomposition, scalar weighted arithmetic–geometric mean, Tonelli's theorem, dominated convergence for series, and the binomial Chernoff bound. The only identity specific to tree shifts is proved directly from unique parents.

Run `python3 tree_aluthge_verifier.py` with the Python standard library. The expected line is `ROOTED_ALUTHGE_DEPTH_DIAGNOSTICS_OK 30516`. It tests randomly generated finite branching trees, arbitrary complex/zero edge weights, a quasi-Banach endpoint, and exact finite-path nonuniformity. It verifies no infinite result and is not a substitute for the analytic argument in `RESULT.md`.

The preceding literature comparison is a best-knowledge statement, not a proof of absolute novelty. Independent mathematical validation has not been performed.

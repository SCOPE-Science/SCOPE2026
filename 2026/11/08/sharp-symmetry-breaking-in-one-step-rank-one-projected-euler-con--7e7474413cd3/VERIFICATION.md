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

# Reproducibility and claim-to-evidence

Run `python verify.py` from the directory containing this document. The script uses only the Python standard library. It checks 1,728 exact-rational cost identities over a parametrized family for which the square root is rational, 2,500 randomized parameter choices for the symmetry-broken and unsplit phases, and eight near-threshold asymptotic instances. A successful execution prints `REPRODUCIBILITY_OK` with those counts.

The full mathematical proof is in `RESULT.md`: the tangent-space projector confirms the exact one-step scheme, the leading eigenprojector establishes the best-rank-one state and a uniform singular gap, and the derivative of a strictly increasing scalar threshold function proves the complete global classification for the infinite parameter ranges. The Taylor expansion separately proves the quartic boundary, square-root branching, cost gap and vanishing matrix-retraction residual.

Finite numerical or rational checks are not exhaustive proofs of the global claim. Calculations assume exact input matrices and a true optimal rank-one Frobenius retraction; they do not certify floating-point implementations, longer time horizons, other low-rank integrators or historical novelty. No independent mathematical audit has been performed.

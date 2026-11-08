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

# Reproducibility and boundaries
Run `python verify.py` with Python 3, SymPy and NumPy installed. It checks symbolic eigenvector, Rayleigh and stochastic-normalization identities, then builds actual full transition matrices for 49 integer parameter pairs (including the previously known four-vertex-path boundary) and compares eigenvalues with the closed formula. A further 294 feasible symmetric invariant competitor matrices are sampled and checked against the claimed minimum. Output on the supplied package: `SYMBOLIC_IDENTITIES_OK`, `FULL_GRAPH_CASES 49`, `RANDOM_FEASIBLE_COMPETITORS 294`, `VERIFICATION_OK`.

Finite numerical eigenvalue comparisons use stated tolerances and are only a stress test. The mathematical proof in RESULT.md covers all integers \(m\ge3\), \(q\ge1\), and all feasible symmetric chains by a symbolic Rayleigh lower bound plus an achieving construction. The tests do not establish novelty, non-invariant uniqueness, or independent certification. Independent mathematical audit has not been performed.

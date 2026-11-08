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

# Reproducible checks and limits

The theorem's proof is mathematical and self-contained apart from standard Gaussian/Wishart density and elementary endpoint Laplace integration, both reconstructed with parameters and normalization in `RESULT.md`. The source-defined least-squares assembly is explicitly reproduced from [1, Section 4.1, equations (18)–(19)].

Invoke `python check_science.py` with NumPy and SciPy. The checker rebuilds the positive-definite full matrix and symplectic subspace, compares the exact sketched matrix to the analytic formula on random draws, checks the eigenvalue identity, numerically integrates the exact probability, runs independent Gaussian-sketch Monte Carlo consistency checks, and probes both asymptotic regimes. An execution finishing with `SCIENTIFIC_CHECKS_OK` means these finite checks passed, not that a machine verified the entire mathematical theorem.

The proof requires Gaussian sketches independent of a fixed basis; no claims are made for CountSketch, non-Gaussian embeddings, adaptive correlated bases, or floating-point edge behavior. No independent mathematical audit or external certification has been performed.

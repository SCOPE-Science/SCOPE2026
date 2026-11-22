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

Finite computational diagnostics are in `verify.py`. They compare full transition-matrix eigenspectra with the independent base-Laplacian formula across cycles, cliques, hypercubes and the Petersen graph; test candidate improvements at smaller apex probabilities; solve small instances over all individual edge weights; and check the cyclic resolvent and asymptotic coefficients.

Run `python verify.py` with NumPy and SciPy available. Finite checks and local numerical solvers are not proofs of global or infinite-dimensional statements. The theorem is justified analytically by strict inverse-trace convexity, uniqueness-driven symmetry, the exact orthogonal spectral splitting, a uniform negative derivative bound, and a root-of-unity resolvent identity. No independent mathematical audit has been performed.

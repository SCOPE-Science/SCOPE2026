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

The analytic proof establishes global optimality for every integer pair \(2\le k\le m/2\). It is not a conclusion drawn from finite search. The `verify.py` program uses only the Python standard library and computes the candidate probability matrix from the displayed formulas. It independently computes full symmetric eigenvalues using Jacobi rotations and compares the full spectrum against the proof's invariant-subspace decomposition. On package replay it reports `PARAMETER_IDENTITIES_OK 437`, `FINITE_SPECTRAL_REPLAY_OK 67`, `FINITE_LOWER_BOUND_GRID_OK 8405`, then `VERIFY_OK`. Finite testing is supplementary; the nonstandard global lower bound and minimizer are proven in RESULT.md by symmetry, matrix monotonicity, strict convexity and explicit algebra. Scientific limitations and uninspected material are documented there and in REVIEW.md. No independent audit has been performed.

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

# Computational consistency checks

Run `python verify.py` with Python 3, NumPy and SciPy. The script tests 42 combinations of the separation and enhancement parameters against tridiagonal finite-section eigenvalues, including both possible positive bound-state branches where sufficiently separated from the continuous band. It separately checks nine fixed-amplitude splitting ratios, and the near-critical limits for five couplings across three chain separations. Its expected terminal output is `CHECKS PASSED`.

The checker does not prove the infinite-volume spectral count, uniqueness of secular roots, infinite-separation asymptotics, or novelty. Those require the analytic matching, root-count, and scaling arguments in `RESULT.md`. Finite Jacobi sections have finite-size band-edge shifts, so eigenvalues closer than the chosen comparison margin to the edge are not used in the strict numerical eigenvalue tolerance checks. The mathematical hypotheses and all algebraic root equations are stated independently of the code.

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

Execute `python quaternionic_moment_checker.py` with Python 3 and the standard library. The checker exhausts the fifteen fixed-point-free pairings of six letters, verifies exactly that fourteen satisfy the symplectic quaternionic-dimension-two trace restriction, reconstructs normalized sixth moments in dimensions 2 through 29 and ranks up to 7 with rational arithmetic, tests both exact nonnegative deficit identities for many rational singular spectra, and evaluates rank-one/full-rank boundary cases. It independently generates quaternionic Stiefel frames from Gaussian quaternionic Gram–Schmidt to compare Monte Carlo sixth moments against exact predictions.

The analytical argument in `RESULT.md` supplies the universal statements. Finite rational checks are consistency checks, and Monte Carlo accuracy is not a proof. Rains's symplectic trace theorem is an explicit published mathematical input; no independent external audit has been completed. The proof deliberately distinguishes the exceptional two-dimensional case from the dimensions at least three.

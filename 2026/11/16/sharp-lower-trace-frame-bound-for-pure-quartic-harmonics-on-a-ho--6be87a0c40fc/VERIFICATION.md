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

# Verification of quartic Hopf-torus trace spectrum

The proof is contained in `RESULT.md`; the standalone `verify_exact.py` checks the relevant Jacobi polynomial normalization integrals exactly, verifies 25 mode counts, recomputes each explicit block formula, and brackets the cubic optimizer by exact rational arithmetic. Execute `python3 verify_exact.py` in the artifact directory. Expected completion line begins `HOPF_QUARTIC_CHECK_OK`. The checks use Python's standard library and rational numbers. They do not replace the analytic proof of the global bound and uniqueness; finite test radii cannot establish an interval-wide theorem.

Independently verified mathematics: not performed. The accessible 2022 random-sphere sampling reference was inspected at abstract level, and universal literature novelty cannot be certified.

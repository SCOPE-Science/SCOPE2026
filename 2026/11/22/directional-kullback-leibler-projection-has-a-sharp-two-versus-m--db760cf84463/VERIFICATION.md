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

# Verification notes

The exact harmonic mean-value identity and Fourier aliasing are proved in `RESULT.md`. The derivative sign factorization and the unique tie equations supply global proofs in all source counts, including the second-order onset at two sources and first-order jumps at higher counts.

To replay finite diagnostics run `python3 CHECK.py` with Python 3. Its numerical quadrature, grid comparisons and algebraic-threshold checks are supporting finite checks and do not certify continuous or infinite parameter ranges. Verify global statements directly from the proof. No independent mathematical audit has been performed.

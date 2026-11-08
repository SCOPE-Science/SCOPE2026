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

# Reproducibility and limits

Run `python verification/check_weighted_prism.py` with Python 3 and NumPy. The checker uses two independent constructions: exact modular ranks of the integer-weighted Hamiltonian's observability Krylov matrix, and complex-frequency Fourier-eigenvector restrictions evaluated numerically at algebraic resonance ratios. The completed replay yields `VERIFY_OK` with 144 modular witness/lower-bound tests, 1,215 pair tests, and 1,040 Fourier resonance tests. The numerical Fourier ranks are evaluated at specified precision and are not formal algebraic certificates for infinitely many dimensions. The exact proof is in `RESULT.md`.

The verification does not establish prior-work uniqueness, finite-time relaxation rates, or an independent external review. Its finite checks are subordinate to the explicit analytic argument.

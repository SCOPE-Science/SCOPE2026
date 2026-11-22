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

The complete analytic derivation and precise quantifiers are in `RESULT.md`. The standalone script `check_atomic_hardy.py` checks finite examples and reproduces `ATOMIC_HARDY_SPECTRAL_DIAGNOSTIC_OK 12069` in an environment with NumPy and SciPy; the phase- and trace-based tests use only Python standard-library mathematics. Galerkin matrices are finite projections and do not certify an infinite-dimensional statement. The exact phase, compactness and asymptotic laws follow from the proof rather than numerical extrapolation.

One complete mathematical review has been performed; independent audit remains unperformed.

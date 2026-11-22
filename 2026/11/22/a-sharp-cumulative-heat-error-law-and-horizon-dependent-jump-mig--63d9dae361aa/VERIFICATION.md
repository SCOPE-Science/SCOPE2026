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

# Verification procedure

Run `python3 check.py` from the directory containing this manuscript to reproduce the numerical and spectral tests using the Python standard library only. The script calculates the unique positive cumulative Gaussian-profile root, compares two independent representations of the time-integrated heat error, verifies the temporal-profile derivative, and tests large-horizon curvature and small-horizon jump localization. All tests evaluate finite quadrature or finite sums; they do not certify the infinite-dimensional theorem. The exact proofs of single-jump reduction, tail-ratio monotonicity, uniform image approximation and large-horizon concavity are in RESULT.md.

The short-horizon switching threshold is not numerically certified. Statements about exact asymptotic limits and all equality cases rely on the analytical argument; the checker is a reproducibility aid, not an independent audit.

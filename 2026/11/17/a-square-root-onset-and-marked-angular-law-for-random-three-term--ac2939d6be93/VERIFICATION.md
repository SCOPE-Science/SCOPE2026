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

The mathematical proof is in `RESULT.md`. Run `python steiner_diagnostics.py` after installing dependencies from `requirements.txt` to reproduce deterministic angular quadrature and independent direct Cartesian simulation. The checker tests the exact atomic mass, near-zero square-root convergence, and finite-threshold probabilities. Its successful diagnostic marker is `CIRCULAR_STEINER_SAVINGS_ATOM_AND_SQRT_LAW_OK`.

Exact analytical steps, rather than Monte Carlo, prove the infinite statements. The conditional joint total-variation limit is supported by an explicit density change of variables and endpoint uniform-integrability bounds. Historical uniqueness and independent mathematical certification have not been established.

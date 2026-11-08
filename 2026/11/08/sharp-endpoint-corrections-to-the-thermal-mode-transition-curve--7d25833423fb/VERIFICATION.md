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

The exact stationary decomposition and all relevant normalizations are written in RESULT.md. The uniqueness proof uses the confluent-hypergeometric differential equation and the exact sign of each root crossing. The modality proof uses the Gaussian variation-diminishing theorem with bounded-variation approximants. The endpoint expansion is obtained by uniform Laplace estimates, not empirical curve fitting.

Run `python -m pip install mpmath` and `python check_phase.py`. The checker performs 67 independent deterministic special-function and asymptotic diagnostics; it is not an exhaustive proof or independent certification. All quoted limitations, including the previously known curvature equation and leading asymptotic, remain in the main statement.

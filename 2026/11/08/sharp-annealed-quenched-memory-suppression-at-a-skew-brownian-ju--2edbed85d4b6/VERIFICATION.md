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

# Reproducibility and verification

From this directory, with Python 3 and `mpmath` installed, run `python verify.py`. This checker performs independent Gaussian-kernel quadrature, tests the exact variance decomposition at multiple positive times and junction biases, checks the rational long-time covariance polynomial, and checks the endpoint and interior asymptotic coefficients. The resulting finite checks corroborate, but do not prove, the universal statements; those are proved in `RESULT.md`.

The skew point is a local-time direction-bias junction, not a finite physical-permeability membrane. All limiting statements apply with positive finite \(L,D,N\) fixed and require no sampling-noise assumptions. No experimental data, Lean proof, independent audit, external certification or machine-checked infinite proof is claimed.

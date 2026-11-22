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

## Direct verification

From the standalone directory, run `python3 check_variance.py`. This checked 60 deterministic conditions, including exact rational enumeration for every 1D signed configuration on three through ten vertices, exact low-dimensional moment identities, independent one-dimensional quadrature and selected high-dimensional leading terms. The full proof uses rotational symmetry, a conditional wedge formula, covariance overlap counting, an almost-sure Gaussian coupling, and gamma/beta moment asymptotics. Those analytic steps rather than the finite script certify the claimed ranges.

## Scope and exclusions

No independent audit or external validation was performed. The random graph must use independently uniform spherical latent points and the deterministic positive-inner-product edge threshold. The asymptotic is at fixed vertex count. Published-source comparisons do not eliminate all priority uncertainty.

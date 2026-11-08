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

# Verification details

The singular values are exact consequences of the three orthogonal Fourier sectors in the proof. `CHECK.py` uses the Frobenius-orthonormal nine-dimensional Hermitian basis to build all eight quadratic measurement rows and compares the independently computed numerical singular values with the closed formulas for multiple positive Gaussian parameter triples and multiple offsets. It tests exact kernel annihilation, aligned-grid rank loss, the global optimality bound, both possible optimum-set regimes, and the leading asymptotic constant near a resonance.

Run with `python CHECK.py` in an environment with NumPy. The numerical checks are finite and cannot certify uniqueness of equivalent results in the literature or replace the analytic derivation. Independent mathematical validation has not been performed.

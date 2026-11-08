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

# Verification

The package contains `verify.py`, requiring only a standard Python interpreter (`python verify.py`). Executing the extracted script reports `PASS 622 structured exact and numerical checks`. Exact rational checks cover the eigenvector sampler and trace constraint for dimensions 2–14 and ten rational spectra per dimension. Deterministic midpoint quadrature confirms the explicit power-family moment formula on four anisotropic spectral pairs for five power parameters. Independent numerical checks confirm the strict ordering in four planar spectra and the continuous tilted-Haar moment matrix for three- and four-dimensional examples with a fixed pseudorandom seed.

The global extremal theorem is proved by the positive-matrix trace constraint, the Haar second-moment identity and exact equality characterization. Strictness and planar uniqueness are supported by the swap integral and exact two-coordinate circle integral. Finite numerical checks do not establish the universal, asymptotic or almost-sure statements. No probabilistic iteration-complexity or high-probability convergence theorem is claimed. Independent audit has not been performed.

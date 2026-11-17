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

The mathematical proof establishes the all-time affine strain decomposition, the three reproduction-threshold regimes, the critical infinite-time amplitude and the rank-one rigidity by direct algebra, monotone iteration and a normalized Perron-profile argument. Numerical and exact-rational verification is reproducible with `python CHECK.py` using only the Python standard library.

The checker tests exact rational identities for five iterations in three threshold regimes, and numerical asymptotics over 100000 iterations at criticality. Finite diagnostics are not substituted for infinite-time proof. The application is a deterministic Euler SIS model, not a stochastic epidemic. No independent mathematical audit has been performed.

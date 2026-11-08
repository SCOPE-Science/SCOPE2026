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

The self-contained proof is in `RESULT.md`; `verify.py` provides a supporting exact-arithmetic and high-precision replay. The latter was executed successfully from the extracted new package with the command `python verify.py` and returned `PASS: 1292 independent rational/algebraic/numeric checks`. No finite test is treated as proof of global convergence. The proof's noncomputational ingredients are the polynomial gradient identity, finite equilibrium classification, invariant half-planes, LaSalle's invariance argument, and the local center-manifold cubic coefficient at the critical value.

The critical equality \(u=1/12\) is included only after the center-manifold sign check, not by extrapolating a hyperbolic stability calculation. The exact result does not extend by assertion to other Allee thresholds, asymmetric coupling, or stochastic population models.

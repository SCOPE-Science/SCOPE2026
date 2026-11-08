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

The standalone `verify.py` reconstructs derivatives of the displayed reactions, derives the exact first-mode threshold equation, and verifies the reduced cubic coefficient and its sign with rational bounds. The source model is Wang–Zou [1, Eq. (81)] with ordinary diffusion; the parameter specialization and nonlinear branch theorem are explicitly scoped in RESULT.md. Approximate decimal evaluations are illustrative and are not used to establish the sign. Verification is algebraic plus analytical center-manifold reasoning; no finite time simulation is claimed to establish infinite-time stability. Independent external audit has not been performed.

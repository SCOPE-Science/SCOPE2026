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

The symbolic checker at `checks/verify.py` verifies the cubic coefficient and the cancellation of the quadratic coefficient in the second iterate, and performs finite simulations for depths 1, 2, 3, 7 and infinity. The exact interval-map global proof requires Coppel's convergence theorem and the analytic inequality; no finite computation certifies all initial conditions or infinite time. The cited original map and historical comparison have not undergone independent validation.

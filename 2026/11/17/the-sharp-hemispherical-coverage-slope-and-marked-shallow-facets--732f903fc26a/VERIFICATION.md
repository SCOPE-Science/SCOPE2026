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
The geometric proof derives an exact random-face plane-height density and angle density, evaluates the acuteness mass, controls a fourth-vertex cone limit, and uses a separate almost-sure nonconcurrence argument to bound multi-face overlaps as \(o(t)\). The attached `checks/verify.py` independently quadratures the angle integrals and samples four sphere points before computing all genuine face planes and containment signs. Its replay printed `FOUR_CAP_HEMISPHERE_CHECKS_OK` and checked the analytic integrals and finite-threshold behavior. The Monte Carlo run is finite evidence, not an infinite proof. Prior art comparison remains provisional; no independent mathematical audit has been performed.

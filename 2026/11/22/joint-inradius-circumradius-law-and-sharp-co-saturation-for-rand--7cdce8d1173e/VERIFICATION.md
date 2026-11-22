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

# Verification of the analytic radius law

The supporting ordinary Python script `checker.py` (standard library only) was run from this artifact package and passed 4,287 diagnostic checks. Its independent discretization of the planar support function and actual projected cylinder rim points matches the closed forms for the inradius and circumradius; midpoint integration in the uniformly distributed viewing-normal coordinate reproduces both marginal CDFs and the simultaneous corner atom. The algebraic optimizer proof uses the exact sign of the derivative, not finite-grid calculations.

Numerical discretization is not a proof for all orientations. The continuum proof is in `RESULT.md`, and no independent audit has been performed. The conclusion is restricted to right circular cylinders and exact orthographic projections.

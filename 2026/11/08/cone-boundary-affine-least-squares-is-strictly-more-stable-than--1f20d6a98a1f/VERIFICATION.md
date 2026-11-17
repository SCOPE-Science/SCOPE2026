---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
    ],
    "status": "passed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Reproduction and limits

The existing `verify_cube_cone.py` performs exact rational checks of the Irwin–Hall surface and volume affine projector formulas and covariance identities in bounded dimensions. No change to that scientific checker is required for the narrower cube theorem. An additional independent exact-rational calculation checked the boundary and volume finite-sum formulas in dimensions 2–9, including the strict comparison and exact values in dimensions two and three. The arbitrary-dimension conclusion follows from the proof in `RESULT.md`, not from these finite checks.

The general cone-volume versus uniform-volume inequality on symmetric convex bodies and the exact volume-cube formula were previously established and are explicitly credited mathematical premises. Formal proof and external expert attestation remain unperformed.

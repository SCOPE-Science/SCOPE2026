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

The source package includes `checks/annular_projection_check.py`, executable with Python, SymPy and mpmath; running it tests algebraic moving-endpoint identities, two exact endpoint constants, independent radial integration at ten sample ratios, and local asymptotic coefficients. Its recorded final marker is `ALL_ANNULAR_AFFINE_PROJECTION_CHECKS_PASSED`.

The infinite-domain claim, strict monotonicity for every real \(0\le a<1\), and the uniqueness of norming evaluation locations follow from the explicit mathematical proof in `RESULT.md`; a finite sample alone would not certify them. The closest general projector paper was examined by primary full-text reading in the relevant sections. No independent mathematical audit has been carried out.

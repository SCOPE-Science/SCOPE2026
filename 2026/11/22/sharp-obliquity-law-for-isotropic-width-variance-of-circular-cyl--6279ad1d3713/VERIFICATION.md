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

# Reproduction and limits

The claim is the single sharp inclination law for the first two isotropic Euclidean projection-width moments of a disk-plus-segment oblique circular cylinder, including the strict monotonicity and sharp stability inequalities at fixed positive radius and generator length.

Run `python verify_oblique_width.py` with Python 3 and no third-party packages. The checker reports `OBLIQUE_CYLINDER_WIDTH_CHECKS_OK 79` after checking eight nontrivial inclination values against a separate azimuthally averaged sphere integral, both endpoint constants, 60 strict finite-difference bounds, exact gap identities at three geometric scales, and direct fixed-seed Cartesian spherical sampling at three inclinations. Check implementations are in the included script, not external paths.

The exact proof derives the support width, evaluates the conditional absolute cosine, reduces its integral to \(\mathbf K\) and \(\mathbf E\), and proves positivity and sharp slope constants from an explicit nonnegative integral on the full parameter interval. Numerical quadrature does not prove an identity on an infinite interval; all such conclusions depend on the analytical proof in `RESULT.md`. The upper endpoint is a limiting planar body, not a member of the full-dimensional family. Comprehensive priority assessment and independent mathematical review have not been performed.

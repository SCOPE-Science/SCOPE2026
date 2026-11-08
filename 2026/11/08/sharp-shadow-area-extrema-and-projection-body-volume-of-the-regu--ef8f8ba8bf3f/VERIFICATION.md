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

# Reproducible mathematical checks

Run `python verify_brightness.py` with NumPy and SciPy installed. The packaged verifier generates all 24 signed coordinate permutations of \((0,1,2)\), projects them to random planes using an orthonormal basis, computes each planar convex-hull area directly, and compares against the independently implemented two-chamber analytic formula for 3,000 seeded directions. It separately checks the exact two endpoint directions. An integer-only three-by-three determinant tally over the seven generators evaluates all \(\binom73=35\) triples and asserts class totals \(8,144,432,432\); a separate three-dimensional convex-hull computation of signed generator sums agrees with \(8128\).

Expected output:

`TRUNCATED_OCTAHEDRON_BRIGHTNESS_OK 3000`

`TRUNCATED_OCTAHEDRON_PROJECTION_BODY_VOLUME_OK 8128`

The analytic proof in `RESULT.md` supplies the universal quantifiers. The finite random checks and the floating-point hull computations are supplemental, not exhaustive. The exact integer determinant tally certifies the finite volume certificate, conditional on the standard zonotope determinant formula. Historical priority and independent mathematical review are not established by these computations.

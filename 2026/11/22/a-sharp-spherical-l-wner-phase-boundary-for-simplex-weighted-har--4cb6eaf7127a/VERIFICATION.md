---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-23.md",
      "INDEPENDENT_AUDIT_2026-11-23.json"
    ]
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Independent mathematical audit

## correctness

PASS

In the stated affine Euclidean metric, simultaneous permutations force the minimum ball to be centered at the constant-block point. Maximizing the squared norm of a centered Minkowski generator pins the largest rank in both permutations at the simplex coordinate. Such points are uniquely exposed by strictly ordered normals with that common maximizing coordinate; strict convexity excludes any additional contacts. For reverse pairing of the unpinned ranks, their pairwise sums are −1, so the centered-permutation dot product is 2h²+h−S=n(n−1)(5−n)/12, where h=(n−1)/2 and S=n(n²−1)/12. The contact block dot product therefore has minimum (n−1)[−n(n−5)/12+λ+λ²/n]. The average over simultaneous permutations makes each covariance block scalar on the sum-zero subspace (constant diagonal and constant off-diagonal); the cross scalar is proportional to the dot product. Mixing the positive and minimum cross-correlation orbits when the minimum is nonpositive gives a centered isotropic measure, including a single orbit at equality. Its averaged containment inequalities and AM–GM certify unique global volume minimization. If all contact dot products are positive the proposed cross-term perturbation cuts volume to first order: noncontacts retain slack for small perturbations by finiteness, and the determinant changes only at second order. Solving the quadratic gives precisely the stated positive-weight boundary and the unit-weight onset n=7 (not n=6). λ=0 and nonspherical semiaxes are outside the claim. Replay: RESULT.md steps 1–5; check.py was inspected, not run, and checks finite rational generators and pinned pairings only.

## originality

PASS

The supported distinction is the exact roundness boundary of the unrestricted enclosing ellipsoid over the weighted family, not the harmonic polytope definition, the unit-weight contact set, or the general ellipsoid criterion. The available strongest comparisons do not determine the sign range of the cross covariance of an arbitrary contact-supported mixture on this family.

## value

PASS

This classifies exactly when a natural enclosing ellipsoid invariant collapses to an ordinary sphere. Simultaneous permutations alone permit cross-block anisotropy; the explicit dimension/weight boundary, including the unit-weight dimensional onset and strict volume improvement outside it, is substantive even without complementary-regime semiaxes.

The dated certificate retains the supplied scientific assessment, sources and limitations.

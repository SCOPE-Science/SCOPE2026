---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-10.md",
      "INDEPENDENT_AUDIT_2026-11-10.json"
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

For each j-face with signed coordinate support I, orthogonal projection onto the affine simplex gives q-sum_{i in I}x_i²+(1-sum_I |x_i|)^2/j; replacement of a smaller selected absolute coordinate by a larger unselected one weakly reduces distance because 1-s>=a+b for the two coordinates. Thus nearest j-face uses the top j magnitudes even on boundaries. Consecutive squared gaps are positive squares; the final R_d yields total l1 slack, and backward recursion recovers a_d through a_1. Independent inverse numerical computation restored 200 random profiles in d=2,3,5,9 within 1e-12. Uniform volume in l1 ball gives Dirichlet(1,...,1) from d+1 exponentials; normalized top order-statistic moments yield stated harmonic formula. Poisson convergence of exponential maxima with fixed j and d q→2 gives joint Z_j=-2-(2/j)sum_{i<=j}log T_i. Gamma/Dirichlet conditioning yields independent Gamma(j,1) and Gamma(j-1,1) decomposition and the stated transform. Finite tests are not used to establish infinity.

## originality

PASS

Best-of-knowledge PASS: the surviving final claim is distinguished by mathematical implications from the inspected prior theorems; see four comparisons and the explicit residual priority risks.

## value

PASS

Euclidean distances to successive face skeletons are a natural multiscale clearance signature in a basic regular convex body. Showing they recover a point's complete symmetry orbit is a meaningful inverse metric fact; the exact finite means and nontrivial dependent gamma-log limit for uniformly sampled points give further useful geometric-probabilistic information. This is not an arbitrary dimension-specific invariant or a renamed extreme order statistic.

The dated certificate retains the supplied scientific assessment, sources and limitations.

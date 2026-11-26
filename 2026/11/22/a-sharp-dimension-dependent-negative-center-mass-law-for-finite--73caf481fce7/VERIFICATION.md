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

In the finite distinct Euclidean setting strict conditional negative definiteness gives a coercive strictly concave quadratic on the affine mass-one hyperplane, so the unique maximizer satisfies Dp=c1. With total rim mass b and center mass a=1−b the trial weighting (a,bp) has constant rim potential Ra+bc and center potential Rb. Solving and using the bound c<2R below verifies existence and the block formula; uniqueness on the augmented space identifies it with the microscopic weighting. A convex barycenter q for the origin has nonnegative entries, so applying t≥t²/(2R) pairwise gives E(q)≥R. Equality in this estimate forces a single antipodal pair of weights 1/2 each, and moving a positive infinitesimal mass to a third rim point strictly increases energy by strict triangle inequality. This also covers the origin on the hull boundary. For the upper bound, subtract uniform spherical measure; the cross term vanishes by rotationally constant potential and the difference is a nonzero compactly supported signed mass-zero measure. The Fourier integral for its energy converges, since its transform is O(|ξ|) at zero and bounded at infinity; strict negativity follows from Fourier uniqueness. The beta law of (1−⟨U,V⟩)/2 with both parameters (d−1)/2 gives C_d by the beta moment and gamma duplication. Jensen and the strict chord-versus-squared-chord inequality give 1<C_d<√2, making the denominator positive and the center weight strictly decreasing in c. The four-point two-antipodal-pair example is transitive and has the stated mean distance, tending to R as the pairs approach coincidence. Distinct antipodally paired equidistributed samples retain the hull condition, and continuity of chord energy plus the upper bound makes their signed optimum tend to C_dR. The interval endpoints are therefore sharp but not attained; the limit C_d→√2 follows from E⟨U,V⟩²=1/d and bounded convergence in probability. For n=2 antipodal sites one gets c=R and center mass zero, as excluded.

## originality

PASS

The general gauging formalism and the signed uniform-sphere energy bound are prior. The equidistant-center formula is an elementary block computation and precisely matches the known transitive special case. The retained contribution is the strictly negative sign with only the Euclidean hull condition, including the equality obstruction when the hull witness is an antipodal pair, and the sharp nonattained center-mass endpoints for all finite nonsymmetric rims in each ambient dimension.

## value

PASS

The center is a canonical insertion into a spherical metric space; its microscopic weight can be negative even though it lies in the ordinary convex hull. The theorem quantifies both the forced sign and the optimal magnitude by ambient dimension without symmetry or assumptions about the rim weights. Strict but unattained endpoints distinguish near-antipodal degenerations from dense-sphere approximations and give sharp constraints for future signed weighting calculations. The value is in this constrained sharp theorem, not the two-by-two linear system or the classical mean chord formula alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.

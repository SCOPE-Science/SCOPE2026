---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-13.md",
      "INDEPENDENT_AUDIT_2026-11-13.json"
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

Removed caps are pairwise disjoint in interiors for 0<=t<=1/2; each is homothetic about a vertex with volume t^d and barycentric mean (1-t)e_i+t mu. By permutation symmetry retained centroid stays mu and covariance is a scalar on the tangent hyperplane. Subtracting exact Dirichlet simplex cap second moments gives normalized inertia J_t/J0=[1-BA]/[1-B], hence the isotropic-ratio formula with intrinsic reference volume. Differentiation yields a positive factor times S_d(t)=1-d+2(d+1)t-(d+3)t^2-2(d+1)t^d(1-t). The stated factorizations at d=2,3,4 and monotone upper bound P_d(t)<=P_d(1/2)=(5-d)/4 for d>=5 prove all monotonicity cases. Independently checked derivative identity at d=2..11 and endpoints using symbolic algebra; finite checks are not a proof for all d.

## originality

PASS

Kipp 2024 is about local/global structural maximizers, simplicial vertices and zonotopes, not the all-t truncation profile. Baci et al. treat uniform points in an untruncated simplex; the raw Dirichlet reference distribution does not give the cut-body covariance ratio. Closely related SCOPE records optimize width, difference-body geometry and Schneider index on truncated simplices but not this isotropic constant. The exact uniform-cap monotonicity and d=2 reversal remain best-of-knowledge uncovered.

## value

PASS

This gives an explicit affine-invariant shape functional along a geometrically natural whole truncation path, with a genuine dimension-2 phase reversal and dimension>=3 strict monotonicity. The exact high-dimensional rectification gap and sharp exceptional planar minimum are meaningful for extremal isotropic geometry; the proof is more than a known simplex constant substitution.

The dated certificate retains the supplied scientific assessment, sources and limitations.

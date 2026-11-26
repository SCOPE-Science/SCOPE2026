---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-24.md",
      "INDEPENDENT_AUDIT_2026-11-24.json"
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

I reconstructed the moments by conditioning on the reference v, rather than on u as in the frozen proof. Put z=1−q, b=x−m, V=||Pv||², W=||(I−P)v||², U=V+W, and X=v·x. Given v, u is Gaussian with mean ρv and covariance zI, also valid when z=0. Then G=m+u(u·b), E[u(u·b)|v]=qv(v·b)+zb, and E[||u||²(u·b)²|v]=q² U(v·b)²+qz[U||b||²+(d+4)(v·b)²]+z²(d+2)||b||², by expanding the standard centered Gaussian moments. For a unit x in one invariant subspace, put ε=1 on ran(P), 0 on ker(P). One has v·b=(1−V)X, m·v=VX, m·b=(ε−V)X², and ||b||²=1+(V−2ε)X². Average using independent χ²_k and χ²_(d−k) variables V,W, and conditional expectation of a squared coordinate equal to its block radius squared divided by rank (used only when that axis exists). Substituting these identities in an independently written integer-polynomial replay verifies both drifts and both printed second-moment polynomials coefficient by coefficient in d,k,q, rather than in a dimension grid. Orthogonal invariance preserving P forces block-scalar first and second moment forms and no mixed block. Nonnegativity of C_parallel−C_perp and the difference q in mean drifts make the parallel multiplier maximal, also at k=d where no other block is present. Expanding the scalar quadratic gives strict contraction exactly at the displayed subcritical q and positive h interval; a positive C_parallel gives the unique minimizer there. Freshness gives the conditional iteration bound. At the boundary the expected hinted projection is unchanged, and above it grows by (1−h[1−(k+1)q])^t; Jensen gives the stated nonconvergence/divergence for nonzero hinted initialization. The two-point noiseless differences on the specified quadratic are exact at every nonzero radius.

## originality

PASS

The control-variate form and the general risk of dependent data reuse have prior coverage. The distinct contribution supported by actual comparisons is the coupled one-probe model's exact rank-dependent drift reversal and optimized worst-case mean-square frontier, not an assertion about the published independent-reference algorithm.

## value

PASS

Reusing a probe to save reference work is a natural algorithmic shortcut. A rank-only threshold that no choice of small positive step can fix beyond the boundary is a substantive limitation, not just an observation of bias. On the safe side the exact moments give a full minimax stepsize calibration, while the quadratic model isolates the reuse mechanism from curvature or measurement noise.

The dated certificate retains the supplied scientific assessment, sources and limitations.

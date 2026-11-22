---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-18.md",
      "INDEPENDENT_AUDIT_2026-11-18.json"
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

The polar radial law f_k(r)=k*sinh(k*r)/(cosh(kR)-1) has boundary density b=k*coth(kR/2), and antipodal angle defect w is uniform on [0,pi]. The exact hyperbolic cosine rule converts D>2R-eps on radial deficits u+v<eps to 1-cos w<q=(eps-u-v)/(2a)(1+O(eps)), with a=tanh(kR)/(4k) and a=R/4 flat. Angular aperture w_max/pi equals sqrt(eps-u-v)/(pi sqrt(a)) times 1+O(eps). Integrate the triangular radial slacks: integral sqrt(eps-u-v)=4 eps^(5/2)/15, hence C=4 b^2/(15 pi sqrt(a)) and the stated formulas. The change W=a*w^2/eps yields W^-1/2 simplex density 15/8 and Dirichlet(1,1,1/2,1), with independent angular marks. The log derivative of coefficient ratio is 5/(2z)-2/sinh(z)-1/sinh(2z)>0. Reviewed full actual source checker, which computes exact angular aperture via 2D quadrature but is finite corroboration, not infinity proof.

## originality

PASS

PASS best knowledge: existing hyperbolic graph papers use graph-edge metrics or expanding ball regimes; Euclidean ellipsoid maximal-interpoint-distance results address n-point extremes and Euclidean distances. None of the inspected statements implies this fixed-radius intrinsic hyperbolic two-point coefficient together with marked Dirichlet limit and inverse curvature.

## value

PASS

PASS: exact rare-pair geodesic tail is a natural intrinsic metric invariant of a constant-curvature disk, and the monotone coefficient gives an explicit inverse-geometric identification from distance data; the rare-event Dirichlet law adds a structural mark distribution. Motivated by distance geometry, not a parameter slice.

The dated certificate retains the supplied scientific assessment, sources and limitations.

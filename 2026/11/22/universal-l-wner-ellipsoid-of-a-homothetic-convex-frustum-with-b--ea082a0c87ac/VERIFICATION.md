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

The affine shear by the linear interpolation ρ(t)e and the invertible horizontal map A⁻¹ put the common base into Löwner position. In those coordinates prescribe horizontal and vertical squared semiaxes a²,b² and center height c. The two normalized rim heights have mean zero with masses (1±c)/2; their variance is (1−c²)/b², hence b²=(d+1)(1−c²). The upper endpoint gauge then fixes a²=r²(d+1)(1+c)/(d+(d+2)c), and the bottom gauge imposes (d+2)(1−q²)c²+2(1+q²)c−d(1−q²)=0. Its unique nonnegative root is the displayed radical and lies in (0,d/(d+2)] for q<1. Endpoint containment extends to the convex hull. Duplicating any base contact probability on the two levels with the prescribed rim masses gives zero horizontal means and mixed moments. The horizontal covariance is scalar by base isotropy; the contacts have norm one, so the trace remaining after vertical variance 1/(d+1) makes the horizontal covariance I_d/(d+1). This is a sufficient Löwner contact certificate and uniqueness gives global optimality. Positive rim masses persist; at q=0 the lower contacts coincide at the apex, and at q=1 c=0 gives the stated cylinder axes and equal level masses. Strict convexity of the enclosing ellipsoid excludes contacts at interior heights, where every frustum point lies on an open segment between distinct levels.

## originality

PASS

The scalar covering formula for a circular or ellipsoidal frustum is already known, and simplex frusta were covered separately. The supported distinct statement is the arbitrary convex-base replacement principle and simultaneous two-level certificate. Applying affine equivariance can remove an ellipsoidal shape but cannot replace an asymmetric body by its enclosing ellipsoid. The general contact criterion supplies a test, not the moment assembly needed to conclude equality rather than just containment.

## value

PASS

The result identifies when the base's entire shape may be discarded for an enclosing-ellipsoid problem. It yields the same exact full-dimensional optimizer and a base-derived certificate for nonsymmetric or nonsmooth bases, and resolves whether either level loses its supporting contacts as truncation varies. This is useful structural information not supplied by the known axisymmetric solution alone.

The dated certificate retains the supplied scientific assessment, sources and limitations.

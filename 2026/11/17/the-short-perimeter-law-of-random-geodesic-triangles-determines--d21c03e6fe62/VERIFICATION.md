---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

All perimeter-short triangles lie within ε/2 of the pinned vertex. In uniformly bounded normal coordinates the squared third side has Euclidean term, quartic term −K(a∧b)²/3, and remainder O((|a|+|b|)³|a−b|²): the smooth squared-distance remainder and its first difference derivative vanish on the diagonal, and its Taylor polynomial through degree four is the stated curvature polynomial. Thus taking square roots is uniform even as a→b. On each four-dimensional ray h is homogeneous of degree one and bounded below on the unit sphere; the curvature correction is of degree three. The uniform perimeter expansion brackets the scaled radial sublevel by intervals with endpoints h⁻¹+K ε²T/(6h⁴)+O(ε³), which justifies the boundary term without differentiating an indicator. The volume-Jacobian term subtracts I1, yielding the local coefficient K(I2−I1)/6. In the independent replay /workspace/reproductions/short_perimeter_ellipse.py, fixing u−v of length c turns the h<1 midpoint region into an ellipse of semiaxes (1−c)/2 and sqrt(1−2c)/2, 0<c<1/2. Integrating its area and second moments gives I0/π²=1/42 and I1/π²=2/495. The boundary integral I2 equals seven times the sublevel integral of c times the squared perpendicular midpoint coordinate by homogeneity, giving I2/π²=1/990. Averaging over normalized area and applying Gauss–Bonnet yields the stated coefficients, for nonorientable surfaces as well. The first coefficient fixes A>0 and the residual sixth-order coefficient fixes χ. The frozen symbolic checker and sphere series are supporting evidence, not the proof for variable curvature.

## originality

PASS

The supported distinct claim is the explicit perimeter-tail coefficient and Euler recovery for arbitrary fixed smooth compact connected boundaryless Riemannian surfaces with area-uniform vertices. The general coefficient is not covered by the inspected round-sphere perimeter law or the different local sampling laws. No priority is claimed for the sphere, for Gauss–Bonnet recovery once the coefficient is known, or for an exhaustive historical search.

## value

PASS

The perimeter of an area-uniform intrinsic triangle is a natural unlabeled scalar statistic. Its leading small-perimeter probability determines area and its first metric correction isolates total curvature, hence Euler characteristic, without observing the vertices or the three sides separately. The exact joint geometric coefficient is needed for the inference, and the variable-metric result is not just a re-evaluation of a sphere formula or a local two-point volume calculation. This is population-law identifiability, not a finite-sample guarantee or a full surface classification.

The dated certificate retains the supplied scientific assessment, sources and limitations.

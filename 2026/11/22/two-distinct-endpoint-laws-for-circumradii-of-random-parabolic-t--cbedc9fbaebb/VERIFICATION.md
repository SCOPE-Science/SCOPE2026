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

For distinct parameters the product of chord lengths cancels the absolute Vandermonde in four times the area, giving the continuous pair-sum product in RESULT.md (1). Its factors give the unique minimum and the two same-sign maximizing corners. The continuous image of the cube is an interval, all its support values have positive-probability neighborhoods even after discarding the diagonals, and each level has volume zero (the squared radius is a polynomial nonconstant in u1 for fixed u2,u3). Independently, use s=(u1+u2,u1+u3,u2+u3), absolute determinant 2, then s_i=sgn(x_i)sqrt(exp(x_i^2)-1). The lower event is a ball of squared radius q=2 log(1+2 epsilon) in the x coordinates and has u-volume (2 pi/3)q^(3/2)+(3 pi/10)q^(5/2)+O(q^(7/2)): the Jacobian is (1/2)(1+3||x||^2/4+O(||x||^4)). Expansion gives 16 pi/3 and 8 pi/5 before dividing by 8a^3. The rescaled u sublevel sets converge in volume to the quadratic ellipsoid with matrix I+11^T, hence in total variation for the normalized conditional densities. At either maximizing corner, the inward loss is c_a sum d_i + O_a(||d||^2), with c_a=2a sqrt(1+4a^2)>0. Compact localization and this linear bound force d=O_a(epsilon); the scaled simplex can be sandwiched between sum cutoffs 1±O_a(epsilon). Two corner factors, simplex volume 1/6 and cube volume 8a^3 give the asserted upper coefficient and remainder. Reflection gives an exactly fair sign and matching reflected shapes once localized, hence the joint conditional limit. Independent replay at a=0.7 gave 165 exact determinant-distance checks; at epsilon=1e-5 the lower volume correction and upper probability coefficient were 5.026500974 and 0.008693108 against 5.026548246 and 0.008693066.

## originality

PASS

The closest inspected same-sampling result concerns the area of the parabolic hull, not the circumradius. The same-day long-chord result is materially related but governs a two-point observable, not this three-point radius. Neither supplies the explicit two endpoints and their conditional laws. The classical radius identity is not original; distinctness attaches to the probabilistic package for this sampling law, not the elementary identity or a priority guarantee.

## value

PASS

For a natural uniform-coordinate sampling model on a curved graph, the radius does not diverge at degenerate limiting triangles. The result distinguishes two quantitatively different coalescence mechanisms, gives a non-leading volume correction and the two conditional shapes. These are useful benchmarks for endpoint probability and geometry rather than just recalculating the classical radius identity.

The dated certificate retains the supplied scientific assessment, sources and limitations.

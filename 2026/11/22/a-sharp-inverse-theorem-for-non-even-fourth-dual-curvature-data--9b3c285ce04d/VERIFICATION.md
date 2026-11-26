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

The radial projection has arc-length Jacobian <x,nu>/|x|^2 on the regular boundary, giving positive weight |x|^2<x,nu>/2 with the declared normalization. The support assumption puts arc-length almost every boundary point in the four closed supporting faces. Their relative complement, if nonempty, would contain a nonzero-length open boundary arc, so the entire boundary lies in those faces and the body equals the coordinate rectangle. Integrating b(b^2+y^2)/2 on the right facet gives b^3(c+d)/2+b(c^3+d^3)/6, and reflection/interchange gives the other masses. Strict monotonicity in the horizontal half-width forces equality of the two half-widths. After writing d=as, c=ast, lambda=(3+kappa)/(2+6kappa) fixes exactly one positive kappa iff 1/6<lambda<3/2. The positive-denominator derivative numerator of F_kappa is -(1+3kappa)[(t^2-t+1)^2+9kappa t^2], and F_kappa ranges from infinity to zero. Thus beta fixes a unique t (not 1 when B!=C); s and the positive scale follow, with all masses recovered. Varying lambda across the open range at fixed nonunit beta gives sharpness even at fixed imbalance. The endpoint obstruction requires an origin-interior body. Replay exact independent side integration and derivative with python /workspace/branches/independent-algebra.py (item 5).

## originality

PASS

The exact even cross theorem already gives the same numerical interval on its B=C slice, and atomic support reduction is standard. The surviving claim is the non-even iff interval and unique geometric inverse without an a priori reflection restriction. No inspected stronger theorem includes those non-even q=4 cross data.

## value

PASS

This is a natural discrete geometric inverse, not one example of facet integration. The target is the first reflection-balanced unequal-antipodal variant of the cross, and the result gives the exact feasible cone, uniqueness against all origin-interior realizers, and a constructive scalar inversion. It is limited to this datum family and exponent, not a general non-even existence or uniqueness theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.

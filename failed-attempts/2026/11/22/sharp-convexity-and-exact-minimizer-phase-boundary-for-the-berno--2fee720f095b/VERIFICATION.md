---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

For the scalar soft label 0<q<1 and g=0, setting p=sigmoid(x) gives E'=(p-q)[1-gamma p(1-p)] and E''=p(1-p)[1-gamma Q_q(p)], with Q_q(p)=-3(p-(1+q)/3)^2+(1-q+q^2)/3. Its vertex is interior and yields the exact inclusive convexity threshold. At equality the curvature vanishes at only that point, so the derivative is strictly increasing; above it the two roots are both interior because Q_q(0)=-q and Q_q(1)=q-1, and bound the entire region of negative curvature. For 0<gamma<4 the bracket in E' stays positive, so E decreases to and increases from the unique solution p=q. This claim is explicitly limited to the standard open stepsize range; it does not assert where exact minimization is lost beyond that range. In fact the unique minimum persists at gamma=4, despite an isolated derivative zero for an unbalanced label. The fixed-gamma label condition concerns convexity in x for a given label, not convexity in q. Independent exact differentiation in probability coordinates and rational witness: python3 /workspace/review_replay.py, check 3 (-7733/540000).

## originality

FAIL

The exact headline threshold is covered at the statement level by the indexed sparse-logistic result d4ff6c7201eb when the penalty is set to zero. This is a strong overlap with a distinct more general claim, not a same-record hit or a priority judgment from the date. Exactness in the standard stepsize range is established general FBE behavior (here a direct derivative sign); combining that behavior with the covered threshold gives the nonconvex-but-exact window. The strict convexity at the frontier and the two roots of the same quadratic do not provide a substantial independent originality remainder. This rejection is for demonstrated mathematical overlap, not a failure to retrieve the complete text.

## value

FAIL

The convex-versus-exact distinction is a meaningful diagnostic for envelope optimization, but this precise diagnostic is already obtained by combining the stronger indexed frontier with standard exactness. The remaining exact curvature roots and stationary-point checks are routine consequences of the same quadratic and the slope bound, with no further distinctive use established for them alone. No independently valuable surviving repair is substantiated.

The dated certificate retains the supplied scientific assessment, sources and limitations.

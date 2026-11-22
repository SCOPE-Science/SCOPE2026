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

For f=A+Bt+C cos t+E sin t, four distinct zeros in any interval of length ≤2π force three zeros of f′, impossible unless their span reaches 2π, and equality leads only to double endpoint contacts; the confluent Wronskian of {1,t,cos,sin} is positive. Exact paired determinant D=4 sin h sin k H shows near h=k=0,d=2π its leading sign is −2π(d−2π), with positive quartic correction at d=2π; compactness and endpoint multiplicities localize all sign reversals near the two endpoint doublets. After t=(εx1,εx2,2π+εx3,2π+εx4), determinant leading homogeneous term π ε³(x1−x2)(x3−x4)(x1+x2−x3−x4) fixes the bounded limiting R. Integrating R in midpoint and half-gap variables with Jacobian 4 gives volume 1/6, and ordered-sampling density 24/L⁴ yields ε⁴/(4π⁴). The rescaled conditional densities converge a.e. and integrate to one, so Scheffe gives total variation; marginal ∫ produces 12a(1−a)². Independent direct determinant ratios tended to 1 for positive/negative test vectors at ε=.1,.03,.01. Finite samples do not prove compactness or TV; analytic argument provides these.

## originality

PASS

Best-of-knowledge O PASS with concrete primary statements compared against the full claim and retained residual priority risks; inaccessible abstracts are not treated as conclusive NOT_COVERING. 

## value

PASS

The one-full-turn threshold is a natural change in orientation of random inscribed tetrahedra on a 3D convex helical arc; the precise fourth-order onset and the complete conditional geometry are statistically interpretable invariants and considerably stronger than deterministic zero-counting.

The dated certificate retains the supplied scientific assessment, sources and limitations.

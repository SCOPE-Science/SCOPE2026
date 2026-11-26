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

For the specified normalized equations with positive rates, β>μ+α, σ=0 and matched nonnegative feedback, stationarity fixes S=(μ+α)/β. Substitution of I=(μP+γkC)/(μ+α) and R=P-I-C into the C balance gives βγC²+[δγk+(δ+γ)(μ+α)+μβ/k]C−δαP=0. The positive root is unique and gives R>0 by that balance, so reconstruction does not add a spurious solution. The determinant and mass equation at fixed candidate I reproduce the scalar infected-root equation, with strictly positive z derivative and negative feedback derivative by the stated factorizations; uniqueness and increasing I also follow from the earlier October theorem. Thus k=1+εI is continuous, strictly increasing and unbounded with k(0)=1. The C derivative has sign opposite δγ−μβ/k², giving strict decline for k>1 at equality, and strict rise then fall across the unique stationary point sqrt(μβ/(δγ)) when μβ>δγ. The supplied radical example satisfies the quadratic and k-to-ε relation; the large-k limit is zero. This is an equilibrium statement only, not stability, transient behavior, or application outside these equations. Inspected VERIFICATION.md and verify.py without executing them.

## originality

PASS

The earlier exact equilibrium characterization and feedback monotonicity of I substantially overlap the setup and proof of the k correspondence. The supported distinction is the new analytic classification and exact turning point for C itself, requiring elimination of the implicitly varying I and analysis of the resulting positive C root. Neither endemic uniqueness nor coordinate reconstruction from a given infected root states or determines the sign by direct specialization alone.

## value

PASS

For the stated mathematical model, the intermediate-state occupancy can behave qualitatively differently from strictly increasing infection prevalence. An exact criterion distinguishing uniform decline from a unique interior maximum, including the location in the original feedback coordinate, is useful for interpreting this equilibrium family and is stronger than reconstructing coordinates pointwise. No clinical, stability, intervention, or broader model conclusion is implied.

The dated certificate retains the supplied scientific assessment, sources and limitations.

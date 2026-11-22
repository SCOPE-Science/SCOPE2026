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

Variance bounds distance from [0,1]^n to O(P) by sqrt(floor(n²/4)/n). Coordinatewise strict convexity forces every bound-attainer to be balanced binary. Constant-vector projection has comparability normal cone and exactly the balanced Hall transport condition by nonnegative flow and max-flow/min-cut; even n is perfect matching. Chain positive-prefix sums give Catalan and coprime cycle-lemma counts; alternating fence has one corner via directed nonnegative Hasse flow. Independent enumeration n=2..10 confirms counts 1,2,2,4,5,10,14,28,42; source rational checker n<=12 inspected.

## originality

PASS

Best-of-knowledge comparison of actual statement/implications, including relevant primary material and related published records; residual priority limitations stated.

## value

PASS

Motivated sharp geometric bound and equality classification on arbitrary finite posets, plus perfect matching equivalence. Same Hasse path underlying chain and fence nevertheless yields Catalan versus unique deepest corners. This exact extremal geometric invariant is mathematically meaningful even without a formula for nonsaturating cases.

The dated certificate retains the supplied scientific assessment, sources and limitations.

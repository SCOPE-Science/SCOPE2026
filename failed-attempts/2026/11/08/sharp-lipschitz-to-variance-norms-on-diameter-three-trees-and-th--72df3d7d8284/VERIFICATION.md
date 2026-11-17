---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-12.md",
      "INDEPENDENT_AUDIT_2026-11-12.json"
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

The double-star tree edge-increment cube is strictly convex in every coordinate for variance because removing an edge shifts a proper subset C and contributes |C|(N-|C|)/N^2 to the quadratic coefficient. Saturated +/-1 edges reduce the problem to two integer counts and, by diagonal and boundary monotonicity, a single nearest-integer square. This proves the closed formula, equality cases, parity and balancing. Independent direct signed-edge enumeration for (a,b)=(1,1),(2,1),(2,2),(3,2),(6,2) corroborated, and exact algebraic comparison for 324 pairs 2<=a,b<=19 proved equality with the earlier bistar polar norm formula. Finite tests support, do not replace, the universal proof.

## originality

FAIL

FAIL: the October 11 bistar symmetric-edge-polytope theorem already computes the exact maximum squared centered Euclidean polar Lipschitz norm M_{a,b}, with identical signed edge extremizers and the threshold L=2U+2 for all a,b>=2. Dividing M by N yields exactly the current spread. That theorem additionally determines contact facet multiplicities and inball center dimensions. Remaining a=1 and fixed-size balancing follow by elementary specialization and do not rescue the unchanged claim.

## value

FAIL

FAIL: the exact natural invariant, optimizer phase transition and equality geometry are already established via Euclidean duality in a prior theorem. The residual fixed-vertex balancing consequence and singleton-leaf boundary are routine and not independently motivated as a new claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.

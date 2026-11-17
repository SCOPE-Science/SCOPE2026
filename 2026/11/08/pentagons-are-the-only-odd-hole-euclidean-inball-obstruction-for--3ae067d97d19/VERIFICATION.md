---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
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

Under the exact h-perfect halfspace model, c_v>=r yields clique barriers f(s)=1/(s+sqrt(s)) and odd cycle barriers g(l)=(l-1)/(2(l+sqrt(l)))=(1-1/sqrt(l))/2. f decreases and g increases; f(3)<g(5)<f(2)<g(7), so max-clique is binding except omega=2 with C5, where pentagon binds. Uniform r1 attains all barriers. Critical supports force coordinates c_v=r on union U and all others vary independently in small positive directions due finitely many strict inequalities, proving dimension n-|U|. The proof provides affinely independent stable-set vertices for max-clique facets and each C5 facet in the triangle-free case; tangent count is n plus #critical supports at uniform center. Handles edgeless omega1 and disconnected graphs.

## originality

PASS

Sharp h-perfect nonperfect C5 exception, all-centers dimension and facet tangencies extend but are not implied by the inspected perfect-graph metric theorem; foundational h-perfect stable-set inequalities are acknowledged as prior.

## value

PASS

Classifies precisely when nonperfect odd-hole constraints alter the Euclidean insphere of an important broad class of graph polytopes, and computes full incenter dimension and sharp facet contacts; the exceptional C5 barrier is meaningful geometry not a numerical novelty claim.

The dated certificate retains the supplied scientific assessment, sources and limitations.

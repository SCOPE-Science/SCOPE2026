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

Each vertex is uniquely exposed by some strict coordinate order, which assigns each eligible simplex to its largest coordinate. Counting the singleton, edge and connected-triple contributions yields the hub and leaf formulas of RESULT.md:36–44. The two endpoint patterns have equal squared distance to the proposed center. An independent exact re-expansion from the squared coordinate sums (python /workspace/independent_checks.py 4) checks both endpoint distances, the barycentric coefficient and 41 positive gap monomials in (s,k-s,q-k). All monomials contain k-s or s(q-k), with both of those monomials present, so the equality locus is exactly the two endpoints. Strict convexity excludes nonvertices. The proposed center is a strict convex mixture of the two orbit means; averaging squared distances gives R_q^2+||z-c_q||^2 for any alternative center z, proving uniqueness. RESULT.md:85 should say squared radius, not radius, is bounded below by this average; the preceding identity gives the intended result. The two unequal hub values identify (s,k) except at (0,0); precisely the first s leaves are indistinguishable. This yields the stated exact vertex count including q=2, and summing the factorial series yields the asymptotic contact fraction. No uploaded checker was executed.

## originality

PASS

Best-of-knowledge pass for the exact enclosing ball and complete vertex/contact classification of this coefficient-one Euclidean realization. The nearest indexed precedents change either the graph or the summands, while the defining paper's documented construction and combinatorial theorems are inputs rather than a Euclidean optimization result. Unavailable full texts are an access risk, not negative evidence.

## value

PASS

The first connected-triple stage and the smallest nonstar complete bipartite family are natural tests of whether known zonotope and star metric behavior extends to a new canonical realization. The solution gives all extremizers rather than a size-by-size radius computation, with a factorial contact orbit plus a distinct two-point orbit and a vanishing contact fraction. The strict gap certificate decides the global metric problem and may be used without enumerating orders.

The dated certificate retains the supplied scientific assessment, sources and limitations.

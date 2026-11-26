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

Every two-edge geodesic is maximal and is precisely an incident pair of edges in one complete bipartite block: its outside endpoints have the same part. A single edge is maximal exactly when both parts are singletons, since otherwise a second vertex in a nonsingleton endpoint part extends it. No zero-edge path is maximal in these connected graphs of order at least two. Thus the forbidden omissions are exactly singleton-pair edges and incident pairs within each remaining block. The choices factor by block, and choosing k endpoints on each side and a bijection gives the displayed coefficient factor. A submaximum matching leaves unused endpoints on both sides, so a maximal omission in each block is maximum; this proves unmixedness, the minimum size, and its falling-factorial count. Every size from zero to the maximum is available in each block, so the degree support is contiguous. For a block of sizes a,b, the classical real-rooted matching polynomial is x^(a+b) M(−1/x²). Every root t of M is nonzero and yields a nonzero root of that matching polynomial by choosing x with −1/x²=t, hence t<0. Reciprocation and the displayed powers of z give exactly the nonpositive-root claim; Newton's inequalities apply after removing the zero-root factor. In the all-singleton case the result reduces to the compulsory-edge monomial. K_{2,2,2} gives three factors z⁴+4z³+2z², with lowest term 8z⁶.

## originality

PASS

The supported distinct contribution is the independent matching-complement model for the edge-hitting problem and the resulting complete enumerator and unmixedness on multipartite graphs. The diameter-two block geometry, complete-graph boundary, matching counts and root theorem are known ingredients, not separate novelty claims.

## value

PASS

The edge-hitting invariant is already motivated in the literature, and complete multipartite graphs are a natural class containing both forced-edge and matching-block behavior. The full distribution and the statement that every inclusion-minimal solution has the same size give concrete information unavailable from a minimum alone. The explicit block model accounts for the effects of singleton parts and explains the enumerator's shape without claiming a new general real-rootedness theorem.

The dated certificate retains the supplied scientific assessment, sources and limitations.

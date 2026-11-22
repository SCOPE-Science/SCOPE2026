---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-17.md",
      "INDEPENDENT_AUDIT_2026-11-17.json"
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

Temporary weighting of all edges by sign of smaller endpoint yields Catalan triangle-splitting recurrence H(i,j)=s_iΣ_kH(i,k)H(k,j), generating series E_L and O_L=−E_L. Formal-series solution gives alternating W_N=0 for even N and C_{(N−3)/2} for odd N. For odd N, any diagonal belongs to C_aC_b triangulations where a+b=N−2 odd; one Catalan factor is even, so W_N(b)≡C_{N−2} mod4 at every frequency. By v2 Catalan=s2(index+1)−1, all coefficients nonzero whenever s2(N−1)≤2. An exact signed triangle recursion at N15 independently yields 132 on alternating set and zero after toggling (0,8),(2,6), with signed containment totals 50,56,20 giving 132−100−112+80=0. All smaller odd N≤13 meet zero-free criterion, so N15 is the first odd singular polygon.

## originality

PASS

Best-of-knowledge comparison of mathematical statements, not title matches; bounded queries and directly inspected relevant sources found no dominating prior result for this precise support/invariant. Remaining risks explicitly retained.

## value

PASS

Triangulation diagonal incidence is a natural associahedron vertex code; a universal mod4 obstruction explains infinite invertible odd families including even-support cases, while the explicit first odd cancellation N15 locates the sharp onset outside those families.

The dated certificate retains the supplied scientific assessment, sources and limitations.

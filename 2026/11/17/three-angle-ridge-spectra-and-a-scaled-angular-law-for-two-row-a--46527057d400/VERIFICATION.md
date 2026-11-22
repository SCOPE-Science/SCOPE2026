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

The fixed-cardinality crown assignment polytope has vertices (e_i,e_j) with i≠j; fractional Hall gives facet description x_i≥0,y_i≥0,x_i+y_i≤1 in affine dimension 2n−2. All 3n facets and exact ridge classification follow from explicit two-tight strict feasible witnesses and forced extra constraints for A_iC_i, B_iC_i, C_iC_j; n=3 additionally loses A_iA_j, B_iB_j and A_iB_i. Projected normals use u_i=e_i−1/n; their signed dot products give precisely acute acos(1/(n−1)), right π/2, obtuse acos(−1/(sqrt2(n−1))). Pair counts n(n−1),n²,2n(n−1) for n≥4 and (0,6,12) at n=3. Normalized probabilities and n asin(1/(n−1))→1 give −1,0,1/sqrt2 atomic limit. Exact independent affine-rank enumeration checked every vertex/facet pair at n=3,4,5 and counts (0,6,12),(12,16,24),(20,25,40), and package checker was read.

## originality

PASS

Best-knowledge original metric all-ridge spectrum and signed asymptotic law of the fixed-cardinality two-row crown/2-assignment polytope. Gill–Linusson’s 2009 primary paper supplies the H-representation/facet combinatorics, not measured Frobenius angles. A closely ranked Resultary result treats full-dimensional rectangular PARTIAL matching polytopes (pq variables), a genuinely different object from fixed-cardinality crown root polytopes (2n−2 dimensions); its two-neighborliness and angle counts do not imply this theorem.

## value

PASS

Determines a natural complete Euclidean ridge-angle invariant for a highly structured fixed-size assignment polytope, including a genuine smallest-dimension topology exception and a nontrivial three-point limiting fluctuation law with positive bias. The metrics and exact multiplicities are not a mere restatement of known assignment facet counts and can serve quantitative geometric comparisons.

The dated certificate retains the supplied scientific assessment, sources and limitations.

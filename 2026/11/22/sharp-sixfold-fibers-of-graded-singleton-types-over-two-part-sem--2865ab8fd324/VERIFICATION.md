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

Rectangle parity allows two complementary rows for a point added to the first class and two complementary columns for the second (out-neighbors there use the complement transpose); a new class allows all orientations independently. The degree fixes n, and each perfect matching of the four residual exponents with positive pair sums yields precisely the proposed part sizes and an admissible parameter digraph. Under normalized row and column weights at most one orientation bit remains. Either balanced weight absorbs that bit; exchange of equally sized parts can identify the bits exactly when the normalized weights agree. Repeated exponent occurrences identify two matchings even as paired exponent multisets, ruling out six types before the distinct-exponent sum 0+1+2+3. I independently enumerated rectangle-valid matrices, explicitly appended one-point extensions and quotiented by permutations. The first witnesses occur at orders 3, 4 and 6, including exactly two types for each of (1,5), (2,4), (3,3) at the six-point witness. The all-order proof does not depend on this finite check.

## originality

PASS

The rectangle representation and the homogeneous age are known. The supported contribution is the conversion of the out-neighbor grading into a complete matching inverse and a sharp uniform ambiguity bound, including the first orders for different types and different part profiles.

## value

PASS

The score grading adds orientation information that the total singleton count loses. Recovering every compatible part-size profile and sharply bounding the number of ordinary isomorphism types by a constant independent of base size solves a concrete inverse problem, not just a handful of examples.

The dated certificate retains the supplied scientific assessment, sources and limitations.

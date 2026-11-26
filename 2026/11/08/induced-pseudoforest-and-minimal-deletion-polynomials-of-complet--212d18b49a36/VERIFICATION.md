---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "passed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-26.md",
      "INDEPENDENT_AUDIT_2026-11-26.json"
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

A selected set meeting at least two parts induces a connected graph. For two parts the edge budget is (a-1)(b-1) <= 1, giving stars and K_{2,2}. For three or more parts the only allowed profile is a triangle: any repeated part creates K_{2,1,1}, and four parts create K_4. Sets in one part are independent. Heredity reduces maximality to one-vertex extensions. Triangles and squares are always maximal, a star with at least three leaves is maximal exactly when the leaf part is full, and a two-leaf star needs full parts of sizes 2 and 1. The empty set, one-part sets and two-part pairs are not maximal under r >= 3. This proves both labelled cardinality polynomials including coincident degrees and the reciprocal complement formula. Dividing the balanced coefficients by their sum gives the two stated probabilities and all missing sizes. Read RESULT.md, VERIFICATION.md and pseudoforest_verifier.py without running the uploaded program. An independently written adjacency, component and extension check in branches/d20a1e2f-cf4c-4876-9eef-80b5482632bf/independent_pseudoforest_check.py passed on 78 profiles, including K_{5,5,5}, with 15,502 feasible subsets and 3,981 maximal sets; this finite check corroborates but does not prove the theorem. No formal verification or expert attestation is asserted.

## originality

PASS

The supported distinct result is the full labelled maximal-pseudoforest enumerator (and hence the deletion enumerator and the exact tripartite size law), not the known forest polynomial or a new pseudoforest-deletion algorithm. No equivalent result was identified in the materially inspected sources.

## value

PASS

A natural family admits an exact enumeration of all inclusion-minimal deletion outcomes, not just optimum size. In a connected regular vertex-transitive graph the enumerator proves an arbitrarily long gap in maximal sizes and a stark difference between a uniformly typical maximal outcome (size four) and the maximum (size m+1).

The dated certificate retains the supplied scientific assessment, sources and limitations.

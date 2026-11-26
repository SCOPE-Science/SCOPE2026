---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
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

The even octavic is g(x²) with g=(z²−az+1)(z²−bz+1), a+b=−u, ab=v−2. The factors are squarefree and disjoint exactly when (a²−4)(b²−4)(a−b)≠0, equivalent to the displayed open set. The quadratics’ resultant is (a−b)², also yielding the stated discriminant. The Cartier–Manin coefficient matrix and prime-field eigenbasis are correct; semilinear iterates preserve exactly the nonzero diagonal slots, and the a-number is the first Cartier corank. Count the three indexed slots, with repetition, as specified by the table and proof, not distinct scalar values. The conic’s homogenization is nonsingular; the two graphs are smooth; restriction of the conic to either graph has one excluded triple root and one allowed simple root. With the intersection of the graphs this gives exactly the stated three transverse intersections, no triple point, and the reduced SNC divisor of the determinant. /workspace/review_replay.py independently checks the coefficient matrix in the eigenbasis, the quadratic resultant, the elimination identities and transversality; no finite census is used to establish the geometric claim.

## originality

FAIL

The principal result is covered by a distinct indexed analysis of the ordered-factor cover of the same smooth marked family. On that cover the rank, determinant and intersections agree under étale base change. Passing to the unordered coefficients identifies pairs of known components and pairs of known rank-one points; the descended claim is not an independent stratification. The two records share a date, so this is a coverage decision, not a chronological priority claim.

## value

FAIL

A complete Hasse-divisor stratification is intrinsically meaningful. Relative to the explicit ordered-cover result, the claimed marked coefficient form changes the labeling rather than adds a new rank phenomenon, arithmetic invariant or geometry. No independently valuable remainder of the frozen finding needs repair.

The dated certificate retains the supplied scientific assessment, sources and limitations.

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

For selected index sets I,J of sizes a,b, the induced graph has ab−|I∩J| edges. With both sizes at least 3, or one size 2 and the other at least 4, this forces a cycle. A (2,3) selection is a forest exactly when the two indices are contained in the three (then it is P5), and (2,2) is a forest exactly when the two index pairs meet. A (2,2) forest extends to (2,3), while smaller-side-at-most-one forests extend to a full side plus one opposite vertex; that last configuration is maximal only for n≥4. Counting these cases gives both polynomials, including exactly six maximal sets at n=3 and 32 at n=4. The gap and minimal feedback-vertex-set conclusions follow by the degrees and taking complements.

## originality

FAIL

A distinct indexed record gives both stronger bivariate polynomials and the same maximal families and feedback-set dual. This is demonstrated mathematical coverage; no inference about authorship or provenance is needed.

## value

FAIL

The crown-family profiles are useful data, but this submission adds no independently useful exact invariant or structural consequence to the more refined existing formulas. The unbounded gap is an immediate subtraction of previously available maximal orders, and the dual enumerator is explicitly present in the matching record.

The dated certificate retains the supplied scientific assessment, sources and limitations.

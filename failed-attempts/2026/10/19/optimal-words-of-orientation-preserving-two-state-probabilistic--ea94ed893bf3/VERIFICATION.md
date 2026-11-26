---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "status": "failed",
    "evidence": [
      "INDEPENDENT_AUDIT_2026-11-25.md",
      "INDEPENDENT_AUDIT_2026-11-25.json"
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

The scalar acceptance map is nondecreasing exactly when its determinant is nonnegative. The optimum prefix values iterate the envelope and are monotone. A unique global winner must have optimal prefixes: replacing an inferior prefix improves the final value for a positive-slope suffix and ties it for a zero-slope suffix. A tie in the active letter also survives a common suffix. An affine difference cannot have signs +,-,+ along a monotone sequence, so a letter cannot recur after a different run. Conversely I checked the ordered crossing formula and the uniform baseline-orbit error <2^(-n-2) versus distance to every threshold >=2^(-n-1), including the vacuous threshold case r=1. All slopes are positive, unused maps are strictly dominated, and strict monotonicity makes the prescribed maximizer unique. Threshold denominators divide 2^(n+1), which gives the stated common denominator r*2^(2n+5) for the matrix entries. Ordered run labels and compositions give the count, OGF and leading coefficient q. The inspected checks are finite corroboration, not the proof. The theorem concerns nonempty words, a fixed length, and nonnegative determinants; it does not classify witnesses with negative determinants.

## originality

FAIL

Two distinct indexed findings give the same restricted characterization, and the stronger one also gives strictly positive rational witnesses and the identical exact count, implying the OGF and growth. Its explicit envelope margins even yield witnesses with O(log n) bits per entry after dyadic rounding. The particular displayed common denominator in the frozen record is correct, but is a weaker, nonsharp precision guarantee for a different witness, not a substantive uncovered classification or precision result. This is a content-coverage finding, not evidence of precedence or derivation from the later-labelled entries.

## value

FAIL

The orientation-preserving restriction defines a worthwhile structural subcase, but the complete classification and count are already covered in the examined catalogue. The given denominator is not shown sharp or to resolve a separate precision problem and is weaker as an asymptotic bit-size bound than a direct consequence of the stronger result. No distinct valuable remainder is established.

The dated certificate retains the supplied scientific assessment, sources and limitations.

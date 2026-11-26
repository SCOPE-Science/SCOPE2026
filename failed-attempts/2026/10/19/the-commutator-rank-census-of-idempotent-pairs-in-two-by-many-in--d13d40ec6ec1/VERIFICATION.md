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

In the square-zero radical, an off-diagonal coefficient is free exactly when its idempotent's two endpoint diagonal bits differ. Of the four two-bit colors, only opposite colors give a nonconstant commutator coefficient, an onto linear form with q lifts per value even in characteristic two. For ordered bottom colors equal/adjacent/opposite (multiplicities 4/8/4), the zero-column weights are a/b/b and the nonzero-column weights are respectively q^2 everywhere, q^2 on the two axes, and q on the axes. Rank one is the disjoint union over lines of matrices supported in that line other than the all-zero matrix; hence the displayed h/c/d terms and coefficients. The total is the square of the single-idempotent count by independently choosing the two bottom bits. Independent columns are realizable for m >= 2, and the deficient-rank bases are strictly below (1+q^2)^2 for q >= 2. An independent matrix-product/determinant check in /workspace/review_evidence/check_3_5.py confirms m=2 for q=2,3,4, including genuine GF(4) with (N0,N1,N2)=(28804,247296,222336). This finite check corroborates, not replaces, the all-field argument. The frozen verification code was inspected, not executed.

## originality

FAIL

An earlier-dated distinct catalogued finding already gives the exact count for each prescribed commutator in every radical-square-zero finite-field quiver algebra. The frozen algebra is exactly such a quiver algebra, and the positive-rank census is obtained by grouping those fibers by ordinary block rank. The earlier result also contains the color and edge-weight mechanism. The specific closed expression compresses the same data but does not escape coverage. This establishes mathematical coverage, not independent proof of a historical first-publication date.

## value

FAIL

Rank of the radical block is a natural and useful statistic, and the powers give a concise evaluation, but the submitted incremental claim is a direct specialization and aggregation of a finer exact invariant, with the same local weighting rule. The three bottom-color cases and line sums do not supply a separate structural finding beyond that specialization.

The dated certificate retains the supplied scientific assessment, sources and limitations.

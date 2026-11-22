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

An order-four ASM is uniquely enumerated by legal alternating 1/3-nonzero rows with column partial sums 0 or 1 and final sums 1. This exhausts 42 labelled matrices, and their mod-3 affine row/column sum constraints give 9 independent coordinates and frequency restriction kernel size 3^7. Integer phase counts c0,c1,c2 over all 3^9=19683 reduced frequencies exactly determine |W|^2=c0^2+c1^2+c2^2-c0c1-c0c2-c1c2. Independent exhaustive recomputation found exactly 734 reduced zeros, 53 distinct squared magnitude levels, least positive squared value 3, maximum 1764, Parseval 42*19683=826686. Multiplication by 3^7 yields full nullity 1,605,258 and rank 41,441,463 in F3^16. Direct enumeration of every single/two-coordinate frequency gives zero at exactly the 16 opposite-sign central horizontal/vertical coordinate pairs, no weight-one zeros. Fourier diagonalization of UNNORMALIZED convolution gives T pseudoinverse norm 1/sqrt(3), condition number 14sqrt(3).

## originality

PASS

The final operator/character claim, not solely its background classification, was compared against the actual published statements and selected primary sources. Bounded checked literature yields no identified covering prior theorem or table for the final new invariant, with explicit remaining priority risks. Exact ternary Fourier nullity and sharp deconvolution gap for order-four alternating-sign matrices.

## value

PASS

Order-four alternating-sign matrices are a canonical finite combinatorial family. Character spectra of their signed entries over F3, first cancellation positions, exact deconvolution rank and sharp inverse condition are natural invariants of a finite convolution operator. The nontrivial exact signed-entry Fourier histogram and 16 minimum-support obstructions are not merely the already known ASM count 42 or a copied table.

The dated certificate retains the supplied scientific assessment, sources and limitations.

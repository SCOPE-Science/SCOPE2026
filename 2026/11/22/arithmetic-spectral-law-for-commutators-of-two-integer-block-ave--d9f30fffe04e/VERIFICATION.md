---
{
  "expert_attestation": {
    "evidence": null,
    "status": "not_performed"
  },
  "independent_audit": {
    "evidence": null,
    "status": "not_performed"
  },
  "lean_verification": {
    "evidence": null,
    "status": "not_performed"
  },
  "schema_version": 1
}
---

# Verification and reproducibility

The proof in `RESULT.md` is analytic. Its decisive algebraic step is the exact compression \(U^*(I-E_m)U=L_{m,n}/n\), obtained by partitioning the underlying finite cell into two-value crossing blocks; this identity and the positive-definite complementary compression justify use of principal angles without missing zero-cosine blocks. The number of nonzero commutator spectral pairs per reduced cell is exactly \(m-1\), even if two displayed magnitudes coincide.

Run `python check.py` with NumPy installed. At preparation, it completed **396** assertions across direct overlap Gram identities, positivity and simple-path spectra, special congruence classes, independently formed commutator matrices, and greatest-common-divisor reductions. The `requirements.txt` dependency is explicitly stated. No computer algebra or finite-size numerical trial is treated as proof of the infinite-dimensional essential-spectrum or sharp norm claims; these follow by a repeated finite-cell unitary decomposition.

A separate literature comparison addressed the generic principal-angle formula, the underlying weighted-composition isometries, and unrelated projection-commutator models. Noncoverage by all historical literature has not been certified; independent review has not occurred.

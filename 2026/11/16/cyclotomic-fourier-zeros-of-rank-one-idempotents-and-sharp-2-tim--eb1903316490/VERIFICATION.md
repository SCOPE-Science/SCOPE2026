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

# Reproducibility and limits

Run `python checker.py` using Python 3 and its standard library. The checker generates rank-one idempotents as actual matrices, independently enumerates every ambient dual matrix, directly tallies the character's absolute-trace exponent histogram, and compares this with the eigenvector-derived prediction modulo the unique cyclotomic relation. It also checks the zero criterion, complete two-dimensional zero counts, and sharp endpoint norm formulas. The checked field sizes/dimensions are \((2,2),(3,2),(4,2),(5,2),(7,2),(2,3)\), amounting to 3891 dual matrices; characteristic two includes the extension field \(\mathbb F_4\).

The checker prints `RANK_ONE_IDEMPOTENT_ORBIT_FOURIER_EXACT_CHECKS_PASS` only after all assertions succeed. Its direct Fourier sums use character-exponent histograms so that equality of cyclotomic sums is verified as exact integer relations rather than approximate complex cancellation. Floating-point calculations are used only to corroborate the displayed norm's real value to a strict numerical tolerance. Those finite checks cannot establish the untested infinite family. The proof in RESULT.md supplies that justification separately.

Self-review: passed. Independent audit: not yet performed.

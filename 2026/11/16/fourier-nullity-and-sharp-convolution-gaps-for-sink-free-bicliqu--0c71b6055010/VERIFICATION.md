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

# Verification

Use Python 3 with no third-party dependencies and run `python check_spectrum.py` in the extracted package. The checker independently enumerates all orientation bitstrings through \(n=8\), validates sink-freeness vertex by vertex, performs an exact integer Walsh--Hadamard transform, and compares all \(87,380\) resulting Fourier coefficients with the symbolic inclusion--exclusion formula. It separately performs \(340\) direct signed support sums for dimensions \(1\) through \(4\), checks Parseval, cardinalities, nullity and sharp positive multiplier magnitude.

Expected final output: `SINK_FREE_BICLIQUE_FOURIER_EXACT_PASS frequencies= 87380 independent_sums= 340`.

The proof in `RESULT.md`, not finite enumeration, establishes the theorem for all integers \(n\ge3\). A separate independent mathematical review has not been performed. The claimed historical distinction is bounded by the inspected literature.

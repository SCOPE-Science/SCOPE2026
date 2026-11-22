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

The accompanying `verify.py` (requires SymPy) performs exact normalization integration, symbolic differentiation of the two half-line score functions, the logarithmic-derivative cubic reductions, rational bracketing of both critical points, the exact comparison identity for their thresholds, and normalization and peak location of the limiting law. It prints high-precision numerical estimates solely as a reproducible supplement.

The global all-parameter and threshold-equality conclusions are proven by monotonicity, uniqueness and derivative signs in RESULT.md. Finite numerical checks are neither presented nor used as an infinite proof. The total-variation convergence follows from pointwise convergence plus Scheffé's lemma. The independent scientific audit remains unperformed, and bibliographic priority is not absolutely certified.

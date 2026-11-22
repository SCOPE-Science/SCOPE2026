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

# Finite-field and symbolic verification

The included `check_cubic_centralizers.py` calculates independent nine-dimensional PBW multiplication matrices and inner-commutator ranks by finite-field Gaussian elimination. It does not copy the compressed four-by-seven proof matrix. It exhaustively checks all controlling low-degree coefficient tuples over the fields with four, seven, and thirteen elements. The accompanying `verification_output.txt` is the captured execution output, including the predicted full-algebra stratum totals and commuting-pair counts.

The general proof separately checks the four-by-seven matrix entries using the multiplication rule and \(1+\zeta+\zeta^2=0\). Its rank case split is exhaustive in every allowed characteristic. The split quadric point count is exact for all finite fields with a primitive cube root, not an inference from experiments. The class-number formula comes from orbit–stabilizer in \(1+J\).

**Limits:** The exhaustive slices and field examples are not independent proofs for every field size. No external mathematical audit has been performed. Originality cannot be established solely by a failed database search; two closest published full texts and selected foundational source sections were compared by mathematical implication.

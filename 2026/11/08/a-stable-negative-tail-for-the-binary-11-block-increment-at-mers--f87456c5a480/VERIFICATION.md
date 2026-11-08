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

The standalone `verify.py` uses only exact `fractions.Fraction` arithmetic and Laurent-polynomial dictionaries; it constructs the eight carry/adjacency states directly from their definitions. It checks \(T_0g=g\), the nontrivial polynomial-vector identity \((T_1^4-\tfrac z2T_1^3)(T_1-I)g=0\), the exact base numerator and first difference, and the initial negative-mass proportions. Each polynomial test is exhaustive over every nonzero monomial coefficient in eight finite state coordinates. It independently compares the finite dyadic sample for eight shifts, which is only corroborative. The infinite claim uses the exact matrix identity plus induction and the geometric carry-tail argument, not enumeration.

Command: `python3 verify.py`

Expected stdout: `VERIFY_OK states=8 zero_suffix=invariant polynomial_identity=exact G4=exact recurrence=exact sharp_thresholds=1..4 negative_tail=45/(128*2^j) finite_integer_samples=8x524288`

Limitations: the algorithm is not an independent peer audit and does not assess bibliographic priority. The symbolic recurrence is specific to the digit pattern and shift family stated in the theorem.

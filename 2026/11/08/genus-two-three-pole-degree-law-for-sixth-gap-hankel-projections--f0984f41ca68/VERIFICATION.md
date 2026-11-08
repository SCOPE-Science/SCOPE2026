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

# Verification scope
Run `python verify_hankel_sixth.py` with SymPy installed. Verified outputs are `GENUS_TWO_DISCRIMINANT_SQUAREFREE_OK`, `FOUR_STEP_LEADING_COEFFICIENTS_OK n=7..81`, `THREE_POLE_DEGREE_FORMULA_OK n=7..81`, and `PRIMARY_LITERATURE_TABLE_MATCH_OK n=10..15: 16,20,22,25,26,30`.

The witness \((a,b,c)=(1,2,3)\) makes the quadratic discriminant squarefree; openness then proves generic squarefreeness. The finite symbolic recurrences independently check all stated periodic leading-coefficient identities in the tested range. The general proof instead uses characteristic roots, Newton branches and pole divisors on a smooth projective genus-two curve. The source table provides only six pre-existing individual degrees; it is not the proof of the all-index formula. Independent validation and historical-priority determination have not been performed.

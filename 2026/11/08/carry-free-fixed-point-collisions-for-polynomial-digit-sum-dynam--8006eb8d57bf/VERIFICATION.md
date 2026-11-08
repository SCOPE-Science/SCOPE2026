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

The proof uses an explicit carry-free base expansion of the composition \(g(g(a))\) and direct three-digit expansions for the two square-map arithmetic progressions. No limiting computation or assumption on unobserved cycles is required.

Run `python3 verify.py` from the extracted directory. The checker independently constructs the translated polynomial coefficient vector and compares its genuine base digits to direct evaluations across 11,880 cases. It checks both square-base progressions at 3,999 parameter values. A further 124,251 direct comparisons test an auxiliary first-two-lift arithmetic criterion as an additional cross-check; that criterion is not required for the theorem. All calculations are exact integers.

Expected output:

```
POLYNOMIAL_FAMILY_OK 11880
SQUARE_ARITHMETIC_PROGRESSIONS_OK 3999
TWO_LIFT_CRITERION_CHECK_OK 124251
VERIFY_OK exact_integer=yes independent_formula_crosschecks=yes finite_tests_not_infinite_proof=yes
```

The checker is finite; it does not certify the unrestricted quantifiers. The correctness argument rests on the coefficientwise noncarry inequality and explicit digit decompositions, with no external computational dependency. Historical priority and external independent audit remain unresolved.
